const { Client } = require("@opensearch-project/opensearch");

const client = new Client({
  node: process.env.ES_URL,
});

const pageSize = 10;

const handler = async (event) => {
  try {
    const query = event.queryStringParameters.query;
    let currentPage = 1;
    if (event.queryStringParameters.page) {
      try {
        currentPage = Math.max(
          1,
          parseInt(event.queryStringParameters.page, 10)
        );
      } catch (e) {
        console.warn(
          `Invalid page ${event.queryStringParameters.page} provided`
        );
      }
    }

    let analyzer_name = "devportal_analyzer" // Needs to match what the index was created with
    const response = await client.search({
      index: "devportal",
      body: {
        sort: ["_score"],
        size: pageSize,
        from: (currentPage - 1) * pageSize,
        query: {
          bool: {
            should: [
              {
                match: {
                  source: {
                    query: "helpcenter",
                    boost: 1
                  }
                }
              },
              {
                match: {
                  source: {
                    query: "devportal",
                    boost: 2
                  }
                }
              },
              {
                match_phrase_prefix: {
                  title: {
                    query: query,
                    slop: 2,
                    boost: 5,
                    analyzer: analyzer_name,
                  },
                },
              },
              {
                match: {
                  title: {
                    query: query,
                    fuzziness: "AUTO"
                  },
                },
              },
              {
                match_phrase_prefix: {
                  description: {
                    query: query,
                    slop: 2,
                    analyzer: analyzer_name,
                  },
                },
              },
              {
                match_phrase_prefix: {
                  content: {
                    query: query,
                    slop: 5,
                    analyzer: analyzer_name,
                  },
                },
              },
              {
                match_phrase_prefix: {
                  url: {
                    query: query,
                    slop: 5,
                    analyzer: analyzer_name,
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
      body: JSON.stringify({
        results,
        resultCount: response.body.hits.total.value,
        pageCount: Math.ceil(response.body.hits.total.value / pageSize),
        currentPage,
      }),
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
