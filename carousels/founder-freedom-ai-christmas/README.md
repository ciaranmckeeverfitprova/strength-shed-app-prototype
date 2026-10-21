# Founder Freedom AI: Christmas carousel ("The Countdown")

11 slides at 1080x1350 (4:5), ready to post in this order: `slides/`. All 11 are also in `FounderFreedom_Christmas_carousel.zip`.

The structure follows the reference 11-slide Christmas offer carousel: cover with checklist, "I'm looking for", "I'll personally", the not-for and is-for lists, proof slides, a "spaces" slide and a pattern-breaking CTA. It's restyled in the Founder Freedom AI black and electric-blue brand.

## Re-render
```
cd source
python3 gen.py                 # writes s01..s11.html
mkdir -p out && node render.cjs  # needs Playwright + Chromium; renders out/sNN.png
```
Fonts: Anton, Instrument Serif and Inter (Google Fonts).
