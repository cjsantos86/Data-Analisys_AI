/* Test of canonical decomposition of Unicode strings.
   Copyright (C) 2009-2016 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* Written by Bruno Haible <bruno@clisp.org>, 2009.  */

#include <config.h>

#include "uninorm.h"

#if !WOE32DLL
/* Check that UNINORM_NFD is defined and links.  */
uninorm_t n = UNINORM_NFD;
#endif

extern void test_u8_nfd (void);
extern void test_u16_nfd (void);
extern void test_u32_nfd (void);

int
main ()
{
  /* Check that UNINORM_NFD is defined and links.  */
  uninorm_t nf = UNINORM_NFD;
  (void) nf;

  test_u32_nfd ();
  test_u16_nfd ();
  test_u8_nfd ();

  return 0;
}
