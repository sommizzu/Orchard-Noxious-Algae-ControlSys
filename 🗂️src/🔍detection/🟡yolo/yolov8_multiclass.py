!pip install opencv-python>=4.6.0
!pip install ultralytics

import torch

print("CUDA Available: ", torch.cuda.is_available())
print("Number of GPUs: ", torch.cuda.device_count())
print("Current GPU: ", torch.cuda.current_device())
print("GPU Name: ", torch.cuda.get_device_name(torch.cuda.current_device()))

# CUDA 사용 확인
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print("Using device:", device)

from ultralytics import YOLO

data_yaml = """
train: /home/work/Bird/final_data_undersampling/train/images
val: /home/work/Bird/final_data_undersampling/valid/images

nc: 7  # number of classes
names: ['fire', 'smoke', 'human', 'boar', 'vehicle', 'license plate', 'bird']  # class names
"""

with open('bird_data.yaml', 'w') as file:
    file.write(data_yaml)

# 모델 로드
model_n = YOLO('yolov8n.pt')  # 사전 학습된 모델 로드

# 모델 학습
results_n = model_n.train(data='bird_data.yaml', epochs=50, project='results', name='yolov8n')  # 데이터셋 경로 및 학습 에포크 설정

# 모델 검증
results_n = model_n.val()

# 최적 가중치 파일을 로드하여 모델 사용
best_model_n = YOLO('results/yolov8n/weights/best.pt')

# ONNX 형식으로 내보내기
best_model_n.export(format='onnx')

# TFLite 형식으로 내보내기
best_model_n.export(format='tflite')

# 모델 로드
model_s = YOLO('yolov8s.pt')  # 사전 학습된 모델 로드

# 모델 학습
results_s = model_s.train(data='bird_data.yaml', epochs=50, project='results', name='yolov8s')  # 데이터셋 경로 및 학습 에포크 설정

# 모델 검증
results_s = model_s.val()

# 최적 가중치 파일을 로드하여 모델 사용
best_model_s = YOLO('results/yolov8s/weights/best.pt')

# ONNX 형식으로 내보내기
best_model_s.export(format='onnx')

# TFLite 형식으로 내보내기
best_model_s.export(format='tflite')

# 모델 로드
model_m = YOLO('yolov8m.pt')  # 사전 학습된 모델 로드

# 모델 학습
results_m = model_m.train(data='bird_data.yaml', epochs=50, project='results', name='yolov8m')  # 데이터셋 경로 및 학습 에포크 설정

# 모델 검증
results_m = model_m.val()

# 최적 가중치 파일을 로드하여 모델 사용
best_model_m = YOLO('results/yolov8m/weights/best.pt')

# ONNX 형식으로 내보내기
best_model_m.export(format='onnx')

# TFLite 형식으로 내보내기
best_model_m.export(format='tflite')

