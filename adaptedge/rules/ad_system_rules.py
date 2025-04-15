from adaptedge.rules.base_rule import BaseRuleTransformation

class AgeTransformation(BaseRuleTransformation):
    def __init__(self, rules_file=None):
        super().__init__(rules_file=rules_file or "configs/ad_system_rules.json")

    def extract_key(self, data):
        return data.get("age", "default")

class GenderTransformation(BaseRuleTransformation):
    def __init__(self, rules_file=None):
        super().__init__(rules_file=rules_file or "configs/ad_system_rules.json")

    def extract_key(self, data):
        return data.get("gender", "default")

class EmotionTransformation(BaseRuleTransformation):
    def __init__(self, rules_file=None):
        super().__init__(rules_file=rules_file or "configs/ad_system_rules.json")

    def extract_key(self, data):
        return data.get("emotion", "default")