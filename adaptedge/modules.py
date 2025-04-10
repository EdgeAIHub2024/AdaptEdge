import json
import random

# 输入模块：模拟用户特征采集
class AdInput:
    def collect_data(self):
        return {
            "age": random.choice(["20-30", "30-40", "40-50"]),
            "gender": random.choice(["male", "female"]),
            "emotion": random.choice(["happy", "neutral", "sad"])
        }

# 转换模块：基于规则推荐广告
class AdTransformation:
    def __init__(self, rules_file="rules.json"):
        with open(rules_file, "r") as f:
            self.rules = json.load(f)

    def process(self, data):
        key = f"{data['age']}_{data['gender']}_{data['emotion']}"
        return self.rules.get(key, {"ad_id": "default", "description": "默认广告"})

# 输出模块：显示广告并模拟反馈
class AdOutput:
    def present(self, result):
        print(f"推荐广告: {result['description']} (ID: {result['ad_id']})")
        stay_time = random.uniform(0, 10)
        print(f"用户停留时间: {stay_time:.2f} 秒")
        return {"stay_time": stay_time}

# 反馈模块：根据停留时间调整权重
class AdFeedback:
    def __init__(self, threshold=5.0):
        self.threshold = threshold
        self.weights = {}

    def update(self, data, result, feedback):
        key = f"{data['age']}_{data['gender']}_{data['emotion']}"
        if feedback["stay_time"] > self.threshold:
            self.weights[key] = self.weights.get(key, 1.0) + 0.1
            print(f"规则 '{key}' 权重增加到 {self.weights[key]:.2f}")
        else:
            self.weights[key] = max(self.weights.get(key, 1.0) - 0.05, 0.1)
            print(f"规则 '{key}' 权重减少到 {self.weights[key]:.2f}")