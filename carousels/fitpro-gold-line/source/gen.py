"""Stamp the 10 Gold Line artboards from per-slide content."""
import pathlib

ROOT = pathlib.Path(__file__).parent
N = 10


def frame(i, photo, content, extra_css="", footer=None):
    bars = "".join(f'<i class="{"on" if k <= i else ""}"></i>' for k in range(1, N + 1))
    if footer is None:
        footer = f'<div class="progress">{bars}</div><div class="swipe">Swipe &rarr;</div>'
    ph = ""
    if photo:
        src, h, pos = photo
        ph = (f'<div class="photo" style="height:{h}px;'
              f'background-image:url(assets/{src});background-position:{pos}"></div>'
              f'<div class="fade" style="top:{int(h*0.5)}px;height:{h - int(h*0.5) + 2}px"></div>'
              f'<div class="topscrim"></div>')
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="shared.css"><style>{extra_css}</style></head><body>
{ph}
<div class="topbar"><img class="mark" src="assets/icon.png"><div class="count"><b>{i:02d}</b> / {N}</div></div>
{content}
<div class="footer">{footer}</div>
</body></html>"""


S = {}

S[1] = frame(1, ("p01.jpg", 900, "center 30%"), """
<div class="block" style="bottom:168px">
  <div class="kicker" style="margin-bottom:34px">The origin story</div>
  <div class="h1" style="font-size:80px">2 years ago I was handed <span class="gold"><em>600&nbsp;phone numbers</em></span> and told to start&nbsp;ringing</div>
</div>""")

S[2] = frame(2, ("p02.jpg", 780, "center 20%"), """
<div class="block" style="bottom:168px">
  <div class="tag" style="margin-bottom:46px">July 2024</div>
  <div class="body" style="font-size:52px;line-height:1.26">My mate Lenny, CEO of ECA Belfast where I qualified as a PT, needed help selling tickets for his <span class="gold"><em>ECA Summit</em></span> that September</div>
</div>""")

S[3] = frame(3, ("p03.jpg", 640, "center 25%"), """
<div class="block" style="bottom:168px">
  <div style="display:flex;align-items:flex-end;gap:34px">
    <div class="gold" style="font-size:330px;font-weight:800;line-height:1;margin:-40px 0 -52px;padding-right:8px;letter-spacing:-.03em">600</div>
    <div style="font-size:44px;line-height:1.12;padding-bottom:6px"><em>past students.</em><br><span class="muted">Names and numbers.</span></div>
  </div>
  <div style="margin-top:58px;border-left:3px solid var(--gold);padding:6px 0 6px 36px">
    <div class="kicker" style="font-size:18px;margin-bottom:16px;gap:0">The brief</div>
    <div style="font-size:48px;font-weight:500;line-height:1.18">Ring them, sell tickets and upsell to&nbsp;VIP</div>
  </div>
  <div class="gold" style="margin-top:46px;font-size:46px;font-style:italic;font-weight:500">So I got to work.</div>
</div>""", ".kicker::before{display:none}")

S[4] = frame(4, ("p04.jpg", 880, "center 20%"), """
<div class="block" style="bottom:168px">
  <div class="muted" style="font-size:46px;font-style:italic">And after a few calls, I thought&hellip;</div>
  <div class="gold" style="font-size:300px;font-weight:800;font-style:italic;line-height:.95;letter-spacing:-.02em;margin:6px 0 4px -10px">Nah!</div>
  <div class="h1" style="font-size:62px">There&rsquo;s a smarter way to do&nbsp;this</div>
</div>""")

S[5] = frame(5, ("p05.jpg", 560, "center 18%"), """
<div class="block" style="bottom:168px">
  <div class="kicker" style="margin-bottom:26px">The smarter way</div>
  <div class="steps">
    <div class="step"><span>01</span><p>Email marketing and text outreach to spark conversations.</p></div>
    <div class="step"><span>02</span><p>Get people on calls instead of catching them cold on the phone.</p></div>
    <div class="step"><span>03</span><p>Ran it by Lenny and he approved, so we got going and it worked a&nbsp;treat.</p></div>
  </div>
  <div class="result">
    <div class="gold" style="font-size:150px;font-weight:800;line-height:1.05;padding-right:6px;margin:-18px 0 -10px">5</div>
    <div><div style="font-size:50px;font-weight:600;line-height:1.05">VIP upgrades</div>
    <div class="muted" style="font-size:34px;font-style:italic;margin-top:8px">and more tickets sold</div></div>
  </div>
</div>""", """
.step{display:flex;gap:30px;align-items:baseline;padding:20px 0;border-top:1px solid rgba(201,162,74,.28)}
.step span{font-family:var(--sans);font-weight:700;font-size:22px;letter-spacing:.2em;color:var(--gold);width:44px;flex:none}
.step p{font-size:36px;line-height:1.24}
.result{display:flex;gap:34px;align-items:center;margin-top:8px;padding-top:34px;border-top:2px solid var(--gold)}
""")

S[6] = frame(6, ("p06.jpg", 720, "center 15%"), """
<div class="block" style="bottom:168px">
  <div class="kicker" style="margin-bottom:30px">Weeks later</div>
  <div class="h1" style="font-size:78px">A few weeks later he rang&nbsp;me.</div>
  <div class="body muted" style="font-size:42px;margin-top:34px">Part of me thought I&rsquo;d overstepped or gone off script a&nbsp;bit.</div>
  <div class="rule" style="margin:44px 0 36px"></div>
  <div class="gold" style="font-size:58px;font-style:italic;font-weight:600">But he said quite the opposite.</div>
</div>""")

S[7] = frame(7, ("p07.jpg", 600, "center 10%"), """
<div class="ghost" style="font-size:520px;right:40px;top:420px">&rdquo;</div>
<div class="block" style="bottom:168px">
  <div class="body muted" style="font-size:42px;font-style:italic">He never wanted someone to just do what they were&nbsp;told.</div>
  <div class="h1" style="font-size:68px;margin-top:34px;line-height:1.12">He wanted <span class="gold"><em>ideas, initiative, creativity,</em></span> someone who&rsquo;d actually&nbsp;think.</div>
  <div class="rule" style="margin:46px 0 34px"></div>
  <div class="body" style="font-size:40px">Which is exactly what I had done without&nbsp;realising.</div>
</div>""")

S[8] = frame(8, ("p08.jpg", 560, "center 12%"), """
<div class="block" style="bottom:168px">
  <div class="h1" style="font-size:62px">That one phone call changed&nbsp;everything.</div>
  <div class="body muted" style="font-size:36px;margin-top:24px">He put me with one of his mastermind clients. I asked him, half-joking, <em style="color:var(--ivory)">&ldquo;Could I do this for other coaches?&rdquo;</em></div>
  <div class="quote">
    <div class="qmark gold">&ldquo;</div>
    <div class="kicker" style="font-size:18px;margin-bottom:18px">He said</div>
    <div style="font-size:54px;font-weight:600;line-height:1.14">Yes, you&rsquo;re basically working as a <span class="gold"><em>virtual assistant</em></span></div>
  </div>
</div>""", """
.quote{position:relative;margin-top:44px;padding:44px 46px 46px;border:2px solid rgba(201,162,74,.75);background:linear-gradient(160deg,rgba(201,162,74,.10),rgba(201,162,74,0) 60%)}
.qmark{position:absolute;top:-62px;right:36px;font-size:190px;font-weight:800;line-height:1;background-color:var(--black);padding:0 16px}
""")

S[9] = frame(9, ("p09.jpg", 600, "70% 15%"), """
<div class="block" style="bottom:168px">
  <div class="kicker" style="margin-bottom:28px">And that was it</div>
  <div class="h1" style="font-size:84px;line-height:1.06">The whole business, sitting right there in<br><span class="gold"><em>a question I almost didn&rsquo;t&nbsp;ask.</em></span></div>
  <div style="display:flex;gap:30px;align-items:flex-start;margin-top:48px;padding-top:36px;border-top:1px solid rgba(201,162,74,.35)">
    <div style="font-family:var(--sans);font-weight:700;font-size:20px;letter-spacing:.24em;color:var(--gold);line-height:1.5;white-space:nowrap">THE<br>LEAP</div>
    <div class="body" style="font-size:36px;line-height:1.3">6 months after the summit, I quit my night shift job to go&nbsp;all&#8209;in.</div>
  </div>
</div>""", ".kicker::before{display:none} .kicker{font-family:var(--serif);font-style:italic;font-weight:500;font-size:46px;letter-spacing:0;text-transform:none}")

S[10] = frame(10, ("p10.jpg", 650, "center 20%"), """
<div class="border"></div>
<div class="block" style="bottom:150px;text-align:center">
  <div style="font-size:50px;font-weight:600;line-height:1.14">Funny how the biggest turns in your life don&rsquo;t announce&nbsp;themselves.</div>
  <div class="body muted" style="font-size:34px;margin:28px auto 0;max-width:820px">You&rsquo;re just sat there with a list of numbers deciding whether to colour inside the lines or&nbsp;not.</div>
  <div class="gold" style="font-size:96px;font-style:italic;font-weight:700;margin-top:30px;line-height:1.1">I&rsquo;m glad I didn&rsquo;t.</div>
  <img src="assets/logo.png" style="width:330px;margin-top:46px">
</div>""", """
.border{position:absolute;inset:26px;border:2px solid var(--gold);z-index:30;pointer-events:none}
.footer{justify-content:center;bottom:68px;color:var(--gold);letter-spacing:.3em;font-size:16px}
.topbar{top:62px}
""", footer="@ciaran_mckeever_fitprova")

for i, html in S.items():
    (ROOT / f"s{i:02d}.html").write_text(html, encoding="utf-8")
print("ok")
