from adaptedge.rules.base_rule import BaseRuleTransformation
from adaptedge.registry import rule_registry
import joblib
import pandas as pd

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

class MLTransformation(BaseRuleTransformation):
    def __init__(self):
        self.model = joblib.load("models/ad_classifier.pkl")
        self.model_features = self.model.feature_names_in_  # 模型期望的特征

    def process(self, data):
        # 提取用户特征
        features = {
            "age": data.get("age", "default"),
            "gender": data.get("gender", "default"),
            "emotion": data.get("emotion", "default")
        }
        # 转换为模型输入
        X = pd.get_dummies(pd.DataFrame([features]))
        # 确保特征对齐
        X = X.reindex(columns=self.model_features, fill_value=0)
        # 预测
        prediction = self.model.predict(X)[0]
        # 解析预测结果
        product_type, style, content = prediction.split("_")
        result = {
            "product_type": product_type,
            "style": style,
            "content": content
        }
        print(f"AI 规则匹配: MLTransformation -> {features} -> {result}")
        return result

rule_registry.register("ad_system.age", AgeTransformation)
rule_registry.register("ad_system.gender", GenderTransformation)
rule_registry.register("ad_system.emotion", EmotionTransformation)
rule_registry.register("ad_system.ml", MLTransformation)