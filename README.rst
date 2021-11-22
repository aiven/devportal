Aiven Developer
===============

This is the source for the Aiven developer documentation at https://developer.aiven.io. We are working to move all of our technical documentation to this platform, and welcome issues and pull requests from everyone.

It is Python-based, with content in `ReStructuredText (rst) <https://docutils.sourceforge.io/rst.html>`_ and rendered by `Sphinx <https://www.sphinx-doc.org/en/master/>`_.

Running locally
---------------

We recommend using a virtual environment like `venv <https://docs.python.org/3/library/venv.html>`_:

    python3 -m venv /path/to/new/virtual/environment

If you call it something other than `venv`, add your preferred name to `<.gitignore>`_.

Install the dependencies::

    pip install -r requirements.txt

Start the HTML version with::

    make livehtml

Your preview should be at http://localhost:8000 (if anything doesn't seem to re-render well, the navigation seems particularly unreliable, try ``make clean`` and then ``make livehtml`` again).

> If you are working on the templates, try the additional `make livehtmlall` command. This disables sphinx's incremental build and also observes changes to the assets, so it's slower but more like a full rebuild when things change.

Windows users
-------------

Replace all `make` commands with `./make` - this uses the `make.bat` file instead of `Makefile` but the functionality should be equivalent.

Making changes
--------------

Please make changes! Even small fixes are very welcome. The content is in the ``docs/`` folder, in `ReStructuredText <https://docutils.sourceforge.io/rst.html>`_.

When you open a pull request, you will get a preview of your changes (useful if you or someone you want to show the work to does not have the tool set up locally). The process also runs some spelling and link checking tasksi so please check the output of the build if it fails.

Running build tasks locally
---------------------------

To run the spell check locally, you will need to have `Vale <https://github.com/errata-ai/vale>`_ installed on your computer and available on your path.

* Check links: ``make linkcheck``
* Check spelling: ``make spell``

If the spellchecker is rejecting words that are valid (such as technology terms), double check the spelling and capitalisation, then add the word to ``.github/styles/Vocab/Docs/accept.txt``.

Navigation Structure
~~~~~~~~~~~~~~~~~~~~

The left-hand navigation menu is driven by a plugin called `Sphinx external TOC <https://sphinx-external-toc.readthedocs.io/en/latest/intro.html>`_. You can find our structure in ``_toc.yml``.

Links
~~~~~

Links are different depending on whether they are external links, links pointing to a specific page on the site, or links pointing to a specific anchor or label.

External links are used for external hyperlinks::

    `ReStructuredText <https://docutils.sourceforge.io/rst.html>`_

To link to another page on the site, use the `:doc: <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#cross-referencing-documents>`_ role::

    Use the :doc:`cli` for scriptable, repeatable actions with Aiven


The ``:doc:`` role uses the page title but if you want to change the link text, you can do so::

    With an :doc:`API <api/index>` you can build any integration you choose

To create a label to link to a particular section (this is also useful if renaming titles that might have links pointing to the old wording), place the label immediately before the section heading::

    .. _tools_cli_tips_tricks:

    Tips and Tricks
    ===============

Then you can refer to the label with a `:ref: <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#cross-referencing-arbitrary-locations>`_ entry::

    There are some :ref:`_tools_cli_tips_tricks` to assist you.


Diagrams
~~~~~~~~

Diagrams use `sphinxcontrib-mermaid <https://github.com/mgaitan/sphinxcontrib-mermaid>`_ and `mermaid.js <https://mermaid-js.github.io/mermaid/#/>`_ syntax.

Importing content
~~~~~~~~~~~~~~~~~

Some of the content for DevPortal came from a previous incarnation of documentation. There is an import script to help with this process.

To set up the import tooling for the first time:

* Install `pandoc <https://pandoc.org/>`_ and make sure the command is in your path
* Change into the ``utils/`` directory
* Run ``pip install -r requirements.txt``

To bring in a page from the previous platform:

* Run ``python import-help-articles.py [paste a URL]``
* Take the resulting ``*.rst`` file and any images, and place them as appropriate in the file structure of the project

License
-------

This work is licensed under a
`Creative Commons Attribution 4.0 International License <http://creativecommons.org/licenses/by/4.0/>`_.
