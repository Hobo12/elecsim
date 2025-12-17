---
applyTo: '**'
---

# ElecSim 容器化执行规范

## 执行要求
当运行或创建 ElecSim 模拟脚本时，使用本工作区的 Docker 容器环境以确保依赖一致性。

### 容器配置
- **标准模拟**：使用根目录 `Dockerfile` 或 `docker-compose.yaml`
- **强化学习训练**：使用 `docker/rllib-server/Dockerfile`
- **环境测试**：使用 `docker/rllib-env/Dockerfile`

