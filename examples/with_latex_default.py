import mplconfig
import matplotlib.pyplot as plt
import numpy as np

# Set general parameters for the plot
figsize = (6, 4)
font_size = 12
dpi = 200
linewidth = 1
mplconfig.set_general_params(figsize=figsize, font_size=font_size, dpi=dpi, linewidth=linewidth)

# Set general parameters
mplconfig.setup_plot_style(
    use_latex=True,
    use_default_latex=True,  # Use default LaTeX rendering
    latex_sans_text=False,  # Use serif text and math, switch to True for sans-serif text
)

x = np.linspace(0, 2 * np.pi, 100)
y = np.cos(x)

plt.plot(x, y, label=r'$\cos(x)$')
plt.title('Cosine Function (LaTeX PGF)')
plt.xlabel(r'$x$')
plt.ylabel(r'$\cos(x)$')
plt.legend()
plt.tight_layout()
plt.savefig('cosine_pgf.pdf')
plt.close()