#!/usr/bin/python
#coding: utf-8

# CopyRight 2015 Allan Psicobyte (psicobyte@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import copy, os, pyPdf, sys

pdf_input = file(sys.argv[1], "rb")

nombre_output = sys.argv[2]

pdf_output = file(nombre_output, "wb")

output = pyPdf.PdfFileWriter()
input1 = pyPdf.PdfFileReader(pdf_input)

pg= input1.getNumPages()

for i in range(0,pg):
    pagina1 = input1.getPage(i)
    pagina2 = copy.copy(pagina1)

    corte= (pagina1.mediaBox.getUpperRight_x() / 2, pagina1.mediaBox.getUpperRight_y())

    pagina1.mediaBox.upperRight = corte
    output.addPage(pagina1)

    pagina2.mediaBox.upperLeft = corte
    output.addPage(pagina2)

output.write(pdf_output)

pdf_output.close
