import { Hono } from 'hono';

const app = new Hono();

app.get('/', (c) => c.json({ message: 'Hello Hono!' }));
app.get('/goodbye', (c) => c.json({ message: 'Goodbye!' }));

export default app;
