import logging
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save


logger = logging.getLogger(__name__)


class SignalHandlers(object):
    """
    Signal handlers for reviewboard signals.
    """

    def __init__(self, extension):
        """Initialize and connect all the signals"""
        self.extension = extension

        post_save.connect(self._user_saved, sender=User,
                          dispatch_uid='defualt_group_extension')

    def disconnect(self):
        """Disconnect the signal handlers"""
        post_save.disconnect(self._user_saved, sender=User)

    def _user_saved(self, **kwargs):
        logger.info("User saved")

        user = kwargs['instance']

        if kwargs['created']:
            logger.info("User {} with id {} created".format(
                user.username, user.pk))

            group, _ = Group.objects.get_or_create(name='default')
            user.groups.add(group)
