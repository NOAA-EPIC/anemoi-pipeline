# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Anemoi Pipeline'
copyright = '2024, EPIC'
author = 'EPIC'
release = 'develop'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    #'sphinxcontrib.bibtex',
]

# bibtex_bibfiles = ['references.bib']

numfig = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

templates_path = ['_templates']
exclude_patterns = []

html_theme_options = {
    "body_max_width": "none", 
    "navigation_depth": 4,
    }


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
