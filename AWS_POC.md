# Set up

Preface: the logic is stored on AWS Lambda so changing the code locally won't help. The instruction is just to run the project for demo purpose, should be improved / streamlined if we go this route.

- Open an OpenSearch service on Aiven sandbox.
- Add this line `export ES_URL="[OpenSearch Service URI]"` to the `.bash_profile` or `.z_profile` depending on your setup.
- Follow the [README instructions](https://github.com/aiven/devportal#local-development) to set up a local development.
- Follow the instructions to create the indices with `make create-index ES_URL=https://opensearch-url/here`, `make index-devportal ES_URL=https://opensearch.url/here`, `make index-helpcenter ES_URL=https://opensearch.url/here`.

# Findings

## Search functionality

The search function is now available on AWS Lambda, enabled by AWS API Gateway to turn it into a REST API. More setup needs to be done, but it's served at for example `https://omyro9h0xg.execute-api.eu-west-1.amazonaws.com/test/search?query=kafka`

The cost for both AWS Lambda and API Gateway should be under 50$ monthly with the assumption that we get 10 million calls.

## Feedback submission functionality

The feedback function is now available on AWS Lambda, enabled by AWS API Gateway to turn it into a REST API as a POST request. Example would be

```
curl --location --request POST 'https://nzuogyzpvd.execute-api.eu-west-1.amazonaws.com/test/createsubmission' \
--header 'Content-Type: application/json' \
--data-raw '{
    "vote": "up",
    "bot-field": "",
    "message": "a new comment"
}'
```

Since it's migrated off Netlify, certains functions are lost (needs further investigation) like the `referrer` and `bot-field`.

The cost would be similar to the search funtionality above.

**Question**: How do we calculate the cost of our service (like OpenSearch and PostgreQL)? Is it a factor?

**Reference**: (AWS Lambda pricing)[https://aws.amazon.com/lambda/pricing/] and (AWS API Gateway pricing)[https://aws.amazon.com/api-gateway/pricing/]
