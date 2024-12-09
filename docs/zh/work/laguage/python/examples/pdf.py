import fitz  # PyMuPDF
import cv2
import numpy as np
from PIL import Image
import PIL.ImageOps
from PIL import ImageFilter
from PIL import ImageEnhance

def black_white_map(value):
    threshold = 160  # 阈值，大于此值为白色，小于等于此值为黑色
    return 0 if value <= threshold else 255

def convert_pdf_to_black_and_white(input_pdf, output_pdf):
    # 打开PDF文件
    document = fitz.open(input_pdf)
    # 创建一个新文档来保存黑白页面
    new_document = fitz.open()

    for page_num in range(len(document)):
        page = document.load_page(page_num)
        # 获取页面的像素映射并转换为灰度
        pixmap = page.get_pixmap(colorspace=fitz.csGRAY)
        # 将fitz的pixmap转换为Pillow的图像格式
        img = Image.frombytes("L", [pixmap.width, pixmap.height], pixmap.samples)

        img2 = PIL.ImageOps.invert(img)
        img2 = img2.point(black_white_map)
        img2 = img2.convert("1")

        # 将Pillow图像对象转换为fitz的pixmap对象
        #     img_bytes = img2.tobytes()
        #     pixmap2 = fitz.Pixmap(fitz.csGRAY, img2.size[0], img2.size[1], img_bytes)

        # 显示图像
        #     img2.show()

        temp_img_path = f"imgs/temp_img_{page_num}.png"
        img2.save(temp_img_path)


        new_page = new_document.new_page(width=pixmap.width, height=pixmap.height)
        image = fitz.open(temp_img_path)
        new_page.insert_image(image[0].rect, filename=temp_img_path)

    # 保存修改后的PDF
    new_document.save(output_pdf)
    new_document.close()
    document.close()
    print(f"PDF文件已成功转换为黑白：{output_pdf}")



# 示例用法
input_pdf = r'C:\Users\wjn_0\Documents\WeChat Files\wxid_dwtvk7j9f16t21\FileStorage\File\2024-05\2024年上-信息系统项目管理师-考前密训2.pdf'
output_pdf = r'cs.pdf'
convert_pdf_to_black_and_white(input_pdf, output_pdf)




