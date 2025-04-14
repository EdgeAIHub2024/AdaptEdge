from adaptedge.core import AdaptEdge
from adaptedge.file_input import FileInput
from adaptedge.ad_system import AdSystemInput, AdSystemOutput, AdSystemFeedback
from adaptedge.transformation_rules import AgeTransformation, GenderTransformation, EmotionTransformation

input_mods = [FileInput("data.txt"), AdSystemInput(use_camera=False)]
trans_mods = [AgeTransformation(), GenderTransformation(), EmotionTransformation()]
output_mod = AdSystemOutput()
feedback_mod = AdSystemFeedback()

system = AdaptEdge(input_mods, trans_mods, output_mod, feedback_mod)
system.run(interval=2.0)