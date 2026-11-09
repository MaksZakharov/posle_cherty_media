# Эталон стиля v4 (сцена v3 в манере густых мазков, 09.11.2026)

Замечание Макса к v3: сцена нормальная, её не переделывать, но потерян стиль. Нужна живопись густыми видимыми мазками, как в `probes/styles_2026-11-09/style4_book_illustration.jpg` и `style_reference_v1/reference.jpg`.

`reference_v4.jpg`: 1920×1080, увеличено из нативных 1280×720 (LANCZOS + лёгкая резкость). Исходник, кропы 1:1 и 4:5 по центру и превью 320×180 лежат в `crops/`.

## Попытки (5)
- a: v3 + style4 как референсы. Мазки появились, но мелкие; сцена сохранена. Стала базой для d.
- b: v3 + style4 + v1/reference. Мазки сильнее, но однообразная «фильтровая» фактура, Аня босая, нога сливается с ножкой стола. Брак.
- c: широкие плоские мазки. Брак: лица ушли в плакатную мультяшность.
- d: a + v1/reference + style4, «реалистичные люди, густое импасто». Мазки по всему кадру, лица реалистичные, но одна нога Ани за ножкой стола.
- e: правка поверх d, менялись только ноги Ани: обе стоят слева от стола, в колготках и школьных туфлях, стол сдвинут чуть вправо. **Принят.**

## Что исправлено относительно v3
1. Видимые густые мазки по всему кадру: стены, шкафы, халат, скатерть, пол, коврик, таз.
2. Меньше гладкой цифровой детализации; люди остались реалистичными.
3. Ноги Ани отделены от ножки стола: обе видны целиком, в туфлях на полу.
4. Сцена v3 сохранена: таз на полу целиком с тенью, колени под прямым углом, голени вертикально, лица по центру, свет лампы, купюры без цифр.

## Промпт (d), референсы: v3/a, style_reference_v1/reference (оригинал), style4_book_illustration.jpg
Repaint the first image with the same scene, composition, poses, faces, light and objects in the same places, in the painting technique of the second and third images: a realistic painterly oil/gouache painting with thick, visible, textured brushstrokes over the entire canvas, like hand-painted impasto: rough horizontal and vertical strokes on the cream walls, streaky strokes on the navy cabinets, heavy folds in the terracotta robe built from strokes, brushy tablecloth, rough strokes on the floor and rug. The texture is clearly paint on canvas, more brushy and rough than the first image, with less smooth fine detail, but the people stay REALISTIC (realistic proportions and faces like in the second image, not stylized, not cartoon). The mother looks up stunned; the 15-year-old girl cries and shouts holding two plain banknotes. Feet flat in the white basin fully visible on the floor with shadow, knees at a right angle; the girl's legs in dark tights clearly in front of the table leg. Correct hands. No text, letters, numbers, border.

## Правка (e), референс: попытка d
Edit the reference image, keep everything identical (composition, kitchen, lamp, faces, mother's pose, robe, basin on the floor, table, colors, thick impasto brushstroke texture everywhere). Only change the girl's legs: both of her legs in dark tights stand together in the open space to the LEFT of the table, between the mother's basin and the table, fully visible from knees to feet with dark school shoes on the floor; the wooden table leg stands separately to the right of her legs with clear space between them. No text, numbers, border.

## Честные недостатки
- Нативно 1280×720, 1920×1080 получено увеличением.
- Мазки мельче и «штриховее», чем в style4 (там крупные плоские пятна); на зуме фактура местами выглядит однообразной, будто фильтр.
- Общая гамма темнее и теплее, чем в style4 (ночь под лампой, а не дневная кухня).
- Стол в правке сдвинулся правее и стал чуть меньше; второй стул за ним.
- Купюры условные, рубли только по цвету.
