# Aiven Docs submitting feedback

Feedback are submitted to a PostgreSQL database maintained by Aiven. Production URI can be found in Devportal 1Password.

## Data

Currently the feedback table has 4 columns:

- **referrer** (string): Page URL where the feedback is submitted. Automatically filled
- **vote** (string): "up" / "down". Either a upvote or downvote. Filled by user when clicking corresponding buttons.
- **message** (string): Feedback field. Filled by user.
- **created_at** (string): Timestamp of the submitted feedback. Automatically filled.

The JS script in `feedback-form.html` would pick up `referrer`, `vote` and `message`by itself while `created_at`is assigned by the lambda upon creating the feedback in the database.

## Testing locally

### One time testing

Following the instructions [here](https://github.com/aiven/devportal/tree/feature/use-aws/aws#development) one should have a `event.CreateFeedbackFunction.local.json` after running `npm run generate-event POST CreateFeedbackFunction`. It looks like this

```
{
	"body":  "eyJ0ZXN0IjoiYm9keSJ9",
	"resource":  "/{proxy+}",
	"path":  "/path/to/resource",
	"httpMethod":  "POST",
}
```

To invoke this API with valid parameters, one should edit the `body` to be a stringified object containing necessary properties mentioned in the section above, e.g. `"body": "{\"url\":\"http://localhost:7777/\",\"vote\":\"down\",\"message\":\"test comment from sam local invoke\"}",`

### Continuous testing

Another way for continuous testing is to have a `env.local.json` with `PG_URL` and `CA_CERT` properly filled. Then one can run `npm run watch` and `npm run start` (in different terminals) and test it with Postman or other API testing tools.

Be aware that when running SAM locally, it could mess with Sphynx autobuild `make livehtml`, causing it to reload repeatedly. Recommendation for now is to use API testing tools when developing the lambda, and only test with the local documentation site when needed.

**Notes**

- The `PG_URL` copied from the Aiven service should have the `sslmode=true` part removed e.g. `postgres://avnadmin:foobar@pg-barbaz-sandbox.aivencloud.com:12691/defaultdb`.

## Gotchas

- When I test with the local doc site, submitting a feedback gives error about CORS?
  - It's likely the URL of the local doc site isn't included in the allowed list of the lambda. To fix this, open the `create-feedback.js`and update the `allowedOrigins` to include your site then deploy it.

```
const  allowedOrigins  =  [
	"https://devportal.pages.dev",
	"http://localhost:[0-9]*",
	"<Your local doc site URL>"
];
```

- When I deploy the first time, I got some error related to samconfig syntax?
  - There could be many causes, but one notable is wrong `CA_CERT` property format. It should look like `PostgresCert=\"-----BEGIN CERTIFICATE-----\n......\n-----END CERTIFICATE-----\n\""`
