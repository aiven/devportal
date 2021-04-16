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

Your preview should be at http://localhost:8000 (if anything doesn't seem to re-render well, the navigation seems particularly unreliable, try ``make clean`` and then ``make livehtml`` again).

Making changes
--------------

Please make changes! Even small fixes are very welcome. The content is in the ``docs/`` folder, in `ReStructuredText <https://docutils.sourceforge.io/rst.html>`_.

When you open a pull request, you will get a preview of your changes (useful if you or someone you want to show the work to does not have the tool set up locally). The process also runs some spelling and link checking tasks. You can also run those locally:

* Check links: ``make linkcheck``
* Check spelling: ``make spell``

If the spellchecker is rejecting words that are valid (such as technology terms), double check the spelling and capitalisation, then add the word to ``.github/workflows/styles/Docs/accept.txt``.

License
-------

This work is licensed under a
`Creative Commons Attribution 4.0 International License <http://creativecommons.org/licenses/by/4.0/>`_.

