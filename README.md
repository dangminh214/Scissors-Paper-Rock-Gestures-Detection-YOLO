# YOLO Realtime predicts Rcok-Paper-Scissors gesture

## Requirements

- All dependecies are included in requirements.txt
- To install depencies

```bash
    pip install -r requirements.txt
```

## Files Details

### notebook.ipynb

- Notebool file to train YOLO model with custom dataset. which is loaded from roboflox
- Export model as an onnx file to use in python file

### main.py

- Python file which runs webcam and detects gestures using exported YOLO model from notebook
- To run python file:

```bash
    python main.py
```

## Sample Images

![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
