from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.use('module://pdftex.pdftex')

fig, ax = plt.subplots(nrows=1)
ax.plot([1, 2, 3], [10, 9, 8])
ax.set_xlabel("\$\\alpha\$")
fig.savefig('test.pdf_tex')
