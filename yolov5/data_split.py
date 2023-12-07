''' 2
cropping.txt 파일의 데이터가 train 폴더와 val 폴더에 있는 이미지에 맞게 train.txt와 val.txt 파일로 분리
'''

import os

# 경로 설정
cropping_file_path = 'C:/Users/user/PycharmProjects/yolov5/whale-categorization-playground/cropping.txt'
train_folder_path = 'C:/Users/user/PycharmProjects/yolov5/whale-categorization-playground/train'
val_folder_path = 'C:/Users/user/PycharmProjects/yolov5/whale-categorization-playground/val'
output_folder_path = os.path.dirname(cropping_file_path)

# cropping.txt에서 데이터 읽기
with open(cropping_file_path, 'r') as file:
    lines = file.readlines()

# train 및 val 폴더에 있는 이미지 파일 목록 생성
train_images = set(os.listdir(train_folder_path))
val_images = set(os.listdir(val_folder_path))

# train.txt 및 val.txt에 데이터 저장
with open(os.path.join(output_folder_path, 'train.txt'), 'w') as train_file, \
     open(os.path.join(output_folder_path, 'val.txt'), 'w') as val_file:
    for line in lines:
        image_name = line.split(',')[0]
        if image_name in train_images:
            train_file.write(line)
        elif image_name in val_images:
            val_file.write(line)
