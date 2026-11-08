import { chromium } from 'playwright';
import { setTimeout as sleep } from 'node:timers/promises';

const baseUrl = process.env.TEST_BASE_URL || 'http://127.0.0.1:4173';
const browser = await chromium.launch({
  headless: true,
  args: ['--no-sandbox', '--enable-webgl', '--use-gl=angle', '--use-angle=swiftshader', '--disable-dev-shm-usage'],
});
const page = await browser.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
const errors = [];
page.on('pageerror', (error) => errors.push(error.message));
page.on('console', (message) => { if (message.type() === 'error') errors.push(message.text()); });

try {
  await page.route('**/test-chat', async (route) => {
    const request = route.request();
    const data = request.postDataJSON();
    await route.fulfill({ status: 200, contentType: 'application/json', body: JSON.stringify({ answer: `Test answer for: ${data.question}` }) });
  });
  await page.goto(baseUrl, { waitUntil: 'networkidle' });
  await sleep(1600);
  const expected = [
    "What is Madhav's CGPA?",
    'Tell me about Madhav\'s projects.',
    'What technologies has Madhav used?',
    'What is Madhav studying?',
    'What experience and leadership roles does Madhav have?',
  ];
  const labels = await page.locator('.suggestion').allTextContents();
  if (labels.length !== 5 || expected.some((item, index) => !labels[index]?.includes(item))) throw new Error(`Suggested questions mismatch: ${JSON.stringify(labels)}`);
  const desktopLayout = await page.evaluate(() => {
    const rect = (selector) => { const el = document.querySelector(selector); if (!el) return null; const r = el.getBoundingClientRect(); return { x: Math.round(r.x), y: Math.round(r.y), width: Math.round(r.width), height: Math.round(r.height), right: Math.round(r.right), bottom: Math.round(r.bottom) }; };
    return { viewport: { width: innerWidth, height: innerHeight }, orb: rect('.celestial'), heading: rect('h1'), subtitle: rect('.subtitle'), questions: rect('.question-list'), composer: rect('.composer-wrap'), scrollWidth: document.documentElement.scrollWidth, scrollHeight: document.documentElement.scrollHeight, canvas: Boolean(document.querySelector('.celestial canvas')) };
  });
  await page.screenshot({ path: 'screenshots/josh-desktop-1440x900.png', fullPage: false });
  const suggestedQuestionResults = [];
  for (const question of expected) {
    if (await page.locator('.home-stage').count() === 0) await page.getByRole('button', { name: 'Home' }).click();
    await page.getByRole('button', { name: question }).click();
    await page.getByText(`Test answer for: ${question}`).waitFor();
    suggestedQuestionResults.push(await page.locator('.message-row.user .message-bubble').last().textContent());
  }
  const allSuggestedQuestionsPassed = suggestedQuestionResults.length === 5 && expected.every((question, index) => suggestedQuestionResults[index] === question);
  await page.getByRole('button', { name: 'Home' }).click();
  const input = page.getByRole('textbox', { name: 'Ask JOSH about Madhav' });
  await input.fill('Check the composer submission');
  await input.press('Enter');
  await page.getByText('Test answer for: Check the composer submission').waitFor();
  const composerSubmitPassed = true;
  await page.screenshot({ path: 'screenshots/josh-conversation-test.png', fullPage: false });

  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto(baseUrl, { waitUntil: 'networkidle' });
  await sleep(1500);
  const mobileLayout = await page.evaluate(() => {
    const rect = (selector) => { const el = document.querySelector(selector); if (!el) return null; const r = el.getBoundingClientRect(); return { x: Math.round(r.x), y: Math.round(r.y), width: Math.round(r.width), height: Math.round(r.height), right: Math.round(r.right), bottom: Math.round(r.bottom) }; };
    return { viewport: { width: innerWidth, height: innerHeight }, orb: rect('.celestial'), heading: rect('h1'), subtitle: rect('.subtitle'), questions: rect('.question-list'), composer: rect('.composer-wrap'), nav: rect('.sidebar'), scrollWidth: document.documentElement.scrollWidth, scrollHeight: document.documentElement.scrollHeight, canvas: Boolean(document.querySelector('.celestial canvas')) };
  });
  await page.screenshot({ path: 'screenshots/josh-mobile-390x844.png', fullPage: false });
  const noHorizontalOverflow = mobileLayout.scrollWidth <= mobileLayout.viewport.width;
  const noErrors = errors.length === 0;
  console.log(JSON.stringify({ desktopLayout, mobileLayout, allSuggestedQuestionsPassed, suggestedQuestionResults, composerSubmitPassed, noHorizontalOverflow, noErrors, errors }, null, 2));
  if (!allSuggestedQuestionsPassed || !noHorizontalOverflow || !noErrors) process.exitCode = 1;
} finally {
  await browser.close();
}
