import json
import random
import os

# 获取项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class AdSystemInput:
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
            ret, frame = self.cap.read()
            if not ret:
                print("读取摄像头失败，使用默认特征")
                return {"age": "未知", "gender": "未知", "emotion": "未知"}
            data = {
                "age": random.choice(["20-30", "30-40", "40-50"]),
                "gender": random.choice(["男", "女"]),
                "emotion": random.choice(["开心", "难过", "平静"])
            }
        else:
            data = {
                "age": random.choice(["20-30", "30-40", "40-50"]),
                "gender": random.choice(["男", "女"]),
                "emotion": random.choice(["开心", "难过", "平静"])
            }
        print(f"输入数据: 年龄={data['age']}, 性别={data['gender']}, 情绪={data['emotion']}")
        return data

    def __del__(self):
        if self.use_camera and self.cap and self.cap.isOpened():
            self.cap.release()
            print("摄像头已释放")

class AdSystemTransformation:
    def __init__(self, rules_file=os.path.join(BASE_DIR, "configs", "ad_system_rules.json")):
        with open(rules_file, "r", encoding="utf-8") as f:
            self.rules = json.load(f)

    def process(self, data):
        key = f"{data['age']}_{data['gender']}_{data['emotion']}"
        result = self.rules.get(key, self.rules["default"])
        print(f"转换结果: 匹配规则 '{key}'")
        return result

class AdSystemOutput:
    def present(self, result):
        print(f"输出推荐: {result['description']} (ID: {result['ad_id']})")
        stay_time = random.uniform(0, 10)
        return {"stay_time": stay_time}

class AdSystemFeedback:
    def __init__(self, threshold=5.0):
        self.threshold = threshold
        self.weights = {}

    def update(self, data, result, feedback):
        key = f"{data['age']}_{data['gender']}_{data['emotion']}"
        stay_time = feedback["stay_time"]
        if stay_time > self.threshold:
            self.weights[key] = self.weights.get(key, 1.0) + 0.1
            print(f"反馈更新: 用户停留时间 {stay_time:.2f} 秒，规则 '{key}' 权重增加到 {self.weights[key]:.2f}")
        else:
            self.weights[key] = max(self.weights.get(key, 1.0) - 0.05, 0.1)
            print(f"反馈更新: 用户停留时间 {stay_time:.2f} 秒，规则 '{key}' 权重减少到 {self.weights[key]:.2f}")