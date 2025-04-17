class AdaptEdge:
    def __init__(self, input_modules, transformation_modules, output_module, feedback_module):
        self.input_modules = input_modules
        self.transformation_modules = transformation_modules
        self.output_module = output_module
        self.feedback_module = feedback_module

    def load_config(self, config_file):
        import json
        from adaptedge.registry import input_registry, rule_registry
        with open(config_file, "r") as f:
            config = json.load(f)
        self.input_modules = []
        for mod in config["input_modules"]:
            self.input_modules.append(input_registry.get(mod["name"], **mod.get("args", {})))
        self.transformation_modules = []
        for mod in config["transformation_modules"]:
            self.transformation_modules.append(rule_registry.get(mod["name"], **mod.get("args", {})))

    def run(self, interval=1.0):
        import time
        while True:
            try:
                data = {}
                for module in self.input_modules:
                    data.update(module.collect_data())
                result = data.copy()
                for transform in self.transformation_modules:
                    result.update(transform.process(result))
                feedback = self.output_module.present(result)
                self.feedback_module.update(data, result, feedback)
                time.sleep(interval)
            except Exception as e:
                print(f"运行错误: {e}")