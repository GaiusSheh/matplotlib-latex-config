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
    use_default_latex=False,  # Use default LaTeX rendering
    # you can uncomment the following lines to use custom fonts
    # main_font='Arial',  # Custom main font
    # sans_font='Arial',  # Custom sans-serif font
    # math_font='Cambria Math',  # Custom math font
    # mathrm_font='Noto Serif',  # Custom font for \mathrm
    # mathcal_font='Brush Script MT',  # Custom font for \mathcal
    # special_font='Arial',  # Custom font for \spchar
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