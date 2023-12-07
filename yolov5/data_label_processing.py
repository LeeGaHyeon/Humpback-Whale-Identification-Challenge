'''4
현재의 라벨 형식은 고래 꼬리 지느러미의 가장자리에 있는 픽셀을 나타내는 여러 지점들로 구성
YOLOv5 형식으로 변환하기 위해서는 먼저 이 지점들을 사용하여 경계 상자(bounding box)를 생성
경계 상자는 객체를 둘러싸는 최소 사각형으로, 이를 위해 각 객체의 최소 x, 최대 x, 최소 y, 최대 y 값을 찾아야 함
이후, 이 경계 상자를 YOLOv5 형식으로 변환
YOLOv5는 객체의 중심 x, 중심 y, 너비, 높이를 정규화된 형태로 저장-정규화는 각 값을 이미지의 너비와 높이로 나누어 계산

따라서, 이 코드는 지정된 디렉토리 내의 모든 .txt 파일을 읽고, 각 파일의 라벨을 YOLOv5 형식으로 변환하여 저장
'''

# import os
# import glob
# from PIL import Image
#
#
# def convert_to_yolov5_format(points, img_width, img_height):
#     # 최소 및 최대 x, y 좌표 찾기
#     x_coords = points[0::2]
#     y_coords = points[1::2]
#     x_min, x_max = min(x_coords), max(x_coords)
#     y_min, y_max = min(y_coords), max(y_coords)
#
#     # 중심 좌표 및 너비, 높이 계산
#     x_center = ((x_min + x_max) / 2) / img_width
#     y_center = ((y_min + y_max) / 2) / img_height
#     width = (x_max - x_min) / img_width
#     height = (y_max - y_min) / img_height
#
#     return [0, x_center, y_center, width, height]  # 클래스 번호 0으로 가정
#
#
# def process_files_in_directory(labels_dir, images_dir):
#     # 해당 디렉토리 내의 모든 .txt 파일 찾기
#     txt_files = glob.glob(os.path.join(labels_dir, '*.txt'))
#
#     for txt_file in txt_files:
#         # 이미지 파일 이름을 가져오기 (txt 파일 이름과 동일)
#         image_file_name = os.path.splitext(os.path.basename(txt_file))[0] + '.jpg'
#         image_file_path = os.path.join(images_dir, image_file_name)
#
#         # 이미지 파일 열기 및 크기 가져오기
#         with Image.open(image_file_path) as img:
#             img_width, img_height = img.size
#
#         # 라벨 파일 처리
#         with open(txt_file, 'r') as file:
#             lines = file.readlines()
#
#         for line in lines:
#             # 클래스 번호와 좌표 분리
#             parts = line.strip().split(',')
#             points = [float(p) for p in parts[1:]]  # 좌표만 추출
#
#             # YOLOv5 형식으로 변환
#             yolov5_label = convert_to_yolov5_format(points, img_width, img_height)
#
#             # 결과를 같은 파일에 저장
#             with open(txt_file, 'w') as file:
#                 file.write(','.join(map(str, yolov5_label)))
#
#
# # # 디렉토리 경로 설정(train)
# # labels_dir = 'C:/Users/user/PycharmProjects/yolov5/whale-categorization-playground/labels/train'
# # images_dir = 'C:/Users/user/PycharmProjects/yolov5/whale-categorization-playground/images/train'
# # process_files_in_directory(labels_dir, images_dir)
#
# # 디렉토리 경로 설정(val)
# labels_dir = 'C:/Users/user/PycharmProjects/yolov5/whale-categorization-playground/labels/val'
# images_dir = 'C:/Users/user/PycharmProjects/yolov5/whale-categorization-playground/images/val'
# process_files_in_directory(labels_dir, images_dir)

'''5
라벨 파일에서 쉼표로 구분된 형식을 공백으로 구분되는 형식으로 변경하는 코드
'''

import os
import glob

def convert_comma_to_space_in_labels(directory_path):
    # 해당 디렉토리의 모든 .txt 파일을 찾음
    txt_files = glob.glob(os.path.join(directory_path, '*.txt'))

    for txt_file in txt_files:
        with open(txt_file, 'r') as file:
            lines = file.readlines()

        # 각 라인에서 쉼표를 공백으로 변경
        new_lines = [line.replace(',', ' ').strip() for line in lines]

        # 변경된 내용을 같은 파일에 저장
        with open(txt_file, 'w') as file:
            for line in new_lines:
                file.write(line + '\n')

# # 디렉토리 경로 설정(train)
# directory_path = 'C:/Users/user/PycharmProjects/yolov5/whale-categorization-playground/labels/train'
# convert_comma_to_space_in_labels(directory_path)

# 디렉토리 경로 설정(val)
directory_path = 'C:/Users/user/PycharmProjects/yolov5/whale-categorization-playground/labels/val'
convert_comma_to_space_in_labels(directory_path)


