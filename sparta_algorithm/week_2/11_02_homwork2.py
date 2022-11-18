shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
	if len(orders) == 0:
		return True

	if orders[0] not in shop_menus:
		return False
	else:
		return is_available_to_order(menus, orders[1:])


result = is_available_to_order(shop_menus, shop_orders)
print(result)
