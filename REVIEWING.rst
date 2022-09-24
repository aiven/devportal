Review Aiven Docs pull requests
===============================

We have many contributors and reviewers, so here's a checklist to share the things we want to look at when reviewing contributions. Please follow these guidelines when reviewing any pull request on Aiven Docs, and don't merge your own work.

At an overall level
-------------------

#. Is this a migration from an old knowledgebase article? Make sure to add the old and new URLs to the migrations sheet when merging.

#. If this addresses an open issue, have we added the magic ``Fixes #123`` incantation to the pull request description? (and if it doesn't address an issue, why not?)

#. Does the build pass? We won't merge if it doesn't, but it's also fine for you to either explain to the author how to fix it, or add one commit to fix the link/markup/typo before you merge.

#. Does this change introduce something that our audience actually needs? Not all contributions must be accepted.

#. Do all the articles in the pull request use clear content types, and are they added to the navigation correctly?

#. Are the titles well-written and useful? Are there subtitles?


In detail for each page changed
-------------------------------

For this section, pull the branch on to your local machine and review the markup and the rendered content alongside one another.

#. Is it clear WHY something should be done as well as how to do it?

#. If there are steps to follow, are they all required, and laid out in the simplest possible order?

#. Do the steps all actually work? Are the commands correct and can you follow the examples?

#. Check the article against the style guide (in ``CONTRIBUTING``).

#. Review the written English in detail, is it clear and friendly? Is it correct and easy to understand?

#. Does the page render well? Is there anything missing?
