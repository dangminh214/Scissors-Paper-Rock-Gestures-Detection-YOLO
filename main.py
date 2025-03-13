from ultralytics import YOLO # type: ignore
import cv2 # type: ignore

model_path = "/home/dang-minh-nguyen/Repositories/Scissors Paper Rock YOLO 2/runs/detect/train3/weights/best.onnx"

model = YOLO(model_path)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break  

    results = model(frame)
    result = results[0]

    annotated_frame = result.plot() 
    cv2.imshow('YOLO Inference', annotated_frame)
    
    # ASCII Code of Esc
    if cv2.waitKey(1) == 27: 
        break

cap.release()
cv2.destroyAllWindows()
