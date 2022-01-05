Contributing to Aiven Developer
===============================

Please read this guide before you open a pull request (yes, there is documentation for how to do documentation). If you're opening an issue, go ahead! And either way, thank you for your input, we appreciate you! :heart_eyes:

* `Before you start`_
* `Content types`_
* `Pull request process`_
* `Style guide`_
* `Further reading`_
* `Appendix A: Templates`_

Before you start
----------------

The **goal** of Aiven Developer is to support and enable developers to achieve their goals, as quickly and easily as possible. We support that by providing accurate information in a concise format and a clear structure. It is better for one contributor to take time to make the content as clear as possible, than for many developers to have to spend time trying to understand something less clear.

Our intended **audience** is very technical, so does not need entry-level explanation of common concepts. They are here for advanced or Aiven-specific information. They might be in a hurry though (for example, during an incident on their platform) so clear, informative and friendly are the themes to aim for.

Content types
-------------

Aiven Developer uses the `Diátaxis Framework <https://diataxis.fr/>`_ as the basis of its content structure. This means that every article should be one of the following types:

* **HowTo** walks a developer through completing a specific task. It has a clear introduction of the task and what is is for, and numbered steps to follow (without choices, if there's more than one way to do something, pick one). If additional explanation could be useful, link to a related concept article.
    - Example: https://developer.aiven.io/docs/products/postgresql/howto/upgrade.html
    - Template: `Howto article template`_

* **Concept** is an explainer article that helps a developer to learn or understand something. Developers researching features, or who need extra background information on something that has been mentioned in a task, rely on these articles to fill gaps in their knowledge. It's common for HowTo articles to link to Concept articles.
    - Example: https://developer.aiven.io/docs/products/postgresql/concepts/pg-connection-pooling.html
    - Template: `Concept article template`_

* **Reference** starts with an overview of what can be found in this section, and then usually a list of some kind. We use this type of article for lists of extensions, configuration parameters, and that sort of bookmark-it-for-reference type of content.
    - Example: https://developer.aiven.io/docs/products/kafka/reference/advanced-params.html

Pull request process
--------------------

The instructions for setting up local development are in the ``README``.

0. We heartily recommend you open an issue so that we can either help with outlines, or know that three people are working on the same thing.

1. Make your changes on a branch. We recommend a maximum of three articles, and don't review large changesets without prior discussion. File names are ``kebab-case``, with hyphens, such as ``connect-with-pgadmin.rst``. Files should also be added to the table of contents file ``_toc.yml`` so they appear in the right location in the navigation.

2. Open a pull request, use the template so we know what it is and why it's a great addition. If you need to publish this quickly for a reason, mention that as well.

3. We have an automated build process that checks your work against our in-house styles, gets product names with the right capitalization, and checks links. Please don't be alarmed if your build fails! View the output of the failed jobs to find out what happened, or we can advise when we review. You can run these locally if you like: ``make spell`` and ``make linkcheck``.

.. tip::

    Don't add commands to the accepted words list, these should always be in ``literal`` markup and ignored by the spell checker. Literal markup can't be used inside link text, so reword your link and sentence to avoid this.

4. Every pull request generates a preview link, that will be added to your pull request as a comment. This link is publicly available and does not change during the lifetime of your pull request. Feel free to share it with others who might want a preview of your changes.

5. Our docs team will review your pull request, and you will receive some feedback. It's expected that there will be 2 or 3 rounds of revisions, but if you'd rather we just made changes ourselves, let us know.

6. The reviewer will merge the pull request once it is ready and has been approved.


Style guide
-----------

These are the guidelines that we use for Aiven Developer; following them helps us keep all the content consistent and easy to follow for our audience. We review your pull request against these guidelines, so for fewer rounds of revisions, follow this advice!

Use a specific template
'''''''''''''''''''''''

See the `Content types`_ section and work out whether you are writing a HowTo, Concept or Reference document. You might be writing more than one to cover the feature you have in mind! Tutorials are also welcome, but always discuss those with us first.

Headings should be in sentence case
'''''''''''''''''''''''''''''''''''

Rather than using Capital Letters for Almost Every Word, titles are written like sentences.

Example: Get partition details of an Apache Kafka topic

 - only the first letter, and the proper noun for the product name, are capitalized

Add hyperlinks
''''''''''''''

If we have other resources that might help a developer, point them out! Whether that's linking to concepts from howto articles, linking to reference materials, adding a section at the end for further reading that links any blog posts or tutorials we have on the topic, or related tasks - it all helps! It's also fine to link to resources on other sites (including competitors), especially upstream documentation resources.

.. note::

    All links should have text that makes it clear where the link goes to. Never use "here" as link text, instead try "the Grafana documentation for the sparkles plugin" or something else descriptive.


Use active wording
''''''''''''''''''

This section was not titled "Using active wording", use the form of language that sounds like a direct order. It's not intended to be rude, but to be very clear about what is needed. Think of commanding Alexa/Siri/[insert voice interface bot here].

Example: Install the excellent tool

Formatting guidelines
'''''''''''''''''''''

Always use ``literal`` formatting for commands, function names, and config options. One limitation is that this can't be used inside links; please reword to work arond this.

Use **bold text** for interactive UI elements, such as buttons. Use *italic text* for non-interactive items such as section headings. Here's an example from the VPC access article::

    On the *Overview* page, scroll down to the *Advanced configuration* section and click **Add configuration option**.

On the *Overview* page, scroll down to the *Advanced configuration* section and click **Add configuration option**.

Use admonitions "note", "tip", and "warning". Avoid the rest of the available admonition types (especially "danger" which traditionally would imply danger to life, which is not a usual feature of a data platform).

Positive and respectful language
''''''''''''''''''''''''''''''''

This is of course, entirely subjective! Some tips that we often give at review time:

- explain (especially in titles) what the user *can* do "install ``aiven-extras``" rather than what they can't do "you can't have root access".
- don't use "just", "simply" or other minimising words, this can easily discourage a user who is already struggling.
- keep empty phrases to a minimum, such as "at the end of the day", if the sentence would make sense without it then we don't need it.

Keep the user in mind, and you won't go far wrong.

Titles
''''''

* Howto articles start with a verb: use present, imperative tense. Example: Claim public schema ownership

* Concept articles often use "About" in their titles. Example: About PostgreSQL disk usage

Use subtitles to break up the article if it's more than a couple of paragraphs, these headings are used in the right hand navigation and really help users to find their way around a longer document.


Screenshots
'''''''''''

Screenshots can be helpful, especially where a user might have difficulty finding a particular element on a screen. They don't need a picture of every button they should click during a process, and whenever we make frontend changes to the web console, every screenshot must be updated. Therefore, use screenshots but only when needed.

All images require alt text.


Example values
''''''''''''''

Example values should not be "foo" or "bar. Instead, if it's a username, try "Alice". If it's an email address use ``someone@example.com``. A user can quickly identify which variable goes where if they look like the values they represent.

When using placeholders in code examples, we use all uppercase. For example: https://developer.aiven.io/docs/products/postgresql/howto/connect-python.html

What not to do
''''''''''''''

The following items are only allowed in strict moderation:

* emoji :smile:
* exclamation marks
* questions, especially in headlines

Formatting tips
'''''''''''''''

Advice on marking up elements correctly can be found in the ``README``.

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


