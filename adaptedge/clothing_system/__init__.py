"""
服装系统模块

这个模块实现了基于用户特征的服装推荐系统
"""

from adaptedge.registry import input_registry, rule_registry, output_registry, feedback_registry

# 导入模块类
from adaptedge.clothing_system.inputs import ClothingSystemInput
from adaptedge.clothing_system.rules import ClothingSystemRule, SkinToneRule, BodyShapeRule
from adaptedge.clothing_system.outputs import ClothingSystemOutput
from adaptedge.clothing_system.feedback import ClothingSystemFeedback

# 注册模块
input_registry.register("clothing_system_input", ClothingSystemInput)
rule_registry.register("clothing_system.rule", ClothingSystemRule)
rule_registry.register("clothing_system.skintone", SkinToneRule)  # 注册肤色规则
rule_registry.register("clothing_system.bodyshape", BodyShapeRule)  # 注册体型规则
output_registry.register("clothing_system_output", ClothingSystemOutput)
feedback_registry.register("clothing_system_feedback", ClothingSystemFeedback)

print("服装系统模块已加载") 