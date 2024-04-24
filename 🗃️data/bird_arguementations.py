import torch
from torchvision import transforms
from PIL import Image
import os
from tqdm import tqdm  
# 이미지 변환을 위한 Transform 객체 생성
transform = transforms.Compose([
    transforms.Grayscale(num_output_channels=1),  # 흑백 변환
    transforms.ColorJitter(brightness=0.5, contrast=0.5, saturation=0.5, hue=0.5),  # 색상 변화
    transforms.RandomAffine(translate=(0.2, 0.2), scale=(0.8, 1.2)),  # 이동, 크기 조정
    transforms.RandomHorizontalFlip(),  # 좌우 반전
    transforms.RandomVerticalFlip(),  # 상하 반전
])

# 원본 새 ~
input_dir = 'C:/Users/User/Desktop/yolo_labels'

# 깜깜해질 새 .. 
output_dir = 'C:/Users/User/Desktop/yolo_labels'

# 폴더 만들기
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 입력 폴더의 모든 이미지 파일 반복 적용
for filename in tqdm(os.listdir(input_dir)):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # 이미지 가져오기
        image_path = os.path.join(input_dir, filename)
        image = Image.open(image_path)

        # 데이터 증강
        augmented_image = transform(image)

        # 증강 이미지 저장
        save_path = os.path.join(output_dir, f'augmented_{filename}')
        augmented_image.save(save_path)