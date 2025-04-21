from adaptedge.core import AdaptEdge
from adaptedge.ad_system import AdSystemOutput, AdSystemFeedback

system = AdaptEdge([], [], AdSystemOutput(), AdSystemFeedback())
system.load_config("configs/ad_system_config.json")
system.run(interval=2.0)