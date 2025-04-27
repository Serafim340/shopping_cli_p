def add_item(cart, item):
    cart.append(item)
    print(f"Товар добавлен: {item}")

def remove_item(cart, item):
    if item in cart:
        cart.remove(item)
        print(f"Товар удален: {item}")
    else:
        print(f"Товар '{item}' не найден в корзине.")

def show_cart(cart):
    print("\nИтоговый список покупок:")
    for item in cart:
        print(f"- {item}")

cart = []

number_add = int(input("Введите количество желаемых покупок: "))
i = 0
while i < number_add:
    item_name = input("Введите наименование желаемого товара: ")
    add_item(cart, item_name)
    i += 1 

if "пример_1" in cart:
    remove_item(cart, "пример_1")

if cart:  
    cart[-1] = "пример_2"

cart.sort()
print(len(cart))

show_cart(cart)