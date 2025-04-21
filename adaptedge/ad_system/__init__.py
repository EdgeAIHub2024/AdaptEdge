"""
广告系统模块

这个模块实现了基于用户特征的广告推荐系统
"""

from adaptedge.registry import input_registry, rule_registry, output_registry, feedback_registry

# 导入模块类
from adaptedge.ad_system.inputs import AdSystemInput
from adaptedge.ad_system.rules import AgeRule, GenderRule, EmotionRule, CompositeRule
from adaptedge.ad_system.outputs import AdSystemOutput
from adaptedge.ad_system.feedback import AdSystemFeedback

# 注册模块
input_registry.register("ad_system_input", AdSystemInput)
rule_registry.register("ad_system.age", AgeRule)
rule_registry.register("ad_system.gender", GenderRule)
rule_registry.register("ad_system.emotion", EmotionRule)
rule_registry.register("ad_system.composite", CompositeRule)
output_registry.register("ad_system_output", AdSystemOutput)
feedback_registry.register("ad_system_feedback", AdSystemFeedback)

print("广告系统模块已加载") 