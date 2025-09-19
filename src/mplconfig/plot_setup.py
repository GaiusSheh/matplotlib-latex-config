# -*- coding: utf-8 -*-
"""
A custom plotting style package for Matplotlib to handle various LaTeX
and native rendering configurations.

Contains two main functions:
1. setup_plot_style: Configures backend, text rendering, and fonts based on flags.
2. set_general_params: A standalone helper to set common visual parameters.
"""

import matplotlib as mpl
import warnings
import os
import shutil
import platform


def _find_latex_installation():
    """
    Automatically detect LaTeX installation and add to PATH if needed.
    Returns a dictionary of available TeX systems.
    """
    available_tex = {}

    # Check if already in PATH
    for tex_system in ['lualatex', 'xelatex', 'pdflatex']:
        if shutil.which(tex_system):
            available_tex[tex_system] = shutil.which(tex_system)

    # If all found, return early
    if len(available_tex) == 3:
        return available_tex

    # Platform-specific search for LaTeX installations
    search_paths = []

    if platform.system() == "Windows":
        # Common MiKTeX installation paths
        username = os.environ.get('USERNAME', '')
        search_paths = [
            f"C:\\Users\\{username}\\AppData\\Local\\Programs\\MiKTeX\\miktex\\bin\\x64",
            "C:\\Program Files\\MiKTeX\\miktex\\bin\\x64",
            "C:\\Program Files (x86)\\MiKTeX\\miktex\\bin\\x64",
            # TeX Live paths
            "C:\\texlive\\2023\\bin\\win64",
            "C:\\texlive\\2024\\bin\\win64",
            "C:\\texlive\\2025\\bin\\win64",
        ]
    elif platform.system() == "Darwin":  # macOS
        search_paths = [
            "/usr/local/texlive/2023/bin/x86_64-darwin",
            "/usr/local/texlive/2024/bin/x86_64-darwin",
            "/usr/local/texlive/2025/bin/x86_64-darwin",
            "/Library/TeX/texbin",
            "/opt/homebrew/bin",
        ]
    elif platform.system() == "Linux":
        search_paths = [
            "/usr/bin",
            "/usr/local/bin",
            "/opt/texlive/2023/bin/x86_64-linux",
            "/opt/texlive/2024/bin/x86_64-linux",
            "/opt/texlive/2025/bin/x86_64-linux",
        ]

    # Search for LaTeX executables
    found_path = None
    for path in search_paths:
        if os.path.exists(path):
            # Check if tex executables exist in this path
            tex_found = 0
            for tex_system in ['lualatex', 'xelatex', 'pdflatex']:
                exe_name = f"{tex_system}.exe" if platform.system() == "Windows" else tex_system
                exe_path = os.path.join(path, exe_name)
                if os.path.exists(exe_path):
                    available_tex[tex_system] = exe_path
                    tex_found += 1

            if tex_found >= 2:  # Found at least 2 TeX systems
                found_path = path
                break

    # Add to PATH if found and not already there
    if found_path:
        current_paths = os.environ.get("PATH", "").split(os.pathsep)
        # Normalize paths for comparison (handle case sensitivity and trailing separators)
        normalized_current_paths = [os.path.normcase(os.path.normpath(p)) for p in current_paths]
        normalized_found_path = os.path.normcase(os.path.normpath(found_path))

        if normalized_found_path not in normalized_current_paths:
            print(f"Found LaTeX installation at: {found_path}")
            print("Adding to PATH for current session...")
            os.environ["PATH"] = found_path + os.pathsep + os.environ["PATH"]
        else:
            print(f"LaTeX installation already in PATH: {found_path}")

        # Re-check availability after adding to PATH
        for tex_system in ['lualatex', 'xelatex', 'pdflatex']:
            if tex_system not in available_tex and shutil.which(tex_system):
                available_tex[tex_system] = shutil.which(tex_system)

    return available_tex


def _get_fallback_tex_system(available_tex, preferred="lualatex"):
    """
    Get the best available TeX system, with fallback logic.
    """
    if preferred in available_tex:
        return preferred

    # Fallback order: lualatex -> xelatex -> pdflatex
    fallback_order = ['lualatex', 'xelatex', 'pdflatex']
    for tex_system in fallback_order:
        if tex_system in available_tex:
            return tex_system

    return None


def set_general_params(
    figsize=(8, 6),
    font_size=12,
    dpi=600,
    linewidth=1.0,
    **kwargs
):
    """
    A standalone function to set general visual parameters.
    This can be called in any configuration mode.
    """
    general_settings = {
        'font.size': font_size,
        'figure.figsize': figsize,
        'figure.dpi': dpi,
        'lines.linewidth': linewidth,
    }
    general_settings.update(kwargs)
    mpl.rcParams.update(general_settings)
    print(f"General parameters set: font_size={font_size}, figsize={figsize}, dpi={dpi}, linewidth={linewidth}.")


def setup_plot_style(
    use_latex=True,
    # --- Parameters for the LaTeX branch ---
    use_default_latex=False,
    latex_sans_text=False,
    # --- Parameters for the PGF (Custom LaTeX) branch ---
    tex_system="lualatex",  # New parameter: "lualatex" (default), "xelatex", or "pdflatex"
    main_font=None,
    sans_font=None,
    math_font=None,
    mathrm_font=None,
    mathcal_font=None,
    special_font=None,
    # --- Parameters for the non-LaTeX branch ---
    mathtext_cm=False
):
    """
    Sets up complex plotting backends and font configurations based on flags.

    PGF Parameters:
    ---------------
    tex_system : str, optional
        TeX system to use with PGF backend. Options: "lualatex" (default), "xelatex", "pdflatex".
        LuaLaTeX and XeLaTeX provide full Unicode support and system font access.
    mathrm_font : str, optional
        Font for the \\mathrm command in math mode. Defaults to 'Cambria'.
    mathcal_font : str, optional
        Font for the calligraphic (\\mathcal) math alphabet. Defaults to 'Brush Script MT'.
    special_font : str, optional
        Font for the custom \\spchar{} command. Defaults to 'Arial'.
    """

    # --- Branch 1: Use LaTeX Rendering ---
    if use_latex:
        print("Mode: LaTeX rendering enabled.")
        if mathtext_cm:
            warnings.warn("'mathtext_cm' is ignored because 'use_latex' is True.", UserWarning)

        # --- Branch 1a: Use Default LaTeX (non-PGF) ---
        if use_default_latex:
            print("--> Sub-mode: Default LaTeX (non-PGF).")
            # ... (This section remains unchanged from the previous version) ...
            if any([main_font, math_font, mathrm_font, mathcal_font, special_font]):
                warnings.warn(
                    "Custom fonts are ignored because 'use_default_latex' is True.",
                    UserWarning
                )
            if latex_sans_text:
                print("----> Style: Sans-serif text, Serif math.")
                preamble = [r"\usepackage{helvet}",
                            r"\usepackage{amsmath}",
                            r"\usepackage{amssymb}"]
            else:
                print("----> Style: Default Serif text and math (Computer Modern).")
                preamble = [r"\usepackage{amsmath}", 
                            r"\usepackage{amssymb}"]
            mpl.rcParams.update({
                "text.usetex": True,
                "font.family": "sans-serif" if latex_sans_text else "serif",
                "text.latex.preamble": "\n".join(preamble),
            })

        # --- Branch 1b: Use Custom Font LaTeX (PGF) ---
        else:
            print("--> Sub-mode: Custom font LaTeX via PGF backend.")

            # Auto-detect LaTeX installation
            print("----> Detecting LaTeX installation...")
            available_tex = _find_latex_installation()

            if not available_tex:
                warnings.warn(
                    "No LaTeX installation found. Please install MiKTeX or TeX Live and ensure "
                    "it's in your system PATH. See README for installation instructions.",
                    UserWarning
                )
                return

            # Auto-select or validate tex_system
            if tex_system not in available_tex:
                fallback_tex = _get_fallback_tex_system(available_tex, tex_system)
                if fallback_tex:
                    print(f"----> '{tex_system}' not found, using '{fallback_tex}' instead")
                    tex_system = fallback_tex
                else:
                    warnings.warn(
                        f"No compatible LaTeX engine found. Available: {list(available_tex.keys())}",
                        UserWarning
                    )
                    return

            try:
                mpl.use("pgf")
                print("----> PGF backend activated.")
                print("!!! NOTE: you should not use plt.show() or savefig() as svg in this mode, "
                      "as it may not render correctly with the PGF backend!!!")
            except ImportError:
                warnings.warn("PGF backend not available. Cannot use custom font mode.", UserWarning)
                return

            # --- Define the new, richer set of default fonts ---
            default_main_font = "Aptos"
            default_sans_font = "Aptos"
            default_math_font = "Cambria Math"
            default_mathrm_font = "Cambria"
            default_mathcal_font = "Brush Script MT"
            default_special_font = "Arial"

            # --- Assign fonts, using user input or defaults ---
            main_font = main_font or default_main_font
            sans_font = sans_font or default_sans_font
            math_font = math_font or default_math_font
            mathrm_font = mathrm_font or default_mathrm_font
            mathcal_font = mathcal_font or default_mathcal_font
            special_font = special_font or default_special_font

            # --- Dynamically build the new, complex preamble ---
            pgf_preamble = [
                r"\usepackage{amsmath}",
                r"\usepackage{fontspec}",
                r"\usepackage{unicode-math}",
                r"\usepackage[UTF8]{ctex}",  # Add ctex for CJK support
                r"\usepackage{upgreek}" # used for upright Greek letters like \upmu
            ]
            
            # Add font settings to the preamble
            pgf_preamble.append(rf"\setmainfont{{{main_font}}}")
            pgf_preamble.append(rf"\setsansfont{{{sans_font}}}")
            pgf_preamble.append(rf"\setmathfont{{{math_font}}}")
            pgf_preamble.append(rf"\setmathrm{{{mathrm_font}}}")

            if mathcal_font:
                pgf_preamble.append(rf"\setmathfont[range=\mathcal]{{{mathcal_font}}}")
            
            if special_font:
                pgf_preamble.append(rf"\newfontfamily\specialfont{{{special_font}}}")
                pgf_preamble.append(r"\newcommand{\spchar}[1]{\text{\specialfont #1}}")

            # --- Apply the configuration ---
            pgf_config = {
                'pgf.texsystem': tex_system,
                'text.usetex': True,
                'pgf.rcfonts': False,
                'pgf.preamble': "\n".join(pgf_preamble)
            }
            mpl.rcParams.update(pgf_config)
            print(f"----> TeX system: {tex_system}")
            print(f"----> Fonts set: Main='{main_font}', Math='{math_font}', "
                  f"mathrm='{mathrm_font}', mathcal='{mathcal_font}', special='{special_font}'.")

    # --- Branch 2: Use Native Matplotlib Rendering (unchanged) ---
    else:
        # ... (This section remains unchanged from the previous version) ...
        print("Mode: Native Matplotlib rendering.")
        if mathtext_cm:
            print("--> Sub-mode: Mathtext with Computer Modern style fonts.")
            mpl.rcParams.update({"text.usetex": False, "mathtext.fontset": "cm"})
        else:
            print("--> Sub-mode: Standard Matplotlib defaults (DejaVu Sans).")
            mpl.rcParams.update({"text.usetex": False, "mathtext.fontset": "dejavusans"})