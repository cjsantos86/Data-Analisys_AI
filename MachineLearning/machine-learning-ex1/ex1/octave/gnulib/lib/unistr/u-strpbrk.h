/* Search for some characters in UTF-8/UTF-16/UTF-32 string.
   Copyright (C) 1999, 2002, 2006, 2009-2016 Free Software Foundation, Inc.
   Written by Bruno Haible <bruno@clisp.org>, 2002.

   This program is free software: you can redistribute it and/or modify it
   under the terms of the GNU Lesser General Public License as published
   by the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

UNIT *
FUNC (const UNIT *str, const UNIT *accept)
{
  /* Optimize two cases.  */
  if (accept[0] == 0)
    return NULL;
  {
    ucs4_t uc;
    int count = U_STRMBTOUC (&uc, accept);
    if (count >= 0 && accept[count] == 0)
      return U_STRCHR (str, uc);
  }
  /* General case.  */
  {
    const UNIT *ptr = str;

    for (;;)
      {
        ucs4_t uc;
        int count = U_STRMBTOUC (&uc, ptr);
        if (count <= 0)
          break;
        if (U_STRCHR (accept, uc))
          return (UNIT *) ptr;
        ptr += count;
      }
    return NULL;
  }
}
