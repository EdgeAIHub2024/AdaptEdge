import json
import time
from adaptedge.registry import input_registry, rule_registry, output_registry, feedback_registry

class AdaptEdge:
    def __init__(self, input_mods=None, trans_mods=None, output_mod=None, feedback_mod=None, config_path=None):
        if config_path:
            try:
                with open(config_path, 'r') as f:
                    config = json.load(f)
                self.input_mods = [input_registry.get(mod["name"], **mod.get("args", {})) for mod in config["input_modules"]]
                self.trans_mods = [rule_registry.get(mod["name"], **mod.get("args", {})) for mod in config["transformation_modules"]]
                self.output_mod = output_registry.get(config["output_module"]["name"], **config["output_module"].get("args", {}))
                self.feedback_mod = feedback_registry.get(config["feedback_module"]["name"], **config["feedback_module"].get("args", {}))
            except Exception as e:
                print(f"配置文件加载错误: {e}")
                raise
        else:
            self.input_mods = input_mods or []
            self.trans_mods = trans_mods or []
            self.output_mod = output_mod
            self.feedback_mod = feedback_mod

    def run(self, interval=2.0):
        """运行系统主循环，interval为循环间隔（秒）"""
        print(f"AdaptEdge系统启动，循环间隔: {interval}秒")
        try:
            while True:
                self.run_once()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("系统被用户中断")
        except Exception as e:
            print(f"运行错误: {e}")
            raise

    def run_once(self):
        """执行一次完整的输入-转换-输出-反馈流程"""
        try:
            # 收集数据
            all_data = {}
            for input_mod in self.input_mods:
                data = input_mod.collect_data()
                if data:
                    all_data.update(data)
            
            if not all_data:
                print("警告: 没有收集到任何数据")
                return
                
            # 应用规则
            results = {}
            for rule_mod in self.trans_mods:
                result = rule_mod.process(all_data)
                if result:
                    results.update(result)
            
            if not results:
                print("警告: 规则处理没有产生结果")
                return
                
            # 输出结果
            if self.output_mod:
                feedback = self.output_mod.output(results)
                
                # 处理反馈
                if self.feedback_mod and feedback:
                    self.feedback_mod.process_feedback(feedback)
            else:
                print("警告: 没有配置输出模块")
                
        except Exception as e:
            print(f"流程执行错误: {e}")
            raise