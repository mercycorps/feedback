import os
from django import template



register = template.Library()

@register.filter(name='filename')
def filename(value):
    return os.path.basename(value.file.name)


@register.filter(name='is_member')
def is_member(user, group_name):
    return user.groups.filter(name=group_name).exists()


@register.filter(name='is_in_multiple_groups')
def is_in_multiple_groups(user, group_name1, group_name2):
    return user.groups.filter(name__in=[group_name1, group_name2]).exists()