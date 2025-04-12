import json
import random
import numpy as np
import os

# 获取项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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
                return {"skin_tone": "未知", "body_shape": "未知"}
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            avg_hsv = np.mean(hsv, axis=(0, 1))
            skin_tone = "浅色" if avg_hsv[2] > 150 else "深色"
            body_shape = random.choice(["苗条", "中等", "偏重"])
            data = {"skin_tone": skin_tone, "body_shape": body_shape}
        else:
            data = {
                "skin_tone": random.choice(["浅色", "深色"]),
                "body_shape": random.choice(["苗条", "中等", "偏重"])
            }
        print(f"输入数据: 肤色={data['skin_tone']}, 体型={data['body_shape']}")
        return data

    def __del__(self):
        if self.use_camera and self.cap and self.cap.isOpened():
            self.cap.release()
            print("摄像头已释放")

class ClothingSystemTransformation:
    def __init__(self, rules_file=os.path.join(BASE_DIR, "configs", "clothing_system_rules.json")):
        with open(rules_file, "r", encoding="utf-8") as f:
            self.rules = json.load(f)

    def process(self, data):
        key = f"{data['skin_tone']}_{data['body_shape']}"
        result = self.rules.get(key, self.rules["default"])
        print(f"转换结果: 匹配规则 '{key}'")
        return result

class ClothingSystemOutput:
    def present(self, result):
        print(f"输出推荐: {result['description']} (ID: {result['clothing_id']})")
        user_score = random.randint(1, 5)
        return {"user_score": user_score}

class ClothingSystemFeedback:
    def __init__(self, score_threshold=3):
        self.threshold = score_threshold
        self.weights = {}

    def update(self, data, result, feedback):
        key = f"{data['skin_tone']}_{data['body_shape']}"
        user_score = feedback["user_score"]
        if user_score >= self.threshold:
            self.weights[key] = self.weights.get(key, 1.0) + 0.1
            print(f"反馈更新: 用户评分 {user_score} 分，规则 '{key}' 权重增加到 {self.weights[key]:.2f}")
        else:
            self.weights[key] = max(self.weights.get(key, 1.0) - 0.05, 0.1)
            print(f"反馈更新: 用户评分 {user_score} 分，规则 '{key}' 权重减少到 {self.weights[key]:.2f}")