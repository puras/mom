class Message:
    """
    消息类，用于表示消息队列中的消息
    """
    def __init__(self, topic: str, data: dict):
        self.topic = topic
        self.data = data
        self.timestamp = None

    def __str__(self):
        return f"Message(topic='{self.topic}', data={self.data})"


class MessageQueue:
    """
    消息队列类，用于管理消息的发布和订阅
    """
    def __init__(self):
        self._subscribers = {}
        self._messages = []

    def subscribe(self, topic: str, callback):
        """
        订阅特定主题的消息
        """
        if topic not in self._subscribers:
            self._subscribers[topic] = []
        self._subscribers[topic].append(callback)

    def publish(self, message: Message):
        """
        发布消息到队列
        """
        self._messages.append(message)
        self._notify_subscribers(message)

    def _notify_subscribers(self, message: Message):
        """
        通知所有订阅了该主题的回调函数
        """
        if message.topic in self._subscribers:
            for callback in self._subscribers[message.topic]:
                callback(message)

    def get_messages(self, topic: str = None):
        """
        获取特定主题的所有消息，或所有消息
        """
        if topic:
            return [msg for msg in self._messages if msg.topic == topic]
        return self._messages


# 全局消息队列实例
_global_queue = MessageQueue()


def publish_message(topic: str, data: dict):
    """
    发布消息到全局队列的便捷函数
    """
    message = Message(topic, data)
    _global_queue.publish(message)
    return message


def subscribe_to_topic(topic: str, callback):
    """
    订阅全局队列主题的便捷函数
    """
    _global_queue.subscribe(topic, callback)
    return _global_queue
