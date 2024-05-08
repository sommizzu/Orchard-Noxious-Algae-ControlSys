import os
import time
import psutil
import csv
from gpiozero import CPUTemperature
from ultralytics import YOLO
import cv2

# 입력 이미지 파일 경로
image_path = '/path/to/image/test.jpg'

# 출력 이미지 파일 경로
image_path_out = '{}_out.jpg'.format(os.path.splitext(image_path)[0])

# 이미지 읽기
image = cv2.imread(image_path)

# YOLOv8 모델 파일 경로
model_path = '/path/to/model/best.pt'

# 실험 시작 시간 기록
start_time = time.time()

# 모델 로딩 시간 측정
model_loading_start = time.time()
model = YOLO(model_path)  # YOLOv8 모델 로드
model_loading_end = time.time()
model_loading_time = model_loading_end - model_loading_start

# 메모리 사용량 측정
memory_usage = psutil.Process().memory_info().rss / 1024 / 1024  # MB 단위

# 객체 탐지 신뢰도 임계값
threshold = 0.5

# 추론 시작
inference_start = time.time()
results = model(image)[0]  # 이미지에 대한 추론 수행
inference_end = time.time()
inference_time = inference_end - inference_start

# 온도 측정
cpu_temp = CPUTemperature()
temperature = cpu_temp.temperature

# 탐지된 객체 정보 반복
for result in results.boxes.data.tolist():
    # 객체의 바운딩 박스 좌표와 신뢰도, 클래스 ID 추출
    x1, y1, x2, y2, score, class_id = result

    # 신뢰도가 임계값보다 높은 경우에만 처리
    if score > threshold:
        # 바운딩 박스 그리기
        cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)

        # 클래스 이름과 신뢰도 텍스트 그리기
        cv2.putText(image, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

# 실험 종료 시간 기록
end_time = time.time()
total_time = end_time - start_time

# 결과 저장
data = [
    ['Device', 'Raspberry Pi'],
    ['Total Time (s)', total_time],
    ['Inference Time (s)', inference_time],
    ['Temperature (°C)', temperature],
    ['Memory Usage (MB)', memory_usage],
    ['Model Loading Time (s)', model_loading_time]
]

with open('experiment_results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# 객체가 탐지된 이미지 저장
cv2.imwrite(image_path_out, image)

# 모든 OpenCV 창 닫기
cv2.destroyAllWindows()