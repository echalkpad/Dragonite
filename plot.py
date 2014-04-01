import prettyplotlib as ppl
import numpy as np

# This is "import matplotlib.pyplot as plt" from the prettyplotlib library
import matplotlib.pyplot as plt

# This is "import matplotlib as mpl" from the prettyplotlib library
import matplotlib as mpl

# Set the random seed for consistency
np.random.seed(12)

fig, ax = plt.subplots(1)

# Show the whole color range
for i in range(8):
    x = np.random.normal(loc=i, size=1000)
    y = np.random.normal(loc=i, size=1000)
    ppl.scatter(ax, x, y, label=str(i))

ppl.legend(ax)

ax.set_title('prettyplotlib `scatter` example\nshowing default color cycle and scatter params')
fig.savefig('scatter_prettyplotlib_default.png')