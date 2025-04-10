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

- Python 3.6 或更高版本
- 支持的硬件：测试于 Jetson Nano（其他平台待适配）

### 步骤

1. 克隆仓库：
   ```
   git clone https://github.com/EdgeAIHub2024/AdaptEdge.git
   cd AdaptEdge
   ```

2. 创建并激活虚拟环境：
   ```
   # 使用Conda创建Python 3.6环境
   conda create -n adaptedge-env python=3.6

   # 激活Conda环境
   conda activate adaptedge-env
   ```

3. 安装项目（开发模式）：
   ```
   # 开发模式安装
   pip install -e .
   ```

4. 运行示例：
   ```
   # 运行广告系统示例
   python examples/ad_system.py
   ```

   运行后，你会看到类似输出：
   ```
   AdaptEdge 系统启动...
   推荐广告: 运动鞋广告 (ID: A001)
   用户停留时间: 6.73 秒
   规则 '20-30_male_happy' 权重增加到 1.10
   ```
## 使用方法

AdaptEdge 的核心是一个循环系统，你可以自定义模块来适配自己的场景：

### 示例代码
```
from adaptedge.core import AdaptEdge
from adaptedge.modules import AdInput, AdTransformation, AdOutput, AdFeedback

system = AdaptEdge(AdInput(), AdTransformation(), AdOutput(), AdFeedback())
system.run(interval=2.0)
```

### 自定义模块

1. 继承核心模块类（InputModule 等）。

2. 实现必要方法（collect_data、process 等）。

3. 初始化并运行。

详情见 adaptedge/core.py。

## 项目结构

AdaptEdge/

├── adaptedge/        # 核心代码

│   ├── core.py       # 框架主类和抽象基类

│   └── modules.py    # 示例模块实现

├── examples/         # 示例应用

│   └── ad_system.py  # 智能广告系统

├── rules.json        # 示例规则文件

└── README.md         # 本文档

## 当前功能与局限

### 已实现

- 基于规则的推荐（JSON 文件驱动）。
- 简单反馈机制（根据模拟数据调整权重）。
- 在 Jetson Nano 上运行稳定。
 
### 局限性

- 输入仅支持模拟数据，暂无真实传感器支持。
- 未集成 AI 模型，仅限规则驱动。
- 功能初步，实验性强。

## 未来计划

- 添加摄像头支持（OpenCV 集成）。
- 尝试加载轻量 AI 模型（如 TensorFlow Lite）。
- 优化反馈机制，支持数据持久化。
- 适配更多硬件（如 Raspberry Pi）。

注：这些计划会根据开发进度和社区反馈逐步推进。

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