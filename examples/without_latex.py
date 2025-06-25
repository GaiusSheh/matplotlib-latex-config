import mplconfig
import matplotlib.pyplot as plt
import numpy as np

# No LaTeX rendering configuration called. used matplotlib's default settings.

# Set general parameters for the plot
figsize = (6, 4)
font_size = 12
dpi = 200
linewidth = 1
mplconfig.set_general_params(figsize=figsize, font_size=font_size, dpi=dpi, linewidth=linewidth)

# Set up the plot style without LaTeX rendering
mplconfig.setup_plot_style(use_latex=False, mathtext_cm=False) # swith to mathtext_cm=True to use Computer Modern fonts

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y, label=r'$\mathrm{Sin}[x]$')
plt.title(r'Sine Function $y=\mathrm{Sin}[x]$')
plt.xlabel(r'Argument $x$')
plt.ylabel(r'Value $y$')
plt.legend()
plt.tight_layout()
plt.show()