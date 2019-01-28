# default_group Extension for Review Board.
from reviewboard.extensions.base import Extension

from default_group.handlers import SignalHandlers


class DefaultGroup(Extension):
    is_configurable = True

    def __init__(self, *args, **kwargs):
        super(DefaultGroup, self).__init__(*args, **kwargs)
        self.signal_handlers = SignalHandlers(self)
