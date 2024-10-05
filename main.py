from tkinter import *

window = Tk()
window.geometry('1000x800')
window.title('Shop')
window.configure(bg="orange")

entry1 = Entry(window, width=50)
entry1.pack()

listbox = Listbox(window, width=50, height=40)

try:
    user_money = int(input('How much money do you have: '))
except ValueError:
    print("Please enter a valid number and try again.")
    user_money = 0

money_label = Label(window, text=f"Remaining Money: ${user_money}", bg="orange")
money_label.pack(pady=10)


items = {
    '1kg Bread': 10,
    '1kg Cake': 15,
    '1kg Buns': 18,
    '1kg Garlic Bread': 12,
    '1 Apple Pie': 14,
    '1 Donuts': 7,
    '1kg Apples': 13,
    '1kg Oranges': 25,
    '1kg Bananas': 32,
    '1kg Plums': 24,
    '1kg Cherries': 15,
    '1kg Pineapples': 23,
    '1kg Watermelons': 17,
    '1kg DragonFruits': 10,
    '1kg Strawberries': 40,
    '1kg Blueberries': 16,
    '1kg Carrots': 20,
    '1kg Tomatoes': 15,
    '1kg Potatoes': 20,
    '1kg Beetroots': 25,
    '1kg Spinach': 20,
    '1kg Capsicum': 4,
    '1kg Beans': 2.5,
    '1kg Corn': 23,
    '1kg Broccoli': 14,
    '1kg Chili': 11,
    '1kg Bitter Gourds': 23,
    '1kg Ginger': 15,
    '1kg Lemon': 10,
    '1kg Cucumber': 15,
    '1kg Onion': 20,
    '1kg Cabbage': 20,
    '1kg Spring Onion': 30,
    '1kg Eggplant': 14,
    '1kg Eggs': 10,
    '1kg Chicken': 12,
    '1 Fish': 15,
    '1 Crab': 18,
    '1 Blue Crab': 20,
    '1kg Prawns': 14,
    '1kg King Prawns': 16,
    '1 Chocolate': 20,
    '50g ChocoChips': 3,
    '10 ChocoEggs': 4,
    '1 KinderJoy': 3,
    '1kg ChocoIceCream': 36,
    '1l Milk': 30,
    '33cl Coke': 15,
    '33cl Fanta': 15,
    '33cl Sprite': 15,
    '1kg Cheese': 15,
    '1kg Butter': 40,
    '1kg Paneer': 30,
    '1kg Ghee': 34
}


for item, price in items.items():
    listbox.insert(END, f'{item} - ${price}')

purchased_items = {}


def selection():
    global user_money
    selected_index = listbox.curselection()

    if not selected_index:
        entry1.delete(0, END)
        entry1.insert(0, 'Please select an item')
        return

    selected_item = listbox.get(selected_index).split(' - ')[0]
    item_price = items[selected_item]

    if user_money >= item_price:
        user_money -= item_price
        money_label.config(text=f"Remaining Money: ${user_money}")


        if selected_item in purchased_items:
            purchased_items[selected_item] += 1
        else:
            purchased_items[selected_item] = 1

        entry1.delete(0, END)
        entry1.insert(0, f'Bought: {selected_item}')
    else:
        entry1.delete(0, END)
        entry1.insert(0, 'Not enough money')

    listbox.selection_clear(0, END)

# Function to print the bill
def print_Bill():
    if not purchased_items:
        entry1.delete(0, END)
        entry1.insert(0, 'No items bought yet')
        return

    window2 = Tk()
    window2.title('Shop Bill')
    window2.geometry('400x400')
    window2.configure(bg="orange")

    bill_label1 = Label(window2, text=f'You have: ${user_money}', bg="orange")
    bill_label1.pack(pady=10)

    bill_label = Label(window2, text='You bought:', bg="orange")
    bill_label.pack(pady=10)

    total_cost = 0
    for item, quantity in purchased_items.items():
        item_price = items[item]
        total_price = item_price * quantity
        total_cost += total_price
        item_label = Label(window2, text=f'- {item} x{quantity} - ${total_price}', bg="orange")
        item_label.pack()


    total_cost_label = Label(window2, text=f'Total Cost: ${total_cost}', bg="orange")
    total_cost_label.pack(pady=10)

    window2.mainloop()


def destroy():
    window.destroy()


button1 = Button(window, text='Buy', command=selection)
button1.pack()

button2 = Button(window, text='Print Bill', command=print_Bill)
button2.pack()

button3 = Button(window, text="Exit", command=destroy)
button3.pack(side=BOTTOM)

listbox.pack(pady=20)

window.mainloop()
