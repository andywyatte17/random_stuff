//
// unlzh_defs.h
//

#pragma once

#define local /*..*/
typedef uint8_t uch;
typedef uint16_t ush;
#define UCHAR_MAX 255

#define THRESHOLD    3
#define DDICSIZ      26624
#define MAXDICBIT   16
#define MATCHBIT     8
#define MAXMATCH   256
#define NC          (UCHAR_MAX + MAXMATCH + 2 - THRESHOLD)
#define NP          (MAXDICBIT + 1)
#define CBIT         9
#define NT          (CODE_BIT + 3)
#define PBIT         5
#define TBIT         5

#if NT > NP
#define NPT NT
#else
#define NPT NP
#endif

#define CTABLESIZE  4096
#define PTABLESIZE 256

#define BITS 16
#define OUTBUFSIZ  16384
#define DIST_BUFSIZE 0x8000
#define THRESHOLD    3
#define DDICSIZ      26624
#define MAXDICBIT   16
#define MATCHBIT     8
#define MAXMATCH   256
#define NC          (UCHAR_MAX + MAXMATCH + 2 - THRESHOLD)
#define NP          (MAXDICBIT + 1)
#define CBIT         9
#define NT          (CODE_BIT + 3)
#define PBIT         5
#define TBIT 5

#if NT > NP
#define NPT NT
#else
#define NPT NP
#endif

static ush left[2 * NC - 1];
static ush right[2 * NC - 1];
static uch  c_len[NC];
static uch  pt_len[NPT];
static ush c_table[CTABLESIZE];
static ush pt_table[PTABLESIZE];

static int in;
static int out;

#define try_byte() (inptr < insize ? inbuf[inptr++] : fill_inbuf(1))
