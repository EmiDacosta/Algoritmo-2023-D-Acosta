from arbol_binario import BinaryTree, get_value_from_file


class Pokemon:
    def __init__(self, nombre, numero, tipos):
        self.nombre = nombre
        self.numero = numero
        self.tipos = tipos

    def __str__(self):
        tipo_str = "/".join(self.tipos)
        return f"nombre: {self.nombre}\nNúmero en la Pokédex: #{self.numero}\nTipo/Tipos: {tipo_str}"
    
arbol_nombre= BinaryTree()
arbol_numero=BinaryTree()
arbol_tipo= BinaryTree()
pokemones = [
    {'nombre':"Bulbasaur", 'numero':1, 'tipo':"Planta-Veneno"},
    {'nombre':"Charmander", 'numero':3, 'tipo':"Fuego"},
    {'nombre':"Squirtle", 'numero':6, 'tipo':"Agua"},
    {'nombre':"Pikachu", 'numero':22, 'tipo':"Eléctrico"},
    {'nombre':"Jigglypuff", 'numero':38,'tipo': "Normal-Hada"},
    {'nombre':"Gengar", 'numero':64, 'tipo':"Fantasma-Veneno"},
    {'nombre':"Snorlax", 'numero':743, 'tipo':"Normal"},
    {'nombre':"Mewtwo", 'numero':50, 'tipo':"Psíquico"},
    {'nombre':"Gyarados", 'numero':230, 'tipo':"Agua-Volador"},
    {'nombre':"Jolteon", 'numero':232, 'tipo':"Eléctrico"},
    {'nombre':"Lycanroc", 'numero':595, 'tipo':"Roca"},
    {'nombre':"Tyrantrum", 'numero':192, 'tipo':"Roca-Dragón"},
    {'nombre':"Machamp", 'numero':78, 'tipo':"Lucha"}
]

for i in pokemones:
    arbol_nombre.insert_node(i['nombre'],[i['numero'],i['tipo']])
    arbol_numero.insert_node(i['numero'],[i['nombre'],i['tipo']])
    arbol_tipo.insert_node(i['tipo'],[i['numero'],i['nombre']])

print('')
arbol_nombre.inorden()
arbol_numero.inorden()
arbol_tipo.inorden() 

#b. 
print('DATOS DE UN POKEMON A PARTIR DE SU NUMERO Y NOMBRE: ')
arbol_numero.search_pokemon_por_numero(25)

arbol_nombre.search_pokemon_por_nombre("Mewtwo")

#c. 
print('POKEMON A PARTIR DE TIPO AGUA, FUEGO, PLANTA Y ELÉCTRICO: ')
arbol_tipo.inorden_tipos()

#d.
print('LISTADO ASCENDENTE POR NUMERO:')
arbol_numero.inorden_numero()
print('LISTADO ASCENDENTE POR NOMBRE:')
arbol_nombre.inorden_nombre()
print('LISTADO ASCENDENTE POR NIVEL POR NOMBRE:')
arbol_nombre.by_level_nombre()
#e.
print('INFO DE JOLTEON, LYCANROC Y TYRANTRUM:')
arbol_nombre.search_pokemon_por_nombre("Jolteon")
arbol_nombre.search_pokemon_por_nombre("Lycanroc")
arbol_nombre.search_pokemon_por_nombre("Tyrantrum")
#f.
contador_electricos=arbol_tipo.contador_pokemon_electricos()
print(f'CANTIDAD DE POKEMONES ELÉCTRICOS:{contador_electricos} ')
contador_acero= arbol_tipo.contador_pokemon_acero()
print(f'CANTIDAD DE POKEMONES ACERO:{contador_acero}')
