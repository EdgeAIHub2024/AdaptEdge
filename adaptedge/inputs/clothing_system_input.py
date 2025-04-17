from adaptedge.registry import input_registry

class ClothingSystemInput:
    def __init__(self, use_camera=False, camera_index=0):
        self.use_camera = use_camera
        self.cap = None
        if use_camera:
            try:
                import cv2
                self.cap = cv2.VideoCapture(camera_index)
                if not self.cap.isOpened():
                    raise RuntimeError(f"无法打开摄像头 {camera_index}")
            except ImportError:
                raise ImportError("使用摄像头需要安装 OpenCV，请运行 `pip install opencv-python`")

    def collect_data(self):
        if self.use_camera and self.cap:
            import cv2
            ret, frame = self.cap.read()
            if not ret:
                print("读取摄像头失败，使用默认特征")
                return {
                    "skin_tone": "浅色",
                    "body_shape": "苗条"
                }
            skin_tone = "浅色"
            body_shape = "苗条"
            data = {
                "skin_tone": skin_tone,
                "body_shape": body_shape
            }
        else:
            import random
            data = {
                "skin_tone": random.choice(["浅色", "深色"]),
                "body_shape": random.choice(["苗条", "中等"])
            }
        print(f"输入数据: 肤色={data['skin_tone']}, 体型={data['body_shape']}")
        return data

    def __del__(self):
        if self.use_camera and self.cap and self.cap.isOpened():
            self.cap.release()
            print("摄像头已释放")

input_registry.register("clothing_system_input", ClothingSystemInput)