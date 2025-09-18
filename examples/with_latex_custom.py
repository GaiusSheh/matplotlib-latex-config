import mplconfig
import matplotlib.pyplot as plt
import numpy as np

print("Testing LuaLaTeX rendering with custom fonts...")
print("Note: Ensure LuaLaTeX is in your system PATH (see README for setup instructions)")

# Set general parameters for the plot
figsize = (6, 4)
font_size = 12
dpi = 200
linewidth = 1
mplconfig.set_general_params(figsize=figsize, font_size=font_size, dpi=dpi, linewidth=linewidth)

# Configure PGF backend with LuaLaTeX
mplconfig.setup_plot_style(
    use_latex=True,
    use_default_latex=False,  # Use PGF backend for custom fonts
    tex_system="lualatex",     # Use LuaLaTeX (default)
    # Custom fonts - uncomment and modify as needed
    # main_font='Times New Roman',
    # sans_font='Arial',
    # math_font='Latin Modern Math',
    # mathrm_font='Times New Roman',
    # mathcal_font='Brush Script MT',
    # special_font='Arial'
)

x = np.linspace(0, 2 * np.pi, 100)
y = np.cos(x)

plt.figure()
plt.plot(x, y, label=r'$\cos(x)$', linewidth=2)
plt.title('Cosine Function (LuaLaTeX + PGF)', fontsize=14)
plt.xlabel(r'$x$ (radians)', fontsize=12)
plt.ylabel(r'$\cos(x)$', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('cosine_lualatex.pdf')
print("Success! PDF saved as 'cosine_lualatex.pdf'")
plt.close()