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
html_title = 'Aiven'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_sitemap',
    'sphinx_panels',
    'sphinxcontrib.mermaid',
    'sphinx_external_toc',
    'sphinx_copybutton',
    'sphinx_gitstamp',
    'sphinxext.opengraph',
    'notfound.extension',
]

# Not Found configuration
# see all options at https://sphinx-notfound-page.readthedocs.io/en/latest/configuration.html
notfound_urls_prefix = None

# OpenGraph configuration
# see all options at https://github.com/wpilibsuite/sphinxext-opengraph#options
ogp_site_url = 'https://developer.aiven.io/'
ogp_description_length = 200
ogp_image = '/_static/images/site-preview.png'

# Mermaid version
mermaid_version = "8.12.0"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build', 'Thumbs.db', '.DS_Store', 'README*', 'scripts', 'utils',
    'CONTRIBUTING.rst', 'REVIEWING.rst', 'includes',
    '.github/vale'
]

# gitstamp config
gitstamp_fmt = "%B %Y"

# sitemap config
html_baseurl = 'https://developer.aiven.io'
# Since we have `language='en'` set (further down) the URLs in the sitemap will
# default to "{version}{lang}{link}", producing things like
#    <url><loc>https://developer.aiven.io/en/docs/platform/howto/create_authentication_token.html</loc></url>
# That doesn't work because we do not produce pages with the `/en` in the URL.
# We need to be explicit that we don't want {version} or {language} in the URLs
sitemap_url_scheme = "{link}"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_favicon = './_static/images/favicon.ico'
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

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
language = "en"
html_extra_path = ['robots.txt']
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

.. |icon-opensearch| image:: /images/icon-opensearch.png
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

.. |icon-flink| image:: /images/icon-flink.svg
   :width: 24px
   :class: no-scaled-link

.. |icon-clickhouse| image:: /images/icon-clickhouse.svg
   :width: 24px
   :class: no-scaled-link

.. |tick| image:: /images/icon-tick.png
   :width: 24px
   :class: no-scaled-link

"""
