Contributing to this repository
===============================

|:smile:| |:heart_eyes:| First off, thanks for taking the time to contribute! With your help, we’re making developers' lives easier. |:heart_eyes:| |:smile:|

The following is a set of tips and guidelines that will help you improve the Aiven developer portal.


What should I know before I contribute?
---------------------------------------

**What is DevPortal?**

DevPortal is Aiven’s developer portal. It’s goal is to provide a comprehensive set of help articles aimed at developers using Aiven’s products. 


**How does DevPortal work?**

It is Python-based, with content in ReStructuredText (rst) and rendered by Sphinx.


**What is the content model?**

DevPortal contains the following content types:
- *Concept* - Conceptual content helps people understand a feature or topic by providing a clear, high-level overview, explanation of how the feature or topic can help them on their journey, and context like use cases or examples. 
- *Task* - Task content helps people complete a task from start to finish while they're using Aiven’s products.
- *Reference* - Referential content provides detailed information that peoplr need while they're actively using Aiven's products.
- *Tutorial* - Tutorials help people learn about products, and solve real world problems by guiding them through the entire workflow to complete a task.

**What is the structure of DevPortal?**

You can see the structure in the left-hand navigation menu. 
It is driven by a plugin called `Sphinx external TOC <https://sphinx-external-toc.readthedocs.io/en/latest/intro.html>`_. 

You can find the current structure in ``_toc.yml``.

If you have an article about any of the Aiven tools (API, CLI, console, Terraform provider, Kubernetes operator), place it in the **Aiven tools** section.
If you have an article about any specific Aiven product (M3, Kafka, Grafana, etc.), nest it in the product-specific section. 
If you have an article with general reference information, place it in the **Resources** section. 


How can I contribute?
---------------------

**Reporting bugs, and suggesting enhancements**

If you notice something is off (anything - from typos to incorrect instructions) or missing, consider opening an issue. 

.. tip::
    Before you open an issue, check all the existing issues for the DevPortal to make sure you're not duplicating it. 


**Contributing via pull requests (PR)**

If you have your own article to add or you want to modify an existing article yourself, here's what you do:

1. Fork the repo.
2. Make your update.
3. Open a pull request (make sure you use a helpful PR and commit message). 
4. Submit your PR, and get it reviewed (one reviewer is required). 

We'll merge it!

.. note::
    Our build runs several checks on your updates - from linting to spell check to broken links to help you commit good content. Look at the **Checks** section in your pull request to make sure everything passes. If anything fails, check the error details, or reach out to us, and we'll help you. 


Style tips
----------

If you're writing content, here are some high-level tips that can be useful:

- Decide what type of content you want to contribute (check the content model above), and use our content type templates - for concept, task, reference and tutorial.

- Write a good title (start with a verb for tasks, and noun for concepts). 

- Note down your main ideas, and decide what formatting will best support these (use the content templates):
    - Ordered lists - for tasks
    - Paragraphs - for definitions and explanations
    - Lists and tables - for reference/options

- Highlight information by using the following elements:
    - Tips - for interesting facts about parts of your content/alternative ways of doing something, and shortcuts
    - Warnings - for important facts readers need to know before proceeding
    - Info - for any extra information (this may be skipped)

- Add good links (internal and external) - properly formatted, to reputable sources of information.

- Choose your visuals (images, diagrams, screenshots) and include them in a specified size (no bigger than…). 



**Style guides and other resources**

- RestrecturedText cheatsheet


|:pray:|  Thanks again for contributing! |:pray:| 

The DevRel team
