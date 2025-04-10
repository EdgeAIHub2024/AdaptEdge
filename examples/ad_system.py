from adaptedge.core import AdaptEdge
from adaptedge.modules import AdInput, AdTransformation, AdOutput, AdFeedback

# 初始化模块
input_mod = AdInput()
trans_mod = AdTransformation(rules_file="rules.json")
output_mod = AdOutput()
feedback_mod = AdFeedback(threshold=5.0)

# 创建并运行 AdaptEdge 系统
system = AdaptEdge(input_mod, trans_mod, output_mod, feedback_mod)
system.run(interval=2.0)