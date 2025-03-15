# 操作图像


# 读取图像
from PIL import Image

im = Image.open("./resources/guido.jpg")
print(im.format, im.size, im.mode)

# im.show()  # 显示图像

# 通过Image对象的crop方法指定剪裁区域剪裁图像
# im.crop((80, 20, 310, 360)).show()


from PIL import ImageFilter

# 使用Image对象的filter方法对图像进行滤镜处理
# ImageFilter模块包含了诸多预设的滤镜也可以自定义滤镜
im.filter(ImageFilter.CONTOUR).show()
