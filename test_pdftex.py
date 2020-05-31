from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.use('module://pdftex.pdftex')

fig, ax = plt.subplots(nrows=1)
ax.plot([1, 2, 3], [8, 7, 6])
import ipdb; ipdb.set_trace()
fig.tight_layout(pad=10)
ax.set_xlabel("\$\\alpha\$")
fig.savefig('test.pdf_tex')
