const { Client } = require("@elastic/elasticsearch");

const client = new Client({
  node: process.env.ES_URL,
});

const handler = async (event) => {
  try {
    const query = event.queryStringParameters.query;

    const response = await client.search({
      index: "devportal",
      body: {
        min_score: 15,
        query: {
          bool: {
            should: [
              {
                term: {
                  source: {
                    value: 'devportal',
                    boost: 5
                  }
                }
              },
              {
                match_phrase_prefix: {
                  title: {
                    query: query,
                    slop: 2,
                    boost: 5,
                  },
                },
              },
              {
                match_phrase_prefix: {
                  description: {
                    query: query,
                    slop: 2,
                  },
                },
              },
              {
                match_phrase_prefix: {
                  content: {
                    query: query,
                    slop: 5,
                  },
                },
              },
            ],
          },
        },
        highlight: {
          pre_tags: ["<b>"],
          post_tags: ["</b>"],
          fields: {
            title: {},
            content: {},
            description: {},
          },
        },
      },
    });

    const results = response.body.hits.hits.map((hit) => ({
      source: hit._source,
      highlight: hit.highlight || {},
    }));

    return {
      statusCode: 200,
      body: JSON.stringify({ results }),
      headers: {
        "Content-Type": "application/json",
      },
    };
  } catch (error) {
    console.error(error);

    return {
      statusCode: 500,
      body: "",
    };
  }
};

module.exports = { handler };
