class BaseRuleTransformation:
    def __init__(self, rules=None, rules_file=None, default_key="default"):
        self.default_key = default_key
        if rules_file:
            import json
            with open(rules_file, "r") as f:
                rules_data = json.load(f)
                self.rules = rules_data.get(self.__class__.__name__.lower(), {})
        else:
            self.rules = rules or {}

    def process(self, data):
        key = self.extract_key(data)
        result = self.rules.get(key, self.rules.get(self.default_key, {}))
        print(f"规则匹配: {self.__class__.__name__} -> {key} -> {result}")
        return result

    def extract_key(self, data):
        raise NotImplementedError("子类必须实现 extract_key 方法")