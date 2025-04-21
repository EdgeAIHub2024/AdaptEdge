import click
import os
import json
import shutil
import importlib
from adaptedge.core import AdaptEdge
from adaptedge.registry import input_registry, rule_registry, output_registry, feedback_registry

@click.group()
def cli():
    """AdaptEdge CLI: 轻量嵌入式 AI 框架"""
    pass

@cli.command()
@click.argument("system")
def init(system):
    """初始化系统模板（例如 adaptedge init clothing_system）"""
    template_config = f"adaptedge/templates/{system}_config.json"
    target_dir = f"apps/{system}"
    target_config = f"{target_dir}/config.json"
    target_script = f"{target_dir}/{system}.py"
    
    if not os.path.exists(template_config):
        click.echo(f"错误：系统 {system} 的模板不存在！可用模板：{get_available_templates()}")
        return
    
    os.makedirs(target_dir, exist_ok=True)
    shutil.copy(template_config, target_config)
    
    example_code = f"""from adaptedge.core import AdaptEdge
system = AdaptEdge(config_path="apps/{system}/config.json")
system.run(interval=2.0)
"""
    with open(target_script, "w") as f:
        f.write(example_code)
    
    click.echo(f"初始化 {system} 完成！配置文件: {target_config}，示例: {target_script}")

@cli.command()
@click.argument("system")
@click.option("--force", is_flag=True, help="强制覆盖已存在的应用")
def create(system, force):
    """创建新应用（例如 adaptedge create retail_system）"""
    # 目录和文件路径设置
    template_config = "adaptedge/templates/base_config.json"
    target_dir = f"apps/{system}"
    target_config = f"{target_dir}/config.json"
    target_script = f"{target_dir}/{system}.py"
    module_dir = f"adaptedge/{system}"
    rules_file = f"{target_dir}/rules.json"
    
    # 检查目录和文件是否已存在
    if os.path.exists(target_config) and not force:
        click.echo(f"错误：应用 {system} 已存在！使用 --force 选项覆盖或选择其他名称。")
        return
    
    # 检查模板目录是否存在
    if not os.path.exists("adaptedge/templates"):
        os.makedirs("adaptedge/templates", exist_ok=True)
        click.echo("注意：已创建模板目录 adaptedge/templates")
    
    # 检查并创建基础模板文件
    if not os.path.exists(template_config):
        base_config = {
            "input_modules": [
                {"name": "{{system}}_input", "args": {}}
            ],
            "transformation_modules": [
                {"name": "{{system}}.rule", "args": {}}
            ],
            "output_module": {"name": "{{system}}_output", "args": {}},
            "feedback_module": {"name": "{{system}}_feedback", "args": {}}
        }
        os.makedirs(os.path.dirname(template_config), exist_ok=True)
        with open(template_config, "w") as f:
            json.dump(base_config, f, indent=4)
        click.echo(f"注意：已创建基础模板 {template_config}")
    
    # 加载并替换模板
    try:
        with open(template_config) as f:
            config = json.load(f)
        config_str = json.dumps(config, indent=4).replace("{{system}}", system)
        config = json.loads(config_str)
    except Exception as e:
        click.echo(f"错误：加载模板失败: {e}")
        return
    
    # 创建目录
    os.makedirs(target_dir, exist_ok=True)
    os.makedirs(module_dir, exist_ok=True)
    
    # 保存配置文件
    with open(target_config, "w") as f:
        json.dump(config, f, indent=4)
    
    # 生成示例代码
    example_code = f"""from adaptedge.core import AdaptEdge

def main():
    system = AdaptEdge(config_path="apps/{system}/config.json")
    system.run(interval=2.0)

if __name__ == "__main__":
    main()
"""
    with open(target_script, "w") as f:
        f.write(example_code)
    
    # 生成模块代码 - 确保导入路径正确
    init_code = f"""# {system} 模块定义
from adaptedge.registry import input_registry, rule_registry, output_registry, feedback_registry

# 导入实现类
from adaptedge.{system}.inputs import {system.capitalize()}Input
from adaptedge.{system}.rules import {system.capitalize()}Rule
from adaptedge.{system}.outputs import {system.capitalize()}Output
from adaptedge.{system}.feedback import {system.capitalize()}Feedback

# 注册模块
input_registry.register("{system}_input", {system.capitalize()}Input)
rule_registry.register("{system}.rule", {system.capitalize()}Rule)
output_registry.register("{system}_output", {system.capitalize()}Output)
feedback_registry.register("{system}_feedback", {system.capitalize()}Feedback)

print(f"已加载 {system} 模块")
"""
    # 创建__init__.py文件
    with open(f"{module_dir}/__init__.py", "w") as f:
        f.write(init_code)
    
    # 确保必要的基类存在
    ensure_base_classes_exist()
    
    # 创建inputs.py文件
    inputs_code = f"""# {system} 输入模块
from adaptedge.base.input import BaseInput

class {system.capitalize()}Input(BaseInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f"{system.capitalize()}Input 已初始化，配置: {{kwargs}}")
        
    def collect_data(self):
        print(f"{system.capitalize()} 正在采集数据...")
        # 返回示例数据
        return {{"source": "{system}", "data_type": "sample"}}
"""
    with open(f"{module_dir}/inputs.py", "w") as f:
        f.write(inputs_code)
    
    # 创建rules.py文件
    rules_code = f"""# {system} 规则模块
from adaptedge.base.rule import BaseRuleTransformation
import json
import os

class {system.capitalize()}Rule(BaseRuleTransformation):
    def __init__(self, rules_file=None, **kwargs):
        rules_path = rules_file or os.path.join("apps", "{system}", "rules.json")
        super().__init__(rules_file=rules_path, **kwargs)
        print(f"{system.capitalize()}Rule 已初始化，规则文件: {{rules_path}}")
    
    def extract_key(self, data):
        print(f"处理数据: {{data}}")
        # 使用可能存在的data_type字段，或者默认值
        return data.get("data_type", "default")
"""
    with open(f"{module_dir}/rules.py", "w") as f:
        f.write(rules_code)
    
    # 创建outputs.py文件
    outputs_code = f"""# {system} 输出模块
from adaptedge.base.output import BaseOutput
import random

class {system.capitalize()}Output(BaseOutput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print(f"{system.capitalize()}Output 已初始化，配置: {{kwargs}}")
        
    def output(self, data):
        print(f"{system.capitalize()} 输出结果: {{data}}")
        # 返回模拟反馈
        return {{"success": True, "user_reaction": random.choice(["positive", "neutral", "negative"])}}
"""
    with open(f"{module_dir}/outputs.py", "w") as f:
        f.write(outputs_code)
    
    # 创建feedback.py文件
    feedback_code = f"""# {system} 反馈模块
from adaptedge.base.feedback import BaseFeedback

class {system.capitalize()}Feedback(BaseFeedback):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.metrics = {{}}
        print(f"{system.capitalize()}Feedback 已初始化，配置: {{kwargs}}")
    
    def process_feedback(self, feedback):
        print(f"{system.capitalize()} 处理反馈: {{feedback}}")
        # 更新指标
        reaction = feedback.get("user_reaction", "neutral")
        self.metrics[reaction] = self.metrics.get(reaction, 0) + 1
        print(f"当前指标: {{self.metrics}}")
        return {{"updated": True, "metrics": self.metrics}}
"""
    with open(f"{module_dir}/feedback.py", "w") as f:
        f.write(feedback_code)
    
    # 生成规则文件
    rules = {
        "default": {"recommendation": "默认推荐", "action": "default_action"},
        "sample": {"recommendation": f"示例{system}推荐", "action": "sample_action"}
    }
    with open(rules_file, "w") as f:
        json.dump(rules, f, indent=4)
    
    # 更新adaptedge/__init__.py以自动导入新模块
    update_main_init(system)
    
    # 运行时测试
    click.echo(f"创建 {system} 完成！配置文件: {target_config}，示例: {target_script}，模块: {module_dir}，规则: {rules_file}")
    click.echo(f"现在可以运行: adaptedge run {system}")

def ensure_base_classes_exist():
    """确保所有必要的基类都存在"""
    # 确保base目录存在
    os.makedirs("adaptedge/base", exist_ok=True)
    
    # 确保input基类存在
    if not os.path.exists("adaptedge/base/input.py"):
        with open("adaptedge/base/input.py", "w") as f:
            f.write("""class BaseInput:
    \"\"\"
    输入模块基类
    
    所有输入模块都应该继承这个类并实现collect_data方法
    \"\"\"
    
    def __init__(self, **kwargs):
        \"\"\"
        初始化输入模块
        
        Args:
            **kwargs: 配置参数
        \"\"\"
        self.config = kwargs
    
    def collect_data(self):
        \"\"\"
        采集数据
        
        Returns:
            dict: 采集到的数据
        
        Raises:
            NotImplementedError: 子类必须实现这个方法
        \"\"\"
        raise NotImplementedError("子类必须实现 collect_data 方法")
""")
    
    # 确保output基类存在
    if not os.path.exists("adaptedge/base/output.py"):
        with open("adaptedge/base/output.py", "w") as f:
            f.write("""class BaseOutput:
    \"\"\"
    输出模块基类
    
    所有输出模块都应该继承这个类并实现output方法
    \"\"\"
    
    def __init__(self, **kwargs):
        \"\"\"
        初始化输出模块
        
        Args:
            **kwargs: 配置参数
        \"\"\"
        self.config = kwargs
    
    def output(self, data):
        \"\"\"
        输出数据
        
        Args:
            data (dict): 要输出的数据
            
        Returns:
            dict: 输出结果
            
        Raises:
            NotImplementedError: 子类必须实现这个方法
        \"\"\"
        raise NotImplementedError("子类必须实现 output 方法")
""")
    
    # 确保feedback基类存在
    if not os.path.exists("adaptedge/base/feedback.py"):
        with open("adaptedge/base/feedback.py", "w") as f:
            f.write("""class BaseFeedback:
    \"\"\"
    反馈处理模块基类
    
    所有反馈处理模块都应该继承这个类并实现process_feedback方法
    \"\"\"
    
    def __init__(self, **kwargs):
        \"\"\"
        初始化反馈处理模块
        
        Args:
            **kwargs: 配置参数
        \"\"\"
        self.config = kwargs
    
    def process_feedback(self, feedback):
        \"\"\"
        处理反馈数据
        
        Args:
            feedback (dict): 反馈数据
            
        Returns:
            dict: 处理结果
            
        Raises:
            NotImplementedError: 子类必须实现这个方法
        \"\"\"
        raise NotImplementedError("子类必须实现 process_feedback 方法")
""")
    
    # 确保rule基类存在
    if not os.path.exists("adaptedge/base/rule.py"):
        with open("adaptedge/base/rule.py", "w") as f:
            f.write("""import json
import os

class BaseRuleTransformation:
    \"\"\"
    规则转换模块基类
    
    所有规则转换模块都应该继承这个类并实现extract_key方法
    \"\"\"
    
    def __init__(self, rules=None, rules_file=None, default_key="default", **kwargs):
        \"\"\"
        初始化规则转换模块
        
        Args:
            rules (dict, optional): 规则字典
            rules_file (str, optional): 规则文件路径
            default_key (str, optional): 默认规则键名
            **kwargs: 其他配置参数
        \"\"\"
        self.default_key = default_key
        self.config = kwargs
        
        if rules_file:
            try:
                with open(rules_file, "r", encoding="utf-8") as f:
                    rules_data = json.load(f)
                    self.rules = rules_data
            except Exception as e:
                print(f"加载规则文件失败: {e}")
                self.rules = {}
        else:
            self.rules = rules or {}

    def process(self, data):
        \"\"\"
        处理输入数据
        
        Args:
            data (dict): 输入数据
            
        Returns:
            dict: 处理结果
        \"\"\"
        key = self.extract_key(data)
        result = self.rules.get(key, self.rules.get(self.default_key, {}))
        print(f"规则匹配: {key} -> {result}")
        return result

    def extract_key(self, data):
        \"\"\"
        从输入数据中提取规则键名
        
        Args:
            data (dict): 输入数据
            
        Returns:
            str: 规则键名
            
        Raises:
            NotImplementedError: 子类必须实现这个方法
        \"\"\"
        raise NotImplementedError("子类必须实现 extract_key 方法")
""")
    
    # 确保__init__.py文件存在
    if not os.path.exists("adaptedge/base/__init__.py"):
        with open("adaptedge/base/__init__.py", "w") as f:
            f.write("""\"\"\"
基础模块
包含所有基类定义
\"\"\"

from adaptedge.base.input import BaseInput
from adaptedge.base.output import BaseOutput
from adaptedge.base.feedback import BaseFeedback
from adaptedge.base.rule import BaseRuleTransformation
""")
    
    # 创建input_types.py文件
    if not os.path.exists("adaptedge/base/input_types.py"):
        with open("adaptedge/base/input_types.py", "w") as f:
            f.write("""from adaptedge.base.input import BaseInput
from adaptedge.registry import input_registry

class FileInput(BaseInput):
    \"\"\"
    文件输入模块
    
    从文件中读取输入数据
    \"\"\"
    
    def __init__(self, filepath=None, **kwargs):
        \"\"\"
        初始化文件输入模块
        
        Args:
            filepath (str): 输入文件路径
            **kwargs: 其他配置参数
        \"\"\"
        super().__init__(**kwargs)
        self.filepath = filepath
        print(f"FileInput 已初始化，文件路径: {filepath}")
        
    def collect_data(self):
        \"\"\"
        从文件中读取数据
        
        Returns:
            dict: 读取的数据
        \"\"\"
        if not self.filepath:
            print("警告: 未指定文件路径")
            return {}
            
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                return {"content": content, "source": "file", "filepath": self.filepath}
        except Exception as e:
            print(f"读取文件错误: {e}")
            return {}

# 注册模块
input_registry.register("file_input", FileInput)
""")

def update_main_init(system):
    """更新adaptedge/__init__.py以导入新模块"""
    init_path = "adaptedge/__init__.py"
    
    # 读取现有内容
    content = ""
    if os.path.exists(init_path):
        with open(init_path, "r") as f:
            content = f.read()
    
    # 检查是否已包含导入语句
    import_line = f"from . import {system}"
    if import_line not in content:
        # 添加导入语句
        with open(init_path, "a") as f:
            if content and not content.endswith("\n"):
                f.write("\n")
            f.write(f"""
# 自动导入 {system} 模块
try:
    {import_line}
except ImportError as e:
    print(f"警告: 无法导入 {system} 模块: {{e}}")
""")

@cli.command()
@click.argument("system")
def run(system):
    """运行系统（例如 adaptedge run clothing_system）"""
    config_path = f"apps/{system}/config.json"
    if not os.path.exists(config_path):
        click.echo(f"错误：配置文件 {config_path} 不存在！请运行 'adaptedge init {system}' 或 'adaptedge create {system}'")
        return
    
    # 先尝试导入模块，确保注册表已更新
    try:
        module_name = f"adaptedge.{system}"
        importlib.import_module(module_name)
        click.echo(f"已加载模块: {module_name}")
    except ImportError as e:
        click.echo(f"警告：导入模块 {module_name} 失败: {e}")
        click.echo("尝试运行，但可能会出现模块未注册错误...")
    
    try:
        system_instance = AdaptEdge(config_path=config_path)
        click.echo(f"运行 {system}...")
        system_instance.run(interval=2.0)
    except Exception as e:
        click.echo(f"运行错误: {e}")
        click.echo("请检查模块是否正确注册，或重新创建应用: adaptedge create --force {system}")

@cli.command()
@click.argument("script")
def convert(script):
    """将手动模块代码转换为配置文件"""
    target_dir = f"apps/{script}"
    config_path = f"{target_dir}/config.json"
    config = {
        "input_modules": [{"name": f"{script}_input", "args": {}}],
        "transformation_modules": [{"name": f"{script}.rule"}],
        "output_module": {"name": f"{script}_output"},
        "feedback_module": {"name": f"{script}_feedback"}
    }
    os.makedirs(target_dir, exist_ok=True)
    with open(config_path, "w") as f:
        json.dump(config, f, indent=4)
    
    example_code = f"""from adaptedge.core import AdaptEdge
system = AdaptEdge(config_path="apps/{script}/config.json")
system.run(interval=2.0)
"""
    with open(f"{target_dir}/{script}.py", "w") as f:
        f.write(example_code)
    
    click.echo(f"转换完成！配置文件: {config_path}")

@cli.command()
def list():
    """列出可用系统"""
    # 列出templates中的系统
    templates = get_available_templates()
    
    # 列出已创建的应用
    apps = []
    if os.path.exists("apps"):
        apps = [d for d in os.listdir("apps") if os.path.isdir(os.path.join("apps", d))]
    
    # 列出已实现的模块
    modules = []
    for d in os.listdir("adaptedge"):
        if os.path.isdir(os.path.join("adaptedge", d)) and d not in ["__pycache__", "templates", "inputs", "outputs", "feedback", "rules"]:
            modules.append(d)
    
    if templates:
        click.echo("可用模板：")
        for t in templates:
            click.echo(f"- {t}")
    
    if apps:
        click.echo("\n已创建应用：")
        for a in apps:
            click.echo(f"- {a}")
    
    if modules:
        click.echo("\n已实现模块：")
        for m in modules:
            click.echo(f"- {m}")
    
    if not (templates or apps or modules):
        click.echo("没有找到任何系统或模板，使用 'adaptedge create <name>' 创建新应用")

@cli.command()
def test():
    """运行单元测试"""
    import pytest
    click.echo("运行单元测试...")
    pytest.main(["tests"])

def get_available_templates():
    template_dir = "adaptedge/templates"
    if not os.path.exists(template_dir):
        return []
    return [f.replace("_config.json", "") for f in os.listdir(template_dir) if f.endswith("_config.json")]

if __name__ == "__main__":
    cli()