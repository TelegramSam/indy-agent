"""
Serializer using json as i/o format.
"""

import json

from python_agent_utils.messages.message import Message


def unpack_dict(dictionary: dict) -> Message:
    deserialized_msg = Message(dictionary)
    return deserialized_msg


# TODO: Should be called `deserialize`
def unpack(dump) -> Message:
    """
    Deserialize from bytes or str to Message
    """
    dump_dict = json.loads(dump)
    deserialized_msg = Message(dump_dict)
    return deserialized_msg


# TODO: Should be called `serialize`
def pack(msg: Message) -> str:
    """
    Serialize from Message to json string or from dictionary to json string.
    """
    return msg.as_json()
