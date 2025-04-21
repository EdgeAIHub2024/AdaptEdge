class BaseOutput:
    """
    输出模块基类
    
    所有输出模块都应该继承这个类并实现output方法
    """
    
    def __init__(self, **kwargs):
        """
        初始化输出模块
        
        Args:
            **kwargs: 配置参数
        """
        self.config = kwargs
    
    def output(self, data):
        """
        输出数据
        
        Args:
            data (dict): 需要输出的数据
            
        Returns:
            dict: 用户反馈信息
        
        Raises:
            NotImplementedError: 子类必须实现这个方法
        """
        raise NotImplementedError("子类必须实现 output 方法") 