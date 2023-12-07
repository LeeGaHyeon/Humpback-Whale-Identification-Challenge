''' 1
cropping.txt 파일 읽기: 이 파일에서 이미지 파일 이름을 파싱하여 리스트로 저장합니다.
폴더에서 이미지 삭제: train 및 test 폴더를 탐색하여 cropping.txt에 없는 이미지 파일을 삭제합니다.
먼저, cropping.txt 파일을 읽고 이미지 파일 이름을 리스트로 저장하는 코드를 작성하겠습니다. 이 리스트를 사용하여 train 및 test 폴더 내의 파일과 비교하고, 리스트에 없는 파일을 삭제할 것입니다.
'''
import os

# cropping.txt 파일에서 이미지 이름을 추출하는 함수
def get_image_names_from_cropping(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    image_names = [line.split(',')[0] for line in lines]
    return set(image_names)

# 특정 폴더에서 cropping.txt에 없는 이미지 삭제하는 함수
def delete_unlisted_images(folder_path, listed_images):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.jpg') and file_name not in listed_images:
            os.remove(os.path.join(folder_path, file_name))

# cropping.txt 파일의 경로
cropping_file_path = 'C:/Users/user/PycharmProjects/yolov5/whale-categorization-playground/cropping.txt'

# 이미지 이름 리스트 가져오기
listed_images = get_image_names_from_cropping(cropping_file_path)

# train 폴더에서 불필요한 이미지 삭제
train_folder_path = 'C:/Users/user/PycharmProjects/yolov5/whale-categorization-playground/train'
delete_unlisted_images(train_folder_path, listed_images)

# test 폴더에서 불필요한 이미지 삭제
test_folder_path = 'C:/Users/user/PycharmProjects/yolov5/whale-categorization-playground/test'
delete_unlisted_images(test_folder_path, listed_images)
