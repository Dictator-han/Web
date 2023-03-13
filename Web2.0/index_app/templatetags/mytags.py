from django import template

register = template.Library()


@register.simple_tag
def show_element_of_list_by_index(raw_list, index):
    try:
        return round(raw_list[index - 1], 2)
    except:
        return ""
