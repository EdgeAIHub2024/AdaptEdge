class BaseInput:
    """
    输入模块基类
    
    所有输入模块都应该继承这个类并实现collect_data方法
    """
    
    def __init__(self, **kwargs):
        """
        初始化输入模块
        
        Args:
            **kwargs: 配置参数
        """
        self.config = kwargs
    
    def collect_data(self):
        """
        采集数据
        
        Returns:
            dict: 采集到的数据
        
        Raises:
            NotImplementedError: 子类必须实现这个方法
        """
        raise NotImplementedError("子类必须实现 collect_data 方法") 