from django.db import models

__all__ = (
    'InstagramUser',
)


class InstagramUser(models.Model):
    name = models.CharField(max_length=50)
    # 내가 팔로우하는 유저 목록: following
    # 나를 팔로우하는 유저 목록: followers
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
    )

    def __str__(self):
        return self.name
