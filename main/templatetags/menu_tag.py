from django import template

from main.models import MenuItem
from main.utils import build_menu_tree

register = template.Library()


@register.inclusion_tag('main/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name: str):
    """
    Шаблонный тег для генерации элементов меню
    """
    request = context['request']
    current_url = request.path
    
    # Оптимизируем запрос
    menu_items = MenuItem.objects.filter(menu__name=menu_name).select_related('parent').order_by('order')
    
    # Получаем активный элемент по url
    active_item = None
    for item in menu_items:
        if item.get_absolute_url().rstrip('/') == current_url.rstrip('/'):
            active_item = item
            break
    
    # Получаем активные родительские элементы пункта меню
    active_parents = []
    if active_item:
        parent = active_item.parent
        while parent:
            active_parents.append(parent.id)
            parent = parent.parent
    
    
    menu_tree = build_menu_tree(menu_items, None, active_item, active_parents)
    
    return {
        'menu_tree': menu_tree,
    }