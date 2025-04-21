from adaptedge.base.rule import BaseRuleTransformation
import os

class ClothingSystemRule(BaseRuleTransformation):
    """
    服装规则转换模块
    
    根据用户特征匹配服装推荐
    """
    
    def __init__(self, rules_file=None, **kwargs):
        """
        初始化服装规则转换模块
        
        Args:
            rules_file (str, optional): 规则文件路径
            **kwargs: 其他配置参数
        """
        rules_path = rules_file or os.path.join("apps", "clothing_system", "rules.json")
        super().__init__(rules_file=rules_path, **kwargs)
        
        # 读取各子规则
        self.skin_rules = self.rules.get("skintonetransformation", {})
        self.body_rules = self.rules.get("bodyshapetransformation", {})
        
        print(f"ClothingSystemRule 已初始化，规则文件: {rules_path}")
    
    def extract_key(self, data):
        """
        从用户特征数据中提取规则键名
        
        Args:
            data (dict): 输入数据，包含肤色和体型
            
        Returns:
            str: 规则键名，格式为"肤色_体型"
        """
        skin_tone = data.get("skin_tone", "未知")
        body_shape = data.get("body_shape", "未知")
        key = f"{skin_tone}_{body_shape}"
        return key
        
    def process(self, data):
        """
        处理输入数据，组合各规则结果
        
        Args:
            data (dict): 输入数据
            
        Returns:
            dict: 处理结果
        """
        skin_tone = data.get("skin_tone", "default")
        body_shape = data.get("body_shape", "default")
        
        # 获取各规则结果
        skin_result = self.skin_rules.get(skin_tone, self.skin_rules.get("default", {}))
        body_result = self.body_rules.get(body_shape, self.body_rules.get("default", {}))
        
        # 组合结果
        result = {}
        result.update(skin_result)
        result.update(body_result)
        
        # 添加服装ID和描述
        if result:
            components = []
            if "color" in result:
                components.append(result["color"])
            if "fit" in result:
                components.append(result["fit"])
                
            description = "".join(components)
            result["clothing_id"] = f"C{hash(description) % 1000:03d}"
            result["description"] = description
            
        print(f"组合规则匹配: {skin_tone}+{body_shape} -> {result}")
        return result

class SkinToneRule(BaseRuleTransformation):
    """
    肤色规则转换模块
    
    根据用户肤色匹配服装推荐
    """
    
    def __init__(self, rules_file=None, **kwargs):
        """
        初始化肤色规则转换模块
        
        Args:
            rules_file (str, optional): 规则文件路径
            **kwargs: 其他配置参数
        """
        rules_path = rules_file or os.path.join("apps", "clothing_system", "rules.json")
        super().__init__(rules_file=rules_path, **kwargs)
        # 按原有规则文件格式取出对应部分
        self.rules = self.rules.get("skintonetransformation", {})
        print(f"SkinToneRule 已初始化，规则文件: {rules_path}")
    
    def extract_key(self, data):
        """
        从用户特征数据中提取肤色
        
        Args:
            data (dict): 输入数据
            
        Returns:
            str: 肤色
        """
        return data.get("skin_tone", "default")

class BodyShapeRule(BaseRuleTransformation):
    """
    体型规则转换模块
    
    根据用户体型匹配服装推荐
    """
    
    def __init__(self, rules_file=None, **kwargs):
        """
        初始化体型规则转换模块
        
        Args:
            rules_file (str, optional): 规则文件路径
            **kwargs: 其他配置参数
        """
        rules_path = rules_file or os.path.join("apps", "clothing_system", "rules.json")
        super().__init__(rules_file=rules_path, **kwargs)
        # 按原有规则文件格式取出对应部分
        self.rules = self.rules.get("bodyshapetransformation", {})
        print(f"BodyShapeRule 已初始化，规则文件: {rules_path}")
    
    def extract_key(self, data):
        """
        从用户特征数据中提取体型
        
        Args:
            data (dict): 输入数据
            
        Returns:
            str: 体型
        """
        return data.get("body_shape", "default") 