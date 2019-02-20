// FunctionOf.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <windows.h>
#include <functional>
#include <type_traits>
#include <stdexcept>
#include <memory>
#include <vector>

struct _cairo_surface;
typedef struct _cairo_surface cairo_surface_t;

struct _cairo;
typedef struct _cairo cairo_t;

cairo_t* /*__cdecl*/ cairo_create(cairo_surface_t*);

void /*__cdecl*/ cairo_destroy(cairo_t*);

typedef enum _cairo_format {
  CAIRO_FORMAT_INVALID = -1,
  CAIRO_FORMAT_ARGB32 = 0,
  CAIRO_FORMAT_RGB24 = 1,
  CAIRO_FORMAT_A8 = 2,
  CAIRO_FORMAT_A1 = 3,
  CAIRO_FORMAT_RGB16_565 = 4,
  CAIRO_FORMAT_RGB30 = 5
} cairo_format_t;

cairo_surface_t * cairo_image_surface_create(cairo_format_t	format, int width, int height);

unsigned char * cairo_image_surface_get_data(cairo_surface_t *surface);

cairo_format_t cairo_image_surface_get_format(cairo_surface_t *surface);

int cairo_image_surface_get_width(cairo_surface_t *surface);

int cairo_image_surface_get_height(cairo_surface_t *surface);

int cairo_image_surface_get_stride(cairo_surface_t *surface);

void cairo_set_source_rgb(cairo_t *cr, double red, double green, double blue);

void cairo_rectangle(cairo_t *cr, double x, double y, double width, double height);

void cairo_fill(cairo_t *cr);

template<typename F>
struct FunctionOf
{
  using f = typename std::remove_pointer<F>::type;
  using type = std::function<f>;
};

struct CairoApiBase
{
  struct Exception : std::runtime_error {
    using  std::runtime_error::runtime_error;
  };
  std::shared_ptr<void> dll;

  template<typename Deleter>
  CairoApiBase(void* pDll, Deleter d) : dll(pDll, d) {}
};

#define DEF_FN(x) FunctionOf<decltype(&::##x)>::type x = \
   (FunctionOf<decltype(&::##x)>::f*)Policy::GetProc(dll.get(), #x)

template<class Policy>
struct CairoApi : CairoApiBase
{
  CairoApi() : CairoApiBase(Policy::LoadLibrary(), [](void* p) { Policy::FreeLibrary(p); })
  {
  }
  DEF_FN(cairo_create);
  DEF_FN(cairo_destroy);
  DEF_FN(cairo_image_surface_create);
  DEF_FN(cairo_image_surface_get_data);
  DEF_FN(cairo_image_surface_get_width);
  DEF_FN(cairo_image_surface_get_height);
  DEF_FN(cairo_image_surface_get_stride);
  DEF_FN(cairo_set_source_rgb);
  DEF_FN(cairo_rectangle);
  DEF_FN(cairo_fill);
};

struct CairoDllPolicy
{
  static void* LoadLibrary() {
    auto v = ::LoadLibraryA("cairo.dll");
    if (!v) throw CairoApi<CairoDllPolicy>::Exception{ "Failed to load cairo.dll" };
    return v;
  }
  static void FreeLibrary(void* p) {
    ::FreeLibrary((HMODULE)p);
  }
  static void* GetProc(void* lib, const char* name) {
    auto v = ::GetProcAddress((HMODULE)lib, name);
    if (!v) throw CairoApi<CairoDllPolicy>::Exception{ std::string{"Failed to load function - "} +name };
    return v;
  }
};

int main() {
  CairoApi<CairoDllPolicy> a;
  auto* surface = a.cairo_image_surface_create(CAIRO_FORMAT_ARGB32, 128, 128);

  auto* ctx = a.cairo_create(surface);

  a.cairo_set_source_rgb(ctx, 1, 0, 0);
  a.cairo_rectangle(ctx, 5, 5, 25, 35);
  a.cairo_fill(ctx);

  a.cairo_destroy(ctx);

  auto* v = a.cairo_image_surface_get_data(surface);
  auto w = a.cairo_image_surface_get_width(surface);
  auto h = a.cairo_image_surface_get_height(surface);
  auto s = a.cairo_image_surface_get_stride(surface);

  if (FILE* fp = fopen("cairo.data", "wb"))
  {
    std::vector<uint8_t> d;
    d.resize(w * 4);
    for (int i = 0; i < h; ++i)
    {
      std::copy_n(v + s * i, 4 * w, d.begin());
      for (int x = 0; x < w; ++x)
        std::rotate(d.data() + x * 4, d.data() + x * 4 + 1, d.data() + x * 4 + 4);
      fwrite(d.data(), 1, w * 4, fp);
    }
    fclose(fp);
  }

  return 0;
}
