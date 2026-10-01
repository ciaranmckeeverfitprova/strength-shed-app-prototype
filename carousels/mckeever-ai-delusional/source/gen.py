"""McKEEVER AI, HOLO SPOTLIGHT: 'I was called delusional' carousel (8 slides)."""
import math, pathlib, random

ROOT = pathlib.Path(__file__).parent
N = 8

ICON = {
    "chat": '<path d="M4 5h16v11H10l-5 4v-4H4z"/><circle cx="9" cy="10.5" r=".6"/><circle cx="12" cy="10.5" r=".6"/><circle cx="15" cy="10.5" r=".6"/>',
    "follow": '<path d="M19.5 12a7.5 7.5 0 1 1-2.2-5.3"/><path d="M20 4v4.5h-4.5"/>',
    "user": '<circle cx="9" cy="8" r="3.6"/><path d="M2.5 20c0-3.8 2.9-6 6.5-6s6.5 2.2 6.5 6"/><path d="M19 7.5v6M16 10.5h6"/>',
    "check": '<rect x="4" y="4" width="16" height="16" rx="3"/><path d="M8 12.3l2.8 2.8L16.2 9"/>',
    "cal": '<rect x="3.5" y="5.5" width="17" height="15" rx="2"/><path d="M3.5 10h17M8 3v5M16 3v5"/><circle cx="12" cy="15" r="1.2"/>',
    "bars": '<path d="M5 20v-7M10 20V8M15 20v-5M20 20V5"/>',
    "bolt": '<path d="M13.5 2.5L5 13.5h6.5l-1 8 8.5-11h-6.5z"/>',
    "moon": '<path d="M20 14.5A8.5 8.5 0 1 1 9.5 4a7 7 0 0 0 10.5 10.5z"/>',
    "pound": '<path d="M16 6.5A3.8 3.8 0 0 0 9 8.5V19M6.5 12.5h7M6 19h11"/>',
}

DEFS = """<defs>
<filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="soft" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="14"/></filter>
<radialGradient id="core"><stop offset="0" stop-color="#ffffff"/><stop offset=".25" stop-color="#bfe9ff"/><stop offset=".6" stop-color="#00AAFF" stop-opacity=".75"/><stop offset="1" stop-color="#00AAFF" stop-opacity="0"/></radialGradient>
<radialGradient id="nodefill" cx=".4" cy=".35"><stop offset="0" stop-color="#0d3a66"/><stop offset="1" stop-color="#020c1a"/></radialGradient>
<linearGradient id="edge" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset=".45" stop-color="#7FD4FF"/><stop offset="1" stop-color="#00AAFF"/></linearGradient>
<linearGradient id="edgeH" x1="0" x2="1"><stop offset="0" stop-color="#00AAFF" stop-opacity=".15"/><stop offset=".5" stop-color="#7FD4FF"/><stop offset="1" stop-color="#ffffff"/></linearGradient>
<linearGradient id="fillUp" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#00AAFF" stop-opacity=".55"/><stop offset="1" stop-color="#00AAFF" stop-opacity="0"/></linearGradient>
</defs>"""


def svg(x, y, w, h, body, z=20, vb=None):
    vb = vb or f"0 0 {w} {h}"
    return f'<svg style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;z-index:{z}" viewBox="{vb}">{DEFS}{body}</svg>'


def icon(name, cx, cy, size, color="#7FD4FF", sw=1.9):
    s = size / 24
    return (f'<g transform="translate({cx - size/2},{cy - size/2}) scale({s})" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{ICON[name]}</g>')


def node(cx, cy, r, ic=None, dashed=True, core=False):
    out = f'<circle cx="{cx+6}" cy="{cy+8}" r="{r}" fill="#0066BB"/>'  # depth layer
    out += f'<circle cx="{cx}" cy="{cy}" r="{r*1.6}" fill="url(#core)" opacity=".35"/>'
    if dashed:
        out += f'<circle cx="{cx}" cy="{cy}" r="{r+11}" fill="none" stroke="#7FD4FF" stroke-width="2" stroke-dasharray="3 6" opacity=".75"/>'
    out += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#nodefill)" stroke="url(#edge)" stroke-width="3.5" filter="url(#glow)"/>'
    out += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#ffffff" stroke-width="1.2" opacity=".8"/>'
    if core:
        out += f'<circle cx="{cx}" cy="{cy}" r="{r*.55}" fill="url(#core)"/>'
    if ic:
        out += icon(ic, cx, cy, r * 1.0, "#bfe9ff", 2.0)
    return out


def dot(cx, cy, r=7):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r*2.4}" fill="url(#core)" opacity=".8"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#0b2b4d" stroke="#7FD4FF" stroke-width="2.5" filter="url(#glow)"/>'
            f'<circle cx="{cx}" cy="{cy}" r="{r*.42}" fill="#ffffff"/>')


def ticks(cx, cy, r, n=120, long_every=10, a0=0, a1=360, op=.55, ln=10):
    out = []
    for k in range(n + 1):
        a = math.radians(a0 + (a1 - a0) * k / n)
        L = ln * (2 if k % long_every == 0 else 1)
        x1, y1 = cx + r * math.cos(a), cy + r * math.sin(a)
        x2, y2 = cx + (r - L) * math.cos(a), cy + (r - L) * math.sin(a)
        out.append(f'M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}')
    return f'<path d="{"".join(out)}" stroke="#7FD4FF" stroke-width="2" opacity="{op}"/>'


def arc(cx, cy, r, a0, a1, w=5, color="url(#edgeH)", glow=True, op=1):
    a0r, a1r = math.radians(a0), math.radians(a1)
    x0, y0 = cx + r*math.cos(a0r), cy + r*math.sin(a0r)
    x1, y1 = cx + r*math.cos(a1r), cy + r*math.sin(a1r)
    large = 1 if (a1 - a0) % 360 > 180 else 0
    f = ' filter="url(#glow)"' if glow else ''
    return f'<path d="M{x0:.1f} {y0:.1f}A{r} {r} 0 {large} 1 {x1:.1f} {y1:.1f}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" opacity="{op}"{f}/>'


def specks(seed, boxes, n=14):
    rnd = random.Random(seed)
    out = []
    for _ in range(n):
        x0, y0, x1, y1 = rnd.choice(boxes)
        x, y = rnd.uniform(x0, x1), rnd.uniform(y0, y1)
        s = rnd.choice([3, 4, 5, 6])
        out.append(f'<i class="speck" style="left:{x:.0f}px;top:{y:.0f}px;width:{s}px;height:{s}px;opacity:{rnd.uniform(.45,1):.2f}"></i>')
    return "".join(out)


def page(i, label, content, css="", chip="", fade=True):
    bars = "".join(f'<i class="{"on" if k <= i else ""}"></i>' for k in range(1, N + 1))
    return f"""<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="shared.css"><style>{css}</style></head><body>
<div class="grid"></div><div class="hair"></div>
{f'<div class="label">{label}</div>' if label else ''}{chip}
{content}
{'<div class="botfade"></div>' if fade else ''}
<img class="logo" src="assets/logo_mai.png"><div class="prog">{bars}</div>
</body></html>"""


def cut(src, x, y, w, extra=""):
    return (f'<div class="cutw" style="left:{x}px;top:{y}px;width:{w}px">'
            f'<img class="cut" src="assets/{src}" style="width:{w}px;{extra}"></div>')


def backlight(cx, cy, r):
    return f'<div class="backlight" style="left:{cx-r}px;top:{cy-r}px;width:{2*r}px;height:{2*r}px"></div>'


S = {}

# ---------- 01 HOOK: title only, arms crossed, live AI system cards ----------
def sys_card(title, sub, ic, tag="LIVE"):
    return f"""<div class="sc"><svg style="position:static;width:58px;height:58px;flex:none" viewBox="0 0 58 58">{DEFS}{node(27,27,23,ic,dashed=False)}</svg>
<div style="flex:1"><div class="sct">{title}</div><div class="scs">{sub}</div></div><div class="live">{tag}</div></div>"""

hook_rings = svg(250, 470, 820, 820,
    ticks(410, 410, 395, 180, 15, op=.45, ln=8)
    + arc(410, 410, 360, 200, 320, 6) + arc(410, 410, 360, 20, 95, 4, op=.8)
    + f'<circle cx="410" cy="410" r="318" fill="none" stroke="#7FD4FF" stroke-width="1.5" stroke-dasharray="2 9" opacity=".6"/>'
    + dot(410 + 360*math.cos(math.radians(320)), 410 + 360*math.sin(math.radians(320)), 8)
    + dot(410 + 360*math.cos(math.radians(200)), 410 + 360*math.sin(math.radians(200)), 6), z=6)

S[1] = page(1, "", f"""
<div class="h glowsoft" style="top:132px;font-size:76px;width:940px">I was called delusional for chasing this.<br>Now I build <span class="b glowtxt">AI that runs businesses.</span></div>
{backlight(700, 760, 420)}{hook_rings}
{cut('c_armscross_smile.png', 400, 520, 640)}
<div class="stack">
  {sys_card('Enquiry answered', 'Replied in 42 seconds', 'chat')}
  {sys_card('Follow up sent', 'Day 3, in your voice', 'follow')}
  {sys_card('Client onboarded', 'Forms and booking done', 'user')}
</div>
{specks(1, [(60, 560, 420, 1150), (900, 480, 1040, 900)])}
""", """
.stack{position:absolute;z-index:22;left:50px;top:650px;width:460px;display:flex;flex-direction:column;gap:34px;transform:perspective(1100px) rotateY(16deg);transform-origin:left center}
.sc{position:relative;display:flex;align-items:center;gap:18px;padding:20px 20px 20px 18px;border-radius:20px;border:2px solid var(--holo);
 background:linear-gradient(155deg,rgba(0,170,255,.45),rgba(0,102,187,.32) 50%,rgba(0,40,100,.6));
 box-shadow:10px 12px 0 rgba(0,70,140,.95),0 0 30px rgba(0,170,255,.55),inset 0 0 26px rgba(127,212,255,.25),inset 0 2px 0 rgba(255,255,255,.35)}
.sct{font-family:var(--head);font-weight:700;font-size:30px;line-height:1.1}
.scs{font-size:21px;color:rgba(255,255,255,.8);margin-top:5px}
.live{font-family:var(--mono);font-weight:800;font-size:14px;letter-spacing:.18em;color:#bff0ff;align-self:flex-start;display:flex;align-items:center;gap:7px}
.live::before{content:"";width:8px;height:8px;border-radius:50%;background:#3dffb0;box-shadow:0 0 8px #3dffb0}
.glowsoft{text-shadow:0 2px 30px rgba(0,0,0,.9)}
""")

# ---------- 02 WHO I AM: holo ID card ----------
id_ring = svg(0, 0, 150, 150, ticks(75, 75, 70, 72, 6, op=.7, ln=6) + arc(75, 75, 70, 200, 330, 4)
              + '<circle cx="75" cy="75" r="50" fill="url(#nodefill)" stroke="url(#edge)" stroke-width="3.5" filter="url(#glow)"/>'
              + '<text x="75" y="88" text-anchor="middle" font-family="Space Grotesk" font-weight="700" font-size="38" fill="#fff">CM</text>', z=2)
S[2] = page(2, "Who I am", f"""
<div class="h" style="top:150px;font-size:128px">Hi, I&rsquo;m <span class="b glowtxt">Ciar&aacute;n.</span></div>
<div class="p" style="top:318px;width:600px;font-size:35px">Former PT. Six years inside fitness businesses. Now building AI for service businesses.</div>
{backlight(830, 760, 380)}
{cut('c_standing.png', 590, 345, 470)}
<div class="holo idc">
  <div class="mono" style="font-size:19px;color:var(--holo);display:flex;align-items:center;gap:12px"><i class="okdot"></i>Profile verified</div>
  <div style="display:flex;align-items:center;gap:22px;margin:24px 0 22px">
    <div style="position:relative;width:150px;height:150px;flex:none">{id_ring}</div>
    <div><div style="font-family:var(--head);font-weight:700;font-size:38px;line-height:1.05">Ciar&aacute;n McKeever</div>
    <div class="mono" style="font-size:18px;color:var(--holo);margin-top:10px;letter-spacing:.3em">Founder</div></div>
  </div>
  <div class="row"><span>Base</span><b>Northern Ireland</b></div>
  <div class="row"><span>Fitness</span><b>6 years</b></div>
  <div class="row"><span>Background</span><b>Personal trainer</b></div>
  <div class="row"><span>Businesses</span><b>FitPro VA, McKEEVER AI</b></div>
</div>
{specks(2, [(60, 480, 560, 560), (60, 1110, 560, 1180)], 10)}
""", """
.idc{left:56px;top:560px;width:540px;padding:30px 34px 22px;transform:perspective(1200px) rotateY(12deg);transform-origin:left center}
.okdot{width:14px;height:14px;border-radius:50%;background:#3dffb0;box-shadow:0 0 10px #3dffb0;display:inline-block}
.row{display:flex;justify-content:space-between;align-items:center;padding:17px 0;border-top:1px solid rgba(127,212,255,.35);font-size:24px}
.row span{font-family:var(--mono);font-weight:700;font-size:17px;letter-spacing:.22em;text-transform:uppercase;color:var(--holo)}
.row b{font-family:var(--head);font-weight:600}
""")

# ---------- 03 WHERE IT STARTED: desk photo, battery at 8 percent ----------
battery = svg(0, 0, 420, 520,
    # moon
    '<circle cx="250" cy="120" r="120" fill="url(#core)" opacity=".45" filter="url(#soft)"/>'
    + '<path d="M300 60a82 82 0 1 0 22 108a66 66 0 0 1 -22 -108z" fill="#0066BB" transform="translate(7 9)"/>'
    + '<path d="M300 60a82 82 0 1 0 22 108a66 66 0 0 1 -22 -108z" fill="#0a3c6e" stroke="url(#edge)" stroke-width="4" filter="url(#glow)"/>'
    + '<path d="M300 60a82 82 0 1 0 22 108a66 66 0 0 1 -22 -108z" fill="url(#core)" opacity=".55"/>'
    # battery
    + '<rect x="58" y="300" width="300" height="130" rx="26" fill="#0066BB" transform="translate(10 12)"/>'
    + '<rect x="58" y="300" width="300" height="130" rx="26" fill="#03101f" stroke="url(#edge)" stroke-width="5" filter="url(#glow)"/>'
    + '<rect x="364" y="338" width="20" height="54" rx="7" fill="#7FD4FF" filter="url(#glow)"/>'
    + '<rect x="76" y="318" width="44" height="94" rx="12" fill="url(#core)"/><rect x="76" y="318" width="44" height="94" rx="12" fill="#ff4d6d" opacity=".0"/>'
    + '<rect x="76" y="318" width="44" height="94" rx="12" fill="none" stroke="#bfe9ff" stroke-width="2"/>'
    + '<text x="240" y="384" text-anchor="middle" font-family="Space Grotesk" font-weight="700" font-size="58" fill="#fff">8%</text>', z=20)
S[3] = page(3, "Where it started", f"""
<div class="photo3"></div>
<div style="position:absolute;left:620px;top:190px;width:420px;height:520px">{battery}</div>
<div class="mono" style="position:absolute;z-index:22;left:690px;top:660px;font-size:22px;line-height:1.75;color:var(--holo)">Sleep: 2 to 3 hrs<br><span style="color:#9aa3ad">Night shift mode</span></div>
<div class="h" style="top:880px;font-size:94px">I qualified in 2020.<br><span class="b glowtxt">Then lockdown hit.</span></div>
<div class="p" style="top:1090px;width:920px;font-size:31px">Gyms closed. I drove deliveries, then worked night shifts on two to three hours sleep. Band on hold. No social life.</div>
{specks(3, [(640, 160, 1040, 700)], 12)}
""", """
.photo3{position:absolute;z-index:3;left:0;top:30px;width:780px;height:866px;background:url(assets/desk_phone.jpg) center/cover;
 filter:saturate(.75) contrast(1.05) brightness(.92);
 -webkit-mask-image:linear-gradient(90deg,#000 55%,transparent 98%),linear-gradient(180deg,transparent 0%,#000 16%,#000 70%,transparent 99%);-webkit-mask-composite:source-in;mask-composite:intersect}
""", chip='<div class="chip manual">Survival mode</div>', fade=False)

# ---------- 04 TURNING POINT: referral network ----------
def tree():
    b = ''
    top = (250, 120)
    lvl2 = [(140, 300), (360, 300)]
    lvl3 = [(80, 470), (200, 470), (300, 470), (420, 470)]
    lvl4 = [(55 + k * 56, 600) for k in range(8)]
    def ln(a, c, op=.85):
        return f'<path d="M{a[0]} {a[1]}L{c[0]} {c[1]}" stroke="#7FD4FF" stroke-width="2.5" stroke-dasharray="7 7" opacity="{op}"/>'
    for p in lvl2: b += ln(top, p)
    for k, p in enumerate(lvl3): b += ln(lvl2[k // 2], p)
    for k, p in enumerate(lvl4): b += ln(lvl3[k // 2], p, .6)
    b += ticks(250, 120, 92, 90, 9, op=.6, ln=7) + arc(250, 120, 92, 180, 300, 4)
    b += node(250, 120, 60, None, dashed=False, core=True) + icon('bolt', 250, 120, 62, '#ffffff', 2.2)
    for p in lvl2: b += node(*p, 42, 'user')
    for p in lvl3: b += node(*p, 32, 'user')
    for p in lvl4: b += dot(*p, 9)
    return b
S[4] = page(4, "The turning point", f"""
<div class="h" style="top:150px;font-size:98px">ECA Belfast<br>Summit, <span class="b glowtxt">2024.</span></div>
<div class="p" style="top:372px;width:660px">Lenny needed help with sales, so I stepped in. He referred me to a client. That client referred another. <b style="color:#fff">FitPro VA was born.</b></div>
{backlight(810, 820, 390)}
{cut('c_phone_right.png', 495, 580, 593)}
<div style="position:absolute;left:40px;top:560px;width:500px;height:640px">{svg(0, 0, 500, 640, tree(), z=22)}</div>
<div class="mono" style="position:absolute;z-index:23;left:62px;top:640px;font-size:17px;color:var(--holo);line-height:1.6">ECA Summit<br><span style="color:#fff;font-family:var(--head);letter-spacing:0;text-transform:none;font-size:24px">One yes</span></div>
<div class="mono" style="position:absolute;z-index:23;left:62px;top:1180px;z-index:30;font-size:18px;color:var(--holo)">Referral by referral</div>
""")

# ---------- 05 THE DOUBT: struck-out word, 6 month timeline ----------
tl = svg(0, 0, 420, 140,
    '<path d="M30 40H390" stroke="url(#edgeH)" stroke-width="4" filter="url(#glow)"/>'
    + dot(30, 40, 9) + dot(210, 40, 9) + node(390, 40, 24, 'bolt', dashed=False), z=22)
S[5] = page(5, "The doubt", f"""
<div class="h" style="top:150px;font-size:76px;width:930px">&ldquo;I was called delusional more than once. <span class="b glowtxt">Even by people close to me.&rdquo;</span></div>
<div class="p" style="top:410px;width:640px">Six months after the Summit, I handed in my notice and went all in.</div>
{backlight(790, 860, 380)}
{cut('c_armscross_serious.png', 470, 580, 640)}
<div class="holo bub"><div class="word">Delusional.</div><div class="strike"></div></div>
<svg style="left:150px;top:836px;width:60px;height:56px;z-index:21" viewBox="0 0 60 56"><path d="M0 0H56L6 50z" fill="#0b4f93" stroke="#7FD4FF" stroke-width="2.5"/></svg>
<div class="mono" style="position:absolute;z-index:22;left:84px;top:930px;font-size:18px;color:var(--holo)">Heard it more than once</div>
<div style="position:absolute;left:54px;top:1010px;width:420px;height:140px">{tl}</div>
<div class="tlab" style="left:44px">Summit</div><div class="tlab" style="left:212px">+6 months</div><div class="tlab b" style="left:400px">All in</div>
{specks(5, [(60, 520, 460, 980)], 9)}
""", """
.bub{left:60px;top:640px;width:420px;height:200px;display:flex;align-items:center;justify-content:center}
.word{font-family:var(--head);font-weight:700;font-size:74px;color:rgba(255,255,255,.62);letter-spacing:-.02em}
.strike{position:absolute;left:44px;right:44px;top:50%;height:7px;border-radius:4px;background:#fff;box-shadow:0 0 12px #fff,0 0 26px var(--blue);transform:rotate(-4deg)}
.tlab{position:absolute;z-index:22;top:1080px;font-family:var(--mono);font-weight:800;font-size:17px;letter-spacing:.16em;text-transform:uppercase;color:#cfefff}
""")

# ---------- 06 THE PROOF: dashboard ----------
pts = [(0, 230), (70, 215), (140, 222), (210, 190), (280, 196), (350, 150), (420, 160), (490, 112), (560, 84), (620, 40)]
d = "M" + " L".join(f"{x} {y}" for x, y in pts)
chart = svg(0, 0, 640, 260,
    f'<path d="{d} L620 260 L0 260z" fill="url(#fillUp)" opacity=".7"/>'
    + f'<path d="{d}" fill="none" stroke="url(#edgeH)" stroke-width="6" stroke-linejoin="round" filter="url(#glow)"/>'
    + dot(620, 40, 11), z=2)
def tile(big, small, ic):
    return f"""<div class="holo tile"><svg style="position:absolute;right:18px;top:18px;width:54px;height:54px" viewBox="0 0 54 54">{DEFS}{node(25,25,21,ic,dashed=False)}</svg>
<div class="tb">{big}</div><div class="ts">{small}</div></div>"""
S[6] = page(6, "What it built", f"""
<div class="photo6"></div>
<div class="h" style="top:160px;font-size:132px">The<br><span class="b glowtxt">proof.</span></div>
<div class="holo dash">
  <div class="mono" style="font-size:18px;color:var(--holo);display:flex;justify-content:space-between"><span>&#9679; Record client</span><span style="color:#bfe9ff">Per month</span></div>
  <div class="big">&pound;45k</div>
  <div style="font-size:28px;color:var(--body)">a month for one client</div>
  <div style="position:absolute;right:40px;bottom:34px;width:470px;height:200px">{chart.replace('width:640px;height:260px', 'width:470px;height:191px')}</div>
</div>
<div class="tiles">
  {tile('&pound;11k', 'in 18 days, a record month', 'bars')}
  {tile('&pound;5k', 'extra in three weeks', 'pound')}
  {tile('60 to 90%', 'of my clients came by referral', 'user')}
</div>
""", """
.photo6{position:absolute;z-index:3;right:0;top:40px;width:660px;height:398px;background:url(assets/desk_laptop.jpg) center/cover;filter:saturate(.8) brightness(.95);
 -webkit-mask-image:linear-gradient(90deg,transparent 0%,#000 38%),linear-gradient(180deg,transparent 0%,#000 18%,#000 72%,transparent 100%);-webkit-mask-composite:source-in;mask-composite:intersect}
.dash{left:56px;top:470px;width:956px;height:390px;padding:34px 40px}
.big{font-family:var(--head);font-weight:700;font-size:170px;line-height:.95;letter-spacing:-.04em;margin:22px 0 6px;text-shadow:0 0 40px rgba(0,170,255,.6)}
.tiles{position:absolute;z-index:20;left:56px;top:910px;width:956px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:28px}
.tile{position:relative;height:250px;padding:30px 26px}
.tb{font-family:var(--head);font-weight:700;font-size:62px;letter-spacing:-.03em;margin-top:64px;white-space:nowrap}
.tiles .tile:last-child .tb{font-size:50px}
.ts{font-size:23px;line-height:1.3;color:var(--body);margin-top:8px}
""", fade=False)

# ---------- 07 WHAT I DO NOW: AI hub with the six systems ----------
SIX = [('chat', 'Enquiry replies'), ('follow', 'Lead follow up'), ('user', 'Client onboarding'),
       ('check', 'Client check-ins'), ('cal', 'Booking + reminders'), ('bars', 'Weekly reporting')]
def hub():
    cx, cy, rx, ry = 470, 330, 360, 190
    b = f'<ellipse cx="{cx}" cy="{cy}" rx="{rx+40}" ry="{ry+30}" fill="none" stroke="#7FD4FF" stroke-width="1.5" stroke-dasharray="2 8" opacity=".6"/>'
    b += f'<ellipse cx="{cx}" cy="{cy+8}" rx="{rx}" ry="{ry}" fill="none" stroke="#0066BB" stroke-width="10"/>'
    b += f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="none" stroke="url(#edgeH)" stroke-width="6" filter="url(#glow)"/>'
    pos = []
    for k in range(6):
        a = math.radians(-90 + k * 60 + 30)
        pos.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
    for p in pos:
        b += f'<path d="M{cx} {cy}L{p[0]:.0f} {p[1]:.0f}" stroke="#7FD4FF" stroke-width="2" stroke-dasharray="6 8" opacity=".7"/>'
    # globe core
    b += f'<circle cx="{cx}" cy="{cy}" r="190" fill="url(#core)" opacity=".5" filter="url(#soft)"/>'
    b += ticks(cx, cy, 118, 96, 8, op=.75, ln=7) + arc(cx, cy, 128, 150, 260, 5) + arc(cx, cy, 128, 330, 30, 5)
    b += f'<circle cx="{cx+8}" cy="{cy+10}" r="96" fill="#0066BB"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="96" fill="url(#nodefill)" stroke="url(#edge)" stroke-width="4" filter="url(#glow)"/>'
    b += f'<circle cx="{cx}" cy="{cy}" r="96" fill="url(#core)" opacity=".75"/>'
    for ry2 in (30, 62, 88):
        b += f'<ellipse cx="{cx}" cy="{cy}" rx="{ry2}" ry="96" fill="none" stroke="#bfe9ff" stroke-width="1.4" opacity=".55"/>'
    for dy in (-60, -30, 0, 30, 60):
        w = math.sqrt(96**2 - dy**2)
        b += f'<path d="M{cx-w:.0f} {cy+dy}H{cx+w:.0f}" stroke="#bfe9ff" stroke-width="1.4" opacity=".55"/>'
    b += f'<text x="{cx}" y="{cy+24}" text-anchor="middle" font-family="Space Grotesk" font-weight="700" font-size="70" fill="#fff" style="filter:drop-shadow(0 0 10px #00AAFF)">AI</text>'
    for (ic, lab), p in zip(SIX, pos):
        b += node(p[0], p[1], 40, ic)
    return b, pos
hb, hpos = hub()
labels = ""
for (ic, lab), (x, y) in zip(SIX, hpos):
    X, Y = x + 50, y + 520
    top = Y + 58 if y >= 300 else Y - 92
    labels += f'<div class="nl" style="left:{X-110:.0f}px;width:220px;top:{top:.0f}px;text-align:center">{lab}</div>'
S[7] = page(7, "What I do now", f"""
<div class="h" style="top:152px;font-size:84px">Now I build AI that<br><span class="b glowtxt">runs the backend.</span></div>
<div class="p" style="top:356px;width:900px;font-size:32px">McKEEVER AI installs done-for-you automation into service businesses. Live in 3 business days. You never touch it.</div>
<div style="position:absolute;left:50px;top:520px;width:940px;height:600px">{svg(0, 0, 940, 600, hb, z=20)}</div>
{labels}
{specks(7, [(60, 480, 1020, 520), (60, 1150, 1020, 1190)], 14)}
""", """
.nl{position:absolute;z-index:24;font-family:var(--mono);font-weight:800;font-size:15px;letter-spacing:.14em;text-transform:uppercase;color:#cfefff;white-space:nowrap;text-shadow:0 0 10px #000,0 0 4px #000}
""", chip='<div class="chip ai">AI mode active</div>', fade=False)

# ---------- 08 CTA ----------
def cta_rings():
    cx, cy = 540, 820
    b = ticks(cx, cy, 340, 200, 20, op=.4, ln=9) + arc(cx, cy, 310, 200, 340, 6) + arc(cx, cy, 310, 20, 60, 4, op=.8)
    b += f'<circle cx="{cx}" cy="{cy}" r="280" fill="none" stroke="#7FD4FF" stroke-width="1.5" stroke-dasharray="2 9" opacity=".6"/>'
    return b
def platform():
    b = ''
    for k, (rx, ry, op, dash) in enumerate([(430, 70, .55, '3 7'), (350, 56, .9, ''), (260, 42, 1, ''), (170, 28, .8, '4 6')]):
        da = f' stroke-dasharray="{dash}"' if dash else ''
        b += f'<ellipse cx="460" cy="110" rx="{rx}" ry="{ry}" fill="none" stroke="url(#edgeH)" stroke-width="{4 if not dash else 2}"{da} opacity="{op}" filter="url(#glow)"/>'
    b += '<ellipse cx="460" cy="110" rx="170" ry="28" fill="url(#core)" opacity=".7"/>'
    return b
orbit_back = svg(80, 700, 920, 300,
    '<ellipse cx="460" cy="120" rx="430" ry="95" fill="none" stroke="#0066BB" stroke-width="9" transform="translate(0 7)"/>'
    '<ellipse cx="460" cy="120" rx="430" ry="95" fill="none" stroke="url(#edgeH)" stroke-width="5" filter="url(#glow)"/>', z=8)
orbit_nodes = svg(80, 700, 920, 300,
    node(40, 130, 46, 'chat') + node(880, 110, 46, 'follow') + node(640, 205, 46, 'user'), z=24)
S[8] = page(8, "Your next step", f"""
<div class="cta"><span>DM me</span><span class="aibox">AI</span></div>
<div class="p" style="top:384px;left:0;width:1080px;text-align:center;font-size:34px">and let&rsquo;s talk about what your business<br>looks like when it runs without you.</div>
{svg(0, 0, 1080, 1350, cta_rings(), z=4)}
{backlight(540, 820, 400)}
{orbit_back}
{cut('c_fullbody.png', 325, 490, 430, '-webkit-mask-image:linear-gradient(180deg,#000 0%,#000 60%,transparent 76%)')}
{orbit_nodes}
<div class="mono" style="position:absolute;z-index:25;left:100px;top:738px;font-size:18px;color:var(--holo)">01</div>
<div class="mono" style="position:absolute;z-index:25;left:944px;top:718px;font-size:18px;color:var(--holo)">02</div>
<div class="mono" style="position:absolute;z-index:25;left:704px;top:812px;font-size:18px;color:var(--holo)">03</div>
<div style="position:absolute;left:80px;top:980px;width:920px;height:220px">{svg(0, 0, 920, 220, platform(), z=6)}</div>
{specks(8, [(60, 480, 300, 1000), (780, 480, 1040, 1000)], 14)}
""", """
.cta{position:absolute;z-index:30;top:150px;left:0;width:1080px;display:flex;justify-content:center;align-items:center;gap:34px;font-family:var(--head);font-weight:700;font-size:168px;letter-spacing:-.04em;line-height:1}
.aibox{color:var(--blue);border:5px solid var(--blue);border-radius:30px;padding:2px 30px 12px;text-shadow:0 0 30px rgba(0,170,255,.8);
 box-shadow:0 0 30px rgba(0,170,255,.8),inset 0 0 30px rgba(0,170,255,.45),10px 12px 0 rgba(0,70,140,.9);background:rgba(0,30,70,.6)}
""", fade=True)

for i, html in S.items():
    (ROOT / f"s{i:02d}.html").write_text(html, encoding="utf-8")
print("ok")
