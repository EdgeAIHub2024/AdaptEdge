class BaseFeedback:
    """
    反馈处理模块基类
    
    所有反馈处理模块都应该继承这个类并实现process_feedback方法
    """
    
    def __init__(self, **kwargs):
        """
        初始化反馈处理模块
        
        Args:
            **kwargs: 配置参数
        """
        self.config = kwargs
        
    def process_feedback(self, feedback):
        """
        处理反馈数据
        
        Args:
            feedback (dict): 反馈数据
            
        Returns:
            dict: 处理结果
            
        Raises:
            NotImplementedError: 子类必须实现这个方法
        """
        raise NotImplementedError("子类必须实现 process_feedback 方法") 