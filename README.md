# MoM

A powerful Python toolkit for building LLM (Large Language Model) -oriented applications and middleware.

## Overview

MoM (Model-oriented Middleware) is a lightweight yet powerful Python library designed for LLM application development. It provides a flexible architecture for building LLM-powered systems, including message queue implementation, agent management, and flow control, allowing you to easily integrate and orchestrate various LLM components in your applications.

## Features

- **LLM-Oriented Architecture**: Designed specifically for building LLM-powered applications
- **Message Queue System**: Flexible publish-subscribe mechanism for LLM communication
- **Agent Management**: Framework for creating and orchestrating AI agents
- **Flow Control**: Tools for managing complex LLM workflows
- **Lightweight Implementation**: No heavy external dependencies
- **Easy Integration**: Seamlessly integrates with existing Python applications and LLM libraries
- **Comprehensive Documentation**: Detailed guides and examples
- **Extensible Design**: Easy to add custom components and adapters

## Installation

You can install MoM using pip:

```bash
pip install mom
```

Or using uv:

```bash
uv add mom
```

## Usage

### Basic Usage

```python
from mom import publish_message, subscribe_to_topic

# Define a callback function to handle messages
def handle_message(message):
    print(f"Received message: {message}")

# Subscribe to a topic
subscribe_to_topic("test_topic", handle_message)

# Publish a message
publish_message("test_topic", {"key": "value", "data": "example"})
```

### Using the MessageQueue Class

```python
from mom import MessageQueue, Message

# Create a message queue instance
mq = MessageQueue()

# Define a callback function
def on_message(message):
    print(f"Callback received: {message}")

# Subscribe to a topic
mq.subscribe("my_topic", on_message)

# Create and publish a message
message = Message("my_topic", {"status": "success", "result": 42})
mq.publish(message)

# Get all messages for a topic
messages = mq.get_messages("my_topic")
print(f"Total messages: {len(messages)}")
```

## API Reference

### Core Components

#### Message Class

- `Message(topic: str, data: dict)`: Create a message for LLM communication
  - `topic`: The message topic (e.g., "llm_response", "agent_request")
  - `data`: The message payload, typically containing LLM prompts, responses, or agent instructions

#### MessageQueue Class

- `MessageQueue()`: Create a message queue for LLM component communication
- `subscribe(topic: str, callback)`: Subscribe to LLM-related events and messages
- `publish(message: Message)`: Publish messages to LLM components
- `get_messages(topic: str = None)`: Retrieve messages for debugging or analysis

#### Convenience Functions

- `publish_message(topic: str, data: dict)`: Publish messages to the global queue
- `subscribe_to_topic(topic: str, callback)`: Subscribe to topics on the global queue

### LLM-Specific Components

#### Agent Management
- `Agent`: Base class for creating AI agents
- `AgentManager`: Orchestrate multiple agents for complex tasks

#### Flow Control
- `Flow`: Define and manage LLM workflow sequences
- `Node`: Building blocks for constructing complex LLM flows

#### RAG (Retrieval-Augmented Generation)
- `RAGPipeline`: Framework for implementing RAG systems
- `DocumentStore`: Interface for document storage and retrieval

#### Entity and Enums
- `LLMEntity`: Base class for LLM-related entities
- `LLMType`: Enumeration of supported LLM providers and models
- `AgentState`: Enumeration of agent states

## Development

### Prerequisites

- Python 3.12 or higher
- uv (for dependency management)

### Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/mom.git
cd mom

# Install development dependencies
uv install -e .[dev]

# Run tests
python -m pytest

# Run linting
ruff check .

# Run type checking
mypy .
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Authors

- Your Name - your.email@example.com
