import random

class ClothingSystemOutput:
    def present(self, result):
        # 适配多规则输出
        color = result.get("color", "白色")
        fit = result.get("fit", "默认款")
        recommendation = f"{color} {fit}上衣"
        print(f"输出推荐: {recommendation}")
        rating = random.randint(1, 5)
        return {"rating": rating}

class ClothingSystemFeedback:
    def __init__(self, threshold=3):
        self.threshold = threshold
        self.weights = {}

    def update(self, data, result, feedback):
        rule_key = f"{data.get('skin_tone', 'default')}_{data.get('body_shape', 'default')}"
        rating = feedback["rating"]
        self.weights[rule_key] = self.weights.get(rule_key, 1.0)
        if rating > self.threshold:
            self.weights[rule_key] += 0.1
        else:
            self.weights[rule_key] -= 0.05
        print(f"反馈更新: 用户评分 {rating} 分，规则 '{rule_key}' 权重调整到 {self.weights[rule_key]:.2f}")