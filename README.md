# sf6-ai-agent
StreetFighter6 AI Agent

##  Installation
```bash
conda create -n sf6 python=3.9
conda activate sf6
python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128  # based on your cuda version
python -m pip install -r requirements.txt
```

##  Train/Inference
- use the script in "yolov11" folder for training and inference
- the base model is yolo11l.pt

## Models&Datasets
- Model: [streetfighter6](https://www.kaggle.com/models/cafechen/streetfighter6)
- Datasets: [streetfighter6](https://www.kaggle.com/datasets/cafechen/streetfighter6)

## Contact Me
📱 WeChat: stevenchen945 
💬 QQ:     45958905

## ffmpeg 
```shell
# Merge steam video files
ffmpeg -protocol_whitelist "file,http,https,tcp,tls" -i session.mpd -c copy bg_1364780_20250610_154512.mp4
# video to image command
ffmpeg -i .\bg_1364780_20250610_154512-01.mp4 bg_1364780_20250610_154512\bg_1364780_20250610_154512_%06d.png
# Capture video clips
ffmpeg -ss 00:12:45 -to 00:22:43 -i .\bg_1364780_20250610_154512.mp4 -c copy bg_1364780_20250610_154512-01.mp4
```

<img src="assets/show.png" width="360" />
