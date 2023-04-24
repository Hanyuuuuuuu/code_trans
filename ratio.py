# 将图片和标注数据按比例切分为 训练集和测试集3:1

import os
import random
from shutil import copy2

# 原始路径
image_original_path = r"D:\document\pyproject\gantest\COCO_PATH\result_images\train2017"
label_original_path = r"D:\document\pyproject\gantest\COCO_PATH\result_annotations\train2017"

# 训练集路径
train_image_path = os.path.join(r"D:\document\pyproject\gantest\COCO_PATH\labels\T\L/")
train_label_path = os.path.join(r"D:\document\pyproject\gantest\COCO_PATH\labels\T\I/")
# 测试集路径
val_image_path = os.path.join(r"D:\document\pyproject\gantest\COCO_PATH\labels\V\L/")
val_label_path = os.path.join(r"D:\document\pyproject\gantest\COCO_PATH\labels\V\I/")


# 检查文件夹是否存在
def mkdir():
    if not os.path.exists(train_image_path):
        os.makedirs(train_image_path)
    if not os.path.exists(train_label_path):
        os.makedirs(train_label_path)

    if not os.path.exists(val_image_path):
        os.makedirs(val_image_path)
    if not os.path.exists(val_label_path):
        os.makedirs(val_label_path)


def main():
    mkdir()
    # 复制移动图片数据
    all_image = os.listdir(image_original_path)
    for i in range(len(all_image)):
        num = random.randint(1, 4)  # 随机给图片赋值，每五个随机赋值一次，抽取不为2的图片
        if num != 2:
            copy2(os.path.join(image_original_path, all_image[i]), train_image_path)
            train_index.append(i)
        else:
            copy2(os.path.join(image_original_path, all_image[i]), val_image_path)
            val_index.append(i)

    # 复制移动标注数据
    all_label = os.listdir(label_original_path)
    for i in train_index:
        copy2(os.path.join(label_original_path, all_label[i]), train_label_path)
    for i in val_index:
        copy2(os.path.join(label_original_path, all_label[i]), val_label_path)


if __name__ == '__main__':
    train_index = []
    val_index = []
    main()