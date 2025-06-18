from .models import MenuItem
from typing import Optional

def build_menu_tree(items: list, parent_id: int, active_item: Optional[MenuItem], active_parents: list):
    """
    Функция для построения дерева
    """
    result = []
    for item in items:
        if item.parent_id == parent_id:
            children = build_menu_tree(items, item.id, active_item, active_parents)
            is_active = item == active_item
            is_parent = item.id in active_parents
            should_expand = is_active or is_parent or (active_item and active_item.parent_id == item.id)


            result.append({
                'item': item,
                'children': children,
                'is_active': is_active,
                'is_parent': is_parent,
                'should_expand': should_expand,
            })
    return result