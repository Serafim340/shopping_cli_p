number_add = int(input("Введите количество желаемых покупок: "))
cart = []
i = 0
while i < number_add:
    cart.append(str(input("Введите наименование желаемого товара: ")))
    i += 1
print(len(cart))
cart.sort()
print(cart)
if "пример_1" in cart:
    cart.remove("пример_1")
cart[-1] = "пример_2"
for item in cart:
    print(item)