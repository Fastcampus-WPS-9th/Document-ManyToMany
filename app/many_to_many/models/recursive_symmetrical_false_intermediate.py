from django.db import models

__all__ = (
    'TwitterUser',
    'Relation',
)


class TwitterUser(models.Model):
    name = models.CharField(max_length=50)
    relation_users = models.ManyToManyField(
        'self',
        through='Relation',
        related_name='+',
        symmetrical=False,
    )

    def __str__(self):
        return self.name


class Relation(models.Model):
    CHOICES_RELATION_TYPE = (
        ('f', 'Follow'),
        ('b', 'Block'),
    )
    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='from_user_relations',
        related_query_name='from_user_relation',
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='to_user_relations',
        related_query_name='to_user_relation',
    )
    relation_type = models.CharField(choices=CHOICES_RELATION_TYPE, max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('from_user', 'to_user'),
        )

    def __str__(self):
        return '{from_user} to {to_user} ({type})'.format(
            from_user=self.from_user.name,
            to_user=self.to_user.name,
            # CHOICES가 정의되어있는 CharField
            #  get_FOO_display() <- FOO: Field명
            type=self.get_relation_type_display(),
        )
