# Эталон стиля v3 (доработка reference_v2, 09.11.2026)

Замечание Макса к v2: колени приподняты, поэтому кажется, что таз стоит не на полу; кадр неоднозначный.

`reference_v3.jpg`: 1920×1080, увеличено из нативных 1280×720 (LANCZOS + лёгкая резкость). Исходник, кропы 1:1 и 4:5 по центру и превью 320×180 лежат в `crops/`.

## Попытки (3)
- a: камера чуть дальше. Брак: таз всё ещё срезан нижней рамкой, пола под ним не видно.
- b: камера с роста, чуть сверху. Фигуры целиком, таз на полу, геометрия верная. Но на оранжевой купюре проступает похожий на «5» узор.
- c: правка поверх b, менялись только купюры (без цифр). **Принят.**

## Что исправлено относительно v2
1. Таз стоит на полу (на коврике) и виден целиком, с тенью. Пол виден вокруг и перед ним, рамка ничего не срезает.
2. Стул обычной высоты. Бёдра горизонтально, колени под прямым углом на уровне сиденья, голени вертикально к полу, ступни плоско на дне таза.
3. Камера дальше и чуть сверху: видно пол, обе фигуры целиком, лица по центру (Ирина ~42% ширины, Аня ~57%).
4. Купюры оранжевая и сиреневая, с абстрактным орнаментом, без цифр и букв.
5. Кухня, лампа, палитра, манера, лица, Аня 15 лет и закрытые халатом колени остались как в v2.

## Промпт (b), референс: style_reference_v2/crops/reference_v2_original_1280x720.jpg
Repaint the reference image as a slightly wider shot from a standing eye level looking a little down, keeping the same night kitchen, lamp, cabinets, table, colors, gouache texture, and the same two people with the same faces and emotions in the center of the frame. Show the full figures: the mother from head to feet, and the floor around her. She sits upright on a normal wooden kitchen chair; her lap is flat and level, knees bent at a right angle, lower legs perpendicular to the floor, both feet resting flat inside a shallow white enamel basin that sits on the floor tiles, with a visible shadow under the basin and floor visible in front of it. The basin is entirely inside the frame. Her long terracotta robe hangs over her knees. The daughter (15-year-old schoolgirl, white blouse, dark skirt, tights) stands beside her, full figure with feet on the floor, crying and shouting, holding two folded orange and lilac banknotes toward her mother. Realistic people, correct perspective of chair, basin and table, correct hands. No text, numbers, logos, frame.

## Правка (c), референс: попытка b
Edit the reference image, keep everything identical (camera, composition, kitchen, lamp, people, faces, poses, legs, chair, basin on the floor with its shadow, table, colors, gouache brushwork). Only change the two banknotes in the girl's hand: make them plain pale orange and pale lilac paper notes with soft abstract ornament, with absolutely no digits, no letters, no numbers, no portraits. No text anywhere.

## Честные недостатки
- Нативно 1280×720, 1920×1080 получено увеличением.
- Лица мельче, чем в v2 (плата за видимый пол); на превью 320×180 эмоции читаются, но слабее.
- Купюры условные, на рубли похожи только цветом.
- Юбка Ани выше колена; её ноги частично за столом, вторая нога за ножкой стола.
- Таз немного «висит» по тону: тень мягкая, коврик тёмный, контакт с полом читается, но не резко.
