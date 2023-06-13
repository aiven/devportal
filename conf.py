# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from dotenv import load_dotenv
load_dotenv()

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Aiven Docs'
copyright = '2022, Aiven Team'
author = 'Aiven Team'
html_title = 'Aiven'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_sitemap',
    'sphinx_design',
    'sphinxcontrib.mermaid',
    'sphinx_external_toc',
    'sphinx_copybutton',
    'sphinx_gitstamp',
    'sphinxext.opengraph',
    'notfound.extension',
    'override_canonical',
]

# Not Found configuration
# see all options at https://sphinx-notfound-page.readthedocs.io/en/latest/configuration.html
notfound_urls_prefix = ''

# OpenGraph configuration
# see all options at https://github.com/wpilibsuite/sphinxext-opengraph#options
ogp_site_url = 'https://docs.aiven.io/'
ogp_description_length = 200
ogp_image = 'https://docs.aiven.io/_static/images/site-preview.png'

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
    '.github/vale', '.venv', 'venv',
]

# gitstamp config
gitstamp_fmt = "%B %Y"

# sitemap config
html_baseurl = 'https://docs.aiven.io'
# Since we have `language='en'` set (further down) the URLs in the sitemap will
# default to "{version}{lang}{link}", producing things like
#    <url><loc>https://docs.aiven.io/en/docs/platform/howto/create_authentication_token.html</loc></url>
# That doesn't work because we do not produce pages with the `/en` in the URL.
# We need to be explicit that we don't want {version} or {language} in the URLs
sitemap_url_scheme = "{link}"

# ``make linkcheck`` is not perfect.
# The following pages are known to cause it problems.
linkcheck_ignore = [
    # Kafka documentation anchors do not seem to be detected. We use the following:
    'https://kafka.apache.org/documentation/#consumerconfigs_auto.offset.reset',
    'https://kafka.apache.org/documentation/#design_consumerposition',
    # Azure Marketplace uses internal links which confuses the checker, so ignoring these:
    'https://portal.azure.com/#view/Microsoft_Azure_Marketplace/MarketplaceOffersBlade/selectedMenuItemId/home',
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_favicon = './_static/images/favicon.ico'
html_theme = 'furo'
html_theme_options = {
    "light_logo": "images/logoLightPride.png",
    "dark_logo": "images/logoDarkPride.png",
    "light_css_variables": {
        "color-brand-primary": "#FF5200",
        "color-brand-content": "#343745",
        "color-link": "#007cc2",
        "color-link--hover": "#016BB2",
        "color-sidebar-link-text": "#343745",
        "color-sidebar-link-text--top-level": "#343745",
        "font-stack": "Inter, sans-serif",
        "color-sidebar-brand-text": "#343745",
        "color-sidebar-background-hover": "#F8F9FB",
        "color-sidebar-item-background--hover": "#F8F9FB",
        "color-foreground-primary": "#333333",
        "color-foreground-secondary": "#4f5366",
        "color-foreground-muted": "#4f5366",
        "color-foreground-border": "#EDEDF0",
        "color-background-primary": "#ffffff",
        "color-background-secondary": "#f7f7fa",
        "color-content-foreground": "#4f5366",
        "color-background-hover": "#c60443",
        "color-background-border": "#EDEDF0",
        "color-highlighted-background": "#1c1c2f",
        "color-inline-code-background": "#4f5366",
        "color-sidebar-background": "#FFFFFF",
        "color-sidebar-background-border": "#EDEDF0",
        "color-sidebar-search-background": "#fff",
        "sd-color-card-background": "#f7f7fa",
        "sd-color-primary": "#343745",
        "sidebar-tree-space-above": "8px",

        # Custom css variables
        "color-search": "#19191D",
        "color-search-focused": "#4A4B57",
        "color-search-border": "#B4B4BB",
        "color-search-border-focused": "#4F5366",
        "color-search-container-outline-focused": "#B4E5FB",
        "color-search-background": "#FFFFFF",
        "color-sidebar-search-icon": "#B4B4BB",
        "color-topnav-background": "#FFFFFF",
        "color-topnav-border": "#EDEEF3",
        "color-topnav-link": "#1A1B22",
        "color-topnav-theme-toggle-border": "rgba(0, 0, 0, 0.1)",
        "color-topnav-button-primary": "#FFFFFF",
        "color-topnav-button-primary-hover": "#FFFFFF",
        "color-topnav-button-primary-background": "#FF5200",
        "color-topnav-button-primary-hover-background": "#F04D00",
        "color-topnav-button-secondary": "#1A1B22",
        "color-topnav-button-secondary-border": "#B4B7C5",
        "color-topnav-button-secondary-hover": "#1A1B22",
        "color-topnav-button-secondary-hover-border": "#4F5366",
        "color-topnav-button-secondary-hover-background": "transparent",
        "color-toc-item-text--active": "#007cc2",
        "color-highlight-on-target": "#EDEEF3",
    },
    "dark_css_variables": {
        "color-brand-primary": "#FF5200",
        "color-brand-content": "#ffffff",
        "color-link": "#6DCDF8",
        "color-link--hover": "#3DBBF5",
        "font-stack": "Inter, sans-serif",
        "color-sidebar-brand-text": "#D2D2D6",
        "color-sidebar-background-hover": "#161825",
        "color-sidebar-item-background--hover": "#161825",
        "color-sidebar-link-text": "#D2D2D6",
        "color-sidebar-link-text--top-level": "#D2D2D6",
        "color-foreground-primary": "#ffffff",
        "color-foreground-secondary": "#D2D2D6",
        "color-foreground-muted": "#D2D2D6",
        "color-foreground-border": "#3A3A44",
        "color-background-primary": "#11111e",
        "color-background-secondary": "#1c1c2f",
        "color-content-foreground": "#D2D2D6",
        "color-background-hover": "#ff3554",
        "color-background-border": "#3A3A44",
        "color-highlighted-background": "#1c1c2f",
        "color-inline-code-background": "#f7f7fa",
        "color-sidebar-background": "#11111E",
        "color-sidebar-background-border": "#3A3A44",
        "color-sidebar-search-background": "#1c1c2f",
        "color-admonition-title-background--tip": "#00c85240",
        "color-admonition-title-background--note": "#00b0ff40",
        "color-admonition-title-background--warning": "#ff910040",
        "color-admonition-title-background--error": "#ff525240",
        "sd-color-card-background": "#0b0b14",
        "sd-color-card-header": "#0b0b14",
        "sd-color-primary": "#3A3A44",
        "sidebar-tree-space-above": "8px",

        # Custom css variables
        "color-search": "#F7F7FA",
        "color-search-focused": "#FFFFFF",
        "color-search-border": "#3A3A44",
        "color-search-border-focused": "#7FD1F7",
        "color-search-container-outline-focused": "#0174BA",
        "color-search-background": "#11111E",
        "color-sidebar-search-icon": "#F7F7FA",
        "color-topnav-background": "#0B0B14",
        "color-topnav-border": "#3A3A44",
        "color-topnav-link": "#F7F7FA",
        "color-topnav-theme-toggle-border": "rgba(255, 255, 255, 0.1)",
        "color-topnav-button-primary": "#FFFFFF",
        "color-topnav-button-primary-hover": "#FFFFFF",
        "color-topnav-button-primary-background": "#FF5200",
        "color-topnav-button-primary-hover-background": "#F04D00",
        "color-topnav-button-secondary": "#f7f7fa",
        "color-topnav-button-secondary-border": "#f7f7fa",
        "color-topnav-button-secondary-hover": "#f7f7fa",
        "color-topnav-button-secondary-hover-border": "#f7f7fa",
        "color-topnav-button-secondary-hover-background": "transparent",
        "color-toc-item-text--active": "#6DCDF8",
        "color-highlight-on-target": "#EDEEF3",
    },
    "navigation_with_keys": True
}

pygments_style = "monokai"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
language = "en"
html_extra_path = ['robots.txt', '_redirects']
html_static_path = ['_static']
html_css_files = ['css/aiven.css']
html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/mobile-header.html",
        "sidebar/mobile-search.html",
        "sidebar/navigation.html",
        "sidebar/mobile-actions.html",
        "sidebar/scroll-end.html",
    ]
}

# -- Replacements -----------------------------------------------------------
rst_epilog = """
.. |icon-challenge-trophy| image:: /images/community/challenge-trophy.svg
   :width: 24px
   :class: no-scaled-link

.. |icon-twitter| image:: /images/social_media/icon-twitter.svg
   :width: 24px
   :class: no-scaled-link

.. |icon-github| image:: /images/social_media/icon-github.svg
   :width: 24px
   :class: no-scaled-link

.. |icon-blog| image:: /images/social_media/icon-blog.svg
   :width: 24px
   :class: no-scaled-link

.. |icon-youtube| image:: /images/social_media/icon-youtube.svg
   :width: 24px
   :class: no-scaled-link

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

.. |beta| replace:: :bdg-secondary:`beta`

.. |preview| replace:: :bdg-secondary:`preview`

"""

html_context = {
   'api_url_search': os.getenv('API_URL_SEARCH'),
   'api_url_create_feedback': os.getenv('API_URL_CREATE_FEEDBACK')
}
