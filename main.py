from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import datetime

# 土台となる賞状のテンプレート画像
img_path = './Certificate-of-merit.jpg'

# 画像に文字を追記する関数
def add_text_to_image(img, text, font_path, font_size, font_color, height, width, max_length=740):
    position = (width, height)
    font = ImageFont.truetype(font_path, font_size)
    draw = ImageDraw.Draw(img)
    if draw.textsize(text, font=font)[0] > max_length:
        while draw.textsize(text + '…', font=font)[0] > max_length:
            text = text[:-1]
        text = text + '…'

    draw.text(position, text, font_color, font=font)

    return img

# 今日の日付を取得
dt_now = datetime.datetime.now()
now = dt_now.strftime('%Y年%m月%d日')
now = dt_now.strftime('%Y年')+"3月1日"

# 名簿(names.txt)にある名前を読み込む
with open('names.txt', 'r') as f:
    for name in f:
        img = Image.open(img_path).copy()

        output = add_text_to_image(
        img=img, 
        text='認 定 証', 
        font_path='./Font/Kyokasho.ttc',
        font_size=100, 
        font_color = (0, 0, 0), 
        height = 200, 
        width = 277
        )

        output = add_text_to_image(
        img=img, 
        text=name, 
        font_path='./Font/Kyokasho.ttc',
        font_size=80, 
        font_color = (0, 0, 0), 
        height = 390, 
        width = 250
        )

        output = add_text_to_image(
        img=img, 
        text='殿', 
        font_path='./Font/Kyokasho.ttc',
        font_size=70, 
        font_color = (0, 0, 0),
        height = 400, 
        width = 675
        )

        output = add_text_to_image(
        img=img, 
        text='　あなたは百人一首', 
        font_path='./Font/Kyokasho.ttc',
        font_size=70, 
        font_color = (0, 0, 0),
        height = 550, 
        width = 140
        )

        output = add_text_to_image(
        img=img, 
        text='大会で　　首覚えた', 
        font_path='./Font/Kyokasho.ttc',
        font_size=70, 
        font_color = (0, 0, 0),
        height = 650, 
        width = 140
        )

        output = add_text_to_image(
        img=img, 
        text='ことを証します', 
        font_path='./Font/Kyokasho.ttc',
        font_size=70, 
        font_color = (0, 0, 0),
        height = 750, 
        width = 140
        )

        output = add_text_to_image(
        img=img, 
        text=now, 
        font_path='./Font/Kyokasho.ttc',
        font_size=50, 
        font_color = (0, 0, 0),
        height = 950, 
        width = 200
        )

        output = add_text_to_image(
        img=img, 
        text='秀水書道教室　楯 秀翠', 
        font_path='./Font/Kyokasho.ttc',
        font_size=50, 
        font_color = (0, 0, 0),
        height = 1050, 
        width = 210
        )

        output.save('./Certificate-of-merit/' + name + '.jpg')