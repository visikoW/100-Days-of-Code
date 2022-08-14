database = {}

def set_name(name):
    """To set your name on the database."""
    database[name] = len(database)

def get_name(name):
    """To get your ID on the database."""
    return database[name]

new_name = set_name(input("Write your name: "))

print(get_name(new_name))
