from ultralytics import YOLO

# Load a pretrained YOLO11l model
model = YOLO("yolo11l.pt")

# Train the model on the COCO8 dataset for 100 epochs
train_results = model.train(
    data="~/dataset/data.yaml",  # Path to dataset configuration file
    epochs=200,  # Number of training epochs
    imgsz=640,  # Image size for training
    device=[0],  # Device to run on (e.g., 'cpu', 0, [0,1,2,3])
    workers=0, # Number of worker threads for data loading. Higher values can speed up data preprocessing but may increase CPU usage. Setting to 0 uses main thread, which can be more stable in some environments.
    batch=32, # Specifies export model batch inference size or the maximum number of images the exported model will process concurrently in predict mode. For Edge TPU exports, this is automatically set to 1.
    cache=True, # Enables caching of dataset images in memory (True/ram), on disk (disk), or disables it (False). Improves training speed by reducing disk I/O at the cost of increased memory usage.
    save_period=10, # Frequency of saving model checkpoints, specified in epochs. A value of -1 disables this feature. Useful for saving interim models during long training sessions.
    project='~/dataset/training_output',  # Name of the project directory where training outputs are saved. Allows for organized storage of different experiments.
    name='yolo11l_sf6'  # Name of the training run. Used for creating a subdirectory within the project folder, where training logs and outputs are stored.
)
