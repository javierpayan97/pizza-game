def custom_sort(e):
    return len(e)

def display(pizzas, n2display=-1):
    n = len(pizzas)
    if n == 0:
        print("NO PIZZAS")
        return
    print(f"----- PIZZAS ({n}) -----")
    if n2display != -1:
        pizzas = pizzas[:n2display]
    for i in pizzas:
        print(i)
    print()
    f_pizza = pizzas[0]
    l_pizza = pizzas[-1]
    print(f"first pizza : {f_pizza}")
    print(f"last pizza : {l_pizza}")

def add_pizza():
    while True:
        new_pizza = input("add new pizza: ")
        if pizzas.count(new_pizza.lower()) != 0:
            print("This pizza already exist, please enter a new pizza")
        else:
            pizzas.append(new_pizza)
            pizzas.sort(reverse=True,key=custom_sort)
            return tuple(pizzas)

pizzas = ["4 cheeses","vegetarian","hawai","calzone","four seasons"]
p = add_pizza()
display(p,3)
