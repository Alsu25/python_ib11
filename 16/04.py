count: int = 1
items: [(str, int)] = []


def add_item(name: str, cost: int):
    items.append((name, cost))


def print_receipt():
    global count
    if not items:
        return
    total: int = 0
    print(f"Чек {count}. Всего предметов: {len(items)}")
    for name, cost in items:
        total += cost
        print(f"{name} - {cost}")
    print(f"Итого: {total}\n-----")
    count += 1
    items.clear()


add_item('Блокнот', 100)
print_receipt()

add_item('Ручка', 70)
print_receipt()
print_receipt()

add_item('Булочка', 15)
add_item('Булочка', 15)
add_item('Чай', 5)
print_receipt()

add_item('Булочка', 15)
add_item('Булочка', 15)