"""
AdaptEdge: 轻量级边缘AI框架

这个框架基于"输入-转换-输出-反馈"的循环设计，
适合在资源受限的边缘设备上运行自适应AI应用。
"""

__version__ = "0.3.0"

# 导入基础组件
from adaptedge import base

# 自动导入各应用系统模块
try:
    from . import ad_system
except ImportError as e:
    print(f"警告: 无法导入广告系统模块: {e}")

try:
    from . import clothing_system
except ImportError as e:
    print(f"警告: 无法导入服装系统模块: {e}")

# 自动导入 retail_system 模块
try:
    from . import retail_system
except ImportError as e:
    print(f"警告: 无法导入 retail_system 模块: {e}")
