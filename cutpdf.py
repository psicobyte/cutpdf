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

def main():

    if len(sys.argv) > 1:

        if os.path.isfile(sys.argv[1]):
            name_input = sys.argv[1]
        else:
            sys.exit("file %s not found" % sys.argv[1])
    else:
        sys.exit("missing origin file operand")

    if len(sys.argv) > 2:
        name_output = sys.argv[2]

    else:
        new_name = "cut_" + os.path.basename(sys.argv[1])
        name_output = os.path.join(os.path.dirname(sys.argv[1]), new_name)

    cutpdf(name_input,name_output)

def cutpdf(name_input,name_output):

    pdf_input = file(name_input, "rb")
    pdf_output = file(name_output, "wb")

    output = pyPdf.PdfFileWriter()
    input1 = pyPdf.PdfFileReader(pdf_input)

    pg= input1.getNumPages()

    for i in range(0,pg):
        page1 = input1.getPage(i)
        page2 = copy.copy(page1)

        cutline= (page1.mediaBox.getUpperRight_x() / 2, page1.mediaBox.getUpperRight_y())

        page1.mediaBox.upperRight = cutline
        output.addPage(page1)

        page2.mediaBox.upperLeft = cutline
        output.addPage(page2)

    output.write(pdf_output)

    pdf_output.close

    return True

if __name__ == "__main__":
    main()
