const { Client } = require('@opensearch-project/opensearch');

const client = new Client({
  node: process.env.ES_URL,
});

const pageSize = 10;

/*
 * CLOUDFLARE REFERENCE:
 * https://developers.cloudflare.com/pages/platform/functions/#writing-your-first-function
 */

export async function onRequestGet({ params }) {
  try {
    const query = params.query;
    let currentPage = 1;
    if (params.page) {
      try {
        currentPage = Math.max(1, parseInt(params.page, 10));
      } catch (e) {
        console.warn(`Invalid page ${params.page} provided`);
      }
    }

    let analyzer_name = 'devportal_analyzer'; // Needs to match what the index was created with
    const response = await client.search({
      index: 'devportal',
      body: {
        sort: [{ sort_priority: 'asc' }, '_score'],
        size: pageSize,
        from: (currentPage - 1) * pageSize,
        query: {
          bool: {
            should: [
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
                    fuzziness: 'AUTO',
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
          pre_tags: ['<b>'],
          post_tags: ['</b>'],
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
        'Content-Type': 'application/json',
      },
    };
  } catch (error) {
    console.error(error);

    return {
      statusCode: 500,
      body: '',
    };
  }
}
