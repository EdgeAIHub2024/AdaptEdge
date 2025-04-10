from abc import ABC, abstractmethod
import time

# 抽象基类
class InputModule(ABC):
    @abstractmethod
    def collect_data(self):
        """采集数据，返回结构化数据"""
        pass

class TransformationModule(ABC):
    @abstractmethod
    def process(self, data):
        """处理输入数据，返回结果"""
        pass

class OutputModule(ABC):
    @abstractmethod
    def present(self, result):
        """呈现结果并返回反馈"""
        pass

class FeedbackModule(ABC):
    @abstractmethod
    def update(self, data, result, feedback):
        """根据反馈更新规则或模型"""
        pass

# 框架核心类
class AdaptEdge:
    def __init__(self, input_mod, trans_mod, output_mod, feedback_mod):
        """初始化 AdaptEdge 系统"""
        self.input = input_mod
        self.trans = trans_mod
        self.output = output_mod
        self.feedback = feedback_mod

    def run(self, interval=1.0):
        """运行主循环，interval 为循环间隔（秒）"""
        print("AdaptEdge 系统启动...")
        while True:
            try:
                data = self.input.collect_data()
                result = self.trans.process(data)
                feedback = self.output.present(result)
                self.feedback.update(data, result, feedback)
                time.sleep(interval)
            except KeyboardInterrupt:
                print("系统退出")
                break
            except Exception as e:
                print(f"运行错误: {e}")