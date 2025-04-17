from adaptedge.core import AdaptEdge
from adaptedge.clothing_system import ClothingSystemOutput, ClothingSystemFeedback

system = AdaptEdge([], [], ClothingSystemOutput(), ClothingSystemFeedback())
system.load_config("configs/clothing_system_config.json")
system.run(interval=2.0)