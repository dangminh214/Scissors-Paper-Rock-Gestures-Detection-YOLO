from ultralytics import YOLO  
import cv2 

model_path = "./update_modell.onnx"

model = YOLO(model_path)
cap = cv2.VideoCapture(0)

# Display Window setup
WINDOW_NAME = "YOLO Inference"
cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)  
cv2.resizeWindow(WINDOW_NAME, 1280, 720)  

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break  

    results = model(frame)
    result = results[0]

    annotated_frame = result.plot() 
    cv2.imshow(WINDOW_NAME, annotated_frame)
    
    # ASCII Code of Esc Button
    if cv2.waitKey(1) == 27: 
        break

cap.release()
cv2.destroyAllWindows()
