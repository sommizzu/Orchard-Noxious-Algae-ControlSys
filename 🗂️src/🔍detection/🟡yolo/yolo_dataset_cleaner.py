import os
import shutil

def remove_empty_labels_and_images(yolo_folder, output_folder, start_number):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    counter = start_number
    for filename in os.listdir(yolo_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(yolo_folder, filename)
            
            # 텍스트 파일이 비어있는지 확인
            if os.path.getsize(file_path) == 0:
                # 빈 텍스트 파일 삭제
                os.remove(file_path)
                
                # 해당 이미지 파일 삭제
                image_filename = os.path.splitext(filename)[0] + ".jpg"
                image_path = os.path.join(yolo_folder, image_filename)
                if os.path.exists(image_path):
                    os.remove(image_path)
            else:
                # 텍스트 파일이 비어있지 않은 경우
                new_filename = f"{counter}.txt"
                new_file_path = os.path.join(output_folder, new_filename)
                shutil.copy(file_path, new_file_path)
                
                # 해당 이미지 파일 복사
                image_filename = os.path.splitext(filename)[0] + ".jpg"
                image_path = os.path.join(yolo_folder, image_filename)
                new_image_filename = f"{counter}.jpg"
                new_image_path = os.path.join(output_folder, new_image_filename)
                shutil.copy(image_path, new_image_path)
                
                counter += 1

yolo_folder = "C:\\Users\\User\\Desktop\\yolo_labels"
output_folder = "C:\\Users\\User\\Desktop\\yolo_labels_renumbered"
start_number = 628
remove_empty_labels_and_images(yolo_folder, output_folder, start_number)