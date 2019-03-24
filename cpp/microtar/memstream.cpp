#include "microtar.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <stdint.h>
#include <algorithm>
#include <memory>

void write();
void read();

void main()
{
  write();
  read();
}

// ...

namespace
{
class MemStream
{
  unsigned pos = 0;

  std::vector<uint8_t> v;
  
  const void* const p = nullptr;
  const unsigned n = 0;

public:
  /// Open buffer for writing - data goes into 'v'
  MemStream() = default;

  /// Open buffer for reading - data is read from [p, p+n).
  MemStream(const void* pIn, unsigned nIn) : p(pIn), n(nIn) {}
  
  int write(mtar_t * /*tar*/, const void *data, unsigned size)
  {
    if(p)
      return MTAR_EWRITEFAIL;
    unsigned new_size = std::max(v.size(), pos + size);
    v.resize(new_size);
    std::copy_n((const uint8_t*)data, size, v.data() + pos);
    pos += size;
    return MTAR_ESUCCESS;
  }

  int read(mtar_t * /*tar*/, void *data, unsigned size)
  {
    auto* src = p ? (const uint8_t*)p : v.data();
    const unsigned end = p ? n : v.size();
    if(pos + size <= end)
    {
      std::copy_n(src + pos, size, (uint8_t*)data);
      pos += size;
      return MTAR_ESUCCESS;
    }
    return MTAR_EREADFAIL;
  }

  int seek(mtar_t *tar, unsigned offset)
  {
    const unsigned end = p ? n : v.size();
    if(offset + pos <= end) {
      pos += offset;
      return MTAR_ESUCCESS;
    }
    return MTAR_ESEEKFAIL;
  }

  std::vector<uint8_t> release_buffer()
  {
    return std::vector<uint8_t>(std::move(v));
  }
};

// ...

extern "C" int file_write(mtar_t *tar, const void *data, unsigned size)
{
  return ((MemStream *)tar->stream)->write(tar, data, size);
}

extern "C" static int file_read(mtar_t *tar, void *data, unsigned size)
{
  return ((MemStream *)tar->stream)->read(tar, data, size);
}

extern "C" static int file_seek(mtar_t *tar, unsigned offset)
{
  return ((MemStream *)tar->stream)->seek(tar, offset);
}

extern "C" static int file_close(mtar_t *tar)
{
  return MTAR_ESUCCESS;
}

// ...

} // namespace

// ...

std::pair<mtar_t, std::unique_ptr<MemStream>> MakeTarWriter()
{
  mtar_t tar = mtar_t{};

  std::unique_ptr<MemStream> ms(new MemStream());
  tar.stream = ms.get();
  tar.read = &file_read;
  tar.write = &file_write;
  tar.seek = &file_seek;
  tar.close = &file_close;

  return std::make_pair(tar, std::move(ms));
}

std::vector<uint8_t> ExtractMemoryFromTarWriter(mtar_t t)
{
  return ((MemStream*)t.stream)->release_buffer();
}

// ...

void write()
{
  const char *str1 = "Hello world";
  const char *str2 = "Goodbye world";

  /* Open archive for writing */
  auto tar_ms = MakeTarWriter();
  auto& tar = tar_ms.first;

  /* Write strings to files `test1.txt` and `test2.txt` */
  mtar_write_file_header(&tar, "test1.txt", strlen(str1));
  mtar_write_data(&tar, str1, strlen(str1));
  mtar_write_file_header(&tar, "test2.txt", strlen(str2));
  mtar_write_data(&tar, str2, strlen(str2));

  /* Finalize -- this needs to be the last thing done before closing */
  mtar_finalize(&tar);

  /* Close archive */
  mtar_close(&tar);

  auto ms = ExtractMemoryFromTarWriter(tar);

  auto* f = fopen("memstream-out.tar", "wb");
  fwrite(ms.data(), 1, ms.size(), f);
  fclose(f);
}

// ...

std::pair<mtar_t, std::unique_ptr<MemStream>> MakeTarReader(const void* p, unsigned n)
{
  mtar_t tar = mtar_t{};

  std::unique_ptr<MemStream> ms(new MemStream(p, n));
  tar.stream = ms.get();
  tar.read = &file_read;
  tar.write = &file_write;
  tar.seek = &file_seek;
  tar.close = &file_close;

  return std::make_pair(tar, std::move(ms));
}

// ...

void read()
{
  /* Open archive for reading */

  MemStream ms;

  FILE* f = fopen("memstream-out.tar", "rb");
  std::vector<uint8_t> v;
  v.resize(1024*1024*8);
  auto n = fread(v.data(), 1, v.size(), f);
  v.resize(n);
  fclose(f);

  mtar_header_t h;
  auto tar_ms = MakeTarReader(v.data(), v.size());
  auto& tar = tar_ms.first;

  /* Print all file names and sizes */
  while ( (mtar_read_header(&tar, &h)) != MTAR_ENULLRECORD ) {
    printf("%s (%d bytes)\n", h.name, h.size);
    mtar_next(&tar);
  }

  /* Load and print contents of file "test.txt" */
  mtar_find(&tar, "test.txt", &h);
  auto* p = calloc(1, h.size + 1);
  mtar_read_data(&tar, p, h.size);
  printf("%s", (const char*)p);
  free(p);

  /* Close archive */
  mtar_close(&tar);
}