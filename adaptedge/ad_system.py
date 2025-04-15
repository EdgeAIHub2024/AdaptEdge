import random

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