from adaptedge.base.feedback import BaseFeedback

class AdSystemFeedback(BaseFeedback):
    """
    广告系统反馈处理模块
    
    处理用户对广告的反馈，调整广告推荐策略
    """
    
    def __init__(self, threshold=5.0, **kwargs):
        """
        初始化广告系统反馈处理模块
        
        Args:
            threshold (float): 停留时间阈值，超过此阈值视为正面反馈
            **kwargs: 其他配置参数
        """
        super().__init__(**kwargs)
        self.threshold = threshold
        self.weights = {}  # 规则权重字典
        self.ad_stats = {}  # 广告统计数据
        print(f"AdSystemFeedback 已初始化，阈值: {threshold}")
    
    def process_feedback(self, feedback):
        """
        处理用户反馈
        
        Args:
            feedback (dict): 反馈数据
            
        Returns:
            dict: 处理结果
        """
        ad_id = feedback.get("ad_id", "unknown")
        stay_time = feedback.get("stay_time", 0)
        clicked = feedback.get("clicked", False)
        
        # 更新广告统计
        if ad_id not in self.ad_stats:
            self.ad_stats[ad_id] = {"impressions": 0, "clicks": 0, "total_stay_time": 0}
        
        self.ad_stats[ad_id]["impressions"] += 1
        if clicked:
            self.ad_stats[ad_id]["clicks"] += 1
        self.ad_stats[ad_id]["total_stay_time"] += stay_time
        
        # 计算点击率和平均停留时间
        impressions = self.ad_stats[ad_id]["impressions"]
        clicks = self.ad_stats[ad_id]["clicks"]
        total_stay_time = self.ad_stats[ad_id]["total_stay_time"]
        
        ctr = clicks / impressions if impressions > 0 else 0
        avg_stay_time = total_stay_time / impressions if impressions > 0 else 0
        
        # 更新权重
        if stay_time > self.threshold:
            # 正面反馈，增加权重
            weight_key = f"ad_{ad_id}"
            self.weights[weight_key] = self.weights.get(weight_key, 1.0) + 0.1
            print(f"广告 {ad_id} 获得正面反馈，权重提升至 {self.weights[weight_key]:.2f}")
        else:
            # 负面反馈，减少权重
            weight_key = f"ad_{ad_id}"
            self.weights[weight_key] = max(self.weights.get(weight_key, 1.0) - 0.05, 0.1)
            print(f"广告 {ad_id} 获得负面反馈，权重降低至 {self.weights[weight_key]:.2f}")
        
        return {
            "ad_id": ad_id,
            "ctr": ctr,
            "avg_stay_time": avg_stay_time,
            "weight": self.weights.get(f"ad_{ad_id}", 1.0)
        } 