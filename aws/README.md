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
  - For example, `ES_URL` and `PG_URL` can be obtained directly from the corresponding Aiven services (OpenSearch & PostgreSQL)
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

With the server running, one can also test the API inside the local documentation site. This is done by changing the API URL inside their corresponding `.html` files, like `_templates/search.html` and `feedback-form.html` to match the local API URL.
(We're currently checking how to make this less manual)

From there, one can run `make livehtml` in the root folder to serve the doc site, and test the functions directly there.

## Production

We use `sam` to help deploy the changes as well. Be noted that if we change the AWS Lambda stack, we also have to change the API URL where it's used e.g. in `feedback-form.html` and in `search.html`.

First, we need to configure our AWS credentials locally so we can deploy (this may change when we use Aiven AWS account) - Open `~/.aws/credentials`, fill:

```
      aws_access_key_id = <access_key_id>
      aws_secret_access_key = <secret_access_key>
```

Both of those can be obtained from [AWS Security Credentials section](https://us-east-1.console.aws.amazon.com/iam/home#/security_credentials$access_key). Be noted that these access keys give unrestricted access to the entire AWS account.

Commands to use:

- `npm run deploy`: This runs a guided version of `sam deploy`.
- ![image](https://user-images.githubusercontent.com/110401626/202171402-9819f989-6260-4b93-a6e1-d2c05d1b9113.png)

  - Be noted that while most of the fields are straight-forward, the `CA_CERT` field [could be too long](https://github.com/aws/aws-sam-cli/issues/1845) to paste here. One workaround is to fill it with a random string, then before the final step to deploy, cancel it, go into `samconfig.toml` to replace the random string with the copied string from `npm run get-cert` above. This would be a non-issue after the first deployment since all the settings are saved so no need to do this every deployment.
  - <img width="644" alt="Screenshot 2022-11-09 at 15 54 44" src="https://user-images.githubusercontent.com/110401626/200848401-c7e2fdc4-8341-4abe-bf56-61d3c618554b.png">
  - This also is to be run every time a new environment parameter / setting is introduced in the future.
  - **Notes**: To deploy to the same stack, make sure the `samconfig.toml` at the end matches the production version (could be found in 1Password > Aiven DevPortal).

- `npm run quick-deploy`: This runs `sam deploy` with the existing `samconfig.toml`
  - To be used when no new environment parameter / setting is introduced

After a successful deployment, it'd show the endpoint for the deployed API like below. One can replace the API URL in the corresponding HTML files for testing with the local doc site.
![image](https://user-images.githubusercontent.com/110401626/202171273-d6344b71-473b-4e2d-8b55-d2dc6bcf7f16.png)

**Notes**: It's possible to check out the stack in AWS in AWS Cloudstack > Stacks > <stack name> for more details.
![image](https://user-images.githubusercontent.com/110401626/202171301-0dd98fc8-f627-412a-a597-cf8d283e4ebf.png)

## Workflow

A simple workflow for a new function called `foo.js` to fetch some data would be:

- Create `foo.js` in `src/handlers` containing codes for the function
- Create `FooFunction` in `template.yaml` under `Resources` to describe the function
- Run `npm run generate-event GET FooFunction` to simulate event for the function (and change it if needed)
- Add environment parameter in `template.yaml` Globals and `env.local.json` if needed
- Run `npm run invoke FooFunction` for one-time testings
- Run `npm run start` and `npm run watch` to test / develop
- Run `npm run deploy` and fill in appropriate values for the new function if needed
