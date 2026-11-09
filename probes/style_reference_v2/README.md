# Эталон стиля v2 (доработка reference_alt из v1, 09.11.2026)

Макс выбрал `style_reference_v1/reference_alt.jpg` («уже лучше»). Замечание: у Ирины ноги слишком задраны, колени подняты, халат задран; нужна естественность без косяков.

`reference_v2.jpg`: 1920×1080, увеличено из нативных 1280×720 (LANCZOS + лёгкая резкость). Исходник, кропы 1:1 и 4:5 по центру и превью 320×180 лежат в `crops/`.

## Попытки (5)
- a, b: правка поверх reference_alt. Брак: колени по-прежнему задраны, голые бёдра.
- c: заново по референсу, с длинным халатом и низким тазом. Поза естественная, купюры рублёвые, но Аня выглядит взрослой. Стала базой.
- d: тоже естественная поза, но сиреневая купюра похожа на доллар, Аня взрослая. Брак.
- e: правка поверх c, только Аня моложе. **Принят.**

## Что исправлено относительно reference_alt
1. Ирина сидит естественно: бёдра почти горизонтально, колени не выше бёдер, голени вниз, ступни на дне низкого таза.
2. Длинный халат закрывает бёдра и колени, голых бёдер нет.
3. Аня моложе: детское круглое лицо, школьная блузка, тёмная юбка, колготки.
4. Купюры рублёвые по цвету (оранжевая и сиреневая), без читаемых цифр.
5. Кисти рук: у Ирины сложены на коленях, у Ани купюры и кулак, пальцы корректны.
6. Кухня, лампа, палитра и манера сохранены, лица в центре.

## Промпт (c), референс: style_reference_v1/crops/reference_alt_original_1280x720.jpg
Painterly realistic book illustration in the exact style, palette, lighting and setting of the reference image (night Russian kitchen, hanging lamp, window with night sky, cream cupboard with teal kettle on the left, navy cabinets and stove on the right, small table with white tablecloth, mug and phone on the right; visible gouache brushstrokes; cream, terracotta, teal, navy).
Irina, the same tired 46-year-old woman with dark hair in a bun, wears a LONG terracotta bathrobe that reaches down to her mid-shins. She sits upright on an ordinary kitchen chair of normal height. Her thighs are horizontal, flat along the chair seat and completely covered by the bathrobe; her knees are covered by the robe and are at the same height as the chair seat, bent at 90 degrees; from the knees her bare lower shins go straight vertically down into a wide, LOW, shallow white enamel basin of hot water standing flat on the floor; her feet rest flat on the bottom of the basin. Natural relaxed sitting posture, modest, like a real photo of a woman soaking her feet. Hands folded calmly on her lap over the robe. She looks up at her daughter, stunned and silent.
Anya, the same daughter, but clearly a 15-year-old schoolgirl (young teen face, slim, white school blouse, dark skirt, dark ponytail), stands next to her leaning in, crying and shouting, holding out two folded Russian banknotes (orange and lilac, plain, no numbers); other fist clenched at her chest.
Both faces in the central part of the frame, realistic anatomy, five fingers, not cartoon. No text, letters, numbers, logos, border.

## Правка (e), референс: попытка c
Edit the reference image, keep absolutely everything the same (kitchen, lamp, colors, painterly gouache brushwork, the mother, her pose, robe, legs, basin, the table, the banknotes, composition). Change only the shouting daughter: make her clearly a 15-year-old schoolgirl, a young teenager, not an adult: rounder softer childish face, smaller nose and jaw, slightly shorter and slimmer narrow shoulders, same crying expression with tears and open mouth shouting, same messy dark ponytail, same white school blouse, dark school skirt knee length with dark tights. Realistic, not cartoon, five fingers. No text.

## Честные недостатки
- Нативно 1280×720, 1920×1080 получено увеличением.
- Нижний край таза срезан рамкой кадра.
- Ирина сидит на обычном стуле, не на низкой табуретке; колени чуть выше середины бедра, но в пределах естественного.
- Юбка Ани выше колена, хотя просил до колена.
- Купюры условные: цвет рублёвый, рисунок нет.
- Лицо Ирины чуть левее центра (около 40% ширины), но в кропах 1:1 и 4:5 оно целиком.
