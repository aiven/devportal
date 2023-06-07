pgvector for AI-powered search in Aiven for PostgreSQL®
=======================================================

In machine learning (ML) models, all data items in a particular data set are mapped into one unified n-dimensional vector space, no matter how big the input data set is. This optimized way of data representation allows for high performance of AI algorithms. Mapping regular data into a vector space requires so called data vectorizing, which is transforming data items into vectors (data structures with at least two components: magnitude and direction). On the vectorized data, you can perform AI-powered operations using different instruments, one of them being pgvector.

Discover the pgvector extension to Aiven for PostgreSQL® and learn how it works. Check why you might need it and what benefits you get using it. 

About pgvector
--------------

pgvector is an open-source vector extension for similarity search. It's available as an extension to your Aiven for PostgreSQL® services. pgvector introduces capabilities to store and search over data of the vector type (ML-generated embeddings). Applying a specific index type for querying a table, the extension enables you to search for vector's exact nearest or approximate nearest neighbors (data items). 

Vector embeddings
'''''''''''''''''

In machine learning, real-world objects and concepts (text, images, video, or audio) are represented as a set of continuous numbers residing in a high-dimensional vector space. These numerical representations are called vector embeddings, and the process of transformation into numerical representations is called vector embedding. Vector embedding allows ML algorithms to identify semantic and syntactic relationships between data, find patterns, and make predictions. Vector representations have different applications, for example, information retrieval, image classification, sentiment analysis, natural language processing, or similarity search.

Vector similarity
'''''''''''''''''

Since on vector embeddings you can use AI tools for capturing relationships between objects (vector representations), you are also able to identify similarities between them in an easily computable and scalable manner.

A vector usually represents a data point, and components of the vector correspond to attributes of the data point.
In most cases, vector similarity calculations use distance metrics, for example, by measuring the straight-line distance between two vectors or the cosine of the angle between two vectors. The greater the resulting value of the similarity calculation is, the more similar the vectors are, with 0 as the minimum value and 1 as the maximum value.

How pgvector works
------------------

Vectorizing
  You generate embeddings for your data, for example, for products catalog.
Storing
  You store the embeddings in Aiven for PostgreSQL using the pgvector extension.
Querying 
  You use the embeddings for the vector similarity search on products catalog.
Indexing
  By default, pgvector executes the *exact* nearest neighbor search, which gives the perfect recall. If you add an index to use the *approximate* nearest neighbor search, you can speed up your search, trading off some recall for performance.

Why use pgvector
----------------

With the pgvector extension, you can perform the vector similarity search and use embedding techniques directly in Aiven for PostgreSQL. pgvector allows for efficient handling of high-dimensional vector data within the Aiven for PostgreSQL database for tasks such as similarity search, clustering, model training, data augmentation, or machine learning.

pgvector helps you optimize and personalize the similarity search experience by improving searching speed and accuracy (also by adding indices).

Typical use cases
-----------------

There are multiple industry applications for similarity searches over vector embeddings:

* e-commerce
* recommendation systems
* fraud detection

.. topic:: Examples
    
    * AI-powered tools can find similarities between products or transactions, which can be used to produce product recommendations or detect potential scams or frauds.
    * Sentiment analysis: words represented with similar vector embeddings have similar sentiment scores.

What's next
-----------

:doc:`Enable and use pgvector on Aiven for PostgreSQL® </docs/products/postgresql/howto/use-pgvector>`

Related reading
---------------

`pgvector README on GitHub <https://github.com/pgvector/pgvector/blob/master/README.md>`_
