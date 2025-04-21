from adaptedge.base.input import BaseInput
import random

class ClothingSystemInput(BaseInput):
    """
    服装系统输入模块
    
    可以从摄像头或随机生成用户特征数据
    """
    
    def __init__(self, use_camera=False, camera_index=0, **kwargs):
        """
        初始化服装系统输入模块
        
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
                import numpy as np
                self.cap = cv2.VideoCapture(camera_index)
                if not self.cap.isOpened():
                    raise RuntimeError(f"无法打开摄像头 {camera_index}")
                print(f"已初始化摄像头 {camera_index}")
            except ImportError:
                raise ImportError("使用摄像头需要安装 OpenCV，请运行 `pip install opencv-python`")
        print(f"ClothingSystemInput 已初始化，使用摄像头: {use_camera}")

    def collect_data(self):
        """
        采集用户特征数据
        
        Returns:
            dict: 包含肤色、体型的数据
        """
        if self.use_camera and self.cap:
            import cv2
            import numpy as np
            ret, frame = self.cap.read()
            if not ret:
                print("读取摄像头失败，使用默认特征")
                return {
                    "skin_tone": "浅色",
                    "body_shape": "苗条"
                }
                
            # 简化起见，这里使用随机值模拟从图像分析得到的用户特征
            # 在实际应用中，这里应该有更复杂的图像处理和特征提取算法
            # 例如：皮肤色调可以通过HSV颜色空间分析得到
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            avg_hsv = np.mean(hsv, axis=(0, 1))
            
            # 基于亮度(V)判断肤色深浅
            skin_tone = "浅色" if avg_hsv[2] > 150 else "深色"
            
            # 模拟体型分析
            body_shape = random.choice(["苗条", "中等", "偏重"])
            
            data = {
                "skin_tone": skin_tone,
                "body_shape": body_shape
            }
        else:
            data = {
                "skin_tone": random.choice(["浅色", "深色"]),
                "body_shape": random.choice(["苗条", "中等", "偏重"])
            }
        print(f"服装系统采集到数据: 肤色={data['skin_tone']}, 体型={data['body_shape']}")
        return data

    def __del__(self):
        """
        释放资源
        """
        if self.use_camera and self.cap and self.cap.isOpened():
            self.cap.release()
            print("摄像头资源已释放") 