#!/usr/bin/env python

import sqlite3
from dotenv import dotenv_values


env = dotenv_values(".env")


def run_query(query: str, params: tuple[str | int | float] = ()) -> any:
    with sqlite3.connect(f"{env['DB_PATH']}+{env['DB_NAME']}") as con:
        cur = con.cursor()
        result = cur.execute(query, params)
        con.commit()
    return result


def get_rows(table: str = "Products") -> any:
    return run_query(f"SELECT * FROM {table}")


def print_rows(rows) -> None:
    print([row for row in rows])


def insert_product(values: tuple[list[str | int | float]]) -> any:
    return run_query("INSERT INTO Products VALUES(NULL, ?, ?, ?, ?, ?)", values)


def insert_brand(values: tuple[list[str | int | float]]) -> any:
    return run_query("INSERT INTO Brands VALUES(NULL, ?)", values)


def delete_product(values: tuple[list[str | int | float]]) -> any:
    return run_query("DELETE FROM Products WHERE product_id=?", values)


def delete_brand(values: tuple[list[str | int | float]]) -> any:
    return run_query("DELETE FROM Brands WHERE brand_id=?", values)


def update_brand():
    ...


def update_product():
    ...


def get_product_details():
    return run_query(
        """SELECT product_name, product_description, product_price, product_stock, brand_name
        FROM Products
        INNER JOIN Brands ON Brands.brand_id = Products.product_brandID;
        """
    )


def create_tables() -> any:
    brands_table = run_query(
        """
            CREATE TABLE IF NOT EXISTS Brands(
                brand_id INTEGER,
                brand_name TEXT NOT NULL UNIQUE,

                PRIMARY KEY (brand_id)
            );
        """
    )
    products_table = run_query(
        """
            CREATE TABLE IF NOT EXISTS Products(
                product_id INTEGER,
                product_name TEXT NOT NULL,
                product_description TEXT,
                product_price REAL NOT NULL DEFAULT 0.0,
                product_stock INTEGER NOT NULL DEFAULT 0,
                product_brandID INTEGER NOT NULL,

                PRIMARY KEY (product_id),
                FOREIGN KEY (product_brandID) REFERENCES Brands(brand_id)
            );
              """
    )
    return (brands_table, products_table)
