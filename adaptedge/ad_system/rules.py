from adaptedge.base.rule import BaseRuleTransformation
import os

class AgeRule(BaseRuleTransformation):
    """
    年龄规则转换模块
    
    根据用户年龄匹配广告规则
    """
    
    def __init__(self, rules_file=None, **kwargs):
        """
        初始化年龄规则转换模块
        
        Args:
            rules_file (str, optional): 规则文件路径
            **kwargs: 其他配置参数
        """
        rules_path = rules_file or os.path.join("apps", "ad_system", "rules.json")
        super().__init__(rules_file=rules_path, **kwargs)
        # 按原有规则文件格式取出对应部分
        self.rules = self.rules.get("agetransformation", {})
        print(f"AgeRule 已初始化，规则文件: {rules_path}")
    
    def extract_key(self, data):
        """
        根据用户年龄提取规则键名
        
        Args:
            data (dict): 输入数据
            
        Returns:
            str: 规则键名
        """
        return data.get("age", "default")

class GenderRule(BaseRuleTransformation):
    """
    性别规则转换模块
    
    根据用户性别匹配广告规则
    """
    
    def __init__(self, rules_file=None, **kwargs):
        """
        初始化性别规则转换模块
        
        Args:
            rules_file (str, optional): 规则文件路径
            **kwargs: 其他配置参数
        """
        rules_path = rules_file or os.path.join("apps", "ad_system", "rules.json")
        super().__init__(rules_file=rules_path, **kwargs)
        # 按原有规则文件格式取出对应部分
        self.rules = self.rules.get("gendertransformation", {})
        print(f"GenderRule 已初始化，规则文件: {rules_path}")
    
    def extract_key(self, data):
        """
        根据用户性别提取规则键名
        
        Args:
            data (dict): 输入数据
            
        Returns:
            str: 规则键名
        """
        return data.get("gender", "default")

class EmotionRule(BaseRuleTransformation):
    """
    情绪规则转换模块
    
    根据用户情绪匹配广告规则
    """
    
    def __init__(self, rules_file=None, **kwargs):
        """
        初始化情绪规则转换模块
        
        Args:
            rules_file (str, optional): 规则文件路径
            **kwargs: 其他配置参数
        """
        rules_path = rules_file or os.path.join("apps", "ad_system", "rules.json")
        super().__init__(rules_file=rules_path, **kwargs)
        # 按原有规则文件格式取出对应部分
        self.rules = self.rules.get("emotiontransformation", {})
        print(f"EmotionRule 已初始化，规则文件: {rules_path}")
    
    def extract_key(self, data):
        """
        根据用户情绪提取规则键名
        
        Args:
            data (dict): 输入数据
            
        Returns:
            str: 规则键名
        """
        return data.get("emotion", "default")

class CompositeRule(BaseRuleTransformation):
    """
    组合规则转换模块
    
    结合用户年龄、性别和情绪匹配广告规则
    """
    
    def __init__(self, rules_file=None, **kwargs):
        """
        初始化组合规则转换模块
        
        Args:
            rules_file (str, optional): 规则文件路径
            **kwargs: 其他配置参数
        """
        rules_path = rules_file or os.path.join("apps", "ad_system", "rules.json")
        super().__init__(rules_file=rules_path, **kwargs)
        print(f"CompositeRule 已初始化，规则文件: {rules_path}")
        
        # 读取各子规则
        self.age_rules = self.rules.get("agetransformation", {})
        self.gender_rules = self.rules.get("gendertransformation", {})
        self.emotion_rules = self.rules.get("emotiontransformation", {})
    
    def extract_key(self, data):
        """
        根据用户特征组合提取规则键名
        
        Args:
            data (dict): 输入数据
            
        Returns:
            str: 规则键名
        """
        age = data.get("age", "未知")
        gender = data.get("gender", "未知")
        emotion = data.get("emotion", "未知")
        return f"{age}_{gender}_{emotion}"
        
    def process(self, data):
        """
        处理输入数据，组合各规则结果
        
        Args:
            data (dict): 输入数据
            
        Returns:
            dict: 处理结果
        """
        age = data.get("age", "default")
        gender = data.get("gender", "default")
        emotion = data.get("emotion", "default")
        
        # 获取各规则结果
        age_result = self.age_rules.get(age, self.age_rules.get("default", {}))
        gender_result = self.gender_rules.get(gender, self.gender_rules.get("default", {}))
        emotion_result = self.emotion_rules.get(emotion, self.emotion_rules.get("default", {}))
        
        # 组合结果
        result = {}
        result.update(age_result)
        result.update(gender_result)
        result.update(emotion_result)
        
        # 添加广告ID和描述
        if result:
            components = []
            if "product_type" in result:
                components.append(result["product_type"])
            if "style" in result:
                components.append(result["style"])
            if "content" in result:
                components.append(result["content"])
                
            description = "、".join(components)
            result["ad_id"] = f"AD{hash(description) % 1000:03d}"
            result["description"] = description
            
        print(f"组合规则匹配: {age}+{gender}+{emotion} -> {result}")
        return result 