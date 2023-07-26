Contributing to Aiven Docs
==========================

Please read this guide before you open a pull request (yes, there is documentation for how to do documentation). If you're opening an issue, go ahead! And either way, thank you for your input, we appreciate you! :heart_eyes:

* `Before you start`_
* `Content types`_
* `Pull request process`_
* `Style guide`_
* `Further reading`_
* `Appendix A: Templates`_

Before you start
----------------

The **goal** of the docs is to support and enable users to achieve their goals, as quickly and easily as possible. We support that by providing accurate information in a concise format and a clear structure. It is better for one contributor to take time to make the content as clear as possible, than for many developers to have to spend time trying to understand something less clear.

Our intended **audience** is very technical, so does not need entry-level explanation of common concepts. They are here for advanced or Aiven-specific information. They might be in a hurry though (for example, during an incident on their platform) so clear, informative and friendly are the themes to aim for.

Content types
-------------

Aiven Docs uses the `Diátaxis Framework <https://diataxis.fr/>`_ as the basis of its content structure. This means that every article should be one of the following types:

* **HowTo** walks a developer through completing a specific task. It has a clear introduction of the task and what is is for, and numbered steps to follow (without choices, if there's more than one way to do something, pick one). If additional explanation could be useful, link to a related concept article.
    - Example: https://docs.aiven.io/docs/products/postgresql/howto/upgrade.html
    - Template: `Howto article template`_

* **Concept** is an explainer article that helps a developer to learn or understand something. Developers researching features, or who need extra background information on something that has been mentioned in a task, rely on these articles to fill gaps in their knowledge. It's common for HowTo articles to link to Concept articles.
    - Example: https://docs.aiven.io/docs/products/postgresql/concepts/pg-connection-pooling.html
    - Template: `Concept article template`_

* **Reference** starts with an overview of what can be found in this section, and then usually a list of some kind. We use this type of article for lists of extensions, configuration parameters, and that sort of bookmark-it-for-reference type of content.
    - Example: https://docs.aiven.io/docs/products/kafka/reference/advanced-params.html

Pull request process
--------------------

The instructions for setting up local development are in the ``README``.

0. We heartily recommend you open an issue so that we can either help with outlines, or know that three people are working on the same thing.

1. Make your changes on a branch. We recommend a maximum of three articles, and don't review large changesets without prior discussion. File names are ``kebab-case``, with hyphens, such as ``connect-with-pgadmin.rst``. Files should also be added to the table of contents file ``_toc.yml`` so they appear in the right location in the navigation.

2. Open a pull request, use the template so we know what it is and why it's a great addition. If you need to publish this quickly for a reason, mention that as well.

   If there is an associated issue, add ``Fixes <issue-URL>`` to the PR description text - this means the issue will automatically get closed when the PR is merged.

3. We have an automated build process that checks your work against our in-house styles, gets product names with the right capitalization, and checks links that you added. Please don't be alarmed if your build fails! View the output of the failed jobs to find out what happened, or we can advise when we review. You can run these locally if you like: ``make spell`` and ``make linkcheck``.
   
.. tip::

    Don't add commands to the accepted words list, these should always be in ``literal`` markup and ignored by the spell checker. Literal markup can't be used inside link text, so reword your link and sentence to avoid this.
    
4. On devportal, some CI/CD processes run weekly. Some of those processes are automation that helps to keep our documentation up-to-date. In another process we [check](https://github.com/aiven/devportal/blob/main/.github/workflows/linkcheck.yaml) for broken links in our docs. If the build fails, a GitHub Issue is open to inform collaborators and maintainers about it.

5. Every pull request generates a preview link, that will be added to your pull request as a comment. This link is publicly available and does not change during the lifetime of your pull request. Feel free to share it with others who might want a preview of your changes.

6. Our docs team will review your pull request, and you will receive some feedback. It's expected that there will be 2 or 3 rounds of revisions, but if you'd rather we just made changes ourselves, let us know.

7. The reviewer will merge the pull request once it is ready and has been approved.


Style guide
-----------

To keep all the content consistent and easy to follow for our audience, use `Google developer documentation style guide <https://developers.google.com/style>`_ for Aiven docs. This sections has exceptions and Aiven-specific guidelines.

.. tip::

    Remember we review your pull request against these guidelines, so for fewer rounds of revisions, follow this advice!

Where possible, these rules are checked automatically using Vale. For more information on how this is set up, see the `Vale readme file <.github/vale/README.rst>`_.

Use a specific template
'''''''''''''''''''''''

See the `Content types`_ section and work out whether you are writing a HowTo, Concept or Reference document. You might be writing more than one to cover the feature you have in mind! If you want to create a tutorial, please discuss that with us first.

Add hyperlinks
''''''''''''''

If we have other resources that might help a developer, point them out! Whether that's linking to concepts from howto articles, linking to reference materials, adding a section at the end for further reading that links any blog posts or tutorials we have on the topic, or related tasks - it all helps! It's also fine to link to resources on other sites (including competitors), especially upstream documentation resources.

.. note::

    All links should have text that makes it clear where the link goes to. Never use "here" as link text, instead try "the Grafana documentation for the sparkles plugin" or something else descriptive.

Formatting guidelines
'''''''''''''''''''''

Advice on marking up elements correctly can be found in the `README <README.rst>`_. Other useful tips and tricks for working with Sphinx and reStructuredText can be found in the :doc:`documentation section <docs/documentation/index>`.

Always use ``literal`` formatting for commands, function names, and config options. One limitation is that this can't be used inside links; please reword to work arond this.

Use **bold text** for interactive UI elements, such as buttons. Use *italic text* for non-interactive items such as section headings. Here's an example from the VPC access article::

    On the *Overview* page, scroll down to the *Advanced configuration* section and click **Add configuration option**.

On the *Overview* page, scroll down to the *Advanced configuration* section and click **Add configuration option**.

Use admonitions "note", "tip", and "warning". Avoid the rest of the available admonition types (especially "danger" which traditionally would imply danger to life, which is not a usual feature of a data platform).

Screenshots
'''''''''''

Screenshots might get outdated as soon as there's a visual change on the Aiven console. Although they can be helpful, especially where a user might have difficulty finding a particular element on a screen, use screenshots only when the textual instruction is not enough to help our audience.

The ``images`` folder reflects the structure of the ``docs`` folder, and the image should be in the folder matching the document that refers to it.

All images require alt text.

We do not use ``gif`` or animation in Aiven docs.

Example values
''''''''''''''

Example values should not be "foo" or "bar. Instead, if it's a username, try "Alice". If it's an email address use ``someone@example.com``. A user can quickly identify which variable goes where if they look like the values they represent.

When using placeholders in code examples, we use all uppercase. For example: https://docs.aiven.io/docs/products/postgresql/howto/connect-python.html

What not to do
''''''''''''''

The following items are only allowed in strict moderation:

* emoji :smile:
* exclamation marks
* questions, especially in headlines

Troubleshooting linting errors 
'''''''''''''''''''''''''''''''

You may get errors from the automated checks when using proper nouns. In these cases, you might need to add the words as an exception or add them to the dictionary file. For information on how to do this, see the `Vale readme file <.github/vale/README.rst>`_.


Further reading
---------------

- `ReStructuredText primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_
- `Diátaxis Framework <https://diataxis.fr/>`_.


Appendix A: Templates
---------------------

These templates help you get started with the different types of content. Feel free to discuss with us if you need something different.

Howto article template
''''''''''''''''''''''

Title template: Start with a verb (e.g. *Connect with Go*, *Install or upgrade an extension*).

::

    Article title
    #############

    First paragraph: Explain what the task helps users accomplish, the benefits of the task, or the purpose of the task. Try to include information that will help users understand when the task is appropriate or why the task is necessary.  The first few words of the article are used in the search results.

    Add links to any related articles such as supporting concept information, or similar tasks, if appropriate.

    Procedural section header here
    -------------------------------

    Include prerequisite information or specific permissions information before we get started.

    1. Then write procedural steps using ordered lists.
    2. Include only one way of doing something.
    3. If there's a shortcut, add it as a **Tip**. 
    4. Use full sentences with proper punctuation to explain a step.
    Optionally, another procedural section here 
    -------------------------------------------

    Keep adding procedures until you've finished writing your article.


Concept article template
''''''''''''''''''''''''

Title template: *About [subject]* (if this is a background information for a task, e.g. *About migrating to Aiven*) / *Subject* (use noun or noun phrase, e.g. *Authentication*, *High availability*)


::

    Article title
    #############

    Introduce your topic with a short description: Answer the question "What is this?" and "Why do I care about this?" If the concept is unfamiliar, start with a brief definition. The first few words of the article also show up in the search results.

    A section here
    --------------

    Write one or two paragraphs about the main idea of your topic. Add lists, diagrams or tables as necessary.

    Another section here
    --------------------

    Write one or two paragraphs about another element of your topic. Keep adding headers and sections until you've completed your article.

    Next steps
    ----------

    (optional) Share some links related to the topic. This could be more detailed upstream documentation, a task article that uses this knowledge. More links are good!


Limited availability note template
'''''''''''''''''''''''''''''''''''

For features that are in the limited availability stage, add the following admonition directly undert the article title:

.. important:: 
    {feature name} is a limited availability feature. If you're interested in trying out this feature, contact your account team or the Aiven support team at support@Aiven.io.


Early availability note template
'''''''''''''''''''''''''''''''''''

For features that are in the early availability stage, add the following admonition directly undert the article title:

.. important:: 
    {feature name} is an early availability feature. To use it, :doc:`enable the feature preview </docs/platform/howto/feature-preview.html>` in your user profile.
