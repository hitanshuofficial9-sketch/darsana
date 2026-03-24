def display_info(**kwargs):
    for keys,items in kwargs.items():
        print(f"keys:{keys} items:{items}")

display_info(name="darsana",age=18)