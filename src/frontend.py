import tkinter as tk
from tkinter import ttk


class MainFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class PriceFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class DescFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title = "Main"
        self.geometry("700x500")

        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        self.frame_main = MainFrame(master=self)
        self.frame_main.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.frame_price = PriceFrame(master=self.frame_main, bg="yellow")
        self.frame_desc = DescFrame(master=self.frame_main, bg="blue")
        self.frame_price.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        self.frame_desc.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        self.button_add = tk.Button(
            self.frame_main, text="Add Product", command=self.add_product
        )
        self.button_modify = tk.Button(
            self.frame_main, text="Modify Product", command=self.modify_product
        )
        self.button_delete = tk.Button(
            self.frame_main, text="Delete Product", command=self.delete_product
        )
        self.button_add.grid(row=0, column=0, padx=5, pady=10)
        self.button_modify.grid(row=1, column=0, padx=5, pady=10)
        self.button_delete.grid(row=2, column=0, padx=5, pady=10)

        self.lable_price = tk.Label(self.frame_price, text="Price")
        self.lable_desc = tk.Label(self.frame_desc, text="Description")
        self.lable_price.grid(row=0, column=0, padx=5, pady=10)
        self.lable_desc.grid(row=2, column=0, padx=5, pady=10)

        self.strVar_price = tk.StringVar(value="0.0")
        self.strVar_desc = tk.StringVar(value="Product without information.")
        self.lable_show_price = tk.Label(
            self.frame_price, text=self.strVar_price.get()
        )
        self.lable_show_desc = tk.Label(self.frame_desc, text=self.strVar_desc.get())
        self.lable_show_price.grid(row=1, column=0, padx=5, pady=10)
        self.lable_show_desc.grid(row=3, column=0, padx=5, pady=10)

        self.table_columns = ("name", "brand", "stock")
        self.table = ttk.Treeview(self, show="headings", columns=self.table_columns)
        self.table.heading("name", text="Name")
        self.table.heading("brand", text="Brand")
        self.table.heading("stock", text="Stock")
        self.table.bind("<<TreeviewSelect>>", self.get_product_details)
        self.table.grid(row=0, column=0, padx=20, pady=20)

    def delete_product(self):
        print("Product Deleted [DEMO]")

    def modify_product(self):
        print("Product Modified [DEMO]")

    def add_product(self):
        print("Product Added [DEMO]")

    def get_product_desc(self):
        ...

    def get_product_price(self):
        ...

    def get_product_details(self):
        ...
