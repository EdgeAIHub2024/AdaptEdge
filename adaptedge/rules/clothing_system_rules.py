from adaptedge.rules.base_rule import BaseRuleTransformation

class SkinToneTransformation(BaseRuleTransformation):
    def __init__(self, rules_file=None):
        super().__init__(rules_file=rules_file or "configs/clothing_system_rules.json")

    def extract_key(self, data):
        return data.get("skin_tone", "default")

class BodyShapeTransformation(BaseRuleTransformation):
    def __init__(self, rules_file=None):
        super().__init__(rules_file=rules_file or "configs/clothing_system_rules.json")

    def extract_key(self, data):
        return data.get("body_shape", "default")