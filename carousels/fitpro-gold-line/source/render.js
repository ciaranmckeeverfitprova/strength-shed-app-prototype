const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const path = require('path'), fs = require('fs');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  const files = process.argv.slice(2).length ? process.argv.slice(2) : fs.readdirSync(__dirname).filter(f => /^s\d+\.html$/.test(f));
  for (const f of files) {
    await p.goto('file://' + path.join(__dirname, f));
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(300);
    await p.screenshot({ path: path.join(__dirname, 'out', f.replace('.html', '.png')) });
  }
  await b.close();
})();
