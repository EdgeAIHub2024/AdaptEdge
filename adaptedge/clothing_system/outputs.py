from adaptedge.base.output import BaseOutput
import random

class ClothingSystemOutput(BaseOutput):
    """
    服装系统输出模块
    
    负责展示服装推荐并收集用户评价
    """
    
    def __init__(self, **kwargs):
        """
        初始化服装系统输出模块
        
        Args:
            **kwargs: 配置参数
        """
        super().__init__(**kwargs)
        print(f"ClothingSystemOutput 已初始化，配置: {kwargs}")
    
    def output(self, data):
        """
        输出服装推荐并收集用户评价
        
        Args:
            data (dict): 服装推荐数据
            
        Returns:
            dict: 用户评价
        """
        clothing_id = data.get("clothing_id", "未知")
        description = data.get("description", "默认服装")
        
        print(f"服装推荐: {description} (ID: {clothing_id})")
        
        # 模拟用户评分
        score = random.randint(1, 5)
        print(f"用户评分: {score} 分")
        
        # 模拟用户其他行为
        try_on = random.choice([True, False])
        purchase = random.random() < 0.3  # 30%概率购买
        
        # 收集反馈数据
        feedback = {
            "clothing_id": clothing_id,
            "user_score": score,
            "try_on": try_on,
            "purchase": purchase,
            "timestamp": random.randint(1000000000, 9999999999)  # 模拟时间戳
        }
        
        return feedback 