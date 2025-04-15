class AgeTransformation:
    def __init__(self):
        self.rules = {
            "20-30": {"product_type": "时尚产品"},
            "30-40": {"product_type": "实用产品"},
            "40-50": {"product_type": "高端产品"},
            "default": {"product_type": "默认产品"}
        }

    def process(self, data):
        age = data.get("age", "default")
        result = self.rules.get(age, self.rules["default"])
        print(f"年龄规则: {age} -> 产品类型 {result['product_type']}")
        return result

class GenderTransformation:
    def __init__(self):
        self.rules = {
            "男": {"style": "运动风格"},
            "女": {"style": "优雅风格"},
            "default": {"style": "默认风格"}
        }

    def process(self, data):
        gender = data.get("gender", "default")
        result = self.rules.get(gender, self.rules["default"])
        print(f"性别规则: {gender} -> 风格 {result['style']}")
        return result

class EmotionTransformation:
    def __init__(self):
        self.rules = {
            "开心": {"content": "正能量广告"},
            "难过": {"content": "治愈广告"},
            "平静": {"content": "常规广告"},
            "default": {"content": "默认广告"}
        }

    def process(self, data):
        emotion = data.get("emotion", "default")
        result = self.rules.get(emotion, self.rules["default"])
        print(f"情绪规则: {emotion} -> 内容 {result['content']}")
        return result