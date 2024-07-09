from enum import Enum


class SendStatus(Enum):
    TO_BE_CONFIRMED = 0
    REJECTED = 1
    TO_BE_SENT = 2
    SENDING = 3
    SENT = 4
    DEBUG_MODE = 5
    INTERNAL_FAILED = 6
    CANCELED = 7
    INTERNAL_BLACKLISTED = 8
    PAUSED = 9
    SENT_TO_PROVIDER = 10
    DELIVERED_TO_PROVIDER = 11
    BLACKLISTED = 12
    NOT_DELIVERED = 13
    DELIVERED = 14
    BLOCKED = 15
    FAILED = 16
    PROCESSING = 17

    def __str__(self):
        return str(self.value)
