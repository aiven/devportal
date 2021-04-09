# Aiven Developer

This is a work in progress.

The site will be a place to hold all our developer-facing content.

It is Python-based, with content in `ReStructuredText (rst)<https://docutils.sourceforge.io/rst.html>`_ and rendered by `Sphinx<https://www.sphinx-doc.org/en/master/>`_.

## Running locally

Install the dependencies::

    pip install -r requirements.txt

Start the HTML version with::

    make livehtml

(if anything doesn't seem to re-render well, the navigation seems particularly unreliable, try ``make clean`` and then ``make livehtml`` again).

## License

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
