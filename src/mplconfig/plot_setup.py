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
    
    New PGF Parameters:
    -------------------
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
                'pgf.texsystem': "xelatex",
                'text.usetex': True,
                'pgf.rcfonts': False,
                'pgf.preamble': "\n".join(pgf_preamble)
            }
            mpl.rcParams.update(pgf_config)
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