import { spawn } from 'node:child_process';
import { setTimeout as sleep } from 'node:timers/promises';

const vite = spawn('pnpm', ['exec', 'vite', '--host', '127.0.0.1', '--port', '4173', '--strictPort'], {
  stdio: 'ignore',
  env: { ...process.env, VITE_CHAT_API_URL: 'http://127.0.0.1:4173/test-chat' },
});
try {
  let ready = false;
  for (let attempt = 0; attempt < 80; attempt += 1) {
    try {
      const response = await fetch('http://127.0.0.1:4173');
      if (response.ok) { ready = true; break; }
    } catch {}
    await sleep(250);
  }
  if (!ready) throw new Error('Vite did not become ready on port 4173');
  const test = spawn(process.execPath, ['tests/ui-smoke.mjs'], { stdio: 'inherit', env: process.env });
  const code = await new Promise((resolve, reject) => {
    test.once('error', reject);
    test.once('exit', (status, signal) => resolve(status ?? (signal ? 1 : 0)));
  });
  process.exitCode = code;
} finally {
  vite.kill('SIGTERM');
}
