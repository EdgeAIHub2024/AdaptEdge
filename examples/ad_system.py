from adaptedge.core import AdaptEdge
from adaptedge.inputs.file_input import FileInput
from adaptedge.inputs.ad_system_input import AdSystemInput
from adaptedge.rules.ad_system_rules import AgeTransformation, GenderTransformation, EmotionTransformation
from adaptedge.ad_system import AdSystemOutput, AdSystemFeedback

input_mods = [FileInput("data.txt"), AdSystemInput(use_camera=False)]
trans_mods = [AgeTransformation(), GenderTransformation(), EmotionTransformation()]
output_mod = AdSystemOutput()
feedback_mod = AdSystemFeedback()

system = AdaptEdge(input_mods, trans_mods, output_mod, feedback_mod)
system.run(interval=2.0)