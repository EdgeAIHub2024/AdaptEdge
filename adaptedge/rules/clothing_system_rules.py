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