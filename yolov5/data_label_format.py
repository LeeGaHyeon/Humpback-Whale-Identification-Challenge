''' 3
프로젝트 디렉토리에서 라벨 파일을 처리하고 각 이미지에 대해 지정된 형식으로 개별 .txt 파일을 생성하는 코드
'''

'''
train.txt
'''
import os

def process_label_file(input_file_path):
    # 입력 파일 경로에서 디렉토리를 구하기 위해 경로를 분할
    base_dir = os.path.dirname(input_file_path)

    with open(input_file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            data = line.strip().split(',')
            # 이미지 이름 추출 후 .jpg 확장자 제거
            image_name = data[0].split('.')[0]
            # 해당하는 .txt 파일 이름 생성
            txt_filename = os.path.join(base_dir, image_name + '.txt')

            with open(txt_filename, 'w') as txt_file:
                # 클래스 라벨 '0'과 나머지 데이터를 작성
                txt_file.write('0,' + ','.join(data[1:]))

# 실제 파일 경로로 이 부분을 교체하세요
input_file_path = 'C:/Users/user/PycharmProjects/yolov5/whale-categorization-playground/labels/train/train.txt'
process_label_file(input_file_path)

# '''
# val.txt
# '''
# import os
#
# def process_label_file(input_file_path):
#     # 입력 파일 경로에서 디렉토리를 구하기 위해 경로를 분할
#     base_dir = os.path.dirname(input_file_path)
#
#     with open(input_file_path, 'r') as file:
#         lines = file.readlines()
#
#         for line in lines:
#             data = line.strip().split(',')
#             # 이미지 이름 추출 후 .jpg 확장자 제거
#             image_name = data[0].split('.')[0]
#             # 해당하는 .txt 파일 이름 생성
#             txt_filename = os.path.join(base_dir, image_name + '.txt')
#
#             with open(txt_filename, 'w') as txt_file:
#                 # 클래스 라벨 '0'과 나머지 데이터를 작성
#                 txt_file.write('0,' + ','.join(data[1:]))
#
# # 실제 파일 경로로 이 부분을 교체하세요
# input_file_path = 'C:/Users/user/PycharmProjects/yolov5/whale-categorization-playground/labels/val/val.txt'
# process_label_file(input_file_path)
