const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const [svg, out, size] of JSON.parse(process.argv[2])) {
    await p.setViewportSize({ width: size, height: size });
    await p.goto('file://' + path.resolve(svg));
    await p.evaluate(s => { const e = document.querySelector('svg'); e.setAttribute('width', s); e.setAttribute('height', s); document.documentElement.style.background='transparent'; }, size);
    await p.screenshot({ path: out, omitBackground: true, clip: { x: 0, y: 0, width: size, height: size } });
  }
  await b.close();
})();
