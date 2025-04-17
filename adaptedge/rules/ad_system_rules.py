from adaptedge.rules.base_rule import BaseRuleTransformation
from adaptedge.registry import rule_registry

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

rule_registry.register("ad_system.age", AgeTransformation)
rule_registry.register("ad_system.gender", GenderTransformation)
rule_registry.register("ad_system.emotion", EmotionTransformation)