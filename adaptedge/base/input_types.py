from adaptedge.base.input import BaseInput
from adaptedge.registry import input_registry

class FileInput(BaseInput):
    """
    文件输入模块
    
    从文件中读取输入数据
    """
    
    def __init__(self, filepath=None, **kwargs):
        """
        初始化文件输入模块
        
        Args:
            filepath (str): 输入文件路径
            **kwargs: 其他配置参数
        """
        super().__init__(**kwargs)
        self.filepath = filepath
        print(f"FileInput 已初始化，文件路径: {filepath}")
        
    def collect_data(self):
        """
        从文件中读取数据
        
        Returns:
            dict: 读取的数据
        """
        if not self.filepath:
            print("警告: 未指定文件路径")
            return {}
            
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                return {"content": content, "source": "file", "filepath": self.filepath}
        except Exception as e:
            print(f"读取文件错误: {e}")
            return {}

# 注册模块
input_registry.register("file_input", FileInput) 