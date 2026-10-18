# autonomous

A minimal Hono HTTP API. Requires Node.js 22 or newer and npm.

Install dependencies and start the server on port 3000:

```sh
npm ci
npm start
```

Check the endpoint:

```sh
curl --fail --include http://localhost:3000/
```

Expect HTTP 200, `Content-Type: application/json`, and:

```json
{"message":"Hello Hono!"}
```

The goodbye endpoint is available at `GET /goodbye`:

```sh
curl --fail --include http://localhost:3000/goodbye
```

It returns HTTP 200, `Content-Type: application/json`, and:

```json
{"message":"Goodbye!"}
```

Run with automatic restarts during development:

```sh
npm run dev
```

Run the endpoint test:

```sh
npm test
```
