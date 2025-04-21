from adaptedge.core import AdaptEdge
system = AdaptEdge(config_path="apps/clothing_system/config.json")
system.run(interval=2.0)