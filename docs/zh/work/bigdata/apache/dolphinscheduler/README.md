---
title: Dolphinscheduler
---

执行策略

并行：如果对于同一个工作流定义，同时有多个工作流实例，则并行执行工作流实例。

串行等待：如果对于同一个工作流定义，同时有多个工作流实例，则串行执行工作流实例。

串行抛弃：如果对于同一个工作流定义，同时有多个工作流实例，则抛弃后生成的工作流实例并杀掉正在跑的实例。

串行优先：如果对于同一个工作流定义，同时有多个工作流实例，则按照优先级串行执行工作流实例。