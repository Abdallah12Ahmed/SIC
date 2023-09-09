import tkinter as tk
def home_page():
    root = tk.Tk()
    root.geometry("1000000000x1000000000")
    root.title("Alibaba Hyper")
    label = tk.Label(root, text="Welcome to Alibaba Hyper", font=('arial', 20))
    label.pack(padx=20, pady=20)

    button_frame = tk.Frame(root)
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)
    button_frame.columnconfigure(2, weight=1)


    btn1 = tk.Button(button_frame, text="Home appliances", font=('Arial', 50))
    btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

    btn2 = tk.Button(button_frame, text="Electronics", font=('Arial', 50))
    btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

    btn3 = tk.Button(button_frame, text="Fashion", font=('Arial', 50))
    btn3.grid(row=1, column=0, sticky=tk.W + tk.E)

    btn4 = tk.Button(button_frame, text="Books", font=('Arial', 50))
    btn4.grid(row=1, column=1, sticky=tk.W + tk.E)

    btn5 = tk.Button(button_frame, text="Sports", font=('Arial', 50))
    btn5.grid(row=2, column=0, sticky=tk.W + tk.E)

    btn6 = tk.Button(button_frame, text="food products", font=('Arial', 50))
    btn6.grid(row=2, column=1, sticky=tk.W + tk.E)

    button_frame.pack(fill='x')

    root.mainloop()

home_page()