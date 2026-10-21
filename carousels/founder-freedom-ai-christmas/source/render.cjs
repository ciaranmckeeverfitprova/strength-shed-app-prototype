const { chromium } = require(require('child_process').execSync('npm root -g').toString().trim() + '/playwright');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  const only = process.argv.slice(2);
  for (let i = 1; i <= 11; i++) {
    const n = String(i).padStart(2, '0');
    if (only.length && !only.includes(n)) continue;
    await p.goto('file://' + __dirname + '/s' + n + '.html', { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(300);
    await p.screenshot({ path: __dirname + '/out/s' + n + '.png' });
  }
  await b.close();
})();
