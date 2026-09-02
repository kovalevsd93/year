# -*- coding: utf-8 -*-
"""Заглушки для медиа-слота платформы в блоке «Комплексное решение»,
пока нет настоящих скриншотов (см. ТЗ). Линейные иллюстрации —
не имитация экрана, а нейтральный знак «здесь будет инструмент»,
поэтому без текста и без вымышленных данных пользователей.
Каждая наследует цвет через currentColor — красится в цвет своего
уровня контейнером-обёрткой."""

_WRAP = ('<svg viewBox="0 0 220 150" fill="none" stroke="currentColor" '
         'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" '
         'aria-hidden="true">%s</svg>')

# 0 — календарь практик: неделя ячеек, часть отмечена
_CALENDAR = ('<rect x="24" y="34" width="172" height="94" rx="12"/>'
             '<path d="M24 62h172"/><path d="M64 24v20M156 24v20"/>'
             '<g stroke-width="1.4">'
             '<rect x="40" y="78" width="20" height="20" rx="5"/><path d="M45 88l4 4 8-9"/>'
             '<rect x="72" y="78" width="20" height="20" rx="5"/><path d="M77 88l4 4 8-9"/>'
             '<rect x="104" y="78" width="20" height="20" rx="5"/>'
             '<rect x="136" y="78" width="20" height="20" rx="5"/><path d="M141 88l4 4 8-9"/>'
             '<rect x="168" y="78" width="20" height="20" rx="5"/>'
             '</g>')

# 1 — тренировка внимания: таймер-кольцо и пять отметок-звуков
_TIMER = ('<circle cx="110" cy="66" r="42"/>'
          '<path d="M110 66V38"/><path d="M110 66l20 8"/>'
          '<g stroke-width="1.4">'
          '<circle cx="58" cy="128" r="5"/><circle cx="84" cy="128" r="5"/>'
          '<circle cx="110" cy="128" r="5"/><circle cx="136" cy="128" r="5"/>'
          '<circle cx="162" cy="128" r="5"/></g>')

# 2 — дневник мыслей: карточка с четырьмя полями разной длины
_DIARY = ('<rect x="30" y="18" width="160" height="114" rx="12"/>'
          '<path d="M50 44h16"/><path d="M78 44h82"/>'
          '<path d="M50 68h16"/><path d="M78 68h64"/>'
          '<path d="M50 92h16"/><path d="M78 92h44"/>'
          '<path d="M50 116h16"/><path d="M78 116h70"/>')

# 3 — дневник экспозиции: лестница шагов, часть пройдена, флажок цели наверху
_LADDER = ('<path d="M20 128h30v-22h30v-22h30v-22h30v-22h30"/>'
           '<path d="M28 118l5 5 9-9"/><path d="M58 96l5 5 9-9"/>'
           '<path d="M170 40v-18"/><path d="M170 22l16 6-16 6"/>')

_SHAPES = (_CALENDAR, _TIMER, _DIARY, _LADDER)


def placeholder(i):
    return _WRAP % _SHAPES[i]
