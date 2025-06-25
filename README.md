# matplotlib-latex-config

A personal, highly configurable plotting style package for Matplotlib with advanced LaTeX support.

## Features

- Flexible LaTeX rendering: switch between native Matplotlib, standard LaTeX, and PGF (custom font) LaTeX rendering.
- Custom font support: specify main, sans-serif, math, and special fonts for your plots.
- General parameter setup: quickly set figure size, font size, DPI, and line width.
- Easy integration: designed for use in any Matplotlib-based workflow.

## Installation

Clone this repository and install locally:

```bash
git clone https://github.com/yourusername/matplotlib-latex-config.git
cd matplotlib-latex-config
pip install .
```

## Usage

### Basic usage

```python
import mplconfig
import matplotlib.pyplot as plt
import numpy as np

# Set general parameters
mplconfig.set_general_params(figsize=(6, 4), font_size=14, dpi=150, linewidth=1.5)

# Use native Matplotlib rendering with Computer Modern math font
mplconfig.setup_plot_style(use_latex=False, mathtext_cm=True)

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y, label=r'$\sin(x)$')
plt.title('Sine Function')
plt.xlabel(r'$x$')
plt.ylabel(r'$\sin(x)$')
plt.legend()
plt.tight_layout()
plt.show()
```

### Advanced: LaTeX PGF backend with custom fonts

```python
import mplconfig
import matplotlib.pyplot as plt
import numpy as np

mplconfig.set_general_params(figsize=(6, 4), font_size=12, dpi=200, linewidth=1)

mplconfig.setup_plot_style(
    use_latex=True,
    use_default_latex=False,
    main_font='Arial',         # Custom main font
    sans_font='Arial',         # Custom sans-serif font
    math_font='Cambria Math',  # Custom math font
    mathrm_font='Noto Serif',  # Custom font for \mathrm
    mathcal_font='Brush Script MT',  # Custom font for \mathcal
    special_font='Arial',      # Custom font for \spchar
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
```

## Examples

See the [`examples/`](examples/) directory for more usage patterns.

## Requirements

- Python >= 3.6
- matplotlib >= 3.5

## Contributing

Pull requests and suggestions are welcome! Please open an issue or submit a PR.

## License

MIT License