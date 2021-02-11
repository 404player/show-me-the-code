### solution

**第 0000 题：** 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
类似于图中效果

![头像](http://i.imgur.com/sg2dkuY.png?1)

**源码**：

```python
__author__ = 'geekboy'

from PIL import Image,ImageDraw,ImageFont

image = Image.open('0.jpg')
w,h = image.size
ttfont = ImageFont.truetype('./sarasa-italic.ttc',100)
draw = ImageDraw.Draw(image)
draw.text((4*w/5,h/5),'5',fill=(255,10,10,),font=ttfont)
image.save('0.0.png','png')
```

**注解** :

本题主要用到了 `pillow ` 第三方图像处理库。  

`Image` 主要用于从文件中加载图像对象并保存， `ImageFont`用于加载字体对象， `ImageDraw`模块在图像中写入文字。  

具体代码库如上图所示。

