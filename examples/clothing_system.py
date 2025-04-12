from adaptedge.core import AdaptEdge
from adaptedge.clothing_system import ClothingSystemInput, ClothingSystemTransformation, ClothingSystemOutput, ClothingSystemFeedback

input_mod = ClothingSystemInput(use_camera=False)
trans_mod = ClothingSystemTransformation()
output_mod = ClothingSystemOutput()
feedback_mod = ClothingSystemFeedback()

system = AdaptEdge(input_mod, trans_mod, output_mod, feedback_mod)
system.run(interval=2.0)