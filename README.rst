Aiven Developer
===============

This is a work in progress.

The site will be a place to hold all our developer-facing content.

It is Python-based, with content in `ReStructuredText (rst) <https://docutils.sourceforge.io/rst.html>`_ and rendered by `Sphinx <https://www.sphinx-doc.org/en/master/>`_.

Running locally
---------------

Install the dependencies::

    pip install -r requirements.txt

Start the HTML version with::

    make livehtml

(if anything doesn't seem to re-render well, the navigation seems particularly unreliable, try ``make clean`` and then ``make livehtml`` again).

License
-------

This work is licensed under a
`Creative Commons Attribution 4.0 International License <http://creativecommons.org/licenses/by/4.0/>`_.

