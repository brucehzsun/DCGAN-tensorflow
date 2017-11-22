# -*- coding: utf-8 -*-
import os
from PIL import Image

if __name__ == '__main__':
    srcPath = r"C:\Users\sunhongzhi\Desktop\temp\test"
    targetDir = r"C:\Users\sunhongzhi\Desktop\temp\target"
    for file_name in os.listdir(srcPath):
        file_path = os.path.join(srcPath, file_name)
        if os.path.isfile(file_path):
            with Image.open(file_path) as image:
                img_width = image.size[0]
                img_height = image.size[1]
                print(image.size)
                targetFile = os.path.join(targetDir, file_name)

                if img_width > img_height:
                    img_width_new = img_height * img_height / img_width
                    x_start = (img_width - img_width_new) / 2
                    x_end = x_start + img_width_new
                    y_start = 0
                    y_end = img_height
                    box = (x_start, y_start, x_end, y_end)  # 设定裁剪区域
                    image = image.crop(box)
                    img_width = img_width_new

                new_image_width = 512
                new_image_height = int(img_height / img_width * new_image_width)
                image = image.resize((new_image_width, new_image_height), Image.ANTIALIAS)

                if new_image_height != 682:
                    x_start = 0
                    x_end = 512
                    y_start = 0
                    y_end = 682
                    box = (x_start, y_start, x_end, y_end)  # 设定裁剪区域
                    image = image.crop(box)
                image.save(targetFile)
