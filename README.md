# PDFTex
An easy way to generate PDF files which could be imported into overleaf with python/matplotlib

## Perquisites
``apt get install inkscape``

## Installation
``pip install git+https://github.com/fvarno/PDFTex#egg=PDFTex``

## Example

```from matplotlib import pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.use('module://pdftex.pdftex')

fig, ax = plt.subplots(nrows=1, figsize=(10, 5))
ax.plot(np.arange(5), np.arange(5)*5+1)
ax.set_xlabel("\$\\alpha\$")
fig.savefig('test.pdf_tex')
```
