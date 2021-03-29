# Dealing with files and error/exception handling

def open_file(file_name):
    try:
        file = open(file_name)
        print("File found")
        print(file.read())
    except FileNotFoundError as errmsg:
        print(f"File not found {errmsg}")
    finally:
        print("Thank you")


open_file("order.txt")
open_file("orders.txt")
