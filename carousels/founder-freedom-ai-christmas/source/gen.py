import random, pathlib

ROOT = pathlib.Path(__file__).parent
N = 11

FLAKE = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round">'
         '<path d="M12 2v20M3.3 7l17.4 10M20.7 7 3.3 17M9 4l3 3 3-3M9 20l3-3 3 3"/></svg>')
TICK = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
CROSS = '<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="3.6" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg>'


def arrow(color="#fff"):
    return (f'<svg class="arrow" viewBox="0 0 74 48" fill="none" stroke="{color}" stroke-width="5" '
            'stroke-linecap="round" stroke-linejoin="round"><path d="M10 6l18 18-18 18M36 6l18 18-18 18"/></svg>')


def snow(seed, n=46, opacity=1.0):
    r = random.Random(seed)
    dots = []
    for _ in range(n):
        s = r.choice([3, 4, 5, 6, 8, 10])
        o = r.uniform(.25, .85) * opacity
        blur = 'filter:blur(2px);' if s >= 8 else ''
        dots.append(f'<i style="left:{r.randint(0,1075)}px;top:{r.randint(0,1345)}px;'
                    f'width:{s}px;height:{s}px;opacity:{o:.2f};{blur}"></i>')
    return '<div class="snow">' + ''.join(dots) + '</div>'


def prog(i):
    return '<div class="prog">' + ''.join(
        f'<b class="{"on" if k == i else "done" if k < i else ""}"></b>' for k in range(1, N + 1)) + '</div>'


def page(i, ground, body, logo_chip=False, last=False, arrow_color="#fff", snow_n=46, snow_op=1.0):
    head = ('<!doctype html><html><head><meta charset="utf-8">'
            '<link rel="preconnect" href="https://fonts.googleapis.com">'
            '<link href="https://fonts.googleapis.com/css2?family=Anton&family=Instrument+Serif:ital@0;1'
            '&family=Inter:wght@400;500;600;700;800;900&display=block" rel="stylesheet">'
            '<link rel="stylesheet" href="shared.css"></head>')
    count = f'<div class="count">{i:02d} <span>/ {N:02d}</span></div>'
    logo = f'<div class="logo{" chip" if logo_chip else ""}"></div>'
    html = (head + f'<body class="{ground}">' + snow(i * 7, snow_n, snow_op) + logo + count + body
            + prog(i) + ('' if last else arrow(arrow_color)) + '</body></html>')
    (ROOT / f's{i:02d}.html').write_text(html, encoding='utf-8')


def bauble_row(extra=''):
    return f'<div class="baubles" {extra}>' + ''.join(f'<div class="bauble">{n}</div>' for n in (1, 2, 3)) + '</div>'


# 01 - cover
page(1, 'g-dark', f'''
<div class="abs" style="left:var(--m);top:190px"><span class="pill">{FLAKE}Christmas AI Install</span></div>
<div class="abs d" style="left:66px;top:262px;font-size:178px">Opportunity</div>
<div class="abs s" style="left:var(--m);top:432px;font-size:60px;color:var(--ice)">for just <span class="hi">3 founders</span> &middot; all before Christmas</div>
<ul class="abs checks" style="left:var(--m);top:580px;width:560px;font:800 35px/1.15 var(--sans);text-transform:uppercase;letter-spacing:.01em">
  <li><span class="tick">{TICK}</span><span style="padding-top:6px">AI automation installed for you</span></li>
  <li><span class="tick">{TICK}</span><span style="padding-top:6px">20+ hours back every&nbsp;week</span></li>
  <li><span class="tick">{TICK}</span><span style="padding-top:6px">Your freedom back before Christmas</span></li>
</ul>
<div class="abs" style="left:56px;top:1040px;transform:rotate(-5deg);z-index:12">
  <span class="ribbon" style="background:var(--red)">Only 3 spaces &mdash; don&rsquo;t miss this</span></div>
<div class="abs" style="right:-120px;bottom:0;width:720px;height:820px;z-index:4;
  background:url(assets/studio_cut.png) center top/auto 1080px no-repeat;
  filter:drop-shadow(0 0 40px rgba(10,132,255,.35))"></div>
<div class="abs" style="right:-120px;bottom:0;width:720px;height:160px;z-index:4;background:linear-gradient(180deg,transparent,#04060b)"></div>
''')

# 02 - three founders
page(2, 'g-dark', f'''
<div class="abs s" style="left:var(--m);top:200px;font-size:92px;color:var(--ice)">I&rsquo;m looking for</div>
<div class="abs d" style="left:66px;top:330px;font-size:240px">Three</div>
<div class="abs d glow" style="left:66px;top:560px;font-size:240px;color:var(--blue)">Founders</div>
<div class="abs" style="left:var(--m);top:850px;width:900px;font:600 50px/1.25 var(--sans)">
  who want their <span class="hi" style="font-weight:800">freedom back</span> before <span class="hi" style="font-weight:800">Christmas.</span></div>
<div class="abs" style="left:var(--m);top:1040px">{bauble_row()}</div>
''')

# 03 - personally (light)
page(3, 'g-light', f'''
<div class="abs d" style="left:66px;top:190px;font-size:150px;color:var(--navy)">I&rsquo;ll</div>
<div class="abs s" style="left:60px;top:300px;font-size:230px;line-height:1;color:var(--blue)">personally</div>
<div class="abs d" style="left:66px;top:580px;font-size:132px;color:var(--navy)">Install AI<br>Automation</div>
<div class="abs d" style="left:66px;top:830px;font-size:132px;color:var(--blue)">Into your<br>business.</div>
<div class="pol" style="left:676px;top:850px;width:330px;height:390px;transform:rotate(5deg)">
  <div class="ph" style="background-image:url(assets/ship.jpg);background-position:28% 8%"></div>
  <div class="cap"><span>Done for you</span><span>&#10052;</span></div></div>
<div class="tape" style="left:770px;top:830px;transform:rotate(-4deg)"></div>
''', logo_chip=True, arrow_color="#0a1b38", snow_op=.9)

# 04 - tedious as hell (laptop photo)
page(4, 'g-dark', f'''
<div class="abs" style="left:0;top:0;width:1080px;height:800px;z-index:2;
  background:url(assets/laptop.jpg) 46% 30%/cover no-repeat"></div>
<div class="abs" style="left:0;top:0;width:1080px;height:300px;z-index:3;background:linear-gradient(180deg,rgba(4,6,11,.75),transparent)"></div>
<div class="abs" style="left:0;top:360px;width:1080px;height:460px;z-index:3;background:linear-gradient(180deg,transparent,#061022 82%)"></div>
<div class="abs" style="left:var(--m);top:540px;z-index:6"><span class="pill">{FLAKE}The offer</span></div>
<div class="abs d" style="left:66px;top:612px;font-size:134px;z-index:6;white-space:nowrap">Admin &amp; backend</div>
<div class="abs s" style="left:68px;top:728px;font-size:150px;line-height:1;z-index:6;color:var(--blue-hi)">automated.</div>
<div class="abs" style="left:var(--m);top:925px;width:930px;z-index:6;font:400 40px/1.4 var(--sans);color:#c6d2e4">
  To automate the admin and repetitive tasks that are, quite honestly, tedious as hell.</div>
<div class="abs" style="left:var(--m);top:1092px;width:930px;z-index:6;font:800 44px/1.25 var(--sans)">
  Nobody wants to do them. <span class="hi" style="white-space:nowrap">So you won&rsquo;t have to.</span></div>
''', logo_chip=True, snow_n=26)

# 05 - freedom (balcony)
page(5, 'g-dark', f'''
<div class="abs" style="left:0;top:0;width:1080px;height:960px;z-index:2;background:url(assets/balcony.jpg) 50% 18%/cover no-repeat"></div>
<div class="abs" style="left:0;top:0;width:1080px;height:230px;z-index:3;background:linear-gradient(180deg,rgba(4,10,24,.8),transparent)"></div>
<div class="abs" style="left:0;top:560px;width:1080px;height:420px;z-index:3;background:linear-gradient(180deg,transparent,#04060b 82%)"></div>
<div class="abs" style="left:var(--m);top:770px;z-index:6"><span class="pill">{FLAKE}The result</span></div>
<div class="abs d glow" style="left:62px;top:830px;font-size:210px;z-index:6;color:var(--blue)">Freedom.</div>
<div class="abs" style="left:var(--m);top:1036px;width:936px;z-index:6;font:800 44px/1.2 var(--sans)">And the time to actually enjoy <span class="s" style="font-weight:400;font-size:62px;color:var(--blue-hi)">Christmas.</span></div>
<div class="abs" style="left:var(--m);top:1112px;width:936px;z-index:6;font:400 31px/1.4 var(--sans);color:#d2dcea">
  Without the stress. Without the laptop open on Christmas Eve.</div>
''', logo_chip=True, snow_n=30)

# 06 - naughty list
def items(rows, icon, color, size=38):
    return ''.join(
        f'<li><span class="{"tick" if icon == TICK else "cross"}">{icon}</span>'
        f'<span style="padding-top:2px;font:600 {size}px/1.3 var(--sans);color:{color}">{t}</span></li>' for t in rows)

page(6, 'g-dark', f'''
<div class="abs" style="left:var(--m);top:200px"><span class="ribbon" style="background:var(--red)">The naughty list</span></div>
<div class="abs d" style="left:66px;top:290px;font-size:200px">This is<br><span class="red">not</span> for</div>
<ul class="abs checks" style="left:var(--m);top:700px;width:900px;gap:46px">
{items(["Founders who&rsquo;d rather keep doing <b>everything themselves</b>",
        "Anyone after a <b>quick hack</b>, not a real system",
        "Businesses happy to keep <b>losing hours to admin</b>"], CROSS, "#e6ecf6")}
</ul>
''')

# 07 - nice list (light)
page(7, 'g-light', f'''
<div class="abs" style="left:var(--m);top:200px"><span class="ribbon" style="background:var(--blue)">The nice list</span></div>
<div class="abs d" style="left:66px;top:290px;font-size:200px;color:var(--navy)">This <span class="blue">is</span><br>for</div>
<ul class="abs checks" style="left:var(--m);top:700px;width:900px;gap:46px">
{items(["Founders <b>buried in admin</b> and repetitive tasks",
        "Founders ready to <b>hand the tedious stuff to AI</b>",
        "Founders who want their <b>evenings, Fridays and Christmas</b> back"], TICK, "#0a1b38")}
</ul>
''', logo_chip=True, arrow_color="#0a1b38", snow_op=.9)

# 08 - receipts
wins = [("Onboarding flows fully automated", "Without the founder or their team lifting a finger."),
        ("A full week of content, handled", "My AI creates, proofs and schedules it. Hours saved every week."),
        ("Stripe audited", "Failed payments caught early, before they cost money."),
        ("Personalised client plans", "Produced faster and looking more premium."),
        ("Client comms and check-ins automated", "Clients stay looked after without anyone chasing.")]
rows = ''.join(
    f'<div style="display:flex;gap:26px;align-items:flex-start;padding:22px 0;border-top:1.5px solid rgba(255,255,255,.12)">'
    f'<div class="d blue glow" style="font-size:54px;line-height:1;width:66px">{k:02d}</div>'
    f'<div><div style="font:800 34px/1.15 var(--sans);letter-spacing:-.01em">{t}</div>'
    f'<div style="font:400 25px/1.35 var(--sans);color:#a9b8cf;margin-top:6px">{s}</div></div></div>'
    for k, (t, s) in enumerate(wins, 1))
page(8, 'g-dark', f'''
<div class="abs" style="left:var(--m);top:186px"><span class="pill">{FLAKE}The receipts</span></div>
<div class="abs s" style="left:var(--m);top:250px;font-size:84px;line-height:1;color:var(--ice)">Over the last year</div>
<div class="abs d" style="left:66px;top:344px;font-size:128px">I have&hellip;</div>
<div class="pol" style="left:686px;top:150px;width:300px;height:380px;padding:14px 14px 54px;transform:rotate(6deg)">
  <div class="ph" style="background-image:url(assets/event.jpg);background-position:50% 30%"></div>
  <div class="cap" style="font-size:15px;bottom:18px"><span>In the room</span><span>&#10052;</span></div></div>
<div class="tape" style="left:770px;top:132px;width:140px;transform:rotate(3deg)"></div>
<div class="abs" style="left:var(--m);top:540px;width:936px">{rows}</div>
''')

# 09 - 20+ hours, before/after
chips = ''.join(
    f'<div style="display:flex;gap:14px;align-items:center;font:600 31px/1 var(--sans)">'
    f'<i style="width:12px;height:12px;border-radius:50%;background:var(--blue);box-shadow:0 0 12px var(--blue)"></i>{t}</div>'
    for t in ["Grow the business", "Get evenings back", "Take Friday afternoon off", "Spend time with family"])
page(9, 'g-dark', f'''
<div class="abs" style="left:var(--m);top:186px;font:800 23px/1 var(--sans);letter-spacing:.2em;color:var(--blue-hi);text-transform:uppercase">Together, these save my clients</div>
<div class="abs d glow" style="left:60px;top:226px;font-size:300px;color:var(--blue)">20+</div>
<div class="abs d" style="left:560px;top:268px;font-size:96px;line-height:.95">Hours every<br>single week.</div>
<div class="pol" style="left:80px;top:556px;width:430px;height:470px;transform:rotate(-4deg)">
  <div class="ph" style="background-image:url(assets/laptop.jpg);background-position:44% 40%"></div>
  <div class="cap"><span>Before</span><span style="color:var(--red)">&#10052;</span></div></div>
<div class="tape" style="left:180px;top:536px;transform:rotate(-8deg)"></div>
<div class="pol" style="left:560px;top:546px;width:430px;height:470px;transform:rotate(3.5deg)">
  <div class="ph" style="background-image:url(assets/dog.jpg);background-position:50% 30%"></div>
  <div class="cap"><span>After</span><span style="color:var(--blue)">&#10052;</span></div></div>
<div class="tape" style="left:690px;top:526px;transform:rotate(5deg)"></div>
<div class="abs" style="left:var(--m);top:1074px;font:800 22px/1 var(--sans);letter-spacing:.2em;color:var(--muted)">TIME TO</div>
<div class="abs" style="left:var(--m);top:1116px;width:936px;display:grid;grid-template-columns:1fr 1fr;row-gap:30px">{chips}</div>
''')

# 10 - only 3 spaces
tags = ''.join(
    f'<div style="transform:rotate({rot}deg);background:#fff;color:#0a1b38;padding:18px 30px 18px 46px;'
    f'font:800 30px/1 var(--sans);letter-spacing:.14em;clip-path:polygon(22px 0,100% 0,100% 100%,22px 100%,0 50%);'
    f'box-shadow:0 10px 24px rgba(0,40,110,.3);position:relative">'
    f'<i style="position:absolute;left:22px;top:50%;width:10px;height:10px;margin-top:-5px;border-radius:50%;background:#0a1b38"></i>SPACE 0{n}</div>'
    for n, rot in ((1, -2), (2, 2), (3, -1.5)))
page(10, 'g-sky', f'''
<div class="abs" style="left:var(--m);top:200px"><span class="pill" style="background:rgba(255,255,255,.18);border-color:rgba(255,255,255,.5)">{FLAKE}Before Christmas</span></div>
<div class="abs s" style="left:var(--m);top:270px;font-size:110px;line-height:1">Only</div>
<div class="abs d" style="left:60px;top:378px;font-size:330px;line-height:.86">3</div>
<div class="abs d" style="left:62px;top:676px;font-size:230px;line-height:.86">spaces.</div>
<div class="abs" style="right:var(--m);top:400px;display:flex;flex-direction:column;gap:26px;align-items:flex-end">{tags}</div>
<div class="abs" style="left:var(--m);top:960px;width:930px;font:600 44px/1.3 var(--sans)">
  That&rsquo;s all I can <span style="background:#fff;color:var(--blue-deep);padding:0 12px;border-radius:8px;font-weight:800">personally install</span>
  before Christmas. Once they&rsquo;re gone, they&rsquo;re gone.</div>
''', logo_chip=True, snow_op=.9)

# 11 - CTA
page(11, 'g-cta', f'''
<div class="abs" style="left:var(--m);top:200px"><span class="pill" style="background:rgba(4,10,30,.25);border-color:rgba(255,255,255,.45)">{FLAKE}3 spaces only</span></div>
<div class="abs s" style="left:var(--m);top:282px;font-size:76px;line-height:1">Want your freedom back?</div>
<div class="abs d" style="left:66px;top:380px;font-size:150px">DM me the word</div>
<div class="abs" style="left:56px;top:560px;z-index:8">
  <div style="position:relative;background:#fff;border-radius:34px;padding:30px 54px 22px;box-shadow:0 24px 50px rgba(0,20,70,.4)">
    <div class="d" style="font-size:170px;color:var(--blue)">&ldquo;Freedom&rdquo;</div>
    <i style="position:absolute;left:70px;bottom:-34px;width:0;height:0;border-left:22px solid transparent;border-right:30px solid transparent;border-top:40px solid #fff"></i>
  </div></div>
<div class="abs s" style="left:var(--m);top:850px;font-size:76px;line-height:1.02;width:520px">and I&rsquo;ll be<br>in touch.</div>
<div class="abs" style="left:var(--m);top:1040px">{bauble_row()}</div>
<div class="abs" style="right:-150px;bottom:0;width:640px;height:700px;z-index:4;
  background:url(assets/studio_cut.png) center top/auto 920px no-repeat;filter:drop-shadow(0 20px 40px rgba(0,20,70,.5))"></div>
''', logo_chip=True, last=True)
print('ok')
