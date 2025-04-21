"""
基础模块
包含所有基类定义
"""

# 导入基类
from adaptedge.base.input import BaseInput
from adaptedge.base.output import BaseOutput
from adaptedge.base.rule import BaseRuleTransformation
from adaptedge.base.feedback import BaseFeedback

# 导入常用输入类型
from adaptedge.base.input_types import FileInput

# 导入特定输入类型
try:
    from adaptedge.base.input_types import FileInput
except ImportError as e:
    print(f"警告: 无法导入特定输入类型: {e}") 