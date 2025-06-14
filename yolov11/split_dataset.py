import os
import random
import shutil

''' 
dataset/                                dataset/
├── images/                             ├── images/
│   ├── a.jpg                           │   ├── train/
│   ├── b.jpg       split into          │   ├── val/
│   └── ...             -->             ├── labels/
├── labels/                             │   ├── train/
│   ├── a.txt                           │   ├── val/
│   ├── b.txt          
│   └── ...            
'''

# Configuration
image_dir = 'D:\sf6\lb\images'  # Path to images
label_dir = 'D:\df6\lb\labels'  # Path to labels
train_ratio = 0.8  # 80% training, 20% validation

# Get all file names without extensions
filenames = [os.path.splitext(f)[0] for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png', '.jpeg'))]
random.shuffle(filenames)

# Split into train and val
train_size = int(len(filenames) * train_ratio)
train_files = filenames[:train_size]
val_files = filenames[train_size:]

# Create destination directories
for subdir in ['train', 'val']:
    os.makedirs(os.path.join(image_dir, subdir), exist_ok=True)
    os.makedirs(os.path.join(label_dir, subdir), exist_ok=True)


# Move image and label files
def move_files(file_list, target):
    for name in file_list:
        img_exts = ['.jpg', '.png', '.jpeg']
        for ext in img_exts:
            src_img = os.path.join(image_dir, name + ext)
            if os.path.exists(src_img):
                shutil.move(src_img, os.path.join(image_dir, target, name + ext))
                break
        src_label = os.path.join(label_dir, name + '.txt')
        if os.path.exists(src_label):
            shutil.move(src_label, os.path.join(label_dir, target, name + '.txt'))


# Perform file moving
move_files(train_files, 'train')
move_files(val_files, 'val')

print(f"Dataset split completed. Train: {len(train_files)}, Val: {len(val_files)}")
