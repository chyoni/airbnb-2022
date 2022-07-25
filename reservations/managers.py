from django.db import models


class CustomReservationManager(models.Manager):

    """이게 뭐냐면, 모델의 objects를 extending하는거임 원래같으면 DoesNotExist는 error를 리턴하는데 이렇게 하면 이제는
    None을 리턴하는거지 뭐 이런식으로 extending이 가능하다정도로만 알고있음 될듯"""

    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None
