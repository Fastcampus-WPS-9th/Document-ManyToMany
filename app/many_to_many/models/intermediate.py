from django.db import models

__all__ = (
    'Person',
    'Group',
    'Membership',
)


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(
        Person,
        # MTM관계에 대한 정보를 가질 테이블을 명시적으로 사용
        through='Membership',
        related_name='group_set',
        related_query_name='group',
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)

    def __str__(self):
        return '{} (Group: {})'.format(
            self.person.name,
            self.group.name,
        )
