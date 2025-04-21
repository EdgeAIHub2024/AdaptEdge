class ModuleRegistry:
    def __init__(self):
        self.modules = {}

    def register(self, name, module_class):
        self.modules[name] = module_class

    def get(self, name, **kwargs):
        module_class = self.modules.get(name)
        if not module_class:
            raise ValueError(f"模块 {name} 未注册")
        return module_class(**kwargs)

input_registry = ModuleRegistry()
rule_registry = ModuleRegistry()
output_registry = ModuleRegistry()
feedback_registry = ModuleRegistry()