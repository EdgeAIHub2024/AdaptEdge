from adaptedge.core import AdaptEdge
from adaptedge.ad_system import AdSystemInput, AdSystemTransformation, AdSystemOutput, AdSystemFeedback

input_mod = AdSystemInput(use_camera=False)
trans_mod = AdSystemTransformation()
output_mod = AdSystemOutput()
feedback_mod = AdSystemFeedback()

system = AdaptEdge(input_mod, trans_mod, output_mod, feedback_mod)
system.run(interval=2.0)