# Overview

## Directory structure

This project contains source code and supporting files for a serverless application that you can deploy with the AWS Serverless Application Model (AWS SAM) command line interface (CLI). It includes the following files and folders:

- `src` - Code for the application's Lambda function.
- `events` - Invocation events that you can use to invoke the function.
- `__tests__` - Unit tests for the application code.
- `template.yaml` - A template that defines the application's AWS resources e.g. functions

# Preparation

- Install [Docker](https://www.docker.com/) and [AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html). We need Docker running in the background for AWS SAM to work. We don't need to interact directly with it.
  - **Notes**: At the moment it seems some new versions of Docker may not work well with AWS SAM CLI, the latest safe version was [**4.7.0**](https://docs.docker.com/desktop/release-notes/#docker-desktop-470). It's possible newer versions may not have this issue. Recommended to install the latest first, then if AWS SAM complains about no Docker found, revert to the older version.
- Run `npm i` inside this directory
- Create a `env.local.json` file based on the existing `env.template.json`. This file helps run the API server with appropriate parameters during development
  - For example, `ES_URL` and `PG_URL` can be obtained directly from the corresponding development Aiven services (OpenSearch & PostgreSQL)
  - **Notes**: The `CA_CERT` for development can be obtained by going to the Aiven PostgreSQL service, download the CA cert into `./aws` directory
  - ![Screenshot 2022-11-09 at 15 19 30](https://user-images.githubusercontent.com/110401626/200845923-0023847b-5f0d-45ef-ba19-d91975faeb3c.png)
  - then run `npm run get-cert <cert file name e.g. ca.pem>`, and paste to that field.
- Create a `.env` file in the root directory storing values for `API_URL_SEARCH` and `API_URL_CREATE_FEEDBACK`. These values will be used later for testing with local documentation site (can be left empty for now or filled with production value).

# Development & Production

Functions are to be modified inside `src/handlers` directory similar to a Node.js project. For "secrets" like DB connection, it uses environment variables. They are defined in `template.yaml` under `Globals > Environment > Variables` then later used in the function (e.g. `process.env.PG_URL`). This way we can separate different environments, keep the "secrets" secured and don't require additional services from AWS like SSM.

## Development

### One time testing

Commands to use:

- `npm run generate-event <API METHOD> <Function name>`: This generates an event for a function we declared in `template.yaml` e.g. `SearchFunction`, then we can modify the event with different parameters for one-time testing.
- `npm run invoke <Function name>`: To be used with the `npm run generate-event` above. This will make a call to the API with parameters defined in the corresponding `event.[].local.json`.

Please check out more details on doing one time testing for the existing functions here:

- [Search function](https://github.com/aiven/devportal/blob/feature/use-aws/aws/SEARCH.md)
- [Creating feedback function](https://github.com/aiven/devportal/blob/feature/use-aws/aws/CreateFeedback.md)

### Continuous testing

Commands to use:

- `npm run watch`: Start a nodemon instance to watch for changes in `js,json,yaml` and run `sam build` when needed.
- `npm run start`: Run this in another terminal window. This creates a server with configurations declared in `env.local.json` above, so we can test the API with Postman / browser / etc.

During development, we may want to supply our own services e.g. OpenSearch / PostgreSQL / etc. through `env.local.json` so it doesn't conflict with production instances.

### Testing with local documentation site

With the server running, one can also test the API inside the local documentation site. This is done by changing the API URL inside their corresponding `.env` files to match the local API URL.

From there, one can run `make livehtml` in the root folder to serve the doc site, and test the functions directly there.

## Production

When merging with master/main branch, GitHub Actions will take care of the deployment to AWS

## Workflow

A simple workflow for improving the existing SearchFunction would be:

- Run `npm run generate-event GET SearchFunction` to simulate event for the function (and change it if needed)
- Run `npm run invoke SearchFunction` for one-time testings
- Run `npm run start` and `npm run watch` to test / develop
