# Aiven Docs submitting feedback

Feedback are submitted to a PostgreSQL database maintained by Aiven. Production URI can be found in Devportal 1Password.

## Data

Currently the feedback table has 4 columns:

- **referrer** (string): Page URL where the feedback is submitted. Automatically filled
- **vote** (string): "up" / "down". Either a upvote or downvote. Filled by user when clicking corresponding buttons.
- **message** (string): Feedback field. Filled by user.
- **created_at** (string): Timestamp of the submitted feedback. Automatically filled.

The JS script in `feedback-form.html` would pick up `referrer`, `vote` and `message`by itself while `created_at`is assigned by the lambda upon creating the feedback in the database.

## Development

### One time invocation

Run `npm run generate-event POST CreateFeedbackFunction` inside `/aws` should give one a `event.CreateFeedbackFunction.local.json`. It looks like this

```
{
	"body":  "eyJ0ZXN0IjoiYm9keSJ9",
	"resource":  "/{proxy+}",
	"path":  "/path/to/resource",
	"httpMethod":  "POST",
}
```

To invoke this API with valid parameters, one should edit the `body` to be a stringified object containing necessary properties mentioned in the section above, e.g. `"body": "{\"url\":\"http://localhost:7777/\",\"vote\":\"down\",\"message\":\"test comment from sam local invoke\"}",`

### Start a live server

Another way for continuous testing is to have a `env.local.json` with `PG_URL` and `CA_CERT` properly filled. Then one can run `npm run watch` and `npm run start` (in different terminals) and test it with Postman or other API testing tools.

Be aware that when running SAM locally, it could mess with Sphynx autobuild, causing it to reload repeatedly. Recommendation for now is to use API testing tools when developing and only test with documentation site when things are somewhat stable.
