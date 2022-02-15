====================================
Notes on what we are doing with Vale
====================================

  (This file may or may not be kept)

  (This ``.vale`` directory will be folded back into ``.github`` when work is finished, to make the configuration available to `vale-action`_)

.. _`vale-action`: https://github.com/errata-ai/vale-action

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

Remember that the first line of ``aiven.dic`` must be the number of dictionary entries (the total number of lines in the file - 1).

``common_replacements``
-----------------------

Notes on the ``common_replacements`` style (extending ``substitution``) are in the file itself.

``first_<Word>_is registered`` checks
-------------------------------------

These extend ``conditional`` to check that there is at least one ``<Word>®`` if there are any occurrences of ``<Word>``.

See `conditional rules are not ordered`_ for why that doesn't do quite what we want (we'd like it to require the occurrence with ``®`` comes first).

We have one file for each ``<Word>`` - for instance, for ``Flink``, ``Kafka``, etc.

We do not ignore case, because it's only the correctly cased version of the word we care about.

Because ``®`` is not a word character, we have to check for ``first`` being the word that is explicitly not followed by ``®``.

Note that the rules for ``Redis`` (needs ``™*``, and it's OK for the ``*`` not to be superscripted) and ``Apache`` (only needs ``®`` if it's not followed by one of the sub-product names) will be different.

One day it might be nice to be able to recognise a correct use in a header that comes before all uses in body text, but that's a task for another day (and might not be possible in vale anyway).

Test files
----------

In the directory ``.vale/tests`` there are pairs of files, with names that contain ``good`` and ``bad``.

The intention is that when vale is run on a ``good`` file, there should be no errors, and when it is run on a ``bad`` file there should be at least one error per significant line (that is, ignoring comments, which should be evident, and blank lines).

In the case of the ``good.rst`` versus ``bad.rst`` files, inline "comments" are used to indicate what sort of error is meant to be triggered by each line in the ``bad`` file (they're not real inline comments because reStructuredText doesn't have those).

I recommend using ``vale --output=line`` for its more compact output format.

Ideally some actual form of programmatic testing would be used, but this is better than nothing.

    Possibly using https://texttest.org/ (heh, a shout out to the Divio documentation system!).

    See also

    * http://emilybache.blogspot.com/2011/11/what-is-text-based-testing.html
    * http://texttest.sourceforge.net/files/textbased_testing.pdf
    * https://www.infoq.com/news/2017/02/approval-testing-texttest/

Known or possible issues
========================

``conditional`` rules are not ordered
-------------------------------------

  *May be a bug of just a feature request, report later.*

That is, a ``conditional`` rule asserts that if there is an occurrence of (text matching) ``first``, then there must also be at least one occurrence of (text matching) ``second``.

The example given in the documentation (for ``WHO`` and its expansion/explanation) implies that ``second`` might be expected to come first, but this is not actually required by the code.

When I've got vale working as we wish, I expect to raise an issue asking that it be possible to request that ordering, since we want to be able to require ``Term®`` comes before ``Term``.

Also, the documentation could do with improvement here, so fix it when able.

Strange behaviour of sentence case
----------------------------------

    *I've yet to prove this is an actual issue, and not something I'm doing wrong.*

In the ``.vale/tests/sentence_case_title_good.rst`` file, some titles are being treated as errors, when one would not expect it. For instance, the title ``Not Aiven`` is an eror, but the title ``Aiven®`` is OK, and longer titles with names in them (that is, capitalised dictionary words) are OK.

I'm going to leave this for the moment and concentrate on other things, and come back to it later to see if I can either work out what is going on, or work out a minimal test case.

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

When there are syntax errors in reStructuredText, it seems that the file gets ignored. This looks just the same as having no vale errors in the file.

Vale checks reStructuredText by first running it through ``rst2html.py``. A quick check suggests that if I do ``rst2html.py <name>.rst > <name>.html``, I still get status code ``0`` if there is an error, but I also get error text written to ``stderr``. So it should, in principle, be possible to tell if something went wrong. (vale probably doesn't want to report the errors as such.)

I haven't looked at the source code yet, but must do so before raising an issue or PR.
