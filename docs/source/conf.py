# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import os

on_rtd = os.environ.get('READTHEDOCS') == 'True'

if not on_rtd:
    import sys
    sys.path.insert(0, "../../salt_nornir/")

# -- Project information -----------------------------------------------------

project = 'salt-nornir'
copyright = '2022, Denis Mulyalin'
author = 'Denis Mulyalin'

# The full version, including alpha/beta/rc tags
release = '0.11.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
'sphinx.ext.autodoc',
'sphinx.ext.napoleon',
'sphinx.ext.autosectionlabel',
'sphinxcontrib.spelling',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# use index.rst instead of contents.rst:
master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# spelling check parameters
spelling_lang='en_US'
tokenizer_lang='en_US'
spelling_word_list_filename='spelling_wordlist.txt'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
if not on_rtd:
    html_theme = 'classic'
else:
    html_theme = 'sphinx_rtd_theme'
    # add level to nav bar - https://stackoverflow.com/questions/27669376/show-entire-toctree-in-read-the-docs-sidebar
    # and this - https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html#table-of-contents-options
    html_theme_options = {
        'navigation_depth': 4,
        'collapse_navigation': True,
        'sticky_navigation': False
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# to make crossreferencing section names between documents work
autosectionlabel_prefix_document = True
