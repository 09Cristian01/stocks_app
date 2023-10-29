import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

import backend as bd


class MainFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class PriceFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class DescFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class Window(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title = "Main"
        self.geometry("700x500")

        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        self.frame_main = MainFrame(master=self)
        self.frame_main.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.frame_price = PriceFrame(master=self.frame_main)
        self.frame_desc = DescFrame(master=self.frame_main)
        self.frame_price.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        self.frame_desc.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        self.button_add = ctk.CTkButton(
            self.frame_main, text="Add Product", command=self.add_product
        )
        self.button_modify = ctk.CTkButton(
            self.frame_main, text="Modify Product", command=self.modify_product
        )
        self.button_delete = ctk.CTkButton(
            self.frame_main, text="Delete Product", command=self.delete_product
        )
        self.button_add.grid(row=0, column=0, padx=5, pady=10)
        self.button_modify.grid(row=1, column=0, padx=5, pady=10)
        self.button_delete.grid(row=2, column=0, padx=5, pady=10)

        self.lable_price = ctk.CTkLabel(self.frame_price, text="Price")
        self.lable_desc = ctk.CTkLabel(self.frame_desc, text="Description")
        self.lable_price.grid(row=0, column=0, padx=5, pady=10)
        self.lable_desc.grid(row=2, column=0, padx=5, pady=10)

        # self.strVar_price = ctk.StringVar(value="0.0")
        # self.strVar_desc = ctk.StringVar(value="Product without information.")
        self.lable_show_price = ctk.CTkLabel(
            self.frame_price, text="0.0$"
        )
        self.lable_show_desc = ctk.CTkLabel(
            self.frame_desc, text="No information"
        )
        self.lable_show_price.grid(row=1, column=0, padx=5, pady=10)
        self.lable_show_desc.grid(row=3, column=0, padx=5, pady=10)

        self.table_columns = ("name", "desc", "price", "brand", "stock")
        self.table = ttk.Treeview(self, show="headings", columns=self.table_columns)
        self.table.heading("name", text="Name")
        self.table.heading("desc", text="Description")
        self.table.heading("price", text="Price")
        self.table.heading("brand", text="Brand")
        self.table.heading("stock", text="Stock")
        self.table.bind("<<TreeviewSelect>>", self.get_product_details)
        self.table.grid(row=0, column=0, padx=20, pady=20)

        self.load_items()

    def delete_product(self):
        print("Product Deleted [DEMO]")

    def modify_product(self):
        print("Product Modified [DEMO]")

    def add_product(self):
        print("Product Added [DEMO]")

    def load_items(self, *args, **kwargs):
        print(f"Args: {args}")
        print(f"Kwargs: {kwargs}")
        items = bd.get_product_details()
        for item in items:
            self.table.insert("", "end", values=item)  # [0], item[3], item[4]))

    def get_product_details(self, *args):
        select_item = self.table.item(self.table.selection())
        self.lable_show_price.configure(text=f"${select_item['values'][2]}")
        self.lable_show_desc.configure(text=select_item["values"][1])
