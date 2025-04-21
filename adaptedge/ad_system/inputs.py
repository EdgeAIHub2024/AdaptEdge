from adaptedge.base.input import BaseInput
import random

class AdSystemInput(BaseInput):
    """
    广告系统输入模块
    
    可以从摄像头或随机生成用户特征数据
    """
    
    def __init__(self, use_camera=False, camera_index=0, **kwargs):
        """
        初始化广告系统输入模块
        
        Args:
            use_camera (bool): 是否使用摄像头
            camera_index (int): 摄像头索引
            **kwargs: 其他配置参数
        """
        super().__init__(**kwargs)
        self.use_camera = use_camera
        self.cap = None
        if use_camera:
            try:
                import cv2
                self.cap = cv2.VideoCapture(camera_index)
                if not self.cap.isOpened():
                    raise RuntimeError(f"无法打开摄像头 {camera_index}")
                print(f"已初始化摄像头 {camera_index}")
            except ImportError:
                raise ImportError("使用摄像头需要安装 OpenCV，请运行 `pip install opencv-python`")
        print(f"AdSystemInput 已初始化，使用摄像头: {use_camera}")

    def collect_data(self):
        """
        采集用户特征数据
        
        Returns:
            dict: 包含年龄、性别、情绪的数据
        """
        if self.use_camera and self.cap:
            import cv2
            ret, frame = self.cap.read()
            if not ret:
                print("读取摄像头失败，使用默认特征")
                return {
                    "age": "20-30",
                    "gender": "男",
                    "emotion": "开心"
                }
            # 简化起见，这里用随机值模拟从图像分析得到的用户特征
            # 实际应用中这里应该有更复杂的图像处理和特征提取算法
            age = "20-30"
            gender = "男"
            emotion = "开心"
            data = {
                "age": age,
                "gender": gender,
                "emotion": emotion
            }
        else:
            data = {
                "age": random.choice(["20-30", "30-40", "40-50"]),
                "gender": random.choice(["男", "女"]),
                "emotion": random.choice(["开心", "难过", "平静"])
            }
        print(f"广告系统采集到数据: 年龄={data['age']}, 性别={data['gender']}, 情绪={data['emotion']}")
        return data

    def __del__(self):
        """
        释放资源
        """
        if self.use_camera and self.cap and self.cap.isOpened():
            self.cap.release()
            print("摄像头资源已释放") 