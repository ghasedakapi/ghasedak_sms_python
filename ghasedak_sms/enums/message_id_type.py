from enum import Enum


class MessageIdType(Enum):
    CLIENT_REFERENCE_ID = 2
    MESSAGE_ID = 1

    def __str__(self):
        return str(self.value)
