# AdaptEdge

**AdaptEdge** 是一个轻量、模块化的嵌入式 AI 框架，旨在探索如何在边缘设备上实现自适应的智能应用。它基于"输入-转换-输出-反馈"的循环设计，适合研究和实验性质的开发，比如智能广告、智能试衣间等场景。目前处于早期 MVP（最小可用版本）阶段，欢迎试用和反馈！

## 项目简介

AdaptEdge 是我的一个实验项目，目标是在资源受限的嵌入式设备（如 Jetson Nano）上实现一个灵活、自适应的 AI 框架。它不是成熟的产品，而是一个正在摸索的原型，希望通过开源和社区协作，探索嵌入式 AI 的可能性。

### 核心特点

- **轻量级**：为边缘设备优化，当前基于 Python 实现。
- **模块化**：输入、转换、输出、反馈四个模块可独立替换。
- **自适应尝试**：支持通过反馈调整规则，未来计划探索在线学习。
- **实验性质**：功能有限，仍在迭代中。

## 安装

### 前置条件

- Python 3.8 或更高版本
- 支持的硬件：测试于 Jetson Nano（其他平台待适配）

### 步骤

1. 克隆仓库：
   ```
   git clone https://github.com/EdgeAIHub2024/AdaptEdge.git
   cd AdaptEdge
   ```

2. 创建并激活虚拟环境：
   ```
   # 使用Conda创建Python 3.8环境
   conda create -n adaptedge-env python=3.8

   # 激活Conda环境
   conda activate adaptedge-env
   ```

3. 安装项目（开发模式）：
   ```
   pip install -e .
   ```
   若使用摄像头，安装 OpenCV：
   ```
   pip install opencv-python
   ```
## 快速开始
AdaptEdge 提供两个示例：智能广告系统和智能试衣间。

   运行广告系统示例
   ```
   python examples/ad_system.py
   ```

   输出示例：
   ```
   输入数据: 年龄=20-30, 性别=男, 情绪=开心
   转换结果: 匹配规则 '20-30_男_开心'
   输出推荐: 运动鞋广告 (ID: A001)
   反馈更新: 用户停留时间 6.73 秒，规则 '20-30_男_开心' 权重增加到 1.10
   ```
   运行智能试衣间示例
   ```
   python examples/clothing_system.py
   ```
   输出示例：
   ```
   输入数据: 肤色=浅色, 体型=苗条
   转换结果: 匹配规则 '浅色_苗条'
   输出推荐: 粉色修身上衣 (ID: C001)
   反馈更新: 用户评分 4 分，规则 '浅色_苗条' 权重增加到 1.10
   ```

## 使用方法

AdaptEdge 的核心是一个循环系统，开发者可自定义模块适配不同场景。

### 示例代码（广告系统）
```
from adaptedge.core | AdaptEdge
from adaptedge.ad_system import AdSystemInput, AdSystemTransformation, AdSystemOutput, AdSystemFeedback

input_mod = AdSystemInput(use_camera=False)  # 用户特征输入（支持 USB 摄像头）
trans_mod = AdSystemTransformation()       # 规则匹配
output_mod = AdSystemOutput()              # 输出推荐
feedback_mod = AdSystemFeedback()          # 权重调整

system = AdaptEdge(input_mod, trans_mod, output_mod, feedback_mod)
system.run(interval=2.0)  # 每 2 秒循环
```

### 自定义模块

1. 继承核心模块类（InputModule 等）。

2. 实现必要方法（collect_data、process 等）。

3. 初始化并运行。

详情见 adaptedge/core.py。

## 项目结构
   ```
   AdaptEdge/
   ├── adaptedge/
   │   ├── __init__.py
   │   ├── core.py              # 核心框架
   │   ├── ad_system.py         # 广告系统模块
   │   ├── clothing_system.py   # 试衣间模块
   ├── configs/
   │   ├── ad_system_rules.json      # 广告规则
   │   ├── clothing_system_rules.json  # 试衣间规则
   ├── examples/
   │   ├── ad_system.py         # 广告示例
   │   ├── clothing_system.py   # 试衣间示例
   └── README.md
   ```

## 配置说明
规则文件位于 configs/，使用中文键值，便于本地化：
ad_system_rules.json：定义年龄、性别、情绪到广告的映射，如 "20-30_男_开心"。

clothing_system_rules.json：定义肤色、体型到服装的映射，如 "浅色_苗条"。

开发者可创建新规则文件，建议命名为 <use_case>_rules.json。
示例规则
configs/ad_system_rules.json：
```
{
   "20-30_男_开心": {"ad_id": "A001", "description": "运动鞋广告"},
   "30-40_女_难过": {"ad_id": "A002", "description": "甜品广告"},
   "default": {"ad_id": "A000", "description": "默认广告"}
}
```

## 当前功能与局限

### 已实现

- 智能广告系统：基于中文规则推荐广告，支持模拟和摄像头输入。
- 智能试衣间：基于肤色、体型推荐服装，使用简单 HSV 检测。
- 模块化设计：在 Jetson Nano 上运行稳定。
 
### 局限性

- 输入：摄像头仅支持 USB，特征提取为模拟或简单算法。
- 规则：仅支持静态 JSON，暂无 AI 模型。
- 硬件：仅测试 Jetson Nano，需适配 Raspberry Pi 等。

## 未来计划

- 增强输入：支持 CSI 摄像头和传感器。
- 集成 AI：加载 TensorFlow Lite 模型。
- 优化反馈：实现数据持久化和在线学习。
- 扩展硬件：适配 Raspberry Pi、ESP32。

注：计划根据社区反馈调整，欢迎提出建议！

## 适用场景（设想）

- **智能广告**：根据用户特征推荐内容。
- **智能试衣间**：基于体型推荐服装。
- **智能家居**：响应环境变化。

## 贡献指南

这是一个实验项目，欢迎一起探索！

1.Fork 本仓库。

2.创建分支：
```
git checkout -b feature/your-feature
```

3.提交更改：
```
git commit -m "Add your feature"
```

4.推送并创建 Pull Request。

有问题或建议？请提交 Issue。

## 许可证

本项目采用 MIT 许可证，详见 LICENSE 文件。

## 联系我

GitHub: https://github.com/EdgeAIHub2024/AdaptEdge

邮箱: edgeaihubteam@gmail.com

## 致谢

感谢所有试用和支持的朋友！AdaptEdge 是一个学习过程，期待和大家一起完善它！