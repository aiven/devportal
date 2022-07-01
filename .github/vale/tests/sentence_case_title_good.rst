This is a title in sentence case
================================

We allow HowTo (a named exception) in a title
---------------------------------------------

Lots of positive words.

Strangely ALL CAPS is OK
------------------------

6 words. ``Strangely`` is first and capitalised, so +1. Lower case words are +1, and ALL CAPS words are also +1. So our total is 6/6, which is better than 80%, so this title is OK.

Multiple things with ® should work, such as Aiven and Flink®
------------------------------------------------------------

11 words, ``Multiple`` is first and capitalised, so +1. ``Aiven`` and ``Flink`` are exceptions, so +1 each. And the lower case words are all +1, so we get a score of 10/11 or 11/11 depending on how it regards the ``®``. In either case, this is a passing score.

Aiven
-----

Is OK, as it's a first word that is capitalised, so a score of 100%.

Aiven and Flink®
----------------

3 words, ``Aiven`` is +1 because it's title-case and first, ``and`` is +1 because it's lower case, ``Flink`` is +1 because it's an exception. So score is 3/3 which is more than 80%, so this title is good.

Aiven and Redis®*
-----------------

3 words, ``Aiven`` is +1 because it's title-case and first, ``and`` is +1 because it's lower case, ``Redis`` is +1 because it's an exception. So score is 3/3 which is more than 80%, so this title is good.

Aiven and Redis
---------------

3 words, ``Aiven`` is +1 because it's title-case and first, ``and`` is +1 because it's lower case, ``Redis`` is +1 because it's an exception. So score is 3/3 which is more than 80%, so this title is good.

Short but Aiven
---------------

3 words, ``Short`` is +1 because it's title-case and first, ``and`` is +1 because it's lower case, ``Aiven`` is +1 because it's an exception. So score is 3/3 which is more than 80%, so this title is good.
