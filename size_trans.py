from PIL import Image
import os

# 原始文件夹路径
original_folder = 'D:/code/yolov5/runs/detect/exp2/roi'
# 保存的新文件夹路径
new_folder = 'D:/code/yolov5/runs/detect/exp2/roi'

# 遍历原始文件夹中的图像
for filename in os.listdir(original_folder):
    img = Image.open(os.path.join(original_folder, filename))
    # 改变尺寸
    img_resized = img.resize((100, 100))   #这里是你要转换的尺寸
    # 保存到新文件夹
    img_resized.save(os.path.join(new_folder, filename))

