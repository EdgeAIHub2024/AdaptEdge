import random

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
            import cv2
            ret, frame = self.cap.read()
            if not ret:
                print("读取摄像头失败，使用默认特征")
                return {
                    "age": "20-30",
                    "gender": "男",
                    "emotion": "开心"
                }
            age = "20-30"
            gender = "男"
            emotion = "开心"
            data = {
                "age": age,
                "gender": gender,
                "emotion": emotion
            }
        else:
            import random
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

class AdSystemOutput:
    def present(self, result):
        product_type = result.get("product_type", "默认产品")
        style = result.get("style", "默认风格")
        content = result.get("content", "默认广告")
        recommendation = f"{product_type} {style} {content}"
        print(f"输出推荐: {recommendation}")
        stay_time = random.uniform(0, 10)
        return {"stay_time": stay_time}

class AdSystemFeedback:
    def __init__(self, threshold=5.0):
        self.threshold = threshold
        self.weights = {}

    def update(self, data, result, feedback):
        rule_key = f"{data.get('age', 'default')}_{data.get('gender', 'default')}_{data.get('emotion', 'default')}"
        stay_time = feedback["stay_time"]
        self.weights[rule_key] = self.weights.get(rule_key, 1.0)
        if stay_time > self.threshold:
            self.weights[rule_key] += 0.1
        else:
            self.weights[rule_key] -= 0.05
        print(f"反馈更新: 用户停留时间 {stay_time:.2f} 秒，规则 '{rule_key}' 权重调整到 {self.weights[rule_key]:.2f}")