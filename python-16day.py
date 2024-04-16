# 开发人：wby
# 类型：python
# coding = utf-8
# 开发时间：2024/4/16  13:17

# 1，图像的简单处理方法

from PIL import Image, ImageFilter

# *****************************************************************
# image = Image.open('./动漫人物1.jpg')
# image.format = 'JPEG'
# size_image = image.resize((900, 650))
# size_image.show()
# *****************************************************************

# 剪裁图像
# image = Image.open('./动漫人物1.jpg')
# rect = 80, 20, 310, 360
# image.crop(rect).show()

# 设置图像大小
# image = Image.open('./动漫人物1.jpg')
# size = 400, 400
# image.thumbnail(size)
# image.show()

# *****************************************************************
# 缩放和粘贴图像
# image1 = Image.open('./动漫人物1.jpg')
# image2 = Image.open('./动漫人物2.jpg')
# rect = 200, 200, 400, 400
# i1 = image2.crop(rect)
# width, height = i1.size
# image1.paste(i1.resize((int(width / 1.5), int(height / 1.5))), (100, 100))
# image1.show()
# *****************************************************************

# 旋转和翻转
# image = Image.open('./动漫人物1.jpg')
# image = image.rotate(180).show()      # 旋转180
# image.show()

# image1 = image.transpose(Image.FLIP_LEFT_RIGHT)   # 左右翻转
# image1.show()

# image2 = image.transpose(Image.FLIP_TOP_BOTTOM)    # 上下翻转
# image2.show()


# 操作像素
# image = Image.open('./动漫人物1.jpg')
# for x in range(400, 600):
#     for y in range(400, 500):
#         image.putpixel((x, y), (110, 110, 110))
#
# image.show()


# 过滤效果
# image = Image.open('./动漫人物1.jpg')
# image.filter(ImageFilter.CONTOUR).show()  # 轮廓过滤器
# image.filter(ImageFilter.SHARPEN).show()    # 锐化过滤器
# ****************************************************************************


# 2，Excel和Word的处理方法
# 2.1 处理Excel表格
# import datetime  # 导入datetime库
# from openpyxl import Workbook  # 导入openpyxl库
#
# wb = Workbook()    # 创建一个工作簿
# ws = wb.active     # ws = wb['Sheet']
# # ws = wb.create_sheet('wby.xlsx')  # 或者创建一个名为wby的sheet
# ws['A1'] = 42
# ws.append([1, 2, 3])   # 在A1中写入42，在A2中写入1,2,3
# ws['A3'] = datetime.datetime.now()   # 在A3中写入当前时间
# wb.save('wby.xlsx')      # 保存Excel文件

# 2.2 处理Word文档
# from docx import Document  # 导入docx库
# from docx.shared import Inches
#
# doc = Document()     # 创建一个Word文档
#
# doc.add_heading('Document Title', 0)  # 添加一个标题
#
# p = doc.add_paragraph('A plain paragraph having some ')  # 添加一个段落
# p.add_run('bold').bold = True   # 添加粗体字
# p.add_run(' and some ')  # 添加普通字
# p.add_run('italic.').italic = True   # 添加斜体字
#
# doc.add_heading('Heading, level 1', level=1)   # 添加一个标题
#
# doc.add_paragraph('Intense quote', style='Intense Quote')  # 添加一个引用段落
#
# doc.add_paragraph('有时候不喜欢你的人对你不好，其实就是对你好。', style='List Bullet')   # 添加一个无序列表
# doc.add_paragraph('Out of sight，out of love. （看不到了，也就不再爱了）', style='List Bullet')   # 添加一个无序列表
# doc.add_paragraph('每一个不曾起舞的日子，都是对生命的辜负。', style='List Bullet')   # 添加一个无序列表
#
# doc.add_paragraph('人生最难的是遇见，更难的其实是重逢。', style='List Number')   # 添加一个有序列表
# doc.add_paragraph('世界上最可怕的人果然就是比自己还了解自己的人。', style='List Number')   # 添加一个有序列表
# doc.add_paragraph('不乱于心，不困于情，不畏将来，不念过往，如此，安好！', style='List Number')   # 添加一个有序列表
#
# doc.add_picture('./动漫人物1.jpg', width=Inches(3))   # 添加一张图片
#
# records = (
#     (1, '101', 'Banana'),
#     (2, '202', 'Eggs'),
#     (3, '303', 'Apples')
# )
#
# table = doc.add_table(rows=1, cols=3)   # 添加一个表格
#
# hdr_cells = table.rows[0].cells   # 获取表头单元格
# hdr_cells[0].text = 'Xh'   # 设置表头内容
# hdr_cells[1].text = 'Id'    # 设置表头内容
# hdr_cells[2].text = 'Desc'  # 设置表头内容
#
# for xv, id, desc in records:
#     row_cells = table.add_row().cells   # 添加一行
#     row_cells[0].text = str(xv)   # 设置行内容
#     row_cells[1].text = id    # 设置行内容
#     row_cells[2].text = desc  # 设置行内容
#
# doc.add_page_break()   # 添加分页符
# doc.save('wby.docx')     # 保存Word文档


# 3，PDF的处理方法
# from reportlab.pdfgen import canvas
#
# # 创建一个PDF文件
# pdf = canvas.Canvas("wby.pdf")
#
# # 添加一个标题
# pdf.setTitle("My First PDF")
#
# # 添加一个段落
# pdf.drawString(100, 750, "Hello, World!---------------------------")
#
# # 保存PDF文件
# pdf.save()


# 4，PDF和Word的相互转换
# 4.1 转换PDF到Word
# from pdf2docx import Converter
# import pdf2docx
# # PDF文件路径
# pdf_file = './wby.pdf'
#
# # 转换PDF到Word
# cv = Converter('./wby.pdf')  # 创建一个转换器对象
# cv.convert('by.docx')   # 转换PDF到Word
# cv.close()  # 关闭转换器对象


# 4.2 转换Word到PDF
# from docx2pdf import convert
#
# # 打开Word文件
# word_file = './wby.docx'
#
# # 转换Word到PDF
# convert(word_file, 'wby.pdf')




