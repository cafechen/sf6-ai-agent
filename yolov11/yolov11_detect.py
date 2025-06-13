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


# Load the YOLOv8 model
model = YOLO(r"best.pt")
screen_region = (26, 50, 1200, 750)


def get_box_area(box):
    # YOLO box contains (x1, y1, x2l, y2)
    x1, y1, x2, y2 = box.xyxy[0]
    width = x2 - x1
    height = y2 - y1
    return width * height, width, height


while True:
    start_time = time.time()

    screen_image = grab_screen(screen_region)

    # Convert BGRA to BGR
    screen_image = cv2.cvtColor(screen_image, cv2.COLOR_BGRA2BGR)

    results = model(screen_image, iou=0.5, conf=0.4)

    # 显示带注释的图像
    annotated_image = results[0].plot()

    cv2.imshow("YOLOv8 Inference - Screen Capture", annotated_image)

    # 按 'q' 键退出循环
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
