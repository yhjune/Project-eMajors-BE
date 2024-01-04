# What is this?
python 이용 PDF 생성 소프트웨어 라이브러리. 또한 차트, 데이터 그래픽, 다양한 비트맵 및 벡터 형식을 pdf로 변환해준다.

# Graphicd and text with pdfgen
## Basic Concepts
- canvas 이용하여 pdf "paint"
- 왼쪽 하단을 (0,0)으로 하는 Cartesian (X,Y) 좌표계 이용
- x 증가 시 right, y 증가 시 up 이 default 세팅

### simple example
```python
from reportlab.pdfgen import canvas
def hello(c):
    c.drawString(100,100,"Hello World")
c = canvas.Canvas("hello.pdf")
hello(c)
c.showPage()
c.save()
```
1. canvas object를 생성
2. hello.pdf를 현재 워킹 디렉토리에 생성한다.
3. hello 함수를 호출하여 canvas를 인자로 전달한다.
4. showPage 메서드를 이용해 canvas의 현재 페이지를 저장하고
5. save 메서드를 사용하여 파일을 저장한 뒤 canvas를 close

### config
```py
from reportlab.lib.pagesizes import letter, A4
myCanvas = Canvas('myfile.pdf', pagesize=letter)
width, height = letter
def __init__(self,filename,
             pagesize=(595.27,841.89),
             bottomup = 1, # switches coordinate systems, botton left
             pageCompression=0, # determines whether the stream of PDF operations for each page is compressed. If output size is important set pageCompression=1 (slower)
             encoding=rl_config.defaultEncoding, #  Its default value is fine unless you very specifically need to use one of the 25 or so characters which are present in MacRoman and not in Winansi.
             verbosity=0 # how much log information is printed
             encrypt=None):
```

### draw operations

draw straight line segments on the canvas.
```py
canvas.line(x1,y1,x2,y2)
canvas.lines(linelist)
```

draw common complex shapes on the canvas.
```py
canvas.grid(xlist, ylist) 
canvas.bezier(x1, y1, x2, y2, x3, y3, x4, y4)
canvas.arc(x1,y1,x2,y2) 
canvas.rect(x, y, width, height, stroke=1, fill=0) 
canvas.ellipse(x1,y1, x2,y2, stroke=1, fill=0)
canvas.wedge(x1,y1, x2,y2, startAng, extent, stroke=1, fill=0) 
canvas.circle(x_cen, y_cen, r, stroke=1, fill=0)
canvas.roundRect(x, y, width, height, radius, stroke=1, fill=0)
```

draw single lines of text on the canvas.
```py
canvas.drawString(x, y, text):
canvas.drawRightString(x, y, text) 
canvas.drawCentredString(x, y, text)
```

used to format text in ways that are not supported directly by the canvas interface. A program creates a text object from the canvas using beginText and then formats text by invoking textobject methods. Finally the textobject is drawn onto the canvas using drawText.
```py
textobject = canvas.beginText(x, y) 
canvas.drawText(textobject)
```


similar to text objects: they provide dedicated control for performing complex graphical drawing not directly provided by the canvas interface. A program creates a path object using beginPath populates the path with graphics using the methods of the path object and then draws the path on the canvas using drawPath.
```py
path = canvas.beginPath() 
canvas.drawPath(path, stroke=1, fill=0, fillMode=None) 
canvas.clipPath(path, stroke=1, fill=0, fillMode=None)
```

ending a page
```py
canvas.showPage()
```

> You need the Python Imaging Library (PIL) to use images with the ReportLab package.

> All state changes (font changes, color settings, geometry transforms, etcetera) are FORGOTTEN when you advance to a new page in pdfgen. Any state settings you wish to preserve must be set up again before the program proceeds with drawing!

### text
```py
textobject.setTextOrigin(x,y)
textobject.setTextTransform(a,b,c,d,e,f)
textobject.moveCursor(dx, dy) # from start of current LINE
(x,y) = textobject.getCursor()
x = textobject.getX(); y = textobject.getY()
textobject.setFont(psfontname, size, leading = None)
textobject.textOut(text)
textobject.textLine(text='')
textobject.textLines(stuff, trim=1)
```

### Features

1. form
2. internal hyperlinks
3. Outline Trees
4. encryption
5. interactive form
   
### Platypus
