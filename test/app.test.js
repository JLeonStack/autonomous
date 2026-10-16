import assert from 'node:assert/strict';
import test from 'node:test';
import app from '../src/app.js';

test('GET / returns the greeting as JSON', async () => {
  const response = await app.request('/');

  assert.equal(response.status, 200);
  assert.match(response.headers.get('content-type'), /^application\/json\b/);
  assert.deepEqual(await response.json(), { message: 'Hello Hono!' });
});
