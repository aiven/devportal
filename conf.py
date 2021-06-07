# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Aiven Developer'
copyright = '2021, Aiven Team'
author = 'Aiven Team'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_panels',
    'sphinxcontrib.mermaid',
    'sphinx_external_toc',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README*']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#FF3554",
        "font-stack": "Inter, sans-serif",
        "color-sidebar-brand-text": "#4a4b57",
        "color-foreground-primary": "#333333",
        "color-foreground-secondary": "#787885",
        "color-foreground-border": "#e1e1e3",
        "color-background-primary": "#e1e1e3",
        "color-background-secondary": "#ffffff",
        "color-content-foreground": "#787885",
        "color-background-hover": "#c60443",
        "color-background-border": "#e1e1e3",
        "color-highlighted-background": "#1c1c2f",
        "color-inline-code-background": "#787885",
        "color-sidebar-background": "#e1e1e3",
        "color-sidebar-background-border": "#e1e1e3",
        "color-sidebar-search-background": "#fff",
    },
    "dark_css_variables": {
        "color-brand-primary": "#ff3554",
        "font-stack": "Inter, sans-serif",
        "color-sidebar-brand-text": "#d2d2d6",
        "color-foreground-primary": "#ffffff",
        "color-foreground-secondary": "#83839d",
        "color-foreground-border": "#e1e1e3",
        "color-background-primary": "#11111e",
        "color-background-secondary": "#1c1c2f",
        "color-background-hover": "#ff3554",
        "color-background-border": "#e1e1e3",
        "color-highlighted-background": "#1c1c2f",
        "color-inline-code-background": "#f7f7fa",
        "color-sidebar-background": "#0b0b14",
        "color-sidebar-background-border": "#e1e1e3",
        "color-sidebar-search-background": "#1c1c2f",
    },
    "navigation_with_keys": True
}

pygments_style = "monokai"
pygments_dark_style = "monokai"

html_extra_path = ["robots.txt"]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['css/aiven.css']

# -- Replacements -----------------------------------------------------------
rst_epilog = """
.. |icon-postgres| image:: /images/icon-pg.svg
   :width: 24px
   :class: no-scaled-link

.. |icon-mysql| image:: /images/icon-mysql.svg
   :width: 24px
   :class: no-scaled-link

.. |icon-kafka| image:: /images/icon-kafka.svg
   :width: 24px
   :class: no-scaled-link

.. |icon-kafka-connect| image:: /images/icon-kafka-connect.svg
   :width: 24px
   :class: no-scaled-link

.. |icon-kafka-mirrormaker| image:: /images/icon-kafka-mirrormaker.svg
   :width: 24px
   :class: no-scaled-link

.. |icon-m3db| image:: /images/icon-m3db.svg
   :width: 24px
   :class: no-scaled-link

.. |icon-influxdb| image:: /images/icon-influxdb.svg
   :width: 24px
   :class: no-scaled-link

.. |icon-elasticsearch| image:: /images/icon-elasticsearch.svg
   :width: 24px
   :class: no-scaled-link

.. |icon-cassandra| image:: /images/icon-cassandra.svg
   :width: 24px
   :class: no-scaled-link

.. |icon-redis| image:: /images/icon-redis.svg
   :width: 24px
   :class: no-scaled-link

.. |icon-grafana| image:: /images/icon-grafana.svg
   :width: 24px
   :class: no-scaled-link

"""
