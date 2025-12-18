from PIL import Image, ImageFilter, ImageDraw, ImageFont

# 1. Открываем изображение
img = Image.open("image_1.jpg")

# 2. Применяем фильтр размытия (Blur)
# Можно настроить радиус размытия: GaussianBlur(радиус)
img = img.filter(ImageFilter.GaussianBlur(radius=5))

# 3. Подготовка к рисованию текста
draw = ImageDraw.Draw(img)
text = "Вариант 1"

# Пытаемся загрузить стандартный шрифт (если нет, будет системный)
try:
    font = ImageFont.truetype("arial.ttf", 36)
except:
    font = ImageFont.load_default()

# 4. Вычисляем позицию (нижний правый угол)
# Получаем размер текста
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

# Отступаем по 20 пикселей от краев
width, height = img.size
position = (width - text_width - 20, height - text_height - 20)

# 5. Рисуем текст (белым цветом)
draw.text(position, text, font=font, fill="white")

# 6. Сохраняем результат
img.save("image_1_edited.jpg")
print("Готово! Файл image_1_edited.jpg создан.")
