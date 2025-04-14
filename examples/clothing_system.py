from adaptedge.core import AdaptEdge
from adaptedge.file_input import FileInput
from adaptedge.clothing_system import ClothingSystemInput, ClothingSystemOutput, ClothingSystemFeedback
from adaptedge.transformation_rules import SkinToneTransformation, BodyShapeTransformation

input_mods = [FileInput("data.txt"), ClothingSystemInput(use_camera=False)]
trans_mods = [SkinToneTransformation(), BodyShapeTransformation()]
output_mod = ClothingSystemOutput()
feedback_mod = ClothingSystemFeedback()

system = AdaptEdge(input_mods, trans_mods, output_mod, feedback_mod)
system.run(interval=2.0)