# myapp/templatetags/custom_tags.py
import math

from django import template
from datetime import datetime
from ..models import *

register = template.Library()


# Custom Tag: Calculate Age
@register.simple_tag
def calculate_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year
    if today.month < birthdate.month or (today.month == birthdate.month and today.day < birthdate.day):
        age -= 1
    return age


@register.simple_tag
def get_degree(profile: Profile):
    educations = profile.education.all()
    if educations:
        return educations[0].degree
    return "None"

@register.simple_tag
def get_skill_left_panel(profile: Profile):
    skills = profile.skill.all().order_by('value').reverse()
    ret = []
    if skills:
        for i in range(0, skills.count(), 2):
            ret.append(skills[i])
    return ret
@register.simple_tag
def get_skill_right_panel(profile: Profile):
    skills = profile.skill.all().order_by('value').reverse()
    ret = []
    if skills:
        for i in range(1, skills.count(), 2):
            ret.append(skills[i])
    return ret

@register.simple_tag
def get_filters(profile: Profile):
    return profile.project.values('type').distinct()