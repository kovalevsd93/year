# -*- coding: utf-8 -*-
import re
from data import *
from css import CSS
from icons import icon, cond_icon, any_icon, marker_uri
import dims
import tool_shots

ACCENT = "#6C5FC0"
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
    kicker = f'<div class="label">{label}</div>' if label else ""
    return (f'<div class="stack stack-m{c} rv">{kicker}'
            f'<h2>{title}</h2>{l}</div>')

# ---------------------------------------------------------------- hero
def hero():
    return f"""
<header class="hero">
 <div class="wrap">
  <div class="hero-in">
   <div class="hero-left stack stack-l">
    <div class="brandline">
      <img src="{logo_uri()}" alt="" width="36" height="36">
      <span><b>Академия здорового мышления</b>Павла Федоренко</span>
    </div>

    <div class="hero-copy stack stack-m">
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
    </div>
   </div>

   <figure class="hero-figure">
     <div class="shot">
       <div class="shot-tags"><span class="tag-glass">ИИ-ассистент</span>
         <span class="tag-glass">Платформа</span><span class="tag-glass">Поддержка 24/7</span></div>
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
  {heading(None, 'С какими проблемами поможет подписка?',
           'Это ваша возможность восстановиться от следующих тревожно-фобических расстройств.')}
  <div class="grid g3 cond-grid">{''.join(cards)}</div>
 </div>
</section>"""

# ---------------------------------------------------------------- levels
# стилизованные иллюстрации вместо линейной заглушки — там, где они уже есть;
# «Эмоции» (0) пока остаётся на tool_shots.placeholder()
LEVEL_SHOT_IMAGES = {
 0: ("assets/emotions-masks.png", "Стилизованная объёмная иллюстрация масок эмоций, символ уровня «Эмоции»"),
 1: ("assets/body-heart.png", "Стилизованная объёмная иллюстрация сердца, символ уровня «Тело»"),
 2: ("assets/mind-brain.png", "Стилизованная объёмная иллюстрация мозга, символ уровня «Мысли»"),
 3: ("assets/behavior-compass.png", "Стилизованный объёмный компас, символ уровня «Поведение»"),
}

def levels():
    """Раскрывающийся список: эмоции → тело → мысли → поведение как
    четыре последовательные стадии одной реакции. Первая строка открыта
    сразу, остальные сворачивают текст и список за собой.

    Справа от списка проявлений — медиа-слот с инструментом платформы,
    который отвечает на «а как вы это лечите». Настоящих скриншотов
    ещё нет (готовит клиент — см. ТЗ), поэтому вместо <picture> сейчас
    линейная иллюстрация; сетка и обёртка .hl-shot-frame рассчитаны на
    прямую замену её содержимого на <picture> без переверстки."""
    rows = []
    for i, (title, ic, cap, items) in enumerate(LEVELS):
        _wash, _line, tint = LEVEL_COLORS[i]
        ink = LEVEL_INK[i]
        _shot_cap, shot_alt = LEVEL_MEDIA[i]
        li = "".join(f"<li>{x}</li>" for x in items)
        # первый пункт открыт всегда и не входит в общую группу — не
        # закрывается, когда открывают остальные три
        open_attr = " open" if i == 0 else ""
        name_attr = "" if i == 0 else ' name="levels"'
        if i in LEVEL_SHOT_IMAGES:
            # реальная картинка вместо линейной заглушки; альт описывает
            # то, что действительно на ней, а не будущий скриншот
            path, shot_img_alt = LEVEL_SHOT_IMAGES[i]
            d = dims.attrs(path)
            frame = (f'<div class="hl-shot-frame">'
                      f'<img src="{png_uri(path)}"{d} alt="{shot_img_alt}" '
                      f'loading="lazy" decoding="async"></div>')
        else:
            frame = (f'<div class="hl-shot-frame" role="img" aria-label="{shot_alt}">'
                      f'{tool_shots.placeholder(i)}</div>')
        rows.append(f"""<details class="hl-row"{name_attr} style="--c:{ink};--ct:{tint}"{open_attr}>
   <summary class="hl-summary">
     <span class="hl-num">0{i + 1}</span>
     <h3>{title}</h3>
     <span class="hl-chevron">{icon('chevron', 'currentColor')}</span>
   </summary>
   <div class="hl-panel">
     <div class="hl-text">
       <p class="hl-cap">{cap}</p>
       <div class="hl-count">{len(items)} проявлений</div>
       <ul class="hl-list">{li}</ul>
     </div>
     <div class="hl-shot">{frame}</div>
   </div>
  </details>""")

    return f"""
<section class="sec">
 <div class="wrap stack stack-l">
  {heading(None,
           'Комплексное решение <br>для устойчивого результата',
           'Научно обоснованными методами прорабатываем тревогу на уровне эмоций, тела, '
           'мыслей и поведения — ради устойчивого результата.')}

  <div class="hublist rv">{''.join(rows)}</div>
 </div>
</section>"""

# ---------------------------------------------------------------- programs
def prog_photo():
    """Only the flagship carries a portrait; the rest stay text.
    Вырезан из фона (был на плоской заливке #EEECF9, которая перестала
    совпадать с фоном карточки, когда там появился градиент)."""
    d = dims.attrs("assets/pavel-course.png")
    return (f'<div class="prog-photo"><img src="{png_uri("assets/pavel-course.png")}"{d} '
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
    ink, tint, tile = SPECTRUM[ci] if ci is not None else ("var(--accent-on-tint)",
                                                           "var(--accent-tint)", "var(--accent-tint)")
    title = f"{t1} {t2}".strip()
    chips = "".join(
        (f'<span class="tag" style="--tc:{SPECTRUM[j][0]};--tt:{SPECTRUM[j][1]}">{lbl}</span>'
         if j is not None else f'<span class="tag tag-plain">{lbl}</span>')
        for lbl, j in tags)
    # one bold line only: the promise. the rest reads as running text
    txt = "".join(f"<p>{re.sub(r'</?b>', '', x)}</p>" for x in body)
    return f"""<article class="course rv" style="--c:{ink};--ct:{tint};--ctile:{tile}">
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
  {heading(None,
           'Доступ к 6 программам <br>Академии здорового мышления',
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
TAKE_INK, TAKE_WASH, _ = SPECTRUM[3]   # один зелёный для вывода во всех карточках клуба

def club():
    cards = []
    for i, (n, title, ic, paras) in enumerate(CLUB):
        ink, _wash, _tile = SPECTRUM[i % len(SPECTRUM)]
        lead = f'<p class="club-lead">{paras[0]}</p>'
        mid = "".join(f"<p>{p}</p>" for p in paras[1:-1])
        take = (f'<p class="club-take"><svg viewBox="0 0 20 20" fill="none" stroke="currentColor" '
                f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
                f'<path d="M4.5 10.5l3.3 3.3L15.5 6"/></svg><span>{paras[-1]}</span></p>'
                if len(paras) > 1 else "")
        cards.append(f'<article class="club rv" style="--c:{TAKE_INK};--ct:{TAKE_WASH}">'
                     f'<div class="ico">{icon(ic, ink)}</div>'
                     f'<h3>{title}</h3>'
                     f'<div class="txt">{lead}{mid}{take}</div></article>')
    return f"""
<section class="sec sec-field">
 <div class="wrap stack stack-l">
  {heading(None, 'Терапевтический клуб <br>с поддержкой 24/7')}

  <blockquote class="quote rv">
   <p>Вы получаете <b>не просто доступ к видеоурокам</b> и массив материалов, которые завтра же
      забросите и забудете. Вы попадаете в уникальное терапевтическое пространство — живое,
      тёплое сообщество людей, которые идут тем же путём восстановления, что и вы.</p>
   <p>Это место, где вас понимают с полуслова, ежедневно поддерживают и помогают двигаться
      вперёд, <b>даже когда очень трудно и опускаются руки.</b></p>
  </blockquote>

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
  {heading(None, 'Два бонуса, которые работают между занятиями',
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
   <button class="btn btn-lg" type="button" data-pay-page="//{SITE_URL.split('://', 1)[1]}/{t['widget_page']}"
     >Оформить подписку{ARROW}</button>
   <div class="tariff-now">{icon('bolt', 'currentColor')}<span>Доступ ко всем материалам
     открывается <b>сразу после оплаты</b></span></div>
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
  {heading(None, 'Знания и методики, которые меняют жизнь',
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
  {heading(None, 'Наши программы прошли более <br>100 000 человек по всему миру',
           'Вот малая часть их отзывов.')}
  <div class="tabs rv" role="tablist" aria-label="Категории отзывов">{''.join(tabs)}</div>
  <div>{''.join(panels)}</div>
  <div class="center rv">{cta('Я тоже так хочу!')}</div>
 </div>
</section>
<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="Отзыв">
  <button class="lb-close" id="lbClose" aria-label="Закрыть">✕</button><img alt="Отзыв участника" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7">
</div>"""

# ---------------------------------------------------------------- footer / legal
def footer():
    logo = logo_uri()
    return f"""
<footer>
 <div class="wrap foot">
  <div style="display:flex;gap:14px;align-items:center">
    <img src="{logo}" width="36" height="36" alt="">
    <div class="col" style="color:var(--ink-2)">Академия здорового мышления<br>Павла Федоренко</div>
  </div>
  <div class="col">ИП «Федоренко Павел Алексеевич»<br>
    ИНН 645 117 313 599<br>
    Служба тех. поддержки: <a href="mailto:info@fdrk.ru">info@fdrk.ru</a></div>
  <div class="col"><a href="#privacy" data-legal-open>Политика конфиденциальности</a><br>
    <a href="https://docs.google.com/document/d/1HNUDFnaErp0vLxzUOEkV9jPRO3QccW7aJG2nHTvISOw/edit?usp=sharing"
       target="_blank" rel="noopener">Договор оферты</a><br>
    <a href="#privacy" data-legal-open>Политика в отношении обработки персональных данных</a></div>
 </div>
</footer>"""

def legal(body):
    return f"""
<section class="legal" id="privacy">
 <div class="wrap">
  <p class="copyright">Copyright © 2012 — 2026.</p>
 </div>
</section>

<div class="legal-modal" id="legalModal" role="dialog" aria-modal="true"
     aria-label="Политика в отношении обработки персональных данных">
  <div class="legal-modal-card">
    <button class="legal-modal-close" id="legalModalClose" aria-label="Закрыть">✕</button>
    <h3 class="legal-modal-title">Политика в отношении обработки персональных данных</h3>
    <div class="legal-body">{body}</div>
  </div>
</div>"""

def pay_modal():
    return """
<div class="pay-modal" id="payModal" role="dialog" aria-modal="true" aria-label="Оформление подписки">
  <div class="pay-modal-card">
    <button class="pay-modal-close" id="payModalClose" aria-label="Закрыть">✕</button>
    <iframe class="pay-modal-body" id="payModalFrame" title="Оформление подписки"></iframe>
  </div>
</div>"""

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

    /* Горизонталь ведём сами: в iOS Safari родная прокрутка внутрь ленты
       не доходила — палец её просто не двигал. touch-action:pan-y оставляет
       браузеру вертикаль (страница листается как обычно), а горизонталь
       целиком наша, поэтому ведёт себя одинаково везде. */
    var dragging = false, startX = 0, startScroll = 0, dist = 0, blockClick = false;
    strip.addEventListener("pointerdown", function(e){
      dragging = true; dist = 0; startX = e.clientX; startScroll = strip.scrollLeft;
    });
    strip.addEventListener("pointermove", function(e){
      if(!dragging) return;
      var dx = e.clientX - startX;
      if(Math.abs(dx) > dist) dist = Math.abs(dx);
      if(dist > 4) strip.scrollLeft = startScroll - dx;
    });
    function endDrag(){
      if(!dragging) return;
      dragging = false;
      blockClick = dist > 4;      /* это был свайп, а не тап — лайтбокс не открываем */
    }
    strip.addEventListener("pointerup", endDrag);
    strip.addEventListener("pointercancel", endDrag);
    strip.addEventListener("pointerleave", endDrag);
    strip.addEventListener("click", function(e){
      if(blockClick){ e.preventDefault(); e.stopPropagation(); blockClick = false; }
    }, true);
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

  var payModal = document.getElementById("payModal"),
      payFrame = document.getElementById("payModalFrame");
  function closePay(){
    payModal.classList.remove("on");
    payFrame.src = "about:blank";
    document.body.style.overflow = "";
  }
  document.querySelectorAll("[data-pay-page]").forEach(function(btn){
    btn.addEventListener("click", function(){
      payFrame.src = btn.getAttribute("data-pay-page");
      payModal.classList.add("on");
      document.body.style.overflow = "hidden";
    });
  });
  document.getElementById("payModalClose").addEventListener("click", closePay);
  payModal.addEventListener("click", function(e){ if(e.target===payModal) closePay(); });
  document.addEventListener("keydown", function(e){
    if(e.key==="Escape" && payModal.classList.contains("on")) closePay();
  });

  var legalModal = document.getElementById("legalModal");
  function closeLegal(){
    legalModal.classList.remove("on");
    document.body.style.overflow = "";
  }
  document.querySelectorAll("[data-legal-open]").forEach(function(a){
    a.addEventListener("click", function(e){
      e.preventDefault();
      legalModal.classList.add("on");
      document.body.style.overflow = "hidden";
    });
  });
  document.getElementById("legalModalClose").addEventListener("click", closeLegal);
  legalModal.addEventListener("click", function(e){ if(e.target===legalModal) closeLegal(); });
  document.addEventListener("keydown", function(e){
    if(e.key==="Escape" && legalModal.classList.contains("on")) closeLegal();
  });
})();
""" % DEADLINE_ISO

def render(inline=None, shots=None):
    return f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Год спокойствия</title>
<meta name="description" content="Годовая подписка к новому учебному году: доступ на 12 месяцев ко всем программам Павла Федоренко и закрытому терапевтическому клубу.">
<style>{CSS}</style>

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
{footer()}
{legal(privacy_html())}
{pay_modal()}
<script>{JS}</script>
"""

def favicon_uri():
    """Логотип-дерево с сайта как иконка вкладки: тот же файл, что в шапке
       и футере, ужатый до 64px и дополненный до квадрата прозрачным полем —
       исходник 192x195, а вкладке нужна ровно квадратная картинка."""
    import base64, subprocess, os, png
    src, fit, dst = "assets/logo-tree.png", "cache/favicon-tree-fit.png", "cache/favicon-tree64.png"
    os.makedirs("cache", exist_ok=True)
    if not os.path.exists(dst):
        subprocess.run(["sips", "-Z", "64", src, "--out", fit], check=True, capture_output=True)
        w, h, rgba = png.read(fit)
        sq = bytearray(64 * 64 * 4)
        ox, oy = (64 - w) // 2, (64 - h) // 2
        for y in range(h):
            row = (oy + y) * 64 * 4 + ox * 4
            sq[row:row + w * 4] = rgba[y * w * 4:(y + 1) * w * 4]
        png.write(dst, 64, 64, sq)
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
<script>if(location.protocol==="http:"&&!/^(localhost|127\\.0\\.0\\.1)$/.test(location.hostname))location.replace("https://"+location.host+location.pathname+location.search+location.hash);</script>
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
<script>window.qualitySchoolHash='06eb61b839a0cefee4967c67ccb099dc'</script>
<script src="https://getcourse.ru/public/js/qr-hidden-banner.js"></script>
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

def logo_uri():
    import base64
    return ("data:image/png;base64,"
            + base64.b64encode(open("assets/logo-tree.png", "rb").read()).decode())

def png_uri(path):
    import base64
    return "data:image/png;base64," + base64.b64encode(open(path, "rb").read()).decode()

if __name__ == "__main__":
    import inline as _inline
    doc = with_fonts(render(shots=_inline.local_shots), GILROY)
    doc = doc.replace("{HERO_CARD}", hero_card_uri())
    doc = shell(doc)
    open("index.html", "w", encoding="utf-8").write(doc)
    dims.save()
    print("index.html written")
