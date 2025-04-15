from adaptedge.core import AdaptEdge
from adaptedge.inputs.file_input import FileInput
from adaptedge.inputs.clothing_system_input import ClothingSystemInput
from adaptedge.rules.clothing_system_rules import SkinToneTransformation, BodyShapeTransformation
from adaptedge.clothing_system import ClothingSystemOutput, ClothingSystemFeedback

input_mods = [FileInput("data.txt"), ClothingSystemInput(use_camera=False)]
trans_mods = [SkinToneTransformation(), BodyShapeTransformation()]
output_mod = ClothingSystemOutput()
feedback_mod = ClothingSystemFeedback()

system = AdaptEdge(input_mods, trans_mods, output_mod, feedback_mod)
system.run(interval=2.0)