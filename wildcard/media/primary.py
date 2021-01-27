from plone.rfc822.interfaces import IPrimaryFieldInfo
from zope.component import adapts
from zope.interface import implementer
from wildcard.media.interfaces import (
    IMediaEnabled, IVideoEnabled
)
from wildcard.media.behavior import IVideo, IAudio


@implementer(IPrimaryFieldInfo)
class PrimaryFieldInfo(object):
    adapts(IMediaEnabled)

    def __init__(self, context):
        self.context = context
        if IVideoEnabled.providedBy(self.context):
            self.fieldname = 'video_file'
            self.field = IVideo[self.fieldname]
        else:
            self.fieldname = 'audio_file'
            self.field = IAudio[self.fieldname]

    @property
    def value(self):
        return self.field.get(self.context)
