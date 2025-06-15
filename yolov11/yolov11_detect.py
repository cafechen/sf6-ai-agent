import cv2
import numpy as np
import win32gui, win32ui, win32con, win32api
from ultralytics import YOLO
import time


def grab_screen(region=None):
    hwin = win32gui.GetDesktopWindow()

    if region:
        left, top, x2, y2 = region
        width = x2 - left + 1
        height = y2 - top + 1
    else:
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)

    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.frombuffer(signedIntsArray, dtype='uint8')
    img.shape = (height, width, 4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())

    return img


# Load the YOLO model
model = YOLO(r"D:\best.pt")
model.fuse()  # Speed up forward inference
screen_region = (0, 50, 1280, 770)

start_time = time.time()

fps_list = []

while True:

    screen_image = grab_screen(screen_region)

    # Convert BGRA to BGR
    screen_image = cv2.cvtColor(screen_image, cv2.COLOR_BGRA2BGR)

    inference_image = cv2.resize(screen_image, (640, 360))

    results = model(inference_image, iou=0.5, conf=0.4)

    # show plot
    annotated_image = results[0].plot()

    end_time = time.time()

    fps = 1 / (end_time - start_time)

    fps_list.append(fps)
    if len(fps_list) > 30:
        fps_list.pop(0)

    # Calculate average FPS
    avg_fps = sum(fps_list) / len(fps_list)

    # Draw FPS on the image
    cv2.putText(annotated_image, f"FPS: {avg_fps:.2f}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("YOLOv11 Inference - Screen Capture", annotated_image)

    # Press 'q' key to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    start_time = time.time()

cv2.destroyAllWindows()
