========================
Notes on how we use Vale
========================

.. contents::


**Note** there is a separate file for `issues <ISSUES.rst>`_ that we might want to fix, both in our use of vale and in vale itself.

The main vale websites are:

* https://github.com/errata-ai/vale/
* https://docs.errata.ai/vale/

and the related:

* https://github.com/errata-ai/vale-action


The organisation of our vale setup
==================================

The top-level file ``.vale.ini`` specifies

* where the vale style files can be found (``.github/vale/styles``)
* what files to check (at the moment, ``.rst`` files)

We store the rest of our vale configuration in the ``.github`` directory, as suggested by `vale-action`_.

The vale-action workflow is specified in ``.github/workflows/link.yaml`` - this determines what checks are run by github when you make a PR, etc.

The rest of the vale specific files are in ``.github/vale``. vale-actions suggests using ``.github/styles`` for the style files, but we also have a README, dictionaries and tests, so it seems sensible to add a specific vale subdirectory.

.. _vale-action: https://github.com/errata-ai/vale-action

Styles
======

Spelling
--------

``.github/vale/styles/Aiven/aiven_spelling.yml``

::

  extends: spelling
  message: "'%s' seems to be a typo"
  # The dictionary directory path appears to be relative to the .vale.ini file
  dicpath: .github/vale/dicts
  # We want to add our dictionary on top of the default dictionary
  append: true
  dictionaries:
    - aiven

This file:

1. Says where to look for local dictionaries (``.github/vale/dicts``)
2. Specifies the message to use when a spelling mistake / typo is discovered
3. Says to *append* the ``aiven`` dictionary to the default dictionary.

For more on dictionaries, see `Dictionaries`_ below.


Capitalised headings
--------------------

``.github/vale/styles/Aiven/capitalization_headings.yml``

We want headings to be in sentence case. ::

  extends: capitalization
  message: "'%s' should be in sentence case"
  level: warning
  scope: heading
  # $title, $sentence, $lower, $upper, or a pattern.
  match: $sentence
  exceptions:
    - HowTo

Internally, this calculates a metric for the title "sentence", and fails it if its score is too low. The code is in the method ``sentence`` in ``vale/internal/check/variables.go`` (it's called from a function created by ``NewCapitalization`` in ``vale/internal/check/capitalization.go``).

**TODO: tidy the following up into something that makes sense**

It seems to be that it looks at each word, and:

1. If the word is UPPER case (or something about the previous word, or it is in the exceptions list) then count it.
2. If it is the first word, and it is not Title case, fail immediately.
3. If it is the first word (which we now know is not UPPER or Title case) or it is lower case, count itself
4. Otherwise, ignore this word.

At the end, the accumulated count, divided by the number of words, must be > 0.8.

So for the title "``Not Aiven, something``", we get:

1. First word "``Not``" matches case (2), so ``count`` becomes 1
2. Second word "``Aiven,``" falls through to (4) and is ignored
3. Third word "``something``" matches (3), so ``count`` becomes 2
4. ``2 / 3 == 0.666...`` so the check fails

(by the way, the comma does not matter - removing it still gives the same result)

I must admit I don't quite understand why this is a proportionality test. A long title with a mid-word capitalised will be OK, but shortening the title will suddently make it fail.

Ah - the following even shows the transition:

* "``Capitalised names from both dictionaries should work, as Tony and Aiven``"

  11 words, count == 9 => 0.818..., which is a success

* "``Capitalised names from both dictionaries should work, Tony and Aiven``"

  10 words, count == 8 -> 0.8, which is a FAILURE

So the question is (a) why the weighting, and (b) why don't capitalised words count towards that weighting?

Particular as "``Not AIVEN, something``" is OK, because the second word is all uppercase, but "``Not Aiven, something``" is not OK.

*Maybe* it's because this is trying to distinguish itself from the "``Every Word Is Capitalised``" style, which it calls ``$title``. For which it uses code from https://github.com/jdkato/titlecase to work out the Title Case version of the given string, and then (essentially) checks words against that result to accumulate a count, which again must be > 0.8. And again, it allows UPPER case words to count as a match.

    **Note to self:** why does the code do ``strings.Title(strings.ToLower(w))`` rather than just ``strings.Title(w)``?

**Note** I think it *used* to work because we had lots of capitalised words in our ``accept.txt``, and they would be added to the exceptions list for this style, which means they count as part of step (1).

**Resolution** This is working as intended, although the documentation could do with explaining how it works.
The solution for us is to add appropriate exception words to the style file. This isn't too onerous as there aren't many such words, and it's probably better to be specific (that is, it's reasonable to say which words are special for titles in the specification for how titles are checked).

(For longer term, see also `Sentence case and headings`_. Since we're making explicit exceptions in the ``capitalization_headings.yml`` style file, if the future provides us with a better sentence cased title option, we will only have this file to alter/fix. This makes this a better option than trying to re-use the older ``accept.txt`` option.)

**Later finding** It appears that an exception can be a phrase, for instance ``Transport Layer Security``. I'm not actually sure how that works (!) but it makes life neater. It may be sensible to amend the list I've been building up to explicitly name some particular titles, rather than just excepting a (longish) set of words.


Common replacements
-------------------

``.github/vale/styles/Aiven/common_replacements.yml``

For instance::

  extends: substitution
  message: "Use '%s' instead of '%s'."
  ignorecase: true
  level: error
  swap:
    ...
    clickhouse: ClickHouse        # Case - and note the H in the middle
    ...
    kakfa: Kafka                  # it's easy to mistype
    ...
    "google cloud storage": "Google Cloud Storage"
    ...
    "Aiven Cassandra": "Aiven for Cassandra"

(much of the file is not shown, hence the ``...``)

Notes on specific terms in the ``common_replacements`` style (extending ``substitution``) are in the file itself.

Since we specify `ignorecase: true`, a rule such as::

  clickhouse: ClickHouse

will match any case variant of "``clickhouse``", and given an error if it is not "``ClickHouse``". Which is what we want.

This sugggests that for all product names where we want to match case exactly, we should have an appropriate rule in this file. (And see the section on `Vale and dictionary case (in)sensitivity`_ to understand why this isn't solved by the entries in the dictionary.)



Checking ``®`` marks and other things
-------------------------------------

``.github/vale/styles/Aiven/first_<Word>_is registered.yml`` and the like

For instance, ``first_Flink_is_registered.yml``::

  extends: conditional
  message: "At least one '%s' must be marked as ®"
  level: error
  scope: text
  ignorecase: false

  first: '\b(Flink)(?!®)'
  second: '(Flink)(?:®)'

These files extend ``conditional`` to check that there is at least one ``<Word>®`` if there are any occurrences of ``<Word>``.

**TODO: tidy the following up into something that makes sense**

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

One day it might be nice to be able to recognise a correct use in a header that comes before all uses in body text, but that's a task for another day (and might not be possible in vale anyway) (in fact, see the `issues <ISSUES.rst>`_ file for something about that).



Dictionaries
============

How dictionaries work
---------------------

Vale uses hunspell compatible dictionaries, but it doesn't use all of the information that can be specified in such dictionaries.

Vale and dictionary case (in)sensitivity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**NOTE: tidy the following up to make sense.**


By default, words specified in a Hunspell dictionary are case insensitive. So ``word`` would match ``word``, ``Word``, ``wOrD`` and other combinations. Similarly, ``TEXT`` would match ``text``, etc. This is discussed at `Hunspell - How to specify case-insensitivity for spell check in dic or aff file`_. For reference, the default ``en_US-web`` dictionary used by vale does not do anything special about this, so it is case-insensitive.

.. _`Hunspell - How to specify case-insensitivity for spell check in dic or aff file`:
    https://stackoverflow.com/questions/33880247/

  **Note:** In theory we could put ``KEEPCASE K`` in the ``aiven.aff`` file, and specify a word as ``/K`` in the ``aiven.dic`` file. However, looking at the source code in ``vale/pkg/spell/aff.go`` shows that vale ignores any ``KEEPCASE`` directives.

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



The default dictionary
----------------------

The default dictionary used by vale is defined at https://github.com/errata-ai/en_US-web

The aiven dictionary
--------------------

The ``aiven`` dictionary is two files:

* ``.github/vale/dicts/aiven.dic`` - the actual words.

* ``.github/vale/dicts/aiven.aff`` - rules for use in the ``.dic`` file. These specify the meaning of the ``/X`` style "switches" om some of the words in the ``.dic`` file.

Remember that the first line of a ``.dic`` file must be the number of dictionary entries (the total number of lines in the file - 1). Although apparently it's only approximate - I'd still like to keep it correct if we can.

The ``.aff`` file is allowed to be empty if it is not needed.

At the moment, the ``aiven.aff`` file is left empty, and if we want singlular and plural forms (for instance) we need to explicitly specify both of them in the ``aiven.dic`` file. This is something that might be addressed in future changes.

Adding words (or not) to the aiven dictionary
---------------------------------------------

The guidelines are:

1. Don't add a word that is already in the default dictionary.
2. Don't add a word that is a command line tool (for instance, ``jq``) if at all possible.
3. Just add the word you need - don't try to generalise for plural, singular, etc.
4. Do try to keep the word count on the first line of the file up-to-date.


Useful links about hunspell dictionaries
----------------------------------------

Useful links to learn about Hunspell compatible dictionaries:

**Note This list needs curation to work out if it's all useful to other people or not.**

* http://hunspell.github.io/

  "Hunspell is the spell checker of LibreOffice, OpenOffice.org, Mozilla Firefox 3 & Thunderbird, Google Chrome, and it is also used by proprietary software packages, like macOS, InDesign, memoQ, Opera and SDL Trados."

* http://manpages.ubuntu.com/manpages/trusty/man4/hunspell.4.html

  "hunspell - format of Hunspell dictionaries and affix files"

  https://linux.die.net/man/4/hunspell is another rendering of the same manpage.

* https://zverok.github.io/blog/2021-03-16-spellchecking-dictionaries.html

  "17 (ever so slightly) weird facts about the most popular dictionary format"

  I found this useful.

  It's part of a series "striving to explain how the world’s most popular spellchecker Hunspell works via its Python port called ``Spylls``

  https://zverok.github.io/spellchecker.html is the series content page

* http://web.archive.org/web/20130810100226/http://www.suares.com/index.php?page_id=25&news_id=233

  saved page on how to create a new dictionary (both files) from scratch

  This references:

  * http://www.openoffice.org/lingucomponent/affix.readme which describes the ``.aff`` file format

* https://www.quora.com/How-do-the-Hunspell-dictionaries-work seems to be a decent introduction


Running checks on github - the vale-action workflow
===================================================

https://github.com/errata-ai/vale-action

The github workflow ``.github/workflows/lint.yaml`` uses ``vale-action`` to run vale.


Why we don't use the Vocab style and ``accept.txt``
===================================================

Or "*Why we're not using the Vale style*"

We dont want to use the Vale style (https://docs.errata.ai/vale/styles#built-in-style)

It provides 3 rules:

* Vale.Spelling
* Vale.Terms and Vale.Avoid - see https://docs.errata.ai/vale/vocab

We used to use `accept.txt` (see https://docs.errata.ai/vale/vocab) to indicate additional correct spellings, but that didn't work well as we added more styles, because words in `accept.txt` are added to the exceptions for various styles. Hence moving to our own (additional) dictionary.

Since we are using our own dictionary now (as well as the default one, see ``aiven_spelling.yml``) we do not need to rely on the Vale.Spelling rule.

Test files
==========

In the directory ``.github/vale/tests`` there are pairs of files, with names that contain ``good`` and ``bad``.

The intention is that when vale is run on a ``good`` file, there should be no errors, and when it is run on a ``bad`` file there should be at least one error per significant line (that is, ignoring comments, which should be evident, and blank lines).

In the case of the ``good.rst`` versus ``bad.rst`` files, inline "comments" are used to indicate what sort of error is meant to be triggered by each line in the ``bad`` file (they're not real inline comments because reStructuredText doesn't have those).

I recommend using ``vale --output=line`` for its more compact output format.

To make it easier to see changes and regressions, the file ``.vale/test/shelltest.test`` can be used with
shelltestrunner_.

For instance::

  brew install shelltestrunner
  shelltest --diff .github/vale/tests/shelltest.test


There's also a similar program, shtst_, if you prefer a Python script (or something that is ``pip install``-able). The test file syntax is very similar. I'm continuing with shelltest because it is more mature, and also because I find the ``--diff`` switch useful (which shtst does not have).

.. _shelltestrunner: https://github.com/simonmichael/shelltestrunner
.. _shtst: https://github.com/obfusk/shtst
