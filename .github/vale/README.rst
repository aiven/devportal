===============================
Introduction to our use of Vale
===============================

.. contents::

What is Vale?
=============

According to its website at https://vale.sh/, "Vale is an open-source, command-line tool that brings your editorial style guide to life."

It provides spell checking, but also allows the definition and use of "styles", which can be used to look for common mistakes in text.

Vale runs on Mac, Linux and Windows, and instructions for downloading it, for all three platforms, are at https://vale.sh/docs/vale-cli/installation/

We *use* Vale in two ways:

1. At the command line, with the ``make spell`` command - this checks the top-level ``index.rst`` file, and all the ``.rst`` files in the ``docs`` directory.
2. In a GitHub action, which is run automatically in PRs.

If you get an error running ``vale``
------------------------------------

Occasionally, when running the ``vale`` command (for instance, via ``make spell``) you may get an error like::

  E100 [docs/platform/concepts/cloud-security.rst] Runtime error

  Post "http://localhost:7069": dial tcp [::1]:7069: connect: connection refused

If so, just run the command again - it appears to be transtory.

The organisation of our Vale setup
==================================

The top-level file ``.vale.ini`` specifies

* where the vale style files can be found (``.github/vale/styles``)
* what files to check (``.rst`` files)
* what styles to use (our own ``Aiven`` style)

We store the details of our vale configuration in ``.github/vale``.

The GitHub action's workflow is specified in ``.github/workflows/link.yaml``.

.. _vale-action: https://github.com/errata-ai/vale-action

**Note** there is also an `issues <ISSUES.rst>`_ file that describes possible future work.

Common replacements
===================

The file `<styles/Aiven/common_replacements.yml` provides corrections for things we think are likely to be common mistakes. This includes common misspellings (``kakfa`` instead of ``Kafka``), getting capitalisation wrong (it should be ``ClickHouse``), and forgetting the ``for`` in ``Aiven for <product>``.


Sentence case headings
======================

Our style guide says that headings should be in "Sentence case". The `<styles/Aiven/capitalization_headings.yml>`_ file contains the rules and exceptions for this.

Why exceptions? Vale doesn't actually insist that "Sentence case" titles contain *no* capitalised words after the first, but the way it calculates what to allow is not obvious, so sometimes it is necessary to add exceptions, to say "it is OK for this word to be capitalised in a title".


Spell checking
==============

Vale ships with an American dictionary (the source is at https://github.com/errata-ai/en_US-web).

The file `<styles/Aiven/aiven_spelling.yml>`_ adds our own dictionary, so that we can define extra vocabulary.
This Aiven dictionary is specified in the file `<dicts/aiven.dic>`_.

Vale will look in the default dictionary first, and then in the Aiven dictionary.

If you need to edit the Aiven dictionary
----------------------------------------

The very first line of `<dicts/aiven.dic>`_ is a count of the number of entries. Please try to keep it up-to-date.

If you don't care about the case of the word, then just put it in the dictionary in lower-case. For instance, ``fakeword`` will match ``fakeword``, ``Fakeword`` and ``fakeWORD``.

If you enter the word in ``mixedCase``, then it won't match a lower-case word, but it also won't forbid the "wrong" mixed-case (for instance, ``MixedCase``). If you care about the specific use of capital letters in a word, it's better to use the `Common Replacements`_ file to be specific about the

We try not to add words that are actually commands, for instance ``jq`` or ``wget``.

Checking registered trademark usage
===================================

It is correct and polite to put the ``®`` (registered trademark) character after particular product names, in at least the first and most prominent use on a page. Style files with names like `<styles/Aiven/first_Flink_is_registered.yml` check for this.

``*Note:** they're not perfect yet, so may not always catch all cases, and may not insist that the product name with ``®`` comes *before* other uses. We will be making improvements in this area.

Test files
==========

Some simple testing of our Aiven style is provided.

In the directory `<tests>`_ there are pairs of files, with names that contain ``good`` and ``bad``.

When Vale is run on a ``good`` file, there should be no errors, and when it is run on a ``bad`` file there should be at least one error per line (ignoring comments and blank lines).

I recommend using ``vale --output=line`` for its more compact output format.

To make it easier to see changes and regressions, the file ``.vale/test/shelltest.test`` can be used with
shelltestrunner_.

For instance::

  brew install shelltestrunner
  shelltest --diff .github/vale/tests/shelltest.test

.. _shelltestrunner: https://github.com/simonmichael/shelltestrunner
