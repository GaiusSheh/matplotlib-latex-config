from .plot_setup import setup_plot_style, set_general_params
from importlib.metadata import version, PackageNotFoundError

try:
    # This will read the version from the installed package's metadata
    # (which was defined in pyproject.toml)
    __version__ = version("matplotlib-latex-config")
except PackageNotFoundError:
    # This is a fallback for when the package is not installed,
    # e.g., when you are developing locally.
    __version__ = "1.0.0-dev"