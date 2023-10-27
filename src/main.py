#!/usr/bin/env python

import backend as bd

print(bd.create_tables())

"""
bd.insert_brand(["Sony"])
bd.insert_brand(["HP"])

bd.insert_product(["Analogic Mouse", "Chainees miki maus", 2.50, 310, 1])
bd.insert_product(["Optical Mouse", "Good Quality, Good Quantity", 9.99, 34, 2])
bd.insert_product(["Monitor", "Cool Monitor", 362.99, 9, 1])
"""

bd.print_rows(bd.get_product_details())

# bd.print_rows(bd.get_rows("Products"))
# bd.print_rows(bd.get_rows("Brands"))
