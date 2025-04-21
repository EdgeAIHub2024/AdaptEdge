from adaptedge.base.feedback import BaseFeedback

class ClothingSystemFeedback(BaseFeedback):
    """
    服装系统反馈处理模块
    
    处理用户对服装推荐的反馈，调整推荐策略
    """
    
    def __init__(self, score_threshold=3, **kwargs):
        """
        初始化服装系统反馈处理模块
        
        Args:
            score_threshold (int): 评分阈值，高于此阈值视为正面评价
            **kwargs: 其他配置参数
        """
        super().__init__(**kwargs)
        self.score_threshold = score_threshold
        self.weights = {}  # 规则权重字典
        self.clothing_stats = {}  # 服装统计数据
        print(f"ClothingSystemFeedback 已初始化，评分阈值: {score_threshold}")
    
    def process_feedback(self, feedback):
        """
        处理用户反馈
        
        Args:
            feedback (dict): 反馈数据
            
        Returns:
            dict: 处理结果
        """
        clothing_id = feedback.get("clothing_id", "未知")
        user_score = feedback.get("user_score", 0)
        try_on = feedback.get("try_on", False)
        purchase = feedback.get("purchase", False)
        
        # 更新服装统计
        if clothing_id not in self.clothing_stats:
            self.clothing_stats[clothing_id] = {
                "impressions": 0, 
                "try_ons": 0, 
                "purchases": 0, 
                "total_score": 0
            }
        
        self.clothing_stats[clothing_id]["impressions"] += 1
        if try_on:
            self.clothing_stats[clothing_id]["try_ons"] += 1
        if purchase:
            self.clothing_stats[clothing_id]["purchases"] += 1
        self.clothing_stats[clothing_id]["total_score"] += user_score
        
        # 计算各种指标
        stats = self.clothing_stats[clothing_id]
        impressions = stats["impressions"]
        try_on_rate = stats["try_ons"] / impressions if impressions > 0 else 0
        purchase_rate = stats["purchases"] / stats["try_ons"] if stats["try_ons"] > 0 else 0
        avg_score = stats["total_score"] / impressions if impressions > 0 else 0
        
        # 更新权重
        if user_score >= self.score_threshold:
            # 正面评价，增加权重
            weight_key = f"clothing_{clothing_id}"
            self.weights[weight_key] = self.weights.get(weight_key, 1.0) + 0.1
            print(f"服装 {clothing_id} 获得正面评价，权重提升至 {self.weights[weight_key]:.2f}")
        else:
            # 负面评价，减少权重
            weight_key = f"clothing_{clothing_id}"
            self.weights[weight_key] = max(self.weights.get(weight_key, 1.0) - 0.05, 0.1)
            print(f"服装 {clothing_id} 获得负面评价，权重降低至 {self.weights[weight_key]:.2f}")
        
        # 如果用户购买了，额外增加权重
        if purchase:
            weight_key = f"clothing_{clothing_id}"
            self.weights[weight_key] = self.weights.get(weight_key, 1.0) + 0.2
            print(f"服装 {clothing_id} 被购买，权重额外提升至 {self.weights[weight_key]:.2f}")
        
        return {
            "clothing_id": clothing_id,
            "try_on_rate": try_on_rate,
            "purchase_rate": purchase_rate,
            "avg_score": avg_score,
            "weight": self.weights.get(f"clothing_{clothing_id}", 1.0)
        } 