# python 操作pdf
# import PyPDF2
# import reportlab


from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

pdf_canvas = canvas.Canvas("resources/demo.pdf", pagesize=A4)
width, height = A4
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader  # 导入ImageReader

pdf_canvas = canvas.Canvas("resources/demo.pdf", pagesize=A4)
width, height = A4

# 绘图
image = ImageReader("resources/glass.jpg")  # 使用ImageReader
pdf_canvas.drawImage(image, 20, height - 395, 250, 375)

# 显示当前页
pdf_canvas.showPage()

# 注册字体文件
# pdfmetrics.registerFont(TTFont("Font1", "resources/fonts/Vera.ttf"))
# pdfmetrics.registerFont(TTFont("Font2", "resources/fonts/青呱石头体.ttf"))

# 绘图
image = ImageReader("resources/glass.jpg")
pdf_canvas.drawImage(image, 20, height - 395, 250, 375)

# 显示当前页
pdf_canvas.showPage()

# 注册字体文件
# pdfmetrics.registerFont(TTFont("Font1", "resources/fonts/Vera.ttf"))
# pdfmetrics.registerFont(TTFont("Font2", "resources/fonts/青呱石头体.ttf"))

# 写字
# pdf_canvas.setFont("Font2", 40)
pdf_canvas.setFillColorRGB(0.9, 0.5, 0.3, 1)
pdf_canvas.drawString(width // 2 - 120, height // 2, "你好，世界！")
# pdf_canvas.setFont("Font1", 40)
pdf_canvas.setFillColorRGB(0, 1, 0, 0.5)
pdf_canvas.rotate(18)
pdf_canvas.drawString(250, 250, "hello, world!")

# 保存
pdf_canvas.save()
