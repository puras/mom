# MoM

一个用于构建面向大语言模型（LLM）应用和中间件的强大Python工具包。

## 概述

MoM（Model-oriented Middleware）是一个轻量级但功能强大的Python库，专为LLM应用开发设计。它提供了灵活的架构，用于构建LLM驱动的系统，包括消息队列实现、智能体管理和流程控制，允许您轻松集成和编排应用程序中的各种LLM组件。

## 特性

- **面向LLM的架构**：专为构建LLM驱动的应用程序设计
- **消息队列系统**：灵活的发布-订阅机制，用于LLM通信
- **智能体管理**：创建和编排AI智能体的框架
- **流程控制**：管理复杂LLM工作流的工具
- **轻量级实现**：无重型外部依赖
- **易于集成**：无缝集成到现有Python应用和LLM库
- **全面的文档**：详细的指南和示例
- **可扩展设计**：易于添加自定义组件和适配器

## 安装

您可以使用pip安装MoM：

```bash
pip install mom
```

或使用uv：

```bash
uv add mom
```

## 使用方法

### 基本使用
```python
from mom import publish_message, subscribe_to_topic

# 定义消息处理回调
def handle_message(message):
    print(f"收到消息: {message}")

# 订阅主题
subscribe_to_topic("test_topic", handle_message)

# 发布消息
publish_message("test_topic", {"key": "value"})
```

### 使用MessageQueue类
```python
from mom import MessageQueue, Message

# 创建消息队列实例
mq = MessageQueue()

# 定义消息处理回调
def on_message(message):
    print(f"回调收到消息: {message}")

# 订阅主题
mq.subscribe("my_topic", on_message)

# 创建并发布消息
message = Message("my_topic", {"key": "value"})
mq.publish(message)

# 获取特定主题的所有消息
messages = mq.get_messages("my_topic")
print(f"消息总数: {len(messages)}")
```

## API参考

### 核心组件

#### Message类

- `Message(topic: str, data: dict)`: 为LLM通信创建消息
  - `topic`: 消息主题（例如："llm_response", "agent_request"）
  - `data`: 消息负载，通常包含LLM提示词、响应或智能体指令

#### MessageQueue类

- `MessageQueue()`: 为LLM组件通信创建消息队列
- `subscribe(topic: str, callback)`: 订阅LLM相关事件和消息
- `publish(message: Message)`: 向LLM组件发布消息
- `get_messages(topic: str = None)`: 检索消息用于调试或分析

#### 便捷函数

- `publish_message(topic: str, data: dict)`: 向全局队列发布消息
- `subscribe_to_topic(topic: str, callback)`: 订阅全局队列的主题

### LLM特定组件

#### 智能体管理
- `Agent`: 创建AI智能体的基类
- `AgentManager`: 编排多个智能体执行复杂任务

#### 流程控制
- `Flow`: 定义和管理LLM工作流序列
- `Node`: 构建复杂LLM流程的基本单元

#### RAG（检索增强生成）
- `RAGPipeline`: 实现RAG系统的框架
- `DocumentStore`: 文档存储和检索的接口

#### 实体和枚举
- `LLMEntity`: LLM相关实体的基类
- `LLMType`: 支持的LLM提供商和模型的枚举
- `AgentState`: 智能体状态的枚举

## 开发

### 前置条件

- Python 3.12或更高版本
- uv（用于依赖管理）

### 设置

```bash
# 克隆仓库
git clone https://github.com/puras/mom.git
cd mom

# 安装开发依赖
uv install -e .[dev]

# 运行测试
python -m pytest

# 运行代码检查
ruff check .

# 运行类型检查
mypy .
```

## 贡献

欢迎贡献！请随时提交Pull Request。

## 许可证

MIT许可证

## 作者

- puras - puras.he@gmail.com
