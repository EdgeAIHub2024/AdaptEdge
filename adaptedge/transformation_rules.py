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

class SkinToneTransformation:
    def __init__(self):
        self.rules = {
            "浅色": {"color": "粉色"},
            "深色": {"color": "深蓝"},
            "default": {"color": "白色"}
        }

    def process(self, data):
        skin_tone = data.get("skin_tone", "default")
        result = self.rules.get(skin_tone, self.rules["default"])
        print(f"肤色规则: {skin_tone} -> 颜色 {result['color']}")
        return result

class BodyShapeTransformation:
    def __init__(self):
        self.rules = {
            "苗条": {"fit": "修身款"},
            "中等": {"fit": "宽松款"},
            "default": {"fit": "默认款"}
        }

    def process(self, data):
        body_shape = data.get("body_shape", "default")
        result = self.rules.get(body_shape, self.rules["default"])
        print(f"体型规则: {body_shape} -> 版型 {result['fit']}")
        return result