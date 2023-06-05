pgvector for AI-powered search in Aiven for PostgreSQL®
=======================================================

To represent data in an optimized way, machine learning (ML) models often uses vectors, which are data structures with at least two components: magnitude and direction. In most cases, vectorizing the data is therefore essential before building an ML model. On the vectorized data, you can perform AI-powered operations (such as model training or data augmentation) using diffent tools, one of them being pgvector.

Discover the pgvector extension to Aiven for PostgreSQL® and learn how it works. Check why you might need it and what benefits you get using it. 

About pgvector
--------------

pgvector is an open-source vector tools for similarity search. It's available as an extension to your Aiven for PostgreSQL® servies. pgvector introduces capabilities to store and search over data of the vector type (ML-generated embeddings). Applying a specific index type for querying a table, the extension enables you to search for vector's exact nearest or approximate nearest neighbors (data items). 


Vector embeddings
'''''''''''''''''

In machine learning, real-world objects and concepts (text, images, video, or audio) are represented as a set of continuous numbers residing in a high-dimensional vector space. These numerical representations are called vector embeddings and the process of transformation into numerical representations is called vector embedding (using ML algorithms to identify semantic and syntactic relationships between data). Vector representations have different applications, for example, information retrieval, image classification, or natural language processing.

Vector similarity
'''''''''''''''''

On vector embeddings, you can use tools supporting AI algorithms for identifying semantic and syntactic relationships between objects. This allows for capturing similarities between the objects in an easily computable and scalable manner.

A vectors usually represents a data point and each vector's component represents a data point's feature or attribute.
In most cases, vector similarity calcualtions use distance metrics, for example, by measuring the straight-line distance between two vectors or the cosine of the angle between two vectors. The greater the calculation resulting value is, the more similar the vectors are, with 0 as the minimum value and 1 as the minimum value.

How pgvector works
------------------

1. Generate embeddings for e.g. products catalog
2. Store them in Aiven for PostgreSQL using the extension pgvector.
3. Use them to provide vector similarity search capabilities for products catalog (perform similarity searches within the vector space).

Why use pgvector
----------------

With the pgvector extension, you can perform the vector similarity search and use embeddings techniques directly in Aiven for PostgreSQL. pgvector allows for efficient handling of high-dimensional vector data within the Aiven for PostgreSQL database for tasks such as similarity search, clustering, or machine learning.

Sample use cases
----------------

Similarity searches over embeddings benefit various industry applications, including e-commerce, recommendation systems, and fraud detection. For example, systems can discern mathematical similarities between products or transactions to create relevant product recommendations or identifying potentially fraudulent activity.

Limitations
-----------

What's next
-----------

:doc:`Enable and use pgvector on Aiven for PostgreSQL® </docs/products/postgresql/howto/use-pgvector>`

Related reading
---------------

`pgvector's README on GitHub <https://github.com/pgvector/pgvector/blob/master/README.md>`_