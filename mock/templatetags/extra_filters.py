from django import template

register = template.Library()
# 新注册一个filter要重启django


@register.filter(name='test_filter', is_safe=True)
def test_filter(value, arg='default value'):
    return str(value) + str(123) + arg


@register.filter
def lower(value):
    return value.lower()


@register.filter(name='cut')
def myCut(value, arg):
    return value.replace(arg, '~')


@register.simple_tag
def test_tag(a, b, c):
    return str(a == b and c == a)


@register.simple_tag
def check_new_review(term, review_term, course_term_ids, joined_term):
    return review_term == term or ((not review_term or review_term not in course_term_ids) and joined_term == term)


@register.simple_tag
def count_rate(review_rate):
    if review_rate != 0 or not review_rate:
        return 0
    else:
        return review_rate / 2.0
