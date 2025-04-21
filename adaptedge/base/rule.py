import json
import os

class BaseRuleTransformation:
    """
    规则转换模块基类
    
    所有规则转换模块都应该继承这个类并实现extract_key方法
    """
    
    def __init__(self, rules=None, rules_file=None, default_key="default", **kwargs):
        """
        初始化规则转换模块
        
        Args:
            rules (dict, optional): 规则字典
            rules_file (str, optional): 规则文件路径
            default_key (str, optional): 默认规则键名
            **kwargs: 其他配置参数
        """
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
        """
        处理输入数据
        
        Args:
            data (dict): 输入数据
            
        Returns:
            dict: 处理结果
        """
        key = self.extract_key(data)
        result = self.rules.get(key, self.rules.get(self.default_key, {}))
        print(f"规则匹配: {key} -> {result}")
        return result

    def extract_key(self, data):
        """
        从输入数据中提取规则键名
        
        Args:
            data (dict): 输入数据
            
        Returns:
            str: 规则键名
            
        Raises:
            NotImplementedError: 子类必须实现这个方法
        """
        raise NotImplementedError("子类必须实现 extract_key 方法") 