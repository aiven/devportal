====================================
Notes on what we are doing with Vale
====================================

  (This file may or may not be kept)

  (This ``.vale`` directory will be folded back into ``.github`` when work is finished, to make the configuration available to `vale-action`_)

.. _`vale-action`: https://github.com/errata-ai/vale-action

Notes
=====

Why we're not using the Vale style
----------------------------------

We dont want to use the Vale style (https://docs.errata.ai/vale/styles#built-in-style)

It provides 3 rules:

* Vale.Spelling
* Vale.Terms and Vale.Avoid - see https://docs.errata.ai/vale/vocab

We used to use `accept.txt` (see https://docs.errata.ai/vale/vocab) to indicate additional correct spellings, but that didn't work well as we added more styles, because words in `accept.txt` are added to the exceptions for various styles. Hence moving to our own (additional) dictionary.

Since we are using our own dictionary now (as well as the default one, see ``aiven_spelling.yml``) we do not need to rely on the Vale.Spelling rule.

``aiven_spelling`` and the ``aiven`` dictionary
-----------------------------------------------

Some notes on dictionaries.


The ``aiven`` dictionary is two files:

* ``aiven.dic`` - the actual words.

* ``aiven.aff`` - rules for use in the ``.dic`` file. These specify the meaning of the ``/X`` style "switches" om some of the words in the ``.dic`` file.

Remember that the first line of a ``.dic`` file must be the number of dictionary entries (the total number of lines in the file - 1).

Note that the ``.aff`` file is allowed to be empty if it is not needed.
    hunspell-how-to-specify-case-insensitivity-for-spell-check-in-dic-or-aff-file`

Vale and dictionary case (in)sensitivity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

By default, words specified in a Hunspell dictionary are case insensitive. So ``word`` would match ``word``, ``Word``, ``wOrD`` and other combinations. Similarly, ``TEXT`` would match ``text``, etc. This is discussed at `Hunspell - How to specify case-insensitivity for spell check in dic or aff file`_. For reference, the default ``en_US-web`` dictionary used by vale does not do anything special about this, so it is case-insensitive.

.. _`Hunspell - How to specify case-insensitivity for spell check in dic or aff file`:
    https://stackoverflow.com/questions/33880247/

.. note:: In theory we could put ``KEEPCASE K`` in the ``aiven.aff`` file, and specify a word as ``/K`` in the ``aiven.dic`` file. However, looking at the source code in ``vale/pkg/spell/aff.go`` shows that vale ignores any ``KEEPCASE`` directives.

How vale works with the dictionary:

* If the word is just specified as lower case (in either or both dictionaries), then any case will match.

* If the word is specifed as lower case and mixed case (either in the same or separate dictionaries), then any case will match.

* If the word is just specifed as mixed case (in either or both dictionaries), then the match must be mixed case, but it need not be the *same* mixed case.

Summarising:

+-------------------------+------------+------------+
|                         | Aiven dictionary        |
|         matches         +------------+------------+
|                         | lower case | mixed case |
+------------+------------+------------+------------+
| default    | lower case | any case   | any case   |
| dictionary +------------+------------+------------+
|            | mixed case | any case   | mixed case |
+------------+------------+------------+------------+


Case studies:

* The default dictionary has ``abecedary``::

    $ vale --output=line "abecedary Abecedary abeCEdary"

   (no errors)

   and if I add ``Abecedary`` to the Aiven dictionary::

    $ vale --output=line "abecedary Abecedary abeCEdary"

* The default dictionary has ``Abba`` and ``abba``::

    $ vale --output=line "abba Abba ABBA aBBa"

  (no errors)

  It doesn't make a difference if I also add ``Abba`` or ``abba`` to the Aiven dictionary.

* The default dictionary has ``Aberdonian``::

    $ vale --output=line "Aberdonian aberdonian aberDOnian"
    stdin.txt:1:12:Aiven.aiven_spelling:'aberdonian' seems to be a typo

  and if I add ``aberdonian`` to the Aiven dictionary::

    $ vale --output=line "Aberdonian aberdonian aberDOnian"

  so that *did* make a difference - it made it case-insensitive, as one might hope.


Useful links about hunspell dictionaries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Useful links to learn about Hunspell compatible dictionaries (for that is what this is):

**Note** *This list needs curation to work out if it's all useful to other people or not.*

* http://hunspell.github.io/

  "Hunspell is the spell checker of LibreOffice, OpenOffice.org, Mozilla Firefox 3 & Thunderbird, Google Chrome, and it is also used by proprietary software packages, like macOS, InDesign, memoQ, Opera and SDL Trados."

* http://manpages.ubuntu.com/manpages/trusty/man4/hunspell.4.html

  "hunspell - format of Hunspell dictionaries and affix files"

  https://linux.die.net/man/4/hunspell is another rendering of the same manpage.

* https://zverok.github.io/blog/2021-03-16-spellchecking-dictionaries.html

  "17 (ever so slightly) weird facts about the most popular dictionary format"

  I found this useful.

  It's part of a series "striving to explain how the world’s most popular spellchecker Hunspell works via its Python port called ****Spylls****"

  https://zverok.github.io/spellchecker.html is the series content page

* http://web.archive.org/web/20130810100226/http://www.suares.com/index.php?page_id=25&news_id=233

  saved page on how to create a new dictionary (both files) from scratch

  This references:

  * http://www.openoffice.org/lingucomponent/affix.readme which describes the ``.aff`` file format

* https://www.quora.com/How-do-the-Hunspell-dictionaries-work seems to be a decent introduction


``common_replacements``
-----------------------

Notes on the ``common_replacements`` style (extending ``substitution``) are in the file itself.

``first_<Word>_is registered`` checks
-------------------------------------

These extend ``conditional`` to check that there is at least one ``<Word>®`` if there are any occurrences of ``<Word>``.

Inside vale, ``first`` is termed the *antecedent*, and ``second`` is termed the *consequent*. I think of ``first`` as the *usage* and ``second`` as the *explanation*.

Each needs to specify one *capture group* (the part of the pattern with ``(`` and ``)``) which will be used as the match for that pattern.

    What vale actually does is:

    1. Find all occurrences of text fragments that match ``second``, the *consequent* or *explanation*, and remember their locations.
    2. Find all occurrences of text fragments that match ``first``, the *antecedent* or *usage*. For each, look to see if the matched string is in any of the strings found in (1) (or in the list of exceptions, but we're ignoring that for now)

    So for their ``WHO`` example:

    * It looks for all occurrences of the ``second`` expression, which is ``<capitalised-word-sequence> (<3-to-5-capital-letters>)``. The capture group is the ``<3-to-5-capital-letters>``.

      * It finds the text ``World Health Organization (WHO)`` and remembers ``["WHO"]`` (that's one capture group, which it remembers in a list)

    * It then looks for occurrences of the ``first`` expression, which is ``<3-to-5-capital-letters>``. Again, the capture group is the ``<3-to-5-capital-letters>``.

      * It finds ``["WHO", "WHO", "DAFB"]`` - one "WHO" in "World Health Organization (WHO)", the standalone "WHO", and the standalone "DAFB"

    * It goes through that second sequence:

      * It looks for "WHO" in each of the strings in the list of ``second`` matches, and finds it
      * It looks for "WHO" in each of the strings in the list of ``second`` matches, and finds it
      * It looks for "DAFB" in each of the strings in the list of ``second`` matches, and does not find it

    * So it produces an error for "DAFB"

    (Why not remove duplicate entries from that list of ``first`` matches? Because if a term *doesn't* match, we want to report an individual error for each one.)

    It's important to understand the details of how this works, because:

    a. it determines what sort of text / regular expression is needed for each of ``first`` and ``second``
    b. it explains why (at the moment) there's no ordering constraint on whether ``second`` needs to come before or after ``first``

    So for the ``Flink®`` case, ``first`` must match the *usage*, the word "``Flink``" whether it is followed by the "``®``" or not, and ``second`` must match the *explanation*, the word "``Flink``" followed by the "``®``" character,

.. note:: **Note to self** the ``vale/internal/check/conditional.go`` method ``Run`` seems to be called multiple times for a file, looping:

          * for each file

            * for a gradually changing "block" - this starts as all the text in the file, and then gradually replaces blocks/elements of the text, from the start, with ``@`` - for instance, the title, then the title and the first paragraph, then the title and the first two paragraphs, and so only

              * for each conditional check

          I don't (as yet) understand the point of that "block" loop.

See `Error matching when characters like ® are present in the text`_ for the problem that is holding this up.

See `conditional rules are not ordered`_ for why that doesn't do quite what we want (we'd like it to require the occurrence with ``®`` comes first).

We have one file for each ``<Word>`` - for instance, for ``Flink``, ``Kafka``, etc. We could (perhaps) make a combined file with a complicated conditional regular expression, but that would be a lot harder to interpret. One file per word is easy to maintain.

* These are errors, because we need to get it right.
* We do not ignore case, because it's only the correctly cased version of the word we care about.

Because ``®`` is not a word character, we have to check for ``first`` being the word that is explicitly not followed by ``®``.

Note that the rules for ``Redis`` (needs ``™*``, and it's OK for the ``*`` not to be superscripted) and ``Apache`` (only needs ``®`` if it's not followed by one of the sub-product names) will be different.

One day it might be nice to be able to recognise a correct use in a header that comes before all uses in body text, but that's a task for another day (and might not be possible in vale anyway).

Trademarky things
-----------------

Temporary list from the internal page:

* Kafka®
* Flink®
* Cassandra®
* ClickHouse®
* OpenSearch®
* PostgreSQL®
* Redis™*
* InfluxDB®
* Grafana®
* Kubernetes®

Plus checking for ``Aiven for <name>`` instead of ``Aiven <name>`` (the former is correct) and also checking for ``Apache®`` when ``Apache`` is *not* followed by a product name (this *may* require listing all the product names in a regular expression, or may just mean checking for ``Apache <capitalised-word>``, which is probably good enough as a first pass).

Test files
----------

In the directory ``.vale/tests`` there are pairs of files, with names that contain ``good`` and ``bad``.

The intention is that when vale is run on a ``good`` file, there should be no errors, and when it is run on a ``bad`` file there should be at least one error per significant line (that is, ignoring comments, which should be evident, and blank lines).

In the case of the ``good.rst`` versus ``bad.rst`` files, inline "comments" are used to indicate what sort of error is meant to be triggered by each line in the ``bad`` file (they're not real inline comments because reStructuredText doesn't have those).

I recommend using ``vale --output=line`` for its more compact output format.

As an experiment, I have introduced testing with shelltestrunner_. See the file ``.vale/test/shelltest.test``. This makes it a lot easier to see the effect of changes I make to the vale setup.

  There's also a similar program, shtst_, if you prefer a Python script (or something that is ``pip install``-able). The test file syntax is very similar. I'm continuing with shelltest because it is more mature, and also because I find the ``--diff`` switch useful (which shtst does not have).

.. _shelltestrunner: https://github.com/simonmichael/shelltestrunner
.. _shtst: https://github.com/obfusk/shtst

Known or possible issues
========================

Error matching when characters like ``®`` are present in the text
-----------------------------------------------------------------

This is the problem I've been having with trying to match conditionals for ``®`` and ``™`` checking.

Characters like ``®`` or ``™`` (U+00AE and U+2122) seem to cause match offset calculations to go wrong.

For instance::

    $ vale --output=line 'World Health Organization (WHO) (R) and WHO or WHO'

but::

    $ vale --output=line 'World Health Organization (WHO) ® and WHO or WHO'
    stdin.txt:1:28:Test.WHO_example:'WHO' has no definition
    stdin.txt:1:39:Test.WHO_example:'WHO' has no definition

I've raised `Vale issue 410`_ with the details on this.

.. _`Vale issue 410`: https://github.com/errata-ai/vale/issues/410

``conditional`` rules are not ordered
-------------------------------------

  *May be a bug of just a feature request, report later.*

That is, a ``conditional`` rule asserts that if there is an occurrence of (text matching) ``first``, then there must also be at least one occurrence of (text matching) ``second``, which contains the string found by ``first``.

  **NOTE** see `first_<Word>_is registered checks`_ for an explanation of how ``conditional`` actually works.

The example given in the documentation (for ``WHO`` and its expansion/explanation) implies that ``second`` might be expected to come first, but this is not actually required by the code.

When I've got vale working as we wish, I expect to raise an issue asking that it be possible to request that ordering, since we want to be able to require ``Term®`` comes before ``Term``.

More documentation (and examples) needed for ``conditional``
------------------------------------------------------------

It turns out this is quite hard to think about! And getting the regular expressions right for non-trivial cases (like registered cases, and *especially* the Redis case) is also non-trivial.

  **NOTE** see `first_<Word>_is registered checks`_ for an explanation of how ``conditional`` actually works.

Strange behaviour of sentence case
----------------------------------

    *I've yet to prove this is an actual issue, and not something I'm doing wrong.*

In the ``.vale/tests/sentence_case_title_good.rst`` file, some titles are being treated as errors, when one would not expect it. For instance, the title ``Not Aiven`` is an eror, but the title ``Aiven®`` is OK, and longer titles with names in them (that is, capitalised dictionary words) are OK.

I'm going to leave this for the moment and concentrate on other things, and come back to it later to see if I can either work out what is going on, or work out a minimal test case.

It is possible that this may be related to `Vale issue 410`_

Missing documentation for dictionary ``append``
-----------------------------------------------

  *Worth doing a PR for.*

There is no documentation for the ``append`` option of the ``spelling`` style.

It's quite an important option, as setting it ``true`` allows appending a dictionary to the default, rather than replacing it.

No error for a file that doesn't exist
--------------------------------------

    *This doesn't affect our real world use of vale, and may not be either fixable or worth fixing.*

If I do ``vale <file-that-does-not-exist>`` I get no errors, and a status code of 0.

Given vale is meant to be used over a directory structure, I'm not sure this is something that will get "fixed".

No error for broken reStructuredText
------------------------------------

    *I'd rather like a fix for this. A quick look at the code suggests a PR might not be too hard.*

When there are syntax errors in reStructuredText, it seems that the file gets ignored. This looks just the same as having no vale errors in the file.

Vale checks reStructuredText by first running it through ``rst2html.py``. A quick check suggests that if I do ``rst2html.py <name>.rst > <name>.html``, I still get status code ``0`` if there is an error, but I also get error text written to ``stderr``. So it should, in principle, be possible to tell if something went wrong. (vale probably doesn't want to report the errors as such.)

Note: the source code appears to be fairly obviously just ignoring ``stderr``. It's possible that fixing this might be fairly simple, *except* that Windows also needs supporting, and I don't know how it handles ``stderr``.

The order of error output does not appear to be deterministic
-------------------------------------------------------------

    *This makes it harder to test things, for instance using shelltester*

For instance, if I run ``vale --output=line .vale/tests/bad.rst``, the order of the lines output is not consistent.
