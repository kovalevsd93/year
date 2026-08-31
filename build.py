# -*- coding: utf-8 -*-
import re
from data import *
from css import CSS
from icons import icon, cond_icon, any_icon, marker_uri
import dims
from figure import figure, spot_css, HOTSPOTS

ACCENT = "#6C5FC0"
MUTED  = "#6F6A85"
# ведёт практику с 2012 года; считаем от года акции, чтобы не забыть обновить
YEARS_IN_PRACTICE = int(DEADLINE_ISO[:4]) - 2012

ARROW = ('<svg viewBox="0 0 26 14" fill="none" stroke="currentColor" stroke-width="1.6" '
         'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
         '<path d="M0 7h24M18 1l6 6-6 6"/></svg>')

def cta(label="Оформить подписку", cls="btn btn-lg"):
    return f'<a class="{cls}" href="{ORDER_LINK}">{label}{ARROW}</a>'

def timer(cls="timer"):
    # короткие подписи — для телефона, там строка должна остаться одной
    units = [("d","дней","д"),("h","часов","ч"),("m","минут","м"),("s","секунд","с")]
    u = "".join(f'<span class="u"><span class="n" data-t="{k}">—</span>'
                f'<span class="l">{v}</span><span class="l-s">{sh}</span></span>'
                for k,v,sh in units)
    return f'<div class="{cls}" role="timer" aria-label="До конца акции">{u}</div>'

def heading(label, title, lead=None, center=True, wide=False):
    c = " center" if center else ""
    lc = "lead lead-w" if wide else "lead"
    l = f'<p class="{lc}">{lead}</p>' if lead else ""
    return (f'<div class="stack stack-m{c} rv"><div class="label">{label}</div>'
            f'<h2>{title}</h2>{l}</div>')

# ---------------------------------------------------------------- hero
def hero():
    return f"""
<header class="hero">
 <div class="wrap">
  <div class="hero-in">
   <div class="hero-left stack stack-l">
    <div class="brandline">
      <img src="{LOGO}" alt="" width="36" height="36">
      <span><b>Академия здорового мышления</b>Павла Федоренко</span>
    </div>

    <div class="hero-copy stack stack-m">
      <div class="label">Годовая подписка · новый учебный год</div>
      <h1>Начните учебный год <br>со спокойствия</h1>
      <p class="hero-sub">Скидка до 85% на все программы Павла Федоренко
        по преодолению тревожных расстройств и неврозов.</p>
    </div>

    <div class="offer">
      <a href="#bonuses">
        <span class="k">{icon('spark', ACCENT)} Бонус 1</span>
        <span class="offer-t">ИИ-ассистент Павла Федоренко</span>
      </a>
      <a href="#bonuses">
        <span class="k">{icon('compass', ACCENT)} Бонус 2</span>
        <span class="offer-t">Интерактивная платформа для работы с тревогой</span>
      </a>
    </div>

    <div class="hero-act stack stack-m">
      <div class="btn-row">
        {cta()}
        <a class="btn btn-lg btn-quiet" href="#programs">Что входит в подписку{ARROW}</a>
      </div>
      <div class="hero-meta">
        <span>{icon('calendar', MUTED)} Акция действует до {DEADLINE_TEXT}</span>
        <span>{icon('users', MUTED)} Осталось 29 из 50 абонементов</span>
      </div>
    </div>
   </div>

   <figure class="hero-figure">
     <div class="shot">
       <div class="shot-tags"><span class="tag-glass">ИИ-ассистент</span>
         <span class="tag-glass">Платформа</span><span class="tag-glass">Клуб 24/7</span></div>
       <img src="{{HERO_CARD}}" width="900" height="1120" alt="Павел Федоренко" loading="eager">
       <figcaption class="shot-foot">
         <div class="nm">Павел Федоренко</div>
         <div class="role">Ведущий специалист по тревожно-фобическим расстройствам
           в России. Магистр психологии, основатель клиники и института КПТ.</div>
         <div class="note">Сам прошёл через тяжёлый невроз и знаю проблему изнутри</div>
         <div class="facts"><span><b>{YEARS_IN_PRACTICE} лет</b> практики</span>
           <span><b>100 000+</b> учеников</span><span><b>30+</b> книг</span></div>
       </figcaption>
     </div>
   </figure>
  </div>
 </div>
</header>"""

# ---------------------------------------------------------------- conditions
def conditions():
    cards = []
    for i, (key, title, desc) in enumerate(DISORDERS):
        ink, tint, tile = SPECTRUM[i]
        last = " cond-wide" if i == len(DISORDERS) - 1 else ""
        cards.append(
            f'<article class="cond{last} rv" style="--c:{ink};--ct:{tint};--ctile:{tile}">'
            f'<span class="cond-ico">{cond_icon(key, "currentColor")}</span>'
            f'<span class="cond-txt"><span class="cond-h">{title}</span>'
            f'<span class="cond-d">{desc}</span></span></article>')
    return f"""
<section class="sec" id="problems">
 <div class="wrap stack stack-l">
  {heading('Кому помогает подписка', 'С какими проблемами поможет подписка?',
           'Это ваша возможность восстановиться от следующих тревожно-фобических расстройств.')}
  <div class="grid g3 cond-grid">{''.join(cards)}</div>
 </div>
</section>"""

# ---------------------------------------------------------------- levels
def level_colors():
    return {ic: LEVEL_COLORS[i][0] for i, (_, ic, _, _) in enumerate(LEVELS)}

def levels():
    hots, tabs, panes = [], [], []
    for i, (title, ic, cap, items) in enumerate(LEVELS):
        x, y = HOTSPOTS[ic]
        wash, line, tint = LEVEL_COLORS[i]
        pressed = "true" if i == 0 else "false"
        hots.append(f'<button class="hot" data-i="{i}" aria-pressed="{pressed}" '
                    f'style="--x:{x};--y:{y};--c:{line}" aria-label="{title}">'
                    f'<span class="lbl">{title}</span><i></i></button>')
        tabs.append(f'<button class="model-tab" role="tab" id="mt{i}" aria-controls="mp{i}" '
                    f'aria-selected="{pressed}" data-wash="{wash}" data-tint="{tint}" '
                    f'style="--c:{line};--ct:{tint}">{title}</button>')
        li = "".join(f"<li>{x}</li>" for x in items)
        panes.append(f'<div class="model-pane" role="tabpanel" id="mp{i}" aria-labelledby="mt{i}"'
                     f'{"" if i == 0 else " hidden"} style="--c:{line};--ci:{LEVEL_INK[i]}">'
                     f'<p class="cap">{cap}</p>'
                     f'<div class="pane-count">{len(items)} проявлений</div>'
                     f'<ul>{li}</ul></div>')

    return f"""
<section class="sec sec-alt">
 <div class="wrap stack stack-l">
  {heading('Четыре уровня работы',
           'Вы получаете комплексное решение <br>для устойчивого результата',
           'Научно обоснованными методами прорабатываем тревогу на уровне эмоций, тела, '
           'мыслей и поведения — ради устойчивого результата.')}

  <div class="model rv" id="model" style="--wash:{LEVEL_COLORS[0][0]};--washt:{LEVEL_COLORS[0][2]}">
   <div class="model-fig">
     <div class="figbox">{figure(LEVELS)}{''.join(hots)}</div>
   </div>
   <div class="model-panel">
     <div class="model-tabs" role="tablist" aria-label="Уровни работы">{''.join(tabs)}</div>
     <div class="model-body">{''.join(panes)}</div>
   </div>
  </div>
 </div>
</section>"""

# ---------------------------------------------------------------- programs
def prog_photo():
    """Only the flagship carries a portrait; the rest stay text."""
    import base64
    b = base64.b64encode(open("assets/pavel-course.jpg", "rb").read()).decode()
    d = dims.attrs("assets/pavel-course.jpg")
    return (f'<div class="prog-photo"><img src="data:image/jpeg;base64,{b}"{d} '
            f'alt="Павел Федоренко" loading="lazy" decoding="async"></div>')

def prog_top(kicker, t1, t2, desc, bullets, part=None, photo=False):
    title = f"{t1} {t2}".strip()
    bl = ("<ul class='prog-list'>" + "".join(f"<li>{b}</li>" for b in bullets) + "</ul>") if bullets else ""
    badge = f'<span class="prog-part">Часть {part}</span>' if part else ""
    cls = "prog-top has-photo" if photo else "prog-top"
    return (f'<div class="{cls}"><div class="prog-head">'
            f'<div class="prog-kickrow">{badge}<span class="prog-kicker">{kicker}</span></div>'
            f'<h3 class="prog-title">{title}</h3>'
            f'<p class="prog-desc">{desc}</p>{bl}</div>'
            f'{prog_photo() if photo else ""}</div>')

def prog_bot(hl, body):
    bd = "".join(f"<p>{p}</p>" for p in body)
    return f'<div class="prog-bot"><div class="hl">{hl}</div><div class="body">{bd}</div></div>'

def course_card(n, kicker, t1, t2, desc, hl, body):
    ic, ci, tags = COURSE_META[n]
    ink, tint, tile = SPECTRUM[ci] if ci is not None else (ACCENT, "var(--accent-tint)",
                                                           "var(--accent-tint)")
    title = f"{t1} {t2}".strip()
    chips = "".join(
        (f'<span class="tag" style="--tc:{SPECTRUM[j][0]};--tt:{SPECTRUM[j][1]}">{lbl}</span>'
         if j is not None else f'<span class="tag tag-plain">{lbl}</span>')
        for lbl, j in tags)
    # one bold line only: the promise. the rest reads as running text
    txt = "".join(f"<p>{re.sub(r'</?b>', '', x)}</p>" for x in body)
    return f"""<article class="course rv" style="--c:{ink};--ctile:{tile}">
   <div class="course-head">
     <span class="course-ico">{any_icon(ic, ink, 24)}</span>
     <span class="course-kicker">{kicker}</span>
   </div>
   <h3 class="course-title">{title}</h3>
   <p class="course-desc">{desc}</p>
   <div class="course-res">
     <p class="course-res-t">{hl}</p>
     {txt}
   </div>
   <div class="course-tags">{chips}</div>
  </article>"""

def programs():
    pair = ""
    for n, (_, k, a, b, d, bl, h, bd, _) in enumerate(PROGRAMS[:2], start=1):
        pair += (f'<article class="prog prog-anchor"><div class="prog-inner">'
                 f'{prog_top(k, a, b, d, bl, part=n, photo=(n == 1))}{prog_bot(h, bd)}'
                 f'</div></article>')
    rest = "".join(course_card(n, k, a, b, d, h, bd)
                   for n, (_, k, a, b, d, bl, h, bd, _) in enumerate(PROGRAMS[2:]))
    return f"""
<section class="sec" id="programs">
 <div class="wrap stack stack-l">
  {heading('Вот что входит в подписку',
           'Вы получаете доступ к 6 программам <br>Академии здорового мышления',
           'Это научно обоснованные знания и самые эффективные методы преодоления '
           'тревожных расстройств и неврозов.')}
  <div class="grid g2">
   <div class="prog-pair rv">
     <div class="pair-head">
       <span class="pair-label">Флагманская программа</span>
       <span class="pair-note">Две части: база и продвинутый уровень</span>
     </div>
     {pair}
   </div>
   {rest}
  </div>
  <div class="center rv">{cta()}</div>
 </div>
</section>"""

# ---------------------------------------------------------------- club
def club():
    cards = []
    for i, (n, title, ic, paras) in enumerate(CLUB):
        ink, tint, tile = SPECTRUM[i % len(SPECTRUM)]
        lead = f'<p class="club-lead">{paras[0]}</p>'
        rest = "".join(f"<p>{p}</p>" for p in paras[1:])
        cards.append(f'<article class="club rv" style="--c:{ink};--ctile:{tile}">'
                     f'<div class="ico">{icon(ic, ink)}</div>'
                     f'<h3>{title}</h3>'
                     f'<div class="txt">{lead}{rest}</div></article>')
    return f"""
<section class="sec sec-field">
 <div class="wrap stack stack-l">
  {heading('Самое главное', 'Терапевтический клуб <br>с поддержкой 24/7')}

  <blockquote class="quote rv">
   <p>Вы получаете <b>не просто доступ к видеоурокам</b> и массив материалов, которые завтра же
      забросите и забудете. Вы попадаете в уникальное терапевтическое пространство — живое,
      тёплое сообщество людей, которые идут тем же путём восстановления, что и вы.</p>
   <p>Это место, где вас понимают с полуслова, ежедневно поддерживают и помогают двигаться
      вперёд, <b>даже когда очень трудно и опускаются руки.</b></p>
  </blockquote>

  <div class="clock rv">
   <div class="clock-h">Почему круглосуточно</div>
   <div class="clock-track">
     <div class="clock-seg clock-night"><span>ночь и раннее утро</span></div>
     <div class="clock-seg clock-day"><span>рабочие часы</span></div>
     <div class="clock-seg clock-night"><span>вечер и ночь</span></div>
   </div>
   <div class="clock-legend">
     <span><i class="cl-dot cl-day"></i>Отвечают психологи и кураторы</span>
     <span><i class="cl-dot cl-night"></i>Отвечают участники из разных стран и часовых поясов</span>
   </div>
  </div>

  <div class="club-list">{''.join(cards)}</div>
 </div>
</section>"""

# ---------------------------------------------------------------- bonuses
BONUSES = [
 ("1", "ИИ-ассистент Павла Федоренко", "spark", "ассистент",
  "Персональный помощник, который помогает разобрать именно вашу ситуацию: увидеть "
  "поиск заверений, избегание и другие тревожные стратегии, понять, где вы снова "
  "попали в привычный тревожный круг, и перейти к конкретной практике.",
  [],
  "Особенно ценно, что обратиться к нему можно именно в тот момент, когда возникает "
  "вопрос: «А что мне делать конкретно сейчас?»",
  "Что о нём пишут участники"),

 ("2", "Интерактивная платформа для работы с тревогой", "compass", None,
  "Доступ к платформе, в которой собраны инструменты для ежедневной работы с тревогой — "
  "не теория, а то, чем пользуются между занятиями.",
  "tools",
  "",
  ""),
]

def bonuses(shots=None):
    cards = []
    for n, title, ic, folder, lead, items, note, shots_title in BONUSES:
        if items == "tools":
            li = ('<div class="tools">' + "".join(
                f'<div class="tool" style="--ctile:{SPECTRUM[k % len(SPECTRUM)][2]}">'
                f'<div class="tool-ico">{icon(t_ic, SPECTRUM[k % len(SPECTRUM)][0])}</div>'
                f'<div><h4>{t_name}</h4><p>{t_desc}</p></div></div>'
                for k, (t_ic, t_name, t_desc) in enumerate(TOOLS)) + '</div>')
        else:
            li = ("<ul class='bonus-list'>" + "".join(f"<li>{x}</li>" for x in items)
                  + "</ul>") if items else ""
        nt = f'<p class="bonus-note">{note}</p>' if note else ""
        imgs = shots(f"бонусы/{folder}") if (shots and folder) else []
        strip = ""
        if imgs:
            cells = "".join(
                f'<button type="button" aria-label="Отзыв {k+1}">'
                f'<img src="{u}"{dims.attrs(f)} alt="Отзыв участника" '
                f'loading="lazy" decoding="async"></button>'
                for k, (u, f) in enumerate(imgs))
            arrow = ('<span class="hint-arrow" aria-hidden="true">'
                     '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                     'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
                     '<path d="M5 12h13M13 6l6 6-6 6"/></svg></span>')
            hint = ('<p class="bonus-shots-hint">Листайте вбок' + arrow
                    + '<span class="hint-tail">нажмите, чтобы открыть целиком</span></p>'
                    if len(imgs) > 1 else
                    '<p class="bonus-shots-hint">Нажмите, чтобы открыть целиком</p>')
            nav = ('<button class="shots-nav prev" type="button" aria-label="Предыдущие отзывы">'
                   '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
                   'stroke-linecap="round" stroke-linejoin="round"><path d="M15 5l-7 7 7 7"/></svg>'
                   '</button>'
                   '<button class="shots-nav next" type="button" aria-label="Следующие отзывы">'
                   '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
                   'stroke-linecap="round" stroke-linejoin="round"><path d="M9 5l7 7-7 7"/></svg>'
                   '</button>')
            strip = (f'<div class="bonus-shots-h">{shots_title}</div>'
                     f'<div class="shots-wrap">{nav}'
                     f'<div class="bonus-shots">{cells}</div></div>{hint}')
        bink, btint, _ = SPECTRUM[6]   # оба бонуса одним тоном
        cards.append(f"""<article class="bonus rv" style="--c:{bink};--ct:{btint}">
   <div class="bonus-head">
     <div class="bonus-mark">{icon(ic, '#FFFFFF')}<span>Бонус {n}</span></div>
     <div class="bonus-body">
       <h3>{title}</h3>
       <p class="bonus-lead">{lead}</p>{li}{nt}
     </div>
   </div>{strip}
  </article>""")
    return f"""
<section class="sec sec-alt" id="bonuses">
 <div class="wrap stack stack-l">
  {heading('Бонусы к подписке', 'Два бонуса, которые работают между занятиями',
           'Программы дают метод. Эти два инструмента помогают применять его в тот самый '
           'момент, когда тревога уже здесь.')}
  <div class="stack stack-m">{''.join(cards)}</div>
  <div class="center rv">{cta()}</div>
 </div>
</section>"""

# ---------------------------------------------------------------- price
# у каждой строки — знак и цвет того же курса, что и в карточках выше
INCLUDED_MARKS = [
 ("check",  ACCENT),          # флагман, часть 1
 ("check",  ACCENT),          # флагман, часть 2
 ("panic",  SPECTRUM[0][0]),  # Паники.НЕТ
 ("health", SPECTRUM[3][0]),  # Свобода от страха за здоровье
 ("body",   SPECTRUM[1][0]),  # 7 телесных практик
 ("people", ACCENT),          # Как не воспитать невротика
]

def tariff_card(t):
    best = " tariff-best" if t.get("best") else ""
    tag = '<span class="tariff-tag">Рекомендуем</span>' if t.get("best") else ""
    has = "".join(f'<li class="yes">{x}</li>' for x in t["has"])
    no = ""
    if t["hasnt"]:
        no = ('<li class="sep">Не входит в этот тариф</li>'
              + "".join(f'<li class="no">{x}</li>' for x in t["hasnt"]))
    return f"""<article class="tariff{best} rv">
   {tag}
   <div class="tariff-name">{t['name']}</div>
   <p class="tariff-lead">{t['lead']}</p>
   <div class="tariff-price">
     <span class="now">{t['price']}</span>
     <span class="old">{t['old']}</span>
     <span class="cut">{t['cut']}</span>
   </div>
   <div class="tariff-inst">В рассрочку {t['inst']} · 365 дней доступа</div>
   <a class="btn btn-lg" href="{ORDER_LINK}">Оформить подписку{ARROW}</a>
   <ul class="tariff-list">{has}{no}</ul>
  </article>"""

def price():
    inc = "".join(f'<li style="--tick:{marker_uri(*INCLUDED_MARKS[i])}">{x}</li>'
                  for i, x in enumerate(INCLUDED))
    inc += "".join(f'<li class="inc-bonus"><span>{x}</span>'
                   f'<span class="inc-tag">Бонус</span></li>'
                   for x in INCLUDED_BONUSES)
    pay = "".join(f'<img src="{u}"{dims.attrs(u)} alt="" loading="lazy">' for u in PAY_LOGOS)
    ins = "".join(f'<img src="{u}"{dims.attrs(u)} alt="" loading="lazy">' for u in INST_LOGOS)
    return f"""
<section class="sec price-sec" id="order">
 <div class="glow glow-a"></div>
 <div class="glow glow-b"></div>
 <div class="wrap stack stack-l">
  {heading('Тариф', 'Знания и методики, которые меняют жизнь',
           'Подписка на 1 год (365 дней) на библиотеку всех программ '
           'по преодолению тревожных расстройств и неврозов.')}


  <div class="tariffs">
   {"".join(tariff_card(t) for t in TARIFFS)}
  </div>

  <div class="side">
   <div class="box rv" style="--ctile:{SPECTRUM[5][2]}">
     <div class="box-ico">{icon('shield', SPECTRUM[5][0])}</div>
     <h3>Оплата любыми банковскими картами</h3>
     <p>Нажмите на кнопку «Оформить подписку», заполните данные и отправьте форму,
        после выберите удобную систему.</p>
     <div class="logos">{pay}</div>
   </div>
   <div class="box rv" style="--ctile:{SPECTRUM[3][2]}">
     <div class="box-ico">{icon('calendar', SPECTRUM[3][0])}</div>
     <h3>Рассрочка до 24 месяцев или оплата частями</h3>
     <p>Нажмите на кнопку «Оформить подписку», заполните данные и отправьте форму,
        после выберите удобный сервис и количество месяцев рассрочки.</p>
     <div class="logos">{ins}</div>
   </div>
  </div>
 </div>
</section>"""

# ---------------------------------------------------------------- reviews
def reviews(inline=None):
    tabs, panels = [], []
    for i, (name, imgs) in enumerate(TABS):
        sel = "true" if i == 0 else "false"
        t_ink, t_tint, _ = SPECTRUM[i % len(SPECTRUM)]
        tabs.append(f'<button class="tab" role="tab" id="tb{i}" aria-controls="tp{i}" '
                    f'aria-selected="{sel}" style="--c:{t_ink};--ct:{t_tint}">{name}</button>')
        cells = []
        for j, rel in enumerate(imgs):
            src = inline(rel) if inline else (CDN + rel)
            dim = dims.attrs(CDN + rel)
            cells.append(
                f'<figure class="rev-card">'
                f'<button type="button" class="rev-shot" aria-label="Открыть отзыв {j+1}">'
                f'<img src="{src}"{dim} alt="Отзыв участника" loading="lazy"></button>'
                f'<a class="rev-src" href="{REVIEW_SOURCE}" target="_blank" rel="noopener">'
                f'Оригинал отзыва'
                f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
                f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
                f'<path d="M8 16 16 8M9.5 8H16v6.5"/></svg></a>'
                f'</figure>')
        panels.append(f'<div class="rev-panel" role="tabpanel" id="tp{i}" aria-labelledby="tb{i}"'
                      f'{"" if i == 0 else " hidden"}><div class="rev">{"".join(cells)}</div></div>')
    return f"""
<section class="sec sec-alt">
 <div class="wrap stack stack-l">
  {heading('Отзывы', 'Наши программы прошли более <br>100 000 человек по всему миру',
           'Вот малая часть их отзывов.')}
  <div class="tabs rv" role="tablist" aria-label="Категории отзывов">{''.join(tabs)}</div>
  <div>{''.join(panels)}</div>
  <div class="center rv">{cta('Я тоже так хочу!')}</div>
 </div>
</section>
<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Отзыв">
  <button class="lb-close" id="lbClose" aria-label="Закрыть">✕</button><img alt="Отзыв участника" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7">
</div>"""

# ---------------------------------------------------------------- consult
def consult():
    return f"""
<section class="sec">
 <div class="wrap">
  <div class="consult rv">
   <div>
    <div class="label">Заявка на консультацию</div>
    <h3 style="margin-top:16px">Не уверены, что подписка подойдёт именно вам?</h3>
    <p>Оставьте заявку на бесплатную консультацию, и в течение 10 минут с вами свяжется
       наш специалист и ответит на все интересующие вопросы.</p>
    <p class="note">Нажимая на кнопку, вы даёте согласие на обработку персональных данных
       и соглашаетесь с политикой конфиденциальности.</p>
   </div>
   <div class="btn-row">
     <a class="btn btn-lg btn-quiet" href="{CONSULT_LINK}">Получить консультацию{ARROW}</a>
   </div>
  </div>
 </div>
</section>"""

# ---------------------------------------------------------------- footer / legal
def footer():
    return f"""
<footer>
 <div class="wrap foot">
  <div style="display:flex;gap:14px;align-items:center">
    <img src="{LOGO_FOOT}"{dims.attrs(LOGO_FOOT)} alt="">
    <div class="col" style="color:var(--ink-2)">Академия здорового мышления<br>Павла Федоренко</div>
  </div>
  <div class="col">Copyright © 2012 — 2026. ИП «Федоренко Павел Алексеевич»<br>
    ИНН 645117313599<br>Служба тех. поддержки: <a href="mailto:info@fdrk.ru">info@fdrk.ru</a></div>
  <div class="col"><a href="#privacy">Политика конфиденциальности</a><br>
    <a href="https://docs.google.com/document/d/1HNUDFnaErp0vLxzUOEkV9jPRO3QccW7aJG2nHTvISOw/edit?usp=sharing"
       target="_blank" rel="noopener">Договор оферты</a></div>
 </div>
</footer>"""

def legal(body):
    return f"""
<section class="legal" id="privacy">
 <div class="wrap">
  <details><summary>Политика в отношении обработки персональных данных</summary>
   <div class="body">{body}</div></details>
 </div>
</section>"""

def privacy_html():
    import io, re
    lines = [l.strip() for l in io.open("privacy.txt", encoding="utf-8").read().split("\n") if l.strip()]
    return "".join(("<h4>" + l + "</h4>") if re.match(r"^\d+\.\s", l) else ("<p>" + l + "</p>")
                   for l in lines[1:])

JS = """
(function(){
  var DEADLINE = new Date("%s").getTime();
  function pad(n){return n<10?"0"+n:""+n}
  function tick(){
    var s = Math.floor(Math.max(0, DEADLINE - Date.now())/1000);
    var v = {d:Math.floor(s/86400), h:Math.floor(s%%86400/3600), m:Math.floor(s%%3600/60), s:s%%60};
    document.querySelectorAll("[data-t]").forEach(function(el){
      var k = el.getAttribute("data-t"); el.textContent = k==="d" ? v.d : pad(v[k]);
    });
  }
  tick(); setInterval(tick, 1000);

  var io = new IntersectionObserver(function(es){
    es.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add("in"); io.unobserve(e.target);} });
  },{rootMargin:"0px 0px -8%% 0px",threshold:.05});
  document.querySelectorAll(".rv").forEach(function(el,i){
    el.style.transitionDelay = ((i%%3)*90) + "ms"; io.observe(el);
  });

  var mTabs = [].slice.call(document.querySelectorAll(".model-tab"));
  var mHots = [].slice.call(document.querySelectorAll(".hot"));
  var mZones = [].slice.call(document.querySelectorAll(".mq-lit"));
  var modelBox = document.getElementById("model");
  function selectLevel(i){
    if(modelBox && mTabs[i]){
      modelBox.style.setProperty("--wash", mTabs[i].dataset.wash);
      modelBox.style.setProperty("--washt", mTabs[i].dataset.tint);
    }
    mTabs.forEach(function(t,j){
      t.setAttribute("aria-selected", j===i ? "true":"false");
      document.getElementById("mp"+j).hidden = (j!==i);
    });
    mHots.forEach(function(h,j){ h.setAttribute("aria-pressed", j===i ? "true":"false"); });
    mZones.forEach(function(z,j){ z.classList.toggle("on", j===i); });
  }
  mTabs.forEach(function(t,i){ t.addEventListener("click", function(){ selectLevel(i); }); });
  mHots.forEach(function(h,i){
    h.addEventListener("click", function(){ selectLevel(i); });
    h.addEventListener("mouseenter", function(){ selectLevel(i); });
  });
  mTabs.forEach(function(t,i){
    t.addEventListener("keydown", function(e){
      var d = e.key==="ArrowRight" ? 1 : e.key==="ArrowLeft" ? -1 : 0;
      if(!d) return;
      e.preventDefault();
      var n = (i + d + mTabs.length) %% mTabs.length;
      selectLevel(n); mTabs[n].focus();
    });
  });
  if(mZones.length) mZones[0].classList.add("on");

  var tabs = [].slice.call(document.querySelectorAll(".tab"));
  tabs.forEach(function(t,i){
    t.addEventListener("click", function(){
      tabs.forEach(function(x,j){
        x.setAttribute("aria-selected", j===i ? "true":"false");
        document.getElementById("tp"+j).hidden = (j!==i);
      });
    });
  });

  document.querySelectorAll(".shots-wrap").forEach(function(w){
    var strip = w.querySelector(".bonus-shots");
    var prev = w.querySelector(".prev"), next = w.querySelector(".next");
    function step(){
      var card = strip.querySelector("button");
      return card ? card.getBoundingClientRect().width + 14 : strip.clientWidth * .8;
    }
    function sync(){
      var max = strip.scrollWidth - strip.clientWidth - 1;
      prev.disabled = strip.scrollLeft <= 0;
      next.disabled = strip.scrollLeft >= max;
      w.classList.toggle("no-nav", max <= 0);
    }
    prev.addEventListener("click", function(){
      strip.scrollBy({left: -step(), behavior: "smooth"}); });
    next.addEventListener("click", function(){
      strip.scrollBy({left: step(), behavior: "smooth"}); });
    strip.addEventListener("scroll", sync, {passive: true});
    addEventListener("resize", sync);
    sync();
  });

  var lb = document.getElementById("lb"), lbImg = lb.querySelector("img");
  document.querySelectorAll(".rev-shot, .bonus-shots button").forEach(function(b){
    b.addEventListener("click", function(){
      lbImg.src = b.getAttribute("data-full") || b.querySelector("img").src;
      lb.classList.add("on");
    });
  });
  function close(){ lb.classList.remove("on"); }
  document.getElementById("lbClose").addEventListener("click", close);
  lb.addEventListener("click", function(e){ if(e.target===lb) close(); });
  document.addEventListener("keydown", function(e){ if(e.key==="Escape") close(); });
})();
""" % DEADLINE_ISO

def render(inline=None, shots=None):
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Год спокойствия</title>
<meta name="description" content="Годовая подписка к новому учебному году: доступ на 12 месяцев ко всем программам Павла Федоренко и закрытому терапевтическому клубу.">
<style>{CSS.replace("__SPOTS__", spot_css(level_colors()))}</style>

<div class="topbar">
 <div class="topbar-in">
  <div class="topbar-txt"><span class="t-full">Акция действует до <b>{DEADLINE_TEXT}</b></span><span class="t-short">До конца акции</span></div>
  {timer()}
  <a class="btn" href="{ORDER_LINK}">Участвовать{ARROW}</a>
 </div>
</div>
{hero()}
{conditions()}
{levels()}
{programs()}
{club()}
{bonuses(shots)}
{price()}
{reviews(inline)}
{consult()}
{footer()}
{legal(privacy_html())}
<script>{JS}</script>
"""

def favicon_uri():
    """Логотип академии как иконка вкладки."""
    import base64, subprocess, os
    src, dst = "assets/Logo_for_web.png", "cache/favicon64.png"
    os.makedirs("cache", exist_ok=True)
    if not os.path.exists(dst):
        subprocess.run(["sips", "-Z", "64", src, "--out", dst],
                       check=True, capture_output=True)
    return "data:image/png;base64," + base64.b64encode(open(dst, "rb").read()).decode()

DESCRIPTION = ("Годовая подписка к новому учебному году: 12 месяцев доступа ко всем "
               "программам Павла Федоренко по преодолению тревожных расстройств "
               "и неврозов плюс закрытый терапевтический клуб с поддержкой 24/7.")

def shell(doc):
    """Полноценный документ для боевой сборки. В артефакт не идёт:
       там обёртку <html>/<head>/<body> добавляет сама площадка."""
    head, _, body = doc.partition("</style>")
    head += "</style>"
    head = head.replace('<meta charset="utf-8">\n', "").replace(
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n', "")
    return f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#FBFAFD">
<link rel="icon" href="{favicon_uri()}">
<meta property="og:type" content="website">
<meta property="og:locale" content="ru_RU">
<meta property="og:url" content="{SITE_URL}/">
<meta property="og:site_name" content="Академия здорового мышления Павла Федоренко">
<meta property="og:title" content="Начните учебный год со спокойствия">
<meta property="og:description" content="{DESCRIPTION}">
<meta property="og:image" content="{SITE_URL}/assets/og.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
{head.strip()}
</head>
<body>
{body.strip()}
</body>
</html>
"""

def with_fonts(doc, mapping):
    for k, v in mapping.items():
        doc = doc.replace(k, v)
    return doc

def hero_card_uri():
    import base64
    return ("data:image/jpeg;base64,"
            + base64.b64encode(open("assets/hero-card.jpg", "rb").read()).decode())

def mannequin_uri():
    import base64
    return ("data:image/png;base64,"
            + base64.b64encode(open("assets/mannequin.png", "rb").read()).decode())

if __name__ == "__main__":
    import inline as _inline
    doc = with_fonts(render(shots=_inline.local_shots), GILROY).replace("__MANNEQUIN__", mannequin_uri())
    doc = doc.replace("{HERO_CARD}", hero_card_uri())
    doc = shell(doc)
    open("index.html", "w", encoding="utf-8").write(doc)
    dims.save()
    print("index.html written")
