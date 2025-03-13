from ultralytics import YOLO  # type: ignore
import cv2

# Train model 
"""model = YOLO("yolo11n-cls.pt")

# Train YOLO Modell with a sepecific dataset

path_dataset = "/home/dang-minh-nguyen/Repositories/Scissors Paper Rock YOLO 2/Rock-Paper-Scissors-1"
results = model.train(data=path_dataset, epochs=10, imgsz=640)"""

# Load the trained model from model runs folder
best_model_path = "/home/dang-minh-nguyen/Repositories/Scissors Paper Rock YOLO 2/runs/classify/train/weights/best.pt"



model = YOLO(best_model_path)

test_scissors_path = "/home/dang-minh-nguyen/Repositories/Scissors Paper Rock YOLO 2/test/scissor_test.jpg"
test_rock_path = "/home/dang-minh-nguyen/Repositories/Scissors Paper Rock YOLO 2/test/rock.jpeg"
test_paper_path = "/home/dang-minh-nguyen/Repositories/Scissors Paper Rock YOLO 2/test/paper.jpg"

# Predict test
test_image_path = test_paper_path

results = model(test_image_path)

# Display test image
original_img = cv2.imread(test_image_path)

cv2.imshow("Test Image", original_img)

cv2.waitKey(0)

cv2.destroyAllWindows()

