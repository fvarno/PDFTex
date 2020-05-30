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

If everything goes through as it should, two files are generated:

``test.pdf_tex``
``test.pdf``

Put these two files always together when using in your LaTeX document. 

An example of importing the generated figures in LaTex document is:

```
\begin{figure}
    \centering
    \def\svgwidth{12.0cm}
    \input{test.pdf_tex}
    \caption{A sample figure.}
    \label{fig:test}
\end{figure}
```

