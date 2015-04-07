# cutpdf
Programa para cortar por la mitad PDFs a doble página.

Convierte un PDF escaneado a doble página en otro con las páginas por separado (y, por tanto, con el doble de páginas).

## Requisitos

Requiere la libería `pyPdf`

## Uso

`cutpdf.py FileInput.pdf [ FileOutput.pdf ]`

Corta verticalmente cada una de las páginas de FileInput.pdf y crea un fichero FileOutput.pdf con ellas.

Si no se le pasa el nombre del fichero de salida crea uno a partir del nombre del fichero original añadiéndole el prefijo "cut_".
