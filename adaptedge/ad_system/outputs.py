from adaptedge.base.output import BaseOutput
import random

class AdSystemOutput(BaseOutput):
    """
    广告系统输出模块
    
    负责展示广告并收集用户反馈
    """
    
    def __init__(self, **kwargs):
        """
        初始化广告系统输出模块
        
        Args:
            **kwargs: 配置参数
        """
        super().__init__(**kwargs)
        print(f"AdSystemOutput 已初始化，配置: {kwargs}")
    
    def output(self, data):
        """
        输出广告数据并收集用户反馈
        
        Args:
            data (dict): 广告数据
            
        Returns:
            dict: 用户反馈
        """
        ad_id = data.get("ad_id", "未知")
        description = data.get("description", "默认广告")
        
        print(f"广告输出: {description} (ID: {ad_id})")
        
        # 模拟用户对广告的反应
        stay_time = round(random.uniform(0, 10), 2)
        print(f"用户停留时间: {stay_time} 秒")
        
        # 收集反馈数据
        feedback = {
            "ad_id": ad_id,
            "stay_time": stay_time,
            "clicked": stay_time > 5,  # 停留时间超过5秒视为点击
            "timestamp": random.randint(1000000000, 9999999999)  # 模拟时间戳
        }
        
        return feedback 