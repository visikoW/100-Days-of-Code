from prettytable import PrettyTable

# inicializando a tabla dos pokemons
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire",])

table.add_row()

print(table)


