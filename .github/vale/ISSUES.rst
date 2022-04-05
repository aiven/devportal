===============================================
Known or possible issues with (our use of) vale
===============================================

Changes for us
==============

These are ideas for things we might want to do in this repository.


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

Ideas for more checks
---------------------

These all probably need ``raw`` mode, to see the actual markup, which I haven't used yet.

* check for markdown style links (so easy to do when we use both markdown and reStructuredText in different places)
* check for missing ``:alt:`` in ``.. image::`` directives (at the moment we're relying on a vale bug to spot these - I'm looking into that elsewhere)
* check for single backticks (as for markdown) where there shoud be double backticks (single backticks in reStructuredText means "use the default role", which in our sphinx setup gives italics, which is a bit confusing and actually quite easy to miss)




Changes for vale
================

These are ideas for thing we might want changing in vale itself.

``conditional`` rules are not ordered
-------------------------------------

  *May be a bug of just a feature request, report later.*

That is, a ``conditional`` rule asserts that if there is an occurrence of (text matching) ``first``, then there must also be at least one occurrence of (text matching) ``second``, which contains the string found by ``first``.

  **NOTE** see `first_<Word>_is registered checks`_ for an explanation of how ``conditional`` actually works.

The example given in the documentation (for ``WHO`` and its expansion/explanation) implies that ``second`` might be expected to come first, but this is not actually required by the code.

When I've got vale working as we wish, I expect to raise an issue asking that it be possible to request that ordering, since we want to be able to require ``Term®`` comes before ``Term``.

More documentation (and examples) needed for ``conditional``
------------------------------------------------------------

  *Vale documentation - up to us to propose*

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

Finding the vale CONTRIBUTING document
--------------------------------------

  *Should be a simple PR.*

It lives in ``.github``. Where I wasn't looking.

I think that there should either be a reference to it in the README (probably the best option), or it should be moved to the top level (which is where I'd expect it, but that doesn't make that the right choice).

https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors seems to indicate that it doesn't matter whether the CONTRIBUTING guide is at the top level or in ``.github`` - in either case it should get shown when someone does a PR (as it was to me).

Pedanting the vale CONTRIBUTING document
----------------------------------------

  *Make a PR.*

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

*Although* it's not clear if we ever *want* to use this ourselves - it's a slippery slope disabling checking on parts of a document...

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
