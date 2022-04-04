====================================
Notes on what we are doing with Vale
====================================

.. contents::

The future of this file
=======================

During development of our vale setup, this file is being used as a collection of notes of what I've learnt and what might be done in the future.

Longer term, this should become actual documentation of our vale setup, and why it is the way it is.

The ``.vale`` directory will be folded back into ``.github`` when work is finished, to make the configuration available to `vale-action`_. This file will be retained and renamed somewhere appropriate.

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

SkippedScope
------------

The ``SkippedScope`` directive can be used in the ``.vale.ini`` file to say what HTML block-level tags to ignore.
See https://docs.errata.ai/vale/config#skippedscopes

For our purposes, we want to add ``a`` (corresponding to links) and ``cite`` (corresponding to things in single backticks).

  (Remember that vale uses ``rst2html.py`` to turn our reStructuredText into something it can consume.)

Except maybe we don't want to ignore ``cite``, because we do want to check inside things like::

  :doc:`Aiven for Apache Kafka® topics <connect-kafka>`

What we *really* want to make sure we ignore is things like::

  `jq <https://stedolan.github.io/jq/>`__

...except that sometimes we put names that do need ®-checking into links. Oh dear.

``aiven_spelling`` and the ``aiven`` dictionary
-----------------------------------------------

Some notes on dictionaries.


The ``aiven`` dictionary is two files:

* ``aiven.dic`` - the actual words.

* ``aiven.aff`` - rules for use in the ``.dic`` file. These specify the meaning of the ``/X`` style "switches" om some of the words in the ``.dic`` file.

Remember that the first line of a ``.dic`` file must be the number of dictionary entries (the total number of lines in the file - 1). Although apparently it's only approximate - I'd still like to keep it correct if we can.

Note that the ``.aff`` file is allowed to be empty if it is not needed.

How I constructed the ``aiven.dic`` dictionary file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Copied the content of ``.github/styles/Vocab/Docs/accept.txt``
2. Prepended a line count
3. Added ``M3`` - is that sensible?
4. For every word of the form ``[Ww]ord``, changed it to just ``word``
5. Removed ``Simple Authentication and Security Layer``. I have no idea how the dictionary would cope with a word with spaces in it, and I'm fairly sure all the individual words are in the main dictionary anyway.
6. Replaced ``fileset[s]`` by two entries, one for ``fileset`` and one for ``filesets``

   (I could instead have started supporting plural annotation via the ``.aff`` file, but that seems overkill in this case)

7. Removed ``jq`` and ``kcat`` - they're just command line tools, not words.

   I'm not sure about ``npm``, ``psql``, ``wget``, ``httpie`` and maybe others, so have left them in for the moment.

   (of course, ``curl`` cheats by being an actual word in the main dictionary!)

#. Recalculated the line count

Still to do:

* check which words are actually in the main dictionary
* decide which words we want to enforce the capitalisation of (see the section on `common_replacements`_)

Addendum: I wrote a little script to detect duplicate words (those that occur in both identically in both dictionaries, ignoring any ``/`` annotation), and that reports:

  Duplicate words are: API, Apache, Cassandra, Elasticsearch, GitHub, Homebrew, Java, Kafka, Kubernetes, MySQL, PostgreSQL, Prometheus, Python, Redis, boot, business, connect, go, hobbyist, operator, spring

So we should consider (a) removing the duplicates, and, perhaps, (b) rechecking this every so often.

Vale and dictionary case (in)sensitivity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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


Useful links about hunspell dictionaries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Useful links to learn about Hunspell compatible dictionaries:

**Note** *This list needs curation to work out if it's all useful to other people or not.*

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


``common_replacements``
-----------------------

Notes on specific terms in the ``common_replacements`` style (extending ``substitution``) are in the file itself.

Since we specify `ignorecase: true`, a rule such as::

  clickhouse: ClickHouse

will match any case variant of "``clickhouse``", and given an error if it is not "``ClickHouse``". Which is what we want.

This sugggests that for all product names where we want to match case exactly, we should have an appropriate rule in this file. (And see the section on `Vale and dictionary case (in)sensitivity`_ to understand why this isn't solved by the entries in the dictionary.)

**Nice to have:** add a rule to detect getting Sphinx style links wrong, because the number of trailing underlines is incorrect. This should be reasonably easy to write, and it's a common error.

(and maybe also a rule to spot markdown-style links!)

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

Other marks and checks
----------------------

We reference Elasticsearch a few times, and that needs a disclaimer/attribution, which I've supplied by hand as necessary. I am not sure if it is worth constructing a specific rule for this (and my first attempt didn't work!).

Other cases that only happen occasionally:

* ``Apache Lucene™`` (which is a trademark of the Apache Software Foundation) in `<../docs/products/opensearch/index.rst>`_ and `<../docs/products/opensearch/dashboards/getting-started.rst>`_. I've added a specific attribution in `PR 605`_.

* ``Apache ZooKeeper`` in `<../docs/products/kafka/concepts/auth-types.rst>`_ and `<../docs/products/kafka/howto/use-zookeeper.rst>`_. This is actually an unregistered trademark (™) of Apache. I've made it refer to "Apache ZooKeeper" rather than "ZooKeeper", and added attribution in both places in `PR 605`_.

* Various names in `<../docs/products/kafka/kafka-connect/concepts/list-of-connector-plugins.rst>`_, which may or may not need ® marks and/or attributions. I've made some attempt for some things in that file in `PR 605`_.

It would be nice to check for ``Apache®`` when ``Apache`` is *not* followed by a product name (this *may* require listing all the product names in a regular expression, or may just mean checking for ``Apache <capitalised-word>``, which is probably good enough as a first pass).

.. _`PR 605`: https://github.com/aiven/devportal/pull/605

``capitalization_headings.yml``
-------------------------------

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

Maybe have a new dictionary for product names
---------------------------------------------

  *Local change.*

We've introduced the new ``aiven.dic`` dictionary, but there are quite a few product names in there.

It might be worth splitting them out into a new ``products.dic`` dictionary. This will make them easier to curate.

There may be other such mini-dictionaries that we want to create as well.

Aiven for Apache XXX independent of Apache XXX
----------------------------------------------

  *Local change.*

I think that given a passage like:

  Something something something Apache XXX® something something Aiven for Apache XXX®.

it is probably "good form" to put the ``®`` on the "bare" and the "Aiven for" forms. This helps to make it clear that the "Aiven for" form is not special. It would be nice if we could make a rule (or rules) that treated this as a separate thing to check (at the moment our rule is only checking for the "Aiven XXX" case without taking into consideration if it is preceded by "Aiven for" or not.)

**Also** I really want rules to prevent things like ``Apache® XXX`` when it should be ``Apache XXX®`` - I think I may say that elsewhere.

Dealing with links that contain code content
--------------------------------------------

  *Local change.*

Consider::

  `kcat <https://something>`_

We *really* want to put ``kcat`` in "code" font, but we also want it as the word in the link.

(Do we ever want code-font and non-code-font words in the same link text? If we can put up with the answer "no" then this is likely to be more possible.)

This should be doable, but I would like to find a way to do it that does not require a lot of knowledge of reStructuredText and/or Sphinx from the person typing.

  (I also don't want to take on the long-abandoned task of making docutils understand nested markup!)

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

Missing documentation for dictionary ``append``
-----------------------------------------------

  *Worth doing a PR for.*

There is no documentation for the ``append`` option of the ``spelling`` style.

It's quite an important option, as setting it ``true`` allows appending a dictionary to the default, rather than replacing it.

Documentation for ``capitalization`` needs extending
----------------------------------------------------

  *Worth doing a PR for. And definitely blogging about.*

As I discovered in the section on `capitalization_headings.yml`_, the capitalization style (and particularly the ``$sentence`` "match") doesn't work quite as one might expect. What it does is reasonable, but could do with explaining, as it can lead to surprises for very short titles.

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

**Note:** check exactly what the ``--sort`` switch does.

Oddity in substitution matching
-------------------------------

  *Not sure what is going on here - might still be a "me" mistake rather than vale*

Looking at the lines in ``.vale/tests/bad.rst``::

  ``literal-text`` MirrorMaker2             -- this is NOT found

  ``literal text`` MirrorMaker2             -- this IS found

the first is not reported as an error, but the second is. If I put some "obvious" debugging into ``vale/internal/check/substitution.go``, it does indeed seem to "see" one and not the other.

I'm not 100% sure this is a vale bug yet, because in trying to say what I want to do for ``MirrorMaker2`` I might be being over-clever.

I'm recording it here because I don't want to investigate further at the moment (I'm currently running my patched vale over the documentation to try to fix all the problems it *does* find). Having a minimal provoking test case means I can come back to this and not forget it.

**NOTE to self** Remember to ``rg -wi MirrorMaker2`` after I've done all the other documentation fixes.

Sentence case and headings
--------------------------

  *A wish. An idea.**

For short titles, the sentence case "80%" rule doesn't work very well. Is there a better algorithm for working out whether the sentence casing is accceptable or not? (this might need to be given a different name). Because adding lots of exceptions is a pain (and feels the wrong solution).

It occurs to me that one possibility is to add a switch to the `capitalization` style to say "allow capitalised words from the dictionary to count towards the total". So ``Gantt`` would count.

Thoughts:

1. It depends on being able to easily look up whether a word is capitalised in the dictionary or dictionaries.
2. It should allow Capitalised (and thus also MixedCase) words.
3. Should it allow things like ``iPod`` - maybe that's *another* shade of the option (I think the existing rules would regard ``iPod`` as not a "counting" word, but need to check)
4. This is meant to apply to ``$sentence`` - does it have any relevance for the other modes? And if not, should an error message be produced if it is specified for other modes?

Finding the CONTRIBUTING document
---------------------------------

  *Should be a simple PR.*

It lives in ``.github``. Where I wasn't looking.

I think that there should either be a reference to it in the README (probably the best option), or it should be moved to the top level (which is where I'd expect it, but that doesn't make that the right choice).

https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors seems to indicate that it doesn't matter whether the CONTRIBUTING guide is at the top level or in ``.github`` - in either case it should get shown when someone does a PR (as it was to me).

Pedanting the CONTRIBUTING document
-----------------------------------

Note that in particular ``make lint`` doesn't do anything any more, as there's no such target.

(so either fix the Makefile, or suggest use of ``gofmt``)

The document says running the tests needs cucumber, ascidoctor and sphinx, but I've found they also need dita-ot and xsltproc (double check that last - I think it's needed, but I already had it installed).

Vale on/off problem with rst2html.py
------------------------------------

  *A wish. Might need a fix in rst2html.py*

The ability to use comments to switch vale off and on again looks very valuable, although in reStructuredText it is of less utility than one might wish because of how comments work (they sort-of work like paragraphs).

However, the expected workaround of marking up::

  .. vale off

  this text should be fine
  ------------------------

  .. vale on

is known not to work, as reported in `issue 340`_ (Vale on/off comments do not work on titles in RST) and may be either impossible or very difficult to fix - in fact, it's apparently a bug in rst2html.py.

.. _`issue 340`: https://github.com/errata-ai/vale/issues/340

Vale on/off inline
------------------

  *Experimentation*

There already is support for ``.. vale off`` and ``.. vale on``, but these can only wrap blocks (and don't work around titles).

Would it be possible to use ``.. raw:: html`` and ``|substitution|`` to provide inline such? So one could write something like ``|vale-off|some text|vale-on|``?

As https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#substitution-definitions says"

  "Substitution definitions allow the power and flexibility of block-level directives to be shared by inline text. They are a way to include arbitrarily complex inline structures within text, while keeping the details out of the flow of text."

Maybe something like::

  .. |vale-on| raw:: html

     <!-- vale on -->

or::

  .. |vale-on| :raw-html:`<!-- vale on -->`

If this works, it may solve some of our other issues without any hacking of vale itself, and without complicated setup in the styles/rules (and it would be a work-around for `Vale on/off problem with rst2html.py`_, and probably worth mentioning in `issue 340`_.

It may also be possible to define the substitutions in the sphinx ``conf.py``, so it's always there.

And lastly, if this does work, it's worth blogging about...

*Although* it's not clear if we ever *want* to use this ourselves - it's a slippery slope disabling checking on parts of a document...

More potential checks
---------------------

  *I should consolidate these suggestions*

These all probably need ``raw`` mode, to see the actual markup, which I haven't used yet.

* check for markdown style links (so easy to do when we use both markdown and reStructuredText in different places)
* check for missing ``:alt:`` in ``.. image::`` directives (at the moment we're relying on a vale bug to spot these - I'm looking into that elsewhere)
* check for single backticks (as for markdown) where there shoud be double backticks (single backticks in reStructuredText means "use the default role", which in our sphinx setup gives italics, which is a bit confusing and actually quite easy to miss)
