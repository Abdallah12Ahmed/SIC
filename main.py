import tkinter as tk
from tkinter import messagebox

user_data = [{
    'admin@gmail.com': {
        'password': 'admin123',
        'name': 'Admin',
        'phone_number': '011111',
    },'normal@gmail.com':{
        'password':'normal123',
        'name':'normal'
    }
}]

items = {
    "Sports":{"Football":{"modul":2022,"brand":"add","price":150},
              "Soccar":{"modul":2020,"barnd":"add","price":200},
              "T-shirt":{"modul":2021,"barnd":"add","price":100},
              "Shorts":{"modul":2022,"brand":"add","price":120},
              "Shoes":{"modul":2015,"brand":"add","price":130},
              "Gloves":{"modul":2019,"brand":"add","price":180}
    },
    "Home appliances":{"Oven":{"modul":2022,"brand":"sharp","price":300},
              "mixer":{"modul":2020,"barnd":"sharp","price":500},
              "television":{"modul":2021,"barnd":"aaa","price":600},
              "iron":{"modul":2022,"brand":"dd","price":50},
              "washing machine":{"modul":2015,"brand":"aaaa","price":130},
              "refrigerator":{"modul":2019,"brand":"vv","price":180}

    },
    "Electronics":{"laptop":{"modul":2022,"brand":"apple","price":300},
              "tablet":{"modul":2020,"barnd":"samsung","price":500},
              "phone":{"modul":2021,"barnd":"apple","price":600},
              "watch":{"modul":2022,"brand":"samsung","price":50},
              "power bank":{"modul":2015,"brand":"apple","price":130},
              "heyboard":{"modul":2019,"brand":"apple","price":180}

    },
    "Fashion":{"T-shirt":{"modul":2022,"brand":"add","price":300},
              "jacket":{"modul":2020,"barnd":"sharp","price":500},
              "shirt":{"modul":2021,"barnd":"aaa","price":600},
              "shoes":{"modul":2022,"brand":"dd","price":50},
              "shorts":{"modul":2015,"brand":"aaaa","price":130},
              "pants":{"modul":2019,"brand":"vv","price":180}

    },
    "Books":{"The Giver":{"modul":2022,"brand":"book","price":300},
              "lion king":{"modul":2020,"barnd":"book","price":500},
              "the idiot brain":{"modul":2021,"barnd":"book","price":600},
              "the 5 am club":{"modul":2022,"brand":"book","price":50},
              "kotler":{"modul":2015,"brand":"book","price":130},
              "infinite":{"modul":2019,"brand":"book","price":180}

    },
    "food products":{"tomatoes":{"modul":2022,"brand":"food","price":300},
              "carrot":{"modul":2020,"barnd":"food","price":500},
              "onion":{"modul":2021,"barnd":"food","price":600},
              "apple":{"modul":2022,"brand":"food","price":50},
              "grapes":{"modul":2015,"brand":"food","price":130},
              "watermelon":{"modul":2019,"brand":"food","price":180}

    }
}

def home_page():
    root = tk.Tk()
    root.geometry("1000x1000")
    root.title("Alibaba Hyper")
    label = tk.Label(root, text="Welcome to Alibaba Hyper", font=('arial', 20))
    label.pack(padx=20, pady=20)

    

    button_frame = tk.Frame(root)
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    button_frame.columnconfigure(2, weight=1)

    def homeapp():
        root.destroy()
        Home_appliances()
    btn1 = tk.Button(button_frame, text="Home appliances", font=('Arial', 50) , command=homeapp)
    btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

    def elec():
        root.destroy()
        Electronics()
    btn2 = tk.Button(button_frame, text="Electronics", font=('Arial', 50), command=elec)
    btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

    def fashion():
        root.destroy()
        Fashion()
    btn3 = tk.Button(button_frame, text="Fashion", font=('Arial', 50), command=fashion)
    btn3.grid(row=1, column=0, sticky=tk.W + tk.E)

    def books():
        root.destroy()
        Books()
    btn4 = tk.Button(button_frame, text="Books", font=('Arial', 50), command=books)
    btn4.grid(row=1, column=1, sticky=tk.W + tk.E)

    def sports():
        root.destroy()
        Sports()
    btn5 = tk.Button(button_frame, text="Sports", font=('Arial', 50), command=sports)
    btn5.grid(row=2, column=0, sticky=tk.W + tk.E)

    def food():
        root.destroy()
        Food()
    btn6 = tk.Button(button_frame, text="food products", font=('Arial', 50), command=food)
    btn6.grid(row=2, column=1, sticky=tk.W + tk.E)

    def back():
        root.destroy()
        open_login_page()
    btn7 = tk.Button(button_frame, text="Back", font=('Arial', 50), command=back)
    btn7.grid(row=3, column=1, sticky=tk.W + tk.E)

    view_cart_button = tk.Button(button_frame, text="View Cart", font=('Arial', 50), command=view_cart)
    view_cart_button.grid(row=3, column=0, sticky=tk.W + tk.E)

    button_frame.pack(fill='x')

    root.mainloop()


def admin_page():
    root = tk.Tk()
    root.geometry("1000x1000")
    root.title("Alibaba Hyper")
    label = tk.Label(root, text="Welcome to Alibaba Hyper", font=('arial', 20))
    label.pack(padx=20, pady=20)

    button_frame = tk.Frame(root)
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    button_frame.columnconfigure(2, weight=1)

    def homeapp():
        root.destroy()
        Home_appliances()

    btn1 = tk.Button(button_frame, text="Home appliances", font=('Arial', 50),command=homeapp)
    btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

    def elec():
        root.destroy()
        Electronics()

    btn2 = tk.Button(button_frame, text="Electronics", font=('Arial', 50), command=elec)
    btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

    def fashion():
        root.destroy()
        Fashion()

    btn3 = tk.Button(button_frame, text="Fashion", font=('Arial', 50), command=fashion)
    btn3.grid(row=1, column=0, sticky=tk.W + tk.E)

    def books():
        root.destroy()
        Books()

    btn4 = tk.Button(button_frame, text="Books", font=('Arial', 50), command=books)
    btn4.grid(row=1, column=1, sticky=tk.W + tk.E)

    def sports():
        root.destroy()
        Sports()

    btn5 = tk.Button(button_frame, text="Sports", font=('Arial', 50), command=sports)
    btn5.grid(row=2, column=0, sticky=tk.W + tk.E)

    def food():
        root.destroy()
        Food()

    btn6 = tk.Button(button_frame, text="food products", font=('Arial', 50), command=food)
    btn6.grid(row=2, column=1, sticky=tk.W + tk.E)

    def back():
        root.destroy()
        open_login_page()

    btn7 = tk.Button(button_frame, text="Back", font=('Arial', 50), command=back)
    btn7.grid(row=3, column=1, sticky=tk.W + tk.E)

    item_management_button = tk.Button(button_frame, text="Item Management", font=('Arial', 50),command=open_item_management)
    item_management_button.grid(row=3, column=0, sticky=tk.W + tk.E)

    button_frame.pack(fill='x')

    root.mainloop()



def open_item_management():
    item_management_window = tk.Tk()
    item_management_window.title("Item Management")

    item_name_label = tk.Label(item_management_window, text="Item Name:")
    item_name_label.pack()
    item_name_entry = tk.Entry(item_management_window)
    item_name_entry.pack()

    item_department_label = tk.Label(item_management_window, text="Department:")
    item_department_label.pack()
    item_department_entry = tk.Entry(item_management_window)
    item_department_entry.pack()

    item_modul_label = tk.Label(item_management_window, text="Modul:")
    item_modul_label.pack()
    item_modul_entry = tk.Entry(item_management_window)
    item_modul_entry.pack()

    item_brand_label = tk.Label(item_management_window, text="Brand:")
    item_brand_label.pack()
    item_brand_entry = tk.Entry(item_management_window)
    item_brand_entry.pack()

    item_price_label = tk.Label(item_management_window, text="Price:")
    item_price_label.pack()
    item_price_entry = tk.Entry(item_management_window)
    item_price_entry.pack()

    def add_or_update_item():
        department_name = item_department_entry.get()
        item_name = item_name_entry.get()
        modul = item_modul_entry.get()
        brand = item_brand_entry.get()
        price = item_price_entry.get()

        if department_name in items:
            if item_name in items[department_name]:
                items[department_name][item_name]["modul"] = modul
                items[department_name][item_name]["brand"] = brand
                items[department_name][item_name]["price"] = price
            else:
                items[department_name][item_name] = {
                    "modul": modul,
                    "brand": brand,
                    "price": price,
                }
        else:
            items[department_name] = {
                item_name: {
                    "modul": modul,
                    "brand": brand,
                    "price": price,
                }
            }
        item_management_window.destroy()
    add_update_button = tk.Button(item_management_window, text="Add/Update Item", command=add_or_update_item)
    add_update_button.pack()

    item_management_window.mainloop()



def open_login_page():
    login_window = tk.Tk()
    login_window.title("Login")

    email_label = tk.Label(login_window, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(login_window)
    email_entry.pack()

    password_label = tk.Label(login_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    error_label = tk.Label(login_window, text="", fg="red")
    error_label.pack()

    def login():
        if email_entry.get() == "admin@gmail.com" and password_entry.get() == "admin123":
            login_window.destroy()
            admin_page()
        elif email_entry.get() == "normal@gmail.com" and password_entry.get() == "normal123":
            login_window.destroy()
            home_page()

        else:
            error_label.config(text="Invalid email or password")

    login_button = tk.Button(login_window, text="Login", command=login)
    login_button.pack()

    def register():
        login_window.destroy()
        open_register_page()
    btn7 = tk.Button(login_window, text="Back to register", command=register)
    btn7.pack()

    login_window.mainloop()


def open_register_page():
    register_window = tk.Tk()
    register_window.title("Register")

    def home():
        register_window.destroy()
        home_page()

    email_label = tk.Label(register_window, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(register_window)
    email_entry.pack()

    name_label = tk.Label(register_window, text="Name:")
    name_label.pack()
    name_entry = tk.Entry(register_window)
    name_entry.pack()

    password_label = tk.Label(register_window, text="Password:")
    password_label.pack()
    password_entry = tk.Entry(register_window, show="*")
    password_entry.pack()

    phone_label_reg = tk.Label(register_window, text='Phone Number:')
    phone_label_reg.pack()
    phone_entry_reg = tk.Entry(register_window)
    phone_entry_reg.pack()

    id_label_reg = tk.Label(register_window, text='Id Number:')
    id_label_reg.pack()
    id_entry_reg = tk.Entry(register_window)
    id_entry_reg.pack()

    age_label_reg = tk.Label(register_window, text='Age:')
    age_label_reg.pack()
    age_entry_reg = tk.Entry(register_window)
    age_entry_reg.pack()

    governorate_label_reg = tk.Label(register_window, text='Governorate:')
    governorate_label_reg.pack()
    governorate_entry_reg = tk.Entry(register_window)
    governorate_entry_reg.pack()

    gender_label_reg = tk.Label(register_window, text='Gender:')
    gender_label_reg.pack()
    gender_entry_reg = tk.Entry(register_window)
    gender_entry_reg.pack()

    register_button = tk.Button(register_window, text="Register", command=home)
    register_button.pack()

    def login():
        register_window.destroy()
        open_login_page()
    btn7 = tk.Button(register_window, text="Back to login", command=login)
    btn7.pack()

    register_window.mainloop()


selected_items = {}

total_price=0

def update_total_price():
    global total_price
    total_price += sum(items[department][product]["price"] for department, product in selected_items)

def view_cart():
    cart_window = tk.Tk()
    cart_window.title("Shopping Cart")

    cart_label = tk.Label(cart_window, text="Shopping Cart", font=('arial', 20))
    cart_label.pack(padx=20, pady=5)

    cart_frame = tk.Frame(cart_window)
    cart_frame.columnconfigure(0, weight=1)
    cart_frame.columnconfigure(1, weight=1)

    for item_name, quantity in selected_items.items():  #
        department_name = item_name.split(":")[0].strip()
        product_name = item_name.split(":")[1].strip()
        price = items[department_name][product_name]["price"]
        item_label = tk.Label(cart_frame, text=f"{product_name} ({quantity}): {price * quantity} USD")
        item_label.grid(row=list(selected_items.keys()).index(item_name), column=0, sticky=tk.W)

    total_price = sum(items[item_name.split(":")[0].strip()][item_name.split(":")[1].strip()]["price"] * quantity for
                      item_name, quantity in selected_items.items())
    total_label = tk.Label(cart_frame, text=f"Total Price: {total_price} USD", font=('arial', 16))
    total_label.grid(row=len(selected_items), column=0, sticky=tk.W)

    cart_frame.pack(fill='x', expand="y")

    def close_cart():
        cart_window.destroy()

    close_button = tk.Button(cart_window, text="Close Cart", command=close_cart)
    close_button.pack()

    cart_window.mainloop()



def Home_appliances():
    root = tk.Tk()
    root.geometry("1000x1000")
    root.title("Alibaba Hyper/Home appliances")
    label = tk.Label(root, text="Welcome to Alibaba Hyper in Department of Home appliances", font=('arial', 20))
    label.pack(padx=20, pady=5)

    button_frame = tk.Frame(root)
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    button_frame.columnconfigure(2, weight=1)
#    button_frame.columnconfigure(3, weight=1)
#    button_frame.columnconfigure(4, weight=1)
#    button_frame.columnconfigure(5, weight=1)

    sort_var = tk.StringVar(root)
    sort_var.set("Sort by Price")
    sort_option = tk.OptionMenu(button_frame, sort_var, "Sort by Price", "Sort by Name")
    sort_option.grid(row=7, column=0, sticky=tk.W + tk.E)

    def sort_products():
        sort_criteria = sort_var.get()
        if sort_criteria == "Sort by Price":
            products_sorted = sorted(products.items(), key=lambda item: item[1]['price'])
        elif sort_criteria == "Sort by Name":
            products_sorted = sorted(products.items())
        else:
            products_sorted = list(products.items())


        for widget in button_frame.winfo_children():
            widget.destroy()

    sort_button = tk.Button(button_frame, text="Sort", command=sort_products)
    sort_button.grid(row=7, column=1, sticky=tk.W + tk.E)


    department_name = "Home appliances"

    products = items.get(department_name, {})

    select_item=[]

    def select_item(item_name):
        if item_name in selected_items:
            select_item.remove(item_name)
        else:
            select_item.append(item_name)
        update_total_price()

    row = 0
    checkedList=[]
    for product_name, product_info in products.items():
        item_name = f"Home appliances: {product_name}"
        item_checkbox = tk.Checkbutton(button_frame, text=f"{product_name}: {product_info['price']} USD",
                                       command=lambda name=item_name: select_item(name))
        item_checkbox.grid(row=row, column=0, sticky=tk.W + tk.E)
        price=product_info['price']
        if item_checkbox == 1:
            checkedList.append(price)
            sum += price




        add_to_cart_button = tk.Button(button_frame, text="Add to Cart", command=view_cart)
        add_to_cart_button.grid(row=row, column=1, sticky=tk.W + tk.E)
        row += 1





    def back():
        root.destroy()
        home_page()
    Back_button = tk.Button(button_frame, text="Back", command=back)
    Back_button.grid(row=7, column=1, sticky=tk.W + tk.E)

    button_frame.pack(fill='x', expand="y")



    root.mainloop()
def Electronics():
    root = tk.Tk()
    root.geometry("1000x1000")
    root.title("Alibaba Hyper/Electronics")
    label = tk.Label(root, text="Welcome to Alibaba Hyper in Department of Electronics", font=('arial', 20))
    label.pack(padx=20, pady=5)

    button_frame = tk.Frame(root)
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    button_frame.columnconfigure(2, weight=1)
#    button_frame.columnconfigure(3, weight=1)
#    button_frame.columnconfigure(4, weight=1)
#    button_frame.columnconfigure(5, weight=1)

    sort_var = tk.StringVar(root)
    sort_var.set("Sort by Price")
    sort_option = tk.OptionMenu(button_frame, sort_var, "Sort by Price", "Sort by Name")
    sort_option.grid(row=7, column=0, sticky=tk.W + tk.E)

    def sort_products():
        sort_criteria = sort_var.get()
        if sort_criteria == "Sort by Price":
            products_sorted = sorted(products.items(), key=lambda item: item[1]['price'])
        elif sort_criteria == "Sort by Name":
            products_sorted = sorted(products.items())
        else:
            products_sorted = list(products.items())

        for widget in button_frame.winfo_children():
            widget.destroy()

    sort_button = tk.Button(button_frame, text="Sort", command=sort_products)
    sort_button.grid(row=7, column=1, sticky=tk.W + tk.E)



    department_name = "Electronics"

    products = items.get(department_name, {})

    select_item = []

    def select_item(item_name):
        if item_name in selected_items:
            selected_items.remove(item_name)
        else:
            selected_items.append(item_name)
        update_total_price()

    row = 0
    checkedList =[]
    sum=0
    for product_name, product_info in products.items():
        item_name = f"Electronics: {product_name}"
        item_checkbox = tk.Checkbutton(button_frame, text=f"{product_name}: {product_info['price']} USD",
                                       command=lambda name=item_name: select_item(name))
        item_checkbox.grid(row=row, column=0, sticky=tk.W + tk.E)

        price=product_info['price']

        if item_checkbox == 1:
            checkedList.append(price)
            sum+=price



        add_to_cart_button = tk.Button(button_frame, text="Add to Cart", command=view_cart)
        add_to_cart_button.grid(row=row, column=1, sticky=tk.W + tk.E)
        row += 1


    def back():
        root.destroy()
        home_page()
    Back_button = tk.Button(button_frame, text="Back", command=back)
    Back_button.grid(row=7, column=1, sticky=tk.W + tk.E)

    button_frame.pack(fill='x', expand="y")

    root.mainloop()

def Fashion():
    root = tk.Tk()
    root.geometry("1000x1000")
    root.title("Alibaba Hyper/Fashion")
    label = tk.Label(root, text="Welcome to Alibaba Hyper in Department of Fashion", font=('arial', 20))
    label.pack(padx=20, pady=5)

    button_frame = tk.Frame(root)
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    button_frame.columnconfigure(2, weight=1)
    #button_frame.columnconfigure(3, weight=1)
    #button_frame.columnconfigure(4, weight=1)
    #button_frame.columnconfigure(5, weight=1)

    sort_var = tk.StringVar(root)
    sort_var.set("Sort by Price")
    sort_option = tk.OptionMenu(button_frame, sort_var, "Sort by Price", "Sort by Name")
    sort_option.grid(row=7, column=0, sticky=tk.W + tk.E)

    def sort_products():
        sort_criteria = sort_var.get()
        if sort_criteria == "Sort by Price":
            products_sorted = sorted(products.items(), key=lambda item: item[1]['price'])
        elif sort_criteria == "Sort by Name":
            products_sorted = sorted(products.items())
        else:
            products_sorted = list(products.items())


        for widget in button_frame.winfo_children():
            widget.destroy()

    sort_button = tk.Button(button_frame, text="Sort", command=sort_products)
    sort_button.grid(row=7, column=1, sticky=tk.W + tk.E)


    department_name = "Fashion"

    products = items.get(department_name, {})

    select_item = []

    def select_item(item_name):
        if item_name in selected_items:
            selected_items.remove(item_name)
        else:
            selected_items.append(item_name)
        update_total_price()

    row = 0
    checkedList=[]
    for product_name, product_info in products.items():
        item_name = f"Fashion: {product_name}"
        item_checkbox = tk.Checkbutton(button_frame, text=f"{product_name}: {product_info['price']} USD",
                                       command=lambda name=item_name: select_item(name))
        item_checkbox.grid(row=row, column=0, sticky=tk.W + tk.E)
        add_to_cart_button = tk.Button(button_frame, text="Add to Cart", command=view_cart)
        add_to_cart_button.grid(row=row, column=1, sticky=tk.W + tk.E)
        row += 1

        price = product_info['price']

        if item_checkbox == 1:
            checkedList.append(price)
            sum += price

    def back():
        root.destroy()
        home_page()
    Back_button = tk.Button(button_frame, text="Back", command=back)
    Back_button.grid(row=7, column=1, sticky=tk.W + tk.E)

    button_frame.pack(fill='x', expand="y")

    root.mainloop()
def Books():
    root = tk.Tk()
    root.geometry("1000x1000")
    root.title("Alibaba Hyper/Books")
    label = tk.Label(root, text="Welcome to Alibaba Hyper in Department of Books ", font=('arial', 20))
    label.pack(padx=20, pady=5)

    button_frame = tk.Frame(root)
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    button_frame.columnconfigure(2, weight=1)
#    button_frame.columnconfigure(3, weight=1)
#    button_frame.columnconfigure(4, weight=1)
#    button_frame.columnconfigure(5, weight=1)

    sort_var = tk.StringVar(root)
    sort_var.set("Sort by Price")
    sort_option = tk.OptionMenu(button_frame, sort_var, "Sort by Price", "Sort by Name")
    sort_option.grid(row=7, column=0, sticky=tk.W + tk.E)

    def sort_products():
        sort_criteria = sort_var.get()
        if sort_criteria == "Sort by Price":
            products_sorted = sorted(products.items(), key=lambda item: item[1]['price'])
        elif sort_criteria == "Sort by Name":
            products_sorted = sorted(products.items())
        else:
            products_sorted = list(products.items())

        for widget in button_frame.winfo_children():
            widget.destroy()

    sort_button = tk.Button(button_frame, text="Sort", command=sort_products)
    sort_button.grid(row=7, column=1, sticky=tk.W + tk.E)


    department_name = "Books"

    products = items.get(department_name, {})

    select_item = []

    def select_item(item_name):
        if item_name in selected_items:
            selected_items.remove(item_name)
        else:
            selected_items.append(item_name)
        update_total_price()

    row = 0
    for product_name, product_info in products.items():
        item_name = f"Books: {product_name}"
        item_checkbox = tk.Checkbutton(button_frame, text=f"{product_name}: {product_info['price']} USD",
                                       command=lambda name=item_name: select_item(name))
        item_checkbox.grid(row=row, column=0, sticky=tk.W + tk.E)
        add_to_cart_button = tk.Button(button_frame, text="Add to Cart", command=view_cart)
        add_to_cart_button.grid(row=row, column=1, sticky=tk.W + tk.E)
        row += 1


    def back():
        root.destroy()
        home_page()
    Back_button = tk.Button(button_frame, text="Back", command=back)
    Back_button.grid(row=7, column=1, sticky=tk.W + tk.E)

    button_frame.pack(fill='x', expand="y")

    root.mainloop()

def Sports():
    root = tk.Tk()
    root.geometry("1000x1000")
    root.title("Alibaba Hyper/Sports")
    label = tk.Label(root, text="Welcome to Alibaba Hyper in Department of Sports ", font=('arial', 20))
    label.pack(padx=20, pady=5)

    button_frame = tk.Frame(root)
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    button_frame.columnconfigure(2, weight=1)
    #    button_frame.columnconfigure(3, weight=1)
    #    button_frame.columnconfigure(4, weight=1)
    #    button_frame.columnconfigure(5, weight=1)

    sort_var = tk.StringVar(root)
    sort_var.set("Sort by Price")
    sort_option = tk.OptionMenu(button_frame, sort_var, "Sort by Price", "Sort by Name")
    sort_option.grid(row=7, column=0, sticky=tk.W + tk.E)

    def sort_products():
        sort_criteria = sort_var.get()
        if sort_criteria == "Sort by Price":
            products_sorted = sorted(products.items(), key=lambda item: item[1]['price'])
        elif sort_criteria == "Sort by Name":
            products_sorted = sorted(products.items())
        else:
            products_sorted = list(products.items())

        for widget in button_frame.winfo_children():
            widget.destroy()

    sort_button = tk.Button(button_frame, text="Sort", command=sort_products)
    sort_button.grid(row=7, column=1, sticky=tk.W + tk.E)


    department_name = "Sports"

    products = items.get(department_name, {})

    select_item = []

    def select_item(item_name):
        if item_name in selected_items:
            selected_items.remove(item_name)
        else:
            selected_items.append(item_name)
        update_total_price()

    row = 0
    for product_name, product_info in products.items():
        item_name = f"Sports: {product_name}"
        item_checkbox = tk.Checkbutton(button_frame, text=f"{product_name}: {product_info['price']} USD",
                                       command=lambda name=item_name: select_item(name))
        item_checkbox.grid(row=row, column=0, sticky=tk.W + tk.E)
        add_to_cart_button = tk.Button(button_frame, text="Add to Cart", command=view_cart)
        add_to_cart_button.grid(row=row, column=1, sticky=tk.W + tk.E)
        row += 1

    def back():
        root.destroy()
        home_page()
    Back_button = tk.Button(button_frame, text="Back", command=back)
    Back_button.grid(row=7, column=1, sticky=tk.W + tk.E)

    button_frame.pack(fill='x', expand="y")

    root.mainloop()


def Food():
    root = tk.Tk()
    root.geometry("1000x1000")
    root.title("Alibaba Hyper/Food")
    label = tk.Label(root, text="Welcome to Alibaba Hyper in Department of Food ", font=('arial', 20))
    label.pack(padx=20, pady=5)

    button_frame = tk.Frame(root)
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    button_frame.columnconfigure(2, weight=1)
#    button_frame.columnconfigure(3, weight=1)
#    button_frame.columnconfigure(4, weight=1)
#    button_frame.columnconfigure(5, weight=1)

    sort_var = tk.StringVar(root)
    sort_var.set("Sort by Price")
    sort_option = tk.OptionMenu(button_frame, sort_var, "Sort by Price", "Sort by Name")
    sort_option.grid(row=7, column=0, sticky=tk.W + tk.E)

    def sort_products():
        sort_criteria = sort_var.get()
        if sort_criteria == "Sort by Price":
            products_sorted = sorted(products.items(), key=lambda item: item[1]['price'])
        elif sort_criteria == "Sort by Name":
            products_sorted = sorted(products.items())
        else:
            products_sorted = list(products.items())

        for widget in button_frame.winfo_children():
            widget.destroy()

    sort_button = tk.Button(button_frame, text="Sort", command=sort_products)
    sort_button.grid(row=7, column=1, sticky=tk.W + tk.E)


    department_name = "food products"

    products = items.get(department_name, {})

    select_item = []

    def select_item(item_name):
        if item_name in selected_items:
            selected_items.remove(item_name)
        else:
            selected_items.append(item_name)
        update_total_price()

    row = 0
    for product_name, product_info in products.items():
        item_name = f"Food: {product_name}"
        item_checkbox = tk.Checkbutton(button_frame, text=f"{product_name}: {product_info['price']} USD",
                                       command=lambda name=item_name: select_item(name))
        item_checkbox.grid(row=row, column=0, sticky=tk.W + tk.E)
        add_to_cart_button = tk.Button(button_frame, text="Add to Cart", command=view_cart)
        add_to_cart_button.grid(row=row, column=1, sticky=tk.W + tk.E)
        row += 1

    def back():
        root.destroy()
        home_page()
    Back_button = tk.Button(button_frame, text="Back", command=back)
    Back_button.grid(row=7, column=1, sticky=tk.W + tk.E)
    button_frame.pack(fill='x', expand="y")

    root.mainloop()

root = tk.Tk()
root.title("User Choice")

label = tk.Label(root, text="Choose an option:")
label.pack()

login_button = tk.Button(root, text="Login", command=open_login_page)
login_button.pack()

register_button = tk.Button(root, text="Register", command=open_register_page)
register_button.pack()

root.mainloop()

