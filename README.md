# matplotlib-latex-config

A personal, highly configurable plotting style package for Matplotlib with advanced LaTeX support.

## Features

- **Flexible LaTeX rendering**: Switch between native Matplotlib, standard LaTeX, and PGF (custom font) LaTeX rendering
- **Multiple TeX engines**: Support for XeLaTeX, LuaLaTeX, and pdfLaTeX via PGF backend
- **Custom font support**: Specify main, sans-serif, math, and special fonts for your plots
- **General parameter setup**: Quickly set figure size, font size, DPI, and line width
- **Easy integration**: Designed for use in any Matplotlib-based workflow

## Requirements

- Python >= 3.6
- matplotlib >= 3.5
- **LaTeX distribution** (for LaTeX rendering modes):
  - **Windows**: MiKTeX or TeX Live
  - **macOS**: MacTeX or TeX Live
  - **Linux**: TeX Live (usually available via package manager)

## Installation

### 1. Install Python Package

Clone this repository and install locally:

```bash
git clone https://github.com/GaiusSheh/matplotlib-latex-config.git
cd matplotlib-latex-config
pip install .
```

### 2. LaTeX Configuration

**Automatic Detection**: The package will automatically detect and configure LaTeX installations on first use. If LaTeX is found but not in PATH, it will be temporarily added for the current session.

**Manual Configuration**: For persistent setup, add LaTeX to your system PATH:

#### Windows (MiKTeX)
Add MiKTeX to your system PATH. Common locations:
- User installation: `C:\Users\{username}\AppData\Local\Programs\MiKTeX\miktex\bin\x64`
- System installation: `C:\Program Files\MiKTeX\miktex\bin\x64`

**Method 1: Via System Properties**
1. Press `Win + R`, type `sysdm.cpl`, press Enter
2. Go to "Advanced" tab → "Environment Variables"
3. Under "System Variables", find and edit "Path"
4. Add your MiKTeX bin directory path

**Method 2: Via PowerShell (Admin)**
```powershell
# Replace with your actual MiKTeX path
$miktexPath = "C:\Users\$env:USERNAME\AppData\Local\Programs\MiKTeX\miktex\bin\x64"
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";$miktexPath", "Machine")
```

#### macOS/Linux
LaTeX distributions are typically added to PATH during installation. Verify with:
```bash
which xelatex lualatex pdflatex
```

### 3. Verify Installation (Optional)

The package automatically detects LaTeX, but you can manually verify:
```bash
# Test individual engines
xelatex --version
lualatex --version
pdflatex --version
```

**Note**: If LaTeX is not in your system PATH, the package will search common installation locations and add them temporarily.

## Usage

### Basic Usage

```python
import mplconfig
import matplotlib.pyplot as plt
import numpy as np

# Set general plot parameters
mplconfig.set_general_params(figsize=(8, 6), font_size=12, dpi=300)

# Configure LaTeX rendering
mplconfig.setup_plot_style(
    use_latex=True,
    use_default_latex=False,  # Use PGF backend for custom fonts
    tex_system="lualatex",    # Options: "lualatex" (default), "xelatex", "pdflatex"
    main_font="Times New Roman",
    math_font="Latin Modern Math"
)

# Create your plot
x = np.linspace(0, 2*np.pi, 100)
plt.plot(x, np.sin(x), label=r'$\sin(x)$')
plt.xlabel(r'$x$')
plt.ylabel(r'$y$')
plt.legend()
plt.savefig('plot.pdf')
```

### Available Rendering Modes

1. **Native Matplotlib** (`use_latex=False`): Fast, no LaTeX required
2. **Standard LaTeX** (`use_latex=True, use_default_latex=True`): Uses system's default LaTeX fonts
3. **PGF with Custom Fonts** (`use_latex=True, use_default_latex=False`): Full font customization with LuaLaTeX/XeLaTeX

### Examples

See the [`examples/`](examples/) directory for detailed usage patterns:
- `without_latex.py` - Native Matplotlib rendering
- `with_latex_default.py` - Standard LaTeX rendering
- `with_latex_custom.py` - PGF backend with LuaLaTeX (custom fonts)

## Troubleshooting

### "lualatex not found" Error
- Verify LaTeX installation: `lualatex --version`
- Ensure LaTeX bin directory is in system PATH
- Restart terminal/IDE after PATH changes

### "xelatex not found" Error (when using XeLaTeX)
- Verify LaTeX installation: `xelatex --version`
- Ensure LaTeX bin directory is in system PATH
- Restart terminal/IDE after PATH changes

### Font Not Found Errors
- Ensure fonts are installed on your system
- For Windows: Install fonts in `C:\Windows\Fonts\`
- Use system font names exactly as they appear in font manager

### PGF Backend Issues
- First run may be slow (LaTeX package downloads)
- Avoid `plt.show()` with PGF backend, use `plt.savefig()` instead
- For SVG output, use different backends