import os
import sys
from datetime import datetime

# Configuration file for the Sphinx documentation builder.
# This is a minimal, reusable template for docs/conf.py


# Put the package root on sys.path so autodoc can import the package.
sys.path.insert(0, os.path.abspath(".."))

# -- Project information -----------------------------------------------------

project = "local-package-installer"
author = "Your Name"
copyright = f"{datetime.now().year}, {author}"

# Try to get the package version from the installed package or fallback.
try:
	import local_package_installer as _pkg  # replace with your package module name
	release = getattr(_pkg, "__version__", "")
except Exception:
	release = ""

# -- General configuration ---------------------------------------------------

extensions = [
	"sphinx.ext.autodoc",
	"sphinx.ext.napoleon",
	"sphinx.ext.viewcode",
	"sphinx.ext.intersphinx",
	"sphinx.ext.autosummary",
]

autosummary_generate = True
autodoc_typehints = "description"
autodoc_member_order = "bysource"
napoleon_google_docstring = True
napoleon_numpy_docstring = False

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# Prefer the readthedocs theme if available, otherwise fall back to the default.
try:
	import sphinx_rtd_theme  # noqa: F401
	html_theme = "sphinx_rtd_theme"
except Exception:
	html_theme = "alabaster"

html_static_path = ["_static"]
html_title = f"{project} documentation"
html_show_sourcelink = True

# -- Intersphinx mapping ----------------------------------------------------

intersphinx_mapping = {
	"python": ("https://docs.python.org/3", None),
}

# -- Helpful helpers for local development -----------------------------------

# If you want to include modules that are not installed but live in the repo,
# adjust sys.path above or set autodoc_mock_imports to avoid import errors:
autodoc_mock_imports = []

# End of conf.py