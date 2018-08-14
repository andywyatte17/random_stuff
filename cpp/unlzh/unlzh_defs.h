//
// unlzh_defs.h
//

#pragma once

#define local static
typedef uint8_t uch;
typedef uint16_t ush;
#define UCHAR_MAX 255

#define THRESHOLD    3
#define DDICSIZ      26624
#define MAXDICBIT   16
#define MATCHBIT     8
#define MAXMATCH   256
#define NC (UCHAR_MAX + MAXMATCH + 2 - THRESHOLD)
  /* alphabet = {0, 1, 2, ..., NC - 1} */
#define NP          (MAXDICBIT + 1)
#define CBIT 9  /* $\lfloor \log_2 NC \rfloor + 1$ */
#define NT          (CODE_BIT + 3)
#define PBIT         5
#define TBIT         5

#define CODE_BIT  16  /* codeword length */

#if NT > NP
#define NPT NT
#else
#define NPT NP
#endif

#define CHAR_BIT 8
#define CTABLESIZE  4096
#define PTABLESIZE 256

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

#define DICBIT    13    /* 12(-lh4-) or 13(-lh5-) */
#define DICSIZ ((unsigned) 1 << DICBIT)

static ush       bitbuf;
static unsigned  subbitbuf;
static int       bitcount;

static ush left[2 * NC - 1];
static ush right[2 * NC - 1];
static uch  c_len[NC];
static uch  pt_len[NPT];
static ush c_table[CTABLESIZE];
static ush pt_table[PTABLESIZE];

static int in;
static int out;

static unsigned blocksize;
