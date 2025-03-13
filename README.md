# Predict Rock Paper Scissors using YOLO

## Load the data from robflox

```bash
    python load_data.py
```

## For first time, train the YOLO model with custome dataset

- Uncomment this part to train model

```bash
    """model = YOLO("yolo11n-cls.pt")

    # Train YOLO Modell with a sepecific dataset

    path_dataset = "/home/dang-minh-nguyen/Repositories/Scissors Paper Rock YOLO 2/Rock-Paper-Scissors-1"
    results = model.train(data=path_dataset, epochs=10, imgsz=640)"""
```

## Run the model to predict

- Change the path of the test image

```bash
    test_scissors_path = "/home/dang-minh-nguyen/Repositories/Scissors Paper Rock YOLO 2/test/scissor_test.jpg"
    test_rock_path = "/home/dang-minh-nguyen/Repositories/Scissors Paper Rock YOLO 2/test/rock.jpeg"
    test_paper_path = "/home/dang-minh-nguyen/Repositories/Scissors Paper Rock YOLO 2/test/paper.jpg"

    # Predict test
    test_image_path = test_paper_path
```

## Results

- Sample Result:

```bash
    image 1/1 /home/dang-minh-nguyen/Repositories/Scissors Paper Rock YOLO 2/test/paper.jpg: 640x640 paper 0.59, scissors 0.38, rock 0.03, 61.7ms
    Speed: 26.7ms preprocess, 61.7ms inference, 0.0ms postprocess per image at shape (1, 3, 640, 640)
```

- This is the predicted probability, look at the predicted rate of the image, the class with the highest predicted probability will be the selected class