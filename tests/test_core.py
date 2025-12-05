import pytest
from mom import Message, MessageQueue, publish_message, subscribe_to_topic


class TestMessage:
    """测试Message类"""
    
    def test_message_creation(self):
        """测试消息创建"""
        msg = Message("test_topic", {"key": "value"})
        assert msg.topic == "test_topic"
        assert msg.data == {"key": "value"}
        assert msg.timestamp is None
    
    def test_message_str(self):
        """测试消息字符串表示"""
        msg = Message("test_topic", {"key": "value"})
        assert str(msg) == "Message(topic='test_topic', data={'key': 'value'})"


class TestMessageQueue:
    """测试MessageQueue类"""
    
    def test_queue_creation(self):
        """测试消息队列创建"""
        mq = MessageQueue()
        assert isinstance(mq, MessageQueue)
    
    def test_subscribe_and_publish(self):
        """测试订阅和发布功能"""
        mq = MessageQueue()
        received_messages = []
        
        def callback(msg):
            received_messages.append(msg)
        
        # 订阅主题
        mq.subscribe("test_topic", callback)
        
        # 发布消息
        msg = Message("test_topic", {"key": "value"})
        mq.publish(msg)
        
        # 验证消息被接收
        assert len(received_messages) == 1
        assert received_messages[0].topic == "test_topic"
        assert received_messages[0].data == {"key": "value"}
    
    def test_get_messages(self):
        """测试获取消息功能"""
        mq = MessageQueue()
        
        # 发布两条消息
        mq.publish(Message("topic1", {"data": "msg1"}))
        mq.publish(Message("topic2", {"data": "msg2"}))
        mq.publish(Message("topic1", {"data": "msg3"}))
        
        # 获取所有消息
        all_messages = mq.get_messages()
        assert len(all_messages) == 3
        
        # 获取特定主题的消息
        topic1_messages = mq.get_messages("topic1")
        assert len(topic1_messages) == 2
        assert all(msg.topic == "topic1" for msg in topic1_messages)
        
        topic2_messages = mq.get_messages("topic2")
        assert len(topic2_messages) == 1
        assert topic2_messages[0].topic == "topic2"


class TestConvenienceFunctions:
    """测试便捷函数"""
    
    def test_publish_message(self):
        """测试publish_message函数"""
        received_messages = []
        
        def callback(msg):
            received_messages.append(msg)
        
        # 订阅全局队列
        subscribe_to_topic("global_topic", callback)
        
        # 使用便捷函数发布消息
        publish_message("global_topic", {"test": "data"})
        
        # 验证消息被接收
        assert len(received_messages) == 1
        assert received_messages[0].topic == "global_topic"
        assert received_messages[0].data == {"test": "data"}
    
    def test_subscribe_to_topic(self):
        """测试subscribe_to_topic函数"""
        received_messages = []
        
        def callback(msg):
            received_messages.append(msg)
        
        # 使用便捷函数订阅主题
        mq = subscribe_to_topic("another_topic", callback)
        
        # 发布消息到同一主题
        publish_message("another_topic", {"key": "value"})
        
        # 验证消息被接收
        assert len(received_messages) == 1
        assert isinstance(mq, MessageQueue)
