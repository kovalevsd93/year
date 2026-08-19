# -*- coding: utf-8 -*-
CSS = r"""
@font-face{font-family:'Gilroy';src:url('__GILROY_R__') format('woff');font-weight:400;font-style:normal;font-display:block}
@font-face{font-family:'Gilroy';src:url('__GILROY_M__') format('woff');font-weight:500;font-style:normal;font-display:block}
@font-face{font-family:'Gilroy';src:url('__GILROY_S__') format('woff');font-weight:600;font-style:normal;font-display:block}
@font-face{font-family:'Gilroy';src:url('__GILROY_B__') format('woff');font-weight:700;font-style:normal;font-display:block}

*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0}
img{max-width:100%;display:block}
button{font:inherit;color:inherit}

/* ------------------------------------------------------------------
   TOKENS
   One accent (lavender-indigo). One warm, used only behind the portrait.
   Neutrals biased toward the accent, never pure grey.
   ------------------------------------------------------------------ */
:root{
  --ground:#FBFAFD;
  --ground-2:#F5F3FA;
  --surface:#FFFFFF;
  --line:#EBE8F4;
  --line-2:#DFDAEE;

  --ink:#241F35;
  --ink-2:#565073;
  --ink-3:#6F6A85;

  --accent:#6C5FC0;
  --accent-hover:#5B4FAB;
  --accent-tint:#EFECFA;
  --accent-line:#C9C1EC;

  --warm:#F3E4E0;             /* morning light — hero glow only */
  --warm-2:#E7E9F6;

  --shadow:0 30px 70px -46px rgba(48,38,96,.30);
  --shadow-s:0 14px 34px -26px rgba(48,38,96,.28);

  --r-lg:30px; --r-md:22px; --r-sm:14px;
  --maxw:1160px;
  --mq:url("__MANNEQUIN__");
  --font:'Gilroy',-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;
}

body{
  font-family:var(--font);
  background:var(--ground);
  color:var(--ink-2);
  font-size:17px;
  line-height:1.72;
  font-weight:400;
  -webkit-font-smoothing:antialiased;
  overflow-x:hidden;
}

/* ------------------------------------------------------------------
   TYPE — three roles, separated by scale, not by weight.
   Display: Gilroy 400 at large size. Light display reads calm;
   bold display reads urgent, which is the wrong register here.
   ------------------------------------------------------------------ */
.display,h1{
  font-size:clamp(34px,4.6vw,55px);
  font-weight:400;
  line-height:1.06;
  letter-spacing:-.035em;
  color:var(--ink);
  margin:0;
  text-wrap:balance;
}
h2{
  font-size:clamp(27px,3.5vw,42px);
  font-weight:400;
  line-height:1.13;
  letter-spacing:-.031em;
  color:var(--ink);
  margin:0;
  text-wrap:balance;
}
h3,h4{font-weight:600;letter-spacing:-.016em;line-height:1.28;color:var(--ink);margin:0}
h3{font-size:19px}
h4{font-size:15px}
p{margin:0}
.em{color:var(--accent)}

.label{
  font-family:var(--font);
  font-size:11px;font-weight:600;letter-spacing:.185em;text-transform:uppercase;
  color:var(--accent);line-height:1.5
}
.label.muted{color:var(--ink-3)}

.lead{font-size:clamp(16px,1.3vw,18px);color:var(--ink-2);max-width:62ch;line-height:1.7}
.lead-w{max-width:82ch}
.center{text-align:center}
.center .lead{margin-left:auto;margin-right:auto}

.stack{display:flex;flex-direction:column}
.stack-s{gap:12px}.stack-m{gap:18px}.stack-l{gap:28px}

/* ------------------------------------------------------------------
   LAYOUT
   ------------------------------------------------------------------ */
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 24px}
.sec{position:relative;padding:78px 0}
.sec-tight{padding:56px 0}
.sec-alt{background:var(--ground-2)}
/* соседние секции на одном фоне не должны складывать отступы */
.sec-alt + .sec-alt{padding-top:0}
@media(max-width:760px){.sec{padding:52px 0}.sec-tight{padding:40px 0}.wrap{padding:0 18px}}

.grid{display:grid;gap:18px}
.g2{grid-template-columns:repeat(2,1fr)}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
@media(max-width:1000px){.g4{grid-template-columns:repeat(2,1fr)}.g3{grid-template-columns:repeat(2,1fr)}}
@media(max-width:680px){.g2,.g3,.g4{grid-template-columns:1fr}}

/* ------------------------------------------------------------------
   BUTTONS
   ------------------------------------------------------------------ */
.btn{
  display:inline-flex;align-items:center;justify-content:center;gap:10px;
  padding:17px 34px;border-radius:999px;border:1px solid transparent;cursor:pointer;
  font-size:16px;font-weight:600;letter-spacing:-.008em;text-decoration:none;
  background:var(--accent);color:#fff;
  transition:background .3s ease,transform .4s cubic-bezier(.2,.7,.3,1),border-color .3s ease
}
.btn:hover{background:var(--accent-hover);transform:translateY(-1px)}
.btn:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.btn-quiet{background:transparent;color:var(--ink);border-color:var(--line-2)}
.btn-quiet:hover{background:var(--surface);border-color:var(--accent-line)}
.btn-lg{padding:20px 42px;font-size:17px}
.btn-row{display:flex;flex-wrap:wrap;gap:14px;align-items:center}
.btn-note{font-size:13.5px;color:var(--ink-3);line-height:1.6}
.price-side .btn-row{margin-top:26px}
.price-side .btn-note{margin-top:14px}

/* ------------------------------------------------------------------
   TOP BAR
   ------------------------------------------------------------------ */
.topbar{position:sticky;top:0;z-index:60;background:rgba(251,250,253,.86);
  backdrop-filter:saturate(140%) blur(14px);-webkit-backdrop-filter:saturate(140%) blur(14px);
  border-bottom:1px solid var(--line)}
.topbar-in{max-width:var(--maxw);margin:0 auto;padding:10px 24px;
  display:flex;align-items:center;gap:22px;justify-content:space-between}
.topbar-txt{font-size:14px;color:var(--ink-2)}
.topbar-txt b{color:var(--ink);font-weight:600}
.topbar .btn{padding:11px 24px;font-size:14px}

.timer{display:flex;gap:14px;align-items:baseline;font-variant-numeric:tabular-nums}
.timer .u{display:flex;align-items:baseline;gap:5px}
.timer .n{font-size:17px;font-weight:600;color:var(--ink);line-height:1.2}
.timer .l{font-size:11px;color:var(--ink-3)}
.timer .l-s{display:none}
.t-short{display:none}
@media(max-width:900px){.t-full{display:none}.t-short{display:inline}}
/* на телефоне подпись, таймер и кнопка держатся в одну строку:
   единицы времени сокращаются до одной буквы */
@media(max-width:620px){
  .topbar-in{padding:8px 12px;gap:8px}
  .topbar-txt{font-size:9.5px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;
    color:var(--ink-3);line-height:1.25;max-width:6.5em}
  .timer{gap:8px;flex:0 0 auto}
  .timer .u{gap:2px}
  .timer .n{font-size:15px}
  .timer .l{display:none}
  .timer .l-s{display:inline;font-size:11px;color:var(--ink-3)}
  .topbar .btn{padding:9px 14px;font-size:12px;white-space:nowrap}
}
@media(max-width:400px){
  .topbar-in{gap:6px;padding:8px 10px}
  .topbar-txt{font-size:9px;letter-spacing:.06em;max-width:5.6em}
  .timer{gap:6px}.timer .n{font-size:14px}.timer .l-s{font-size:10px}
  .topbar .btn{padding:9px 11px;font-size:11.5px}
}

/* ------------------------------------------------------------------
   HERO — near-white ground; the only warmth on the page sits behind
   the portrait, where it reads as morning light.
   ------------------------------------------------------------------ */
.hero{position:relative;overflow:hidden;
  background:linear-gradient(180deg,#FAF7FB 0%,#F7F4FC 42%,#FBF7F6 74%,var(--ground) 100%)}
.hero-in{position:relative;z-index:2;display:grid;grid-template-columns:1.06fr .94fr;
  gap:48px;align-items:center;padding:64px 0 76px}



.brandline{display:flex;align-items:center;gap:12px}
.brandline img{width:36px;height:36px;border-radius:10px}
.brandline span{font-size:13px;line-height:1.4;color:var(--ink-3)}
.brandline b{display:block;color:var(--ink-2);font-weight:600}

.hero-sub{font-size:clamp(16px,1.4vw,18.5px);color:var(--ink-2);max-width:50ch;line-height:1.68}

.offer{display:grid;grid-template-columns:1fr 1fr;gap:0;
  border-top:1px solid var(--line-2);border-bottom:1px solid var(--line-2)}
.offer > a{display:block;padding:16px 24px 16px 0;text-decoration:none;color:inherit;
  transition:opacity .3s ease}
.offer > a:hover{opacity:.7}
.offer > a:focus-visible{outline:2px solid var(--accent);outline-offset:3px;border-radius:8px}
.offer > a + a{padding-left:24px;border-left:1px solid var(--line-2)}
.offer .k{display:flex;align-items:center;gap:7px;
  font-size:11px;font-weight:600;letter-spacing:.16em;text-transform:uppercase;color:var(--accent)}
.offer .k svg{width:16px;height:16px;flex:none}
.offer-t{display:block;margin-top:9px;font-size:15px;font-weight:600;color:var(--ink);
  line-height:1.32;letter-spacing:-.014em}
.offer p{margin-top:9px;font-size:13.5px;line-height:1.6;color:var(--ink-2)}
.offer b{color:var(--ink);font-weight:600}
@media(max-width:560px){
  .offer{grid-template-columns:1fr}
  .offer > a{padding:15px 0}
  .offer > a + a{padding-left:0;border-left:0;border-top:1px solid var(--line)}
}

.hero-meta{font-size:13.5px;color:var(--ink-3);display:flex;flex-wrap:wrap;
  align-items:center;gap:8px 22px}
.hero-meta span{display:inline-flex;align-items:center;gap:7px}

.hero-figure{position:relative;justify-self:center;width:100%;max-width:392px;margin:0}
.hero-figure .glowwrap{position:absolute;left:50%;top:38%;transform:translate(-50%,-50%);
  width:124%;pointer-events:none}
.hero-figure .glowwrap::before{content:"";display:block;padding-bottom:100%;
  border-radius:50%;
  background:radial-gradient(circle,var(--warm) 0%,var(--warm-2) 44%,rgba(231,233,246,0) 68%);
  opacity:.85}
.portrait{position:relative;margin-bottom:-44px}
.portrait img{width:100%;height:auto}

/* the card the portrait stands behind — it hides the crop and carries the facts */
.cred{position:relative;z-index:2;background:var(--surface);border:1px solid var(--line);
  border-radius:var(--r-md);padding:18px 20px 16px;box-shadow:0 24px 50px -34px rgba(48,38,96,.30)}
.cred-label{font-size:10px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;
  color:var(--accent)}
.cred-name{font-size:18px;font-weight:600;color:var(--ink);
  letter-spacing:-.02em;line-height:1.2}
.cred-role{margin-top:6px;font-size:13px;line-height:1.45;color:var(--ink-2)}
.cred-meta{margin-top:7px;font-size:12.5px;line-height:1.5;color:var(--ink-3)}
.cred-note{margin-top:12px;padding:10px 13px;border-radius:11px;background:var(--accent-tint);
  font-size:12.5px;line-height:1.45;color:var(--accent)}
.cred-stats{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 9px;
  margin-top:13px;padding-top:12px;border-top:1px solid var(--line);
  font-size:12.5px;color:var(--ink-3)}
.cred-stats span{display:inline-flex;align-items:baseline;gap:5px;white-space:nowrap}
.cred-stats span + span::before{content:"·";margin-right:4px;opacity:.55}
.cred-stats b{font-weight:600;color:var(--ink);font-size:14px;letter-spacing:-.01em;
  font-variant-numeric:tabular-nums}

/* on a phone the headline comes first; Павел sits between the copy and the buttons */
@media(max-width:940px){
  .hero-in{display:flex;flex-direction:column;align-items:stretch;
    padding:38px 0 48px;gap:26px}
  .hero-left{display:contents}
  .brandline{order:1}
  .hero-copy{order:2}
  .hero-figure{order:3;align-self:flex-start;width:100%;max-width:420px}
  .offer{order:4}
  .hero-act{order:5}
  .portrait{margin-bottom:-46px}
  .cred{padding:20px 22px 18px}
  .cred-name{font-size:19px}
  .cred-role{font-size:13.5px}
  .cred-note{font-size:13px}
}

/* ------------------------------------------------------------------
   CONDITIONS — no numbering. The set is unordered, so nothing numbers it.
   ------------------------------------------------------------------ */
.cond{position:relative;display:block;background:var(--surface);border:1px solid var(--line);
  border-radius:var(--r-md);padding:26px 26px 28px;
  transition:border-color .35s ease,transform .5s cubic-bezier(.2,.7,.3,1)}
.cond:hover{transform:translateY(-3px);border-color:var(--c)}

.cond-ico{display:grid;place-items:center;width:48px;height:48px;border-radius:15px;
  background:var(--ctile);margin-bottom:20px}
.cond-txt{display:block}
.cond-h{display:block;font-size:17.5px;font-weight:600;color:var(--ink);
  letter-spacing:-.016em;line-height:1.28}
.cond-d{display:block;margin-top:11px;font-size:14.5px;line-height:1.65;color:var(--ink-2)}

/* seven cards in a three-up grid: the last one runs the full width on purpose */
.cond-wide{grid-column:1/-1;display:grid;grid-template-columns:auto 1fr;gap:0 22px;
  align-items:start}
.cond-wide .cond-ico{margin-bottom:0}
.cond-wide .cond-d{max-width:70ch}
@media(max-width:680px){.cond-wide{grid-template-columns:1fr}
  .cond-wide .cond-ico{margin-bottom:20px}}

/* levels — four named parts of one CBT model, so they read as a set */
.lvl{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-md);padding:28px}
.lvl .ico{width:42px;height:42px;border-radius:13px;display:grid;place-items:center;
  background:var(--accent-tint);margin-bottom:20px}
.lvl h3{font-size:16px;letter-spacing:.005em}
.lvl .cap{margin-top:10px;font-size:13.5px;color:var(--ink-3);line-height:1.6}
.lvl ul{list-style:none;margin:20px 0 0;padding:0;display:grid;gap:11px}
.lvl li{position:relative;padding-left:20px;font-size:14px;line-height:1.6;color:var(--ink-2)}
.lvl li::before{content:"";position:absolute;left:2px;top:9px;width:5px;height:5px;border-radius:50%;
  background:var(--accent-line)}


/* ------------------------------------------------------------------
   FOUR-LEVEL MODEL — a figure you can interrogate.
   Selecting a level lights the part of the body it works on and
   swaps in that level's symptoms. Nothing moves on its own.
   ------------------------------------------------------------------ */
.model{display:grid;grid-template-columns:.82fr 1.18fr;gap:52px;align-items:center}
@media(max-width:900px){.model{grid-template-columns:1fr;gap:34px}
  .figbox{max-width:min(250px,62vw)}}

.figbox{position:relative;width:100%;max-width:min(300px,58vw);margin:0 auto}

/* the mannequin: its own alpha is the mask, a gradient inside picks the zone */
.mq{position:relative;width:100%;aspect-ratio:419/688;isolation:isolate}
.mq::before{content:"";position:absolute;left:12%;right:6%;bottom:-2%;height:5%;
  background:radial-gradient(ellipse at center,rgba(96,86,140,.20),rgba(96,86,140,0) 70%)}
.mq-base,.mq-lit{position:absolute;inset:0;background-repeat:no-repeat;
  background-size:contain;background-position:center}
.mq-base{background-image:var(--mq)}
.mq-lit{
  -webkit-mask-image:var(--mq);mask-image:var(--mq);
  -webkit-mask-size:contain;mask-size:contain;
  -webkit-mask-position:center;mask-position:center;
  -webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;
  mix-blend-mode:multiply;opacity:0;
  transition:opacity .45s cubic-bezier(.2,.7,.3,1)}
.mq-lit.on{opacity:1}
__SPOTS__

.hot{position:absolute;left:var(--x);top:var(--y);transform:translate(-50%,-50%);
  width:34px;height:34px;padding:0;border:0;background:none;cursor:pointer;
  display:grid;place-items:center;z-index:2}
.hot i{display:block;width:11px;height:11px;border-radius:50%;background:var(--surface);
  border:2px solid var(--line-2);box-shadow:0 2px 8px rgba(60,50,110,.18);
  transition:all .4s cubic-bezier(.2,.7,.3,1)}
.hot:hover i{border-color:var(--c);transform:scale(1.15)}
.hot[aria-pressed="true"] i{background:var(--c);border-color:var(--c);transform:scale(1.3)}
.hot:focus-visible{outline:2px solid var(--c);outline-offset:2px;border-radius:50%}
.hot .lbl{position:absolute;left:50%;top:-30px;transform:translateX(-50%);
  white-space:nowrap;font-size:12px;font-weight:600;letter-spacing:.02em;color:var(--ink);
  background:var(--surface);border:1px solid var(--line);border-radius:999px;padding:4px 11px;
  opacity:0;pointer-events:none;transition:opacity .3s ease}
.hot:hover .lbl,.hot:focus-visible .lbl{opacity:1}

.model-tabs{display:flex;flex-wrap:nowrap;gap:8px}
.model-tab{flex:1 1 0;min-width:0;text-align:center;
  padding:10px 14px;border-radius:999px;background:transparent;white-space:nowrap;
  border:1.5px solid var(--line-2);color:var(--ink-2);font-size:14.5px;cursor:pointer;
  transition:all .3s ease}
.model-tab:hover{border-color:var(--c);color:var(--ink)}
.model-tab[aria-selected="true"]{background:var(--ct);border-color:var(--c);
  color:var(--ink);font-weight:600}
.model-tab:focus-visible{outline:2px solid var(--c);outline-offset:3px}

.model-body{margin-top:30px;min-height:280px}
.model-pane[hidden]{display:none}
.model-pane{animation:paneIn .38s cubic-bezier(.2,.7,.3,1) both}
@keyframes paneIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
.model-pane .cap{font-size:15.5px;line-height:1.66;color:var(--ink-2);max-width:52ch}
.model-pane ul{list-style:none;margin:24px 0 0;padding:0;display:grid;gap:0}
.model-pane li{position:relative;padding:12px 0 12px 26px;font-size:15.5px;line-height:1.6;
  color:var(--ink-2);border-top:1px solid var(--line)}
.model-pane li:first-child{border-top:0}
.model-pane li::before{content:"";position:absolute;left:2px;top:20px;width:6px;height:6px;
  border-radius:50%;background:var(--c)}
@media(max-width:900px){.model-body{min-height:0}}

@media(prefers-reduced-motion:reduce){.model-pane{animation:none}}

/* ------------------------------------------------------------------
   PROGRAMS — colour encodes rank, not variety. The main programme is
   the anchor and gets the accent; the other five stay neutral.
   ------------------------------------------------------------------ */
.prog{border:1px solid var(--line);border-radius:var(--r-md);overflow:hidden;background:var(--surface);
  display:flex;flex-direction:column;
  transition:border-color .4s ease,transform .5s cubic-bezier(.2,.7,.3,1)}
.prog:hover{border-color:var(--accent-line);transform:translateY(-3px)}
.prog-top{padding:30px;border-bottom:1px solid var(--line)}
.prog-head{min-width:0}

/* only the flagship carries a portrait; it is pre-composited on the card's tint */
.prog-top.has-photo{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:0 16px;
  padding-right:0;padding-bottom:0}
.prog-photo{width:clamp(210px,25vw,330px);align-self:end;justify-self:end}
.prog-photo img{display:block;width:100%;height:auto}
@media(max-width:1000px){.prog-photo{width:200px}}
@media(max-width:820px){.prog-photo{width:240px}}
@media(max-width:560px){
  /* на телефоне Павел уходит под текст и встаёт в угол карточки */
  .prog-top.has-photo{grid-template-columns:1fr;padding-right:30px;padding-bottom:0}
  .prog-photo{width:min(96%,360px);justify-self:end;margin-top:-14px}}
.prog-kicker{display:inline-block;border:1px solid var(--line-2);border-radius:999px;
  padding:5px 12px;font-size:11px;color:var(--ink-3);letter-spacing:.01em;white-space:nowrap}
.prog-title{margin-top:18px;font-size:clamp(20px,2vw,24px);font-weight:500;line-height:1.2;
  letter-spacing:-.024em;color:var(--ink);text-wrap:balance}
.prog-desc{margin-top:15px;font-size:14.5px;line-height:1.65;color:var(--ink-2);max-width:44ch}
.prog-list{list-style:none;margin:14px 0 0;padding:0;display:grid;gap:6px}
.prog-list li{position:relative;padding-left:19px;font-size:14px;color:var(--ink-2)}
.prog-list li::before{content:"";position:absolute;left:2px;top:9px;width:5px;height:5px;border-radius:50%;
  background:var(--accent-line)}
.prog-bot{padding:26px 30px 30px;flex:1}
.prog-bot .hl{font-size:15px;font-weight:600;color:var(--ink);line-height:1.45;letter-spacing:-.012em}
.prog-bot .body{margin-top:14px;display:grid;gap:10px}
.prog-bot .body p{font-size:14px;line-height:1.66;color:var(--ink-2)}
.prog-bot .body b{color:var(--ink);font-weight:600}

.prog-kickrow{display:flex;flex-wrap:nowrap;align-items:center;gap:8px}
@media(max-width:1000px){.prog-kickrow{flex-wrap:wrap}}
.prog-part{display:inline-block;white-space:nowrap;padding:5px 12px;border-radius:999px;
  background:var(--accent);color:#fff;font-size:11px;font-weight:600;letter-spacing:.09em;
  text-transform:uppercase}

/* the flagship is one programme in two parts, so the two cards share one frame */
.prog-pair{grid-column:1/-1;border:1px solid var(--accent-line);border-radius:var(--r-md);
  overflow:hidden;background:var(--surface)}
.pair-head{display:flex;flex-wrap:wrap;align-items:baseline;gap:6px 14px;
  padding:13px 30px;background:var(--accent);color:#fff}
.pair-label{font-size:11px;font-weight:600;letter-spacing:.18em;text-transform:uppercase}
.pair-note{font-size:13px;opacity:.85}
.prog-pair > .prog{border:0;border-radius:0}
.prog-pair > .prog:hover{transform:none}
.prog-pair > .prog + .prog{border-top:1px solid var(--accent-line)}

.prog-anchor{border-color:var(--accent-line)}
.prog-anchor .prog-top{background:var(--accent-tint);border-bottom:0}
.prog-anchor .prog-kicker{border-color:var(--accent-line);color:var(--accent)}
.prog-anchor .prog-inner{display:grid;grid-template-columns:1.38fr .62fr;gap:0}
.prog-anchor .prog-bot{border-left:1px solid var(--accent-line)}
@media(max-width:820px){
  .prog-anchor .prog-inner{grid-template-columns:1fr}
  .prog-anchor .prog-bot{border-left:0;border-top:1px solid var(--accent-line)}
}
.prog-anchor .prog-inner{align-items:stretch}


/* ------------------------------------------------------------------
   COURSE CARDS — the four practical courses.
   The chip colour is the same colour that condition carries in the
   grid above, so the palette says the same thing in both places.
   ------------------------------------------------------------------ */
.course{display:flex;flex-direction:column;background:var(--surface);
  border:1px solid var(--line);border-radius:var(--r-md);padding:28px 28px 24px;
  transition:border-color .35s ease,transform .5s cubic-bezier(.2,.7,.3,1)}
.course:hover{transform:translateY(-3px);border-color:var(--c)}
.course-head{display:flex;align-items:center;gap:12px}
.course-ico{flex:none;width:46px;height:46px;border-radius:14px;display:grid;place-items:center;
  background:var(--ctile)}
.course-kicker{font-size:11px;font-weight:600;letter-spacing:.15em;text-transform:uppercase;
  color:var(--ink-3);line-height:1.4}
.course-title{margin-top:18px;font-size:clamp(20px,2.1vw,26px);font-weight:500;line-height:1.2;
  letter-spacing:-.024em;color:var(--ink);text-wrap:balance}
.course-desc{margin-top:14px;font-size:14.5px;line-height:1.65;color:var(--ink-2);max-width:46ch}

.course-res{margin-top:22px;padding-top:20px;border-top:1px solid var(--line)}
.course-res-t{font-size:15px;font-weight:600;line-height:1.45;color:var(--c);
  letter-spacing:-.012em}
.course-res p{margin-top:9px;font-size:14px;line-height:1.65;color:var(--ink-2)}

.course-tags{display:flex;flex-wrap:wrap;gap:7px;margin-top:auto;padding-top:24px}
.tag{padding:5px 12px;border-radius:999px;font-size:12px;line-height:1.4;
  color:var(--tc);background:var(--tt)}
.tag-plain{color:var(--ink-3);background:var(--ground-2)}
@media(max-width:680px){.course{padding:24px 22px 20px}}

/* ------------------------------------------------------------------
   CLUB
   ------------------------------------------------------------------ */
.club{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-md);padding:28px;
  display:flex;flex-direction:column;gap:15px;
  transition:border-color .4s ease,transform .5s cubic-bezier(.2,.7,.3,1)}
.club:hover{border-color:var(--c);transform:translateY(-3px)}
.club .head{display:flex;gap:14px;align-items:flex-start}
.club .ico{width:42px;height:42px;border-radius:13px;flex:none;display:grid;place-items:center;
  background:var(--ctile)}
.club h3{font-size:17px}
.club p{font-size:14px;line-height:1.68;color:var(--ink-2)}
.club .txt{display:grid;gap:9px}

/* the quote carries itself typographically — no container needed */
.quote{margin:0;background:var(--surface);border:1px solid var(--line);
  border-radius:var(--r-lg);padding:clamp(24px,2.8vw,38px);
  display:grid;grid-template-columns:1fr 1fr;gap:26px 36px}
.quote p{font-size:clamp(15.5px,1.3vw,18px);line-height:1.62;color:var(--ink-2);
  letter-spacing:-.01em;text-wrap:pretty}
@media(max-width:760px){.quote{grid-template-columns:1fr;gap:16px}}
.quote b{color:var(--ink);font-weight:600}

/* how "24/7" actually works: two shifts, one day */
.clock{max-width:760px;margin:0 auto;text-align:center}
.clock-h{font-size:11px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;
  color:var(--ink-3);text-align:center}
.clock-track{display:grid;grid-template-columns:1.15fr 1.4fr 1.45fr;gap:4px;margin-top:14px}
.clock-seg{height:44px;border-radius:10px;display:grid;place-items:center;padding:0 8px}
.clock-seg span{font-size:11.5px;line-height:1.3;text-align:center;white-space:nowrap;
  overflow:hidden;text-overflow:ellipsis;max-width:100%}
.clock-night{background:var(--ground-2);border:1px solid var(--line);color:var(--ink-3)}
.clock-day{background:var(--accent);color:#fff}
.clock-day span{font-weight:600}
.clock-legend{display:flex;flex-wrap:wrap;justify-content:center;gap:8px 26px;
  margin-top:14px;font-size:13.5px;color:var(--ink-2)}
.clock-legend span{display:inline-flex;align-items:center;gap:9px}
.cl-dot{width:10px;height:10px;border-radius:50%;flex:none}
.cl-day{background:var(--accent)}
.cl-night{background:var(--ground-2);border:1px solid var(--line-2)}
@media(max-width:620px){
  .clock-track{grid-template-columns:1fr;gap:6px}
  .clock-seg{height:38px}
  .clock-seg span{white-space:normal}
}

/* club cards: first line is the takeaway, the rest supports it */
.club-lead{font-size:15px;font-weight:600;color:var(--ink);line-height:1.5;
  letter-spacing:-.012em}

/* ------------------------------------------------------------------
   BONUSES
   ------------------------------------------------------------------ */
.bonus{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);
  padding:clamp(26px,3vw,40px)}
.bonus-head{display:grid;grid-template-columns:auto minmax(0,1fr);gap:0 26px;align-items:start}
@media(max-width:680px){.bonus-head{grid-template-columns:1fr;gap:18px}}
.bonus-mark{display:flex;align-items:center;gap:10px;padding:10px 18px;border-radius:999px;
  background:var(--c);color:#fff;white-space:nowrap}
.bonus-mark span{font-size:11.5px;font-weight:600;letter-spacing:.16em;text-transform:uppercase}
.bonus-mark svg{width:18px;height:18px}
.bonus-body h3{font-size:clamp(19px,2vw,24px);font-weight:600;letter-spacing:-.02em;line-height:1.25}
.bonus-lead{margin-top:13px;font-size:16px;line-height:1.7;color:var(--ink-2);max-width:70ch}
.bonus-list{list-style:none;margin:18px 0 0;padding:0;display:grid;gap:0;max-width:62ch}
.bonus-list li{position:relative;padding:11px 0 11px 28px;font-size:15.5px;line-height:1.55;
  color:var(--ink-2);border-top:1px solid var(--line)}
.bonus-list li:first-child{border-top:0}
.bonus-list li::before{content:"";position:absolute;left:1px;top:16px;width:16px;height:16px;
  background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%236C5FC0' stroke-width='2.4' stroke-linecap='round' stroke-linejoin='round'><path d='M20 6L9 17l-5-5'/></svg>");
  background-size:contain;background-repeat:no-repeat;background-position:center}
.tools{display:grid;grid-template-columns:1fr 1fr;gap:0;margin-top:24px;
  border-top:1px solid var(--line)}
.tool{display:grid;grid-template-columns:auto minmax(0,1fr);gap:0 14px;align-items:start;
  padding:18px 22px 18px 0;border-bottom:1px solid var(--line)}
.tool:nth-child(even){padding-left:22px;border-left:1px solid var(--line)}
.tool-ico{width:36px;height:36px;border-radius:11px;display:grid;place-items:center;
  background:var(--ctile)}
.tool-ico svg{width:19px;height:19px}
.tool h4{font-size:15px;font-weight:600;color:var(--ink);letter-spacing:-.012em;line-height:1.3}
.tool p{margin-top:6px;font-size:13.5px;line-height:1.6;color:var(--ink-2)}
@media(max-width:720px){
  .tools{grid-template-columns:1fr}
  .tool{padding:16px 0}
  .tool:nth-child(even){padding-left:0;border-left:0}}

.bonus-note{margin-top:18px;padding:14px 18px;border-radius:14px;background:var(--ct);
  color:var(--c);font-size:15px;line-height:1.6;max-width:70ch}

.bonus-shots-h{margin-top:28px;font-size:11px;font-weight:600;letter-spacing:.18em;
  text-transform:uppercase;color:var(--ink-3)}
.bonus-shots{display:flex;gap:14px;overflow-x:auto;margin-top:16px;padding-bottom:10px;
  scroll-snap-type:x proximity}
.bonus-shots button{flex:none;width:min(540px,84vw);padding:0;border:1px solid var(--line);
  background:var(--surface);border-radius:14px;overflow:hidden;cursor:zoom-in;display:block;
  scroll-snap-align:start;transition:border-color .3s ease,transform .4s cubic-bezier(.2,.7,.3,1)}
.bonus-shots button:hover{transform:translateY(-2px);border-color:var(--accent-line)}
.bonus-shots button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.bonus-shots img{display:block;width:100%;height:auto}
.bonus-shots::-webkit-scrollbar{height:8px}
.bonus-shots::-webkit-scrollbar-thumb{background:var(--line-2);border-radius:99px}
.bonus-shots-hint{display:flex;align-items:center;gap:7px;margin-top:8px;
  font-size:12.5px;color:var(--ink-3)}
.hint-tail{color:var(--ink-3);opacity:.85}
.hint-tail::before{content:"·";margin-right:7px}
/* стрелка мягко уходит вбок и возвращается — подсказка, что справа есть ещё.
   Мигание для этой аудитории не годится, поэтому только медленный сдвиг */
.hint-arrow{display:inline-flex;color:var(--accent)}
.hint-arrow svg{width:15px;height:15px;animation:nudge 2.8s ease-in-out infinite}
@keyframes nudge{0%,55%,100%{transform:none}28%{transform:translateX(5px)}}

/* ------------------------------------------------------------------
   PRICE
   ------------------------------------------------------------------ */
.price-grid{display:grid;grid-template-columns:1fr;gap:20px}
.price-cols{display:grid;grid-template-columns:1.15fr .85fr;gap:clamp(28px,4vw,56px)}
.price-side{display:flex;flex-direction:column}
@media(max-width:900px){.price-cols{grid-template-columns:1fr;gap:30px}}
/* мягкие цветные пятна за секцией со стоимостью */
.price-sec{overflow:hidden}
.price-sec > .wrap{position:relative;z-index:1}
.glow{position:absolute;border-radius:50%;filter:blur(90px);pointer-events:none;z-index:0}
.glow-a{width:460px;height:460px;left:-170px;top:60px;background:#F4EBCF;opacity:.5}
.glow-b{width:420px;height:420px;right:-150px;bottom:-60px;background:#CFDAF4;opacity:.45}

.price-main{position:relative;overflow:hidden;background:var(--surface);
  border:1px solid var(--line);border-radius:var(--r-lg);
  padding:clamp(28px,3.4vw,46px)}
.inc{list-style:none;margin:24px 0 0;padding:0;display:grid;gap:0}
.inc li{position:relative;padding:13px 0 13px 30px;font-size:15.5px;line-height:1.55;color:var(--ink-2);
  border-top:1px solid var(--line)}
.inc li:first-child{border-top:0;padding-top:0}
.inc li:first-child::before{top:3px}
.inc li::before{content:"";position:absolute;left:0;top:15px;width:19px;height:19px;
  background-image:var(--tick);
  background-size:contain;background-position:center;background-repeat:no-repeat}

.inc-bonus{display:flex;align-items:center;justify-content:space-between;gap:14px;
  color:var(--ink)}
.inc-tag{flex:none;padding:3px 10px;border-radius:999px;
  background:var(--accent-tint);color:var(--accent);font-size:10.5px;font-weight:600;
  letter-spacing:.14em;text-transform:uppercase}
.inc li.inc-bonus::before{background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%236C5FC0' stroke-width='2.2' stroke-linecap='round' stroke-linejoin='round'><path d='M12 4l1.9 5.1L19 11l-5.1 1.9L12 18l-1.9-5.1L5 11l5.1-1.9L12 4Z'/></svg>")}

.keynote{margin-top:0;padding:24px;border:1px solid var(--accent-line);border-radius:var(--r-md);
  background:var(--accent-tint)}
.keynote p{margin-top:12px;color:var(--ink-2);font-size:14.5px;line-height:1.66}

.pricebox{margin-top:26px;padding-top:24px;border-top:1px solid var(--line);
  display:flex;flex-wrap:wrap;align-items:baseline;gap:16px}
.price-now{font-size:clamp(34px,4.2vw,48px);font-weight:400;color:var(--ink);letter-spacing:-.035em;
  line-height:1;font-variant-numeric:tabular-nums}
.price-old{font-size:18px;color:var(--ink-3);text-decoration:line-through;font-variant-numeric:tabular-nums}
.price-badge{padding:5px 13px;border-radius:999px;background:#F9F0E9;color:#92663F;
  font-size:13px;font-weight:600}
.price-inst{margin-top:11px;font-size:14px;color:var(--ink-3)}

.side{display:grid;grid-template-columns:1fr 1fr;gap:20px}
@media(max-width:820px){.side{grid-template-columns:1fr}}
.side .box{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-md);padding:24px}
.box-ico{width:40px;height:40px;border-radius:13px;display:grid;place-items:center;
  background:var(--ctile);margin-bottom:16px}
.side p{margin-top:10px;font-size:13.5px;line-height:1.65;color:var(--ink-3)}
.logos{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin-top:18px}
.logos img{height:20px;width:auto;opacity:.62;filter:grayscale(1)}

/* ------------------------------------------------------------------
   REVIEWS
   ------------------------------------------------------------------ */
.tabs{display:flex;flex-wrap:wrap;gap:8px;justify-content:center}
.tab{padding:10px 20px;border-radius:999px;background:transparent;border:1px solid var(--line-2);
  color:var(--ink-2);font-size:14px;cursor:pointer;transition:all .3s ease}
.tab:hover{border-color:var(--c);color:var(--ink)}
.tab[aria-selected="true"]{background:var(--ct);border-color:var(--c);
  color:var(--ink);font-weight:600}
.tab:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.rev-panel[hidden]{display:none}
.rev{columns:5;column-gap:14px;margin-top:36px}
@media(max-width:1000px){.rev{columns:3}}
@media(max-width:620px){.rev{columns:2}}
.rev-card{break-inside:avoid;width:100%;margin:0 0 14px;padding:0;
  border:1px solid var(--line);background:var(--surface);border-radius:var(--r-sm);
  overflow:hidden;display:flex;flex-direction:column;
  transition:border-color .3s ease,transform .4s cubic-bezier(.2,.7,.3,1)}
.rev-card:hover{transform:translateY(-2px);border-color:var(--accent-line)}
.rev-shot{display:block;width:100%;padding:0;border:0;background:none;cursor:zoom-in}
.rev-shot:focus-visible{outline:2px solid var(--accent);outline-offset:-3px}
.rev img{width:100%;height:auto;display:block}
.rev-src{display:inline-flex;align-items:center;gap:6px;padding:11px 14px;
  border-top:1px solid var(--line);font-size:12.5px;color:var(--ink-3);
  text-decoration:none;transition:color .3s ease}
.rev-src:hover{color:var(--accent)}
.rev-src:focus-visible{outline:2px solid var(--accent);outline-offset:-3px}
.rev-src svg{width:13px;height:13px;flex:none}

.lb{position:fixed;inset:0;z-index:100;background:rgba(36,31,53,.6);backdrop-filter:blur(8px);
  display:grid;place-items:center;padding:28px;opacity:0;pointer-events:none;transition:opacity .35s ease}
.lb.on{opacity:1;pointer-events:auto}
.lb img{max-width:min(880px,92vw);max-height:86vh;width:auto;border-radius:16px}
.lb-close{position:absolute;top:22px;right:24px;width:44px;height:44px;border-radius:50%;border:0;
  background:rgba(255,255,255,.92);cursor:pointer;font-size:19px;color:var(--ink);line-height:1}

/* ------------------------------------------------------------------
   CONSULT / FOOTER / LEGAL
   ------------------------------------------------------------------ */
.consult{border:1px solid var(--line);border-radius:var(--r-lg);background:var(--surface);
  padding:clamp(28px,3.6vw,48px);display:grid;grid-template-columns:1.3fr .7fr;gap:28px;align-items:center}
@media(max-width:820px){.consult{grid-template-columns:1fr}}
.consult h3{font-size:clamp(20px,2.2vw,26px);font-weight:400;letter-spacing:-.026em}
.consult p{margin-top:13px;font-size:15.5px;line-height:1.68;color:var(--ink-2);max-width:52ch}
.consult .note{margin-top:13px;font-size:12.5px;color:var(--ink-3);line-height:1.6}
.consult .btn-row{justify-content:flex-end}
@media(max-width:820px){.consult .btn-row{justify-content:flex-start}}

footer{padding:44px 0 38px;border-top:1px solid var(--line);background:var(--ground-2)}
.foot{display:flex;flex-wrap:wrap;gap:26px;justify-content:space-between;align-items:flex-start}
.foot img{width:32px;height:32px}
.foot .col{font-size:13.5px;color:var(--ink-3);line-height:1.75;max-width:34ch}
.foot a{color:var(--ink-2);text-decoration:none;border-bottom:1px solid var(--line-2)}
.foot a:hover{color:var(--accent)}

.legal{background:var(--ground-2)}
.legal details{max-width:var(--maxw);margin:0 auto;border-top:1px solid var(--line)}
.legal summary{cursor:pointer;padding:22px 0;font-size:14px;color:var(--ink-3);list-style:none;
  display:flex;justify-content:space-between;align-items:center;gap:16px}
.legal summary::-webkit-details-marker{display:none}
.legal summary:hover{color:var(--ink-2)}
.legal summary::after{content:"+";font-size:19px;line-height:1}
.legal details[open] summary::after{content:"–"}
.legal .body{padding:0 0 34px;max-height:440px;overflow:auto;font-size:13px;line-height:1.75;color:var(--ink-3)}
.legal .body h4{font-size:13.5px;color:var(--ink-2);margin:20px 0 8px;font-weight:600}
.legal .body p{margin:0 0 9px}

/* ------------------------------------------------------------------
   MOTION
   ------------------------------------------------------------------ */
.rv{opacity:0;transform:translateY(14px);
  transition:opacity .9s cubic-bezier(.2,.7,.3,1),transform .9s cubic-bezier(.2,.7,.3,1)}
.rv.in{opacity:1;transform:none}
@media(prefers-reduced-motion:reduce){
  *{animation:none !important;transition-duration:.001ms !important;scroll-behavior:auto !important}
  .rv{opacity:1;transform:none}
}

/* на телефоне четыре уровня и кнопки первого экрана держим в одну строку */
@media(max-width:620px){
  h2{font-size:23px;line-height:1.2}
  h2 br{display:none}
  .model-tabs{flex-wrap:nowrap;gap:6px}
  .model-tab{padding:9px 6px;font-size:clamp(11px,3.1vw,14px)}
}
@media(max-width:940px){
  .hero-act .btn-row{flex-wrap:nowrap;gap:10px}
  .hero-act .btn{flex:1 1 0;min-width:0;padding:14px 10px;white-space:nowrap;
    font-size:clamp(12px,3.4vw,16px)}
}
"""
