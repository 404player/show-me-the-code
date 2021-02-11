# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     0.py
   Description :
   Author :       geekboy
   date：          2021/2/11
-------------------------------------------------
   Change Activity:
                   2021/2/11:
-------------------------------------------------
"""
__author__ = 'geekboy'

from PIL import Image,ImageDraw,ImageFont

image = Image.open('0.jpg')
w,h = image.size
ttfont = ImageFont.truetype('./sarasa-italic.ttc',100)
draw = ImageDraw.Draw(image)
draw.text((4*w/5,h/5),'5',fill=(255,10,10,),font=ttfont)
image.save('0.0.png','png')




