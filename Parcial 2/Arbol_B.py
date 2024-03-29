from cola import Cola
import linecache


def get_value_from_file(file_name, index):
    line = linecache.getline(file_name, index)
    line_split = line.split(';')
    line_split.pop()
    return line_split


class NodeTree():

    def __init__(self, value, other_values=None, other_values3=None, fourth_value=None):
        self.value = value
        self.other_values = other_values
        self.other_values3 = other_values3
        self.fourth_value = fourth_value
        self.left = None
        self.right = None
        self.height = 0


class BinaryTree:

    def __init__(self):
        self.root = None

    def height(self, root):  
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root): 
        if root is not None:
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = (left_height if left_height >
                           right_height else right_height) + 1

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):  
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                if self.height(root.left.left) >= self.height(root.left.right):
                    root = self.simple_rotation(root, True)
                else:
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                if self.height(root.right.right) >= self.height(root.right.left):
                    root = self.simple_rotation(root, False)
                else:
                    root = self.double_rotation(root, False)
        return root

    def insert_node(self, value, other_values=None, other_values3=None, fourth_value=None):

        def __insertar(root, value, other_values, other_values3, fourth_value):
            if root is None:
                return NodeTree(value, other_values, other_values3, fourth_value)
            elif value < root.value:
                root.left = __insertar(
                    root.left, value, other_values, other_values3, fourth_value)
            else:
                root.right = __insertar(
                    root.right, value, other_values, other_values3, fourth_value)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insertar(
            self.root, value, other_values, other_values3, fourth_value)

    def by_level(self):
        if self.root is not None:
            cola_tree = Cola()
            cola_tree.arrive(self.root)
            while cola_tree.size() > 0:
                node = cola_tree.atention()
                print(node.value)
                # a = input()
                if node.left is not None:
                    cola_tree.arrive(node.left)
                if node.right is not None:
                    cola_tree.arrive(node.right)
        
    def by_level_nombre(self):
        if self.root is not None:
            cola_arbol = Cola()
            cola_arbol.arrive(self.root)
            while cola_arbol.size() > 0:
                node = cola_arbol.atention()
                print(f"Nombre: {node.value}. Numero: {node.other_values[0]}. Tipo: {node.other_values[1]}")
                if node.left is not None:
                    cola_arbol.arrive(node.left)
                if node.right is not None:
                    cola_arbol.arrive(node.right)  

    def inorden(self):  
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        __inorden(self.root)

    def inorden_file(self, file_name):
        def __inorden_file(root, file_name):
            if root is not None:
                __inorden_file(root.left, file_name)
                value = get_value_from_file(file_name, root.other_values)
                print(root.value, value[0])
                __inorden_file(root.right, file_name)

        __inorden_file(self.root, file_name)

    def inorden_file_lightsaber(self, file_name, lightsaber_color):
        def __inorden_file_lightsaber(root, file_name, lightsaber_color):
            if root is not None:
                __inorden_file_lightsaber(
                    root.left, file_name, lightsaber_color)
                value = get_value_from_file(file_name, root.other_values)
                if lightsaber_color in value[4].split('/'):
                    print(root.value, value[4].split('/'))
                __inorden_file_lightsaber(
                    root.right, file_name, lightsaber_color)

        __inorden_file_lightsaber(self.root, file_name, lightsaber_color)

    def inorden_super_or_villano(self, is_hero):
        def __inorden_s_v(root, is_hero):
            if root is not None:
                __inorden_s_v(root.left, is_hero)
                if root.other_values is is_hero:
                    print(root.value)
                __inorden_s_v(root.right, is_hero)

        __inorden_s_v(self.root, is_hero)

    def inorden_start_with(self, cadena, heroe):
        def __inorden_start_with(root, cadena, heroe):
            if root is not None:
                __inorden_start_with(root.left, cadena, heroe)
                if root.other_values is heroe and root.value.upper().startswith(cadena):
                    print(root.value)
                __inorden_start_with(root.right, cadena, heroe)
        __inorden_start_with(self.root, cadena, heroe)

    def inorden_start_with_jedi(self, cadena):
        def __inorden_start_with_jedi(root, cadena):
            if root is not None:
                __inorden_start_with_jedi(root.left, cadena)
                if root.value.upper().startswith(cadena):
                    print(root.value)
                __inorden_start_with_jedi(root.right, cadena)

        __inorden_start_with_jedi(self.root, cadena)


    def inorden_tipos(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                tipos = root.value.split("-")
                for tipo in tipos:
                    if tipo in ["Agua", "Fuego", "Planta", "Eléctrico"]:
                        print(root.other_values[1])
                __inorden(root.right)
        __inorden(self.root)
    
    def inorden_numero(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(f'Numero:{root.value} - Nombre:{root.other_values[0]} - Tipo:{root.other_values[1]}')
                __inorden(root.right)
        __inorden(self.root)

    def inorden_nombre(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(f'Nombre:{root.value} - Numero:{root.other_values[0]} - Tipo:{root.other_values[1]}')
                __inorden(root.right)
        __inorden(self.root)
    

    def postorden(self):  
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        __postorden(self.root)

    def preorden(self):  
        def __preorden(root):
            if root is not None:
                print(root.value, root.height)
                __preorden(root.left)
                __preorden(root.right)

        __preorden(self.root)

 
    def search_by_coincidence(self, value):
        def __search_by_coincidence(root, value):
            if root is not None:
                if root.value.startswith(value):
                    print(root.value)
                __search_by_coincidence(root.left, value)
                __search_by_coincidence(root.right, value)

        __search_by_coincidence(self.root, value)

    def search(self, key): 
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    return root
                elif key < root.value:
                    return __search(root.left, key)
                else:
                    return __search(root.right, key)

        return __search(self.root, key)

    def search_pokemon_por_numero(self,key):
        def __search(root,key):
            if root is not None:
                if root.value==key:
                    print(f'Numero:{root.value}- Nombre:{root.other_values[0]} - Tipo:{root.other_values[1]}')
                elif key< root.value:
                    return __search(root.left,key)
                else:
                    return __search(root.right,key)
        
        return __search(self.root,key)

    def search_pokemon_por_nombre(self,key):
        def __search(root,key):
            if root is not None:
                if key in root.value:
                    print(f'Nombre:{root.value} - Numero:{root.other_values[0]} - Tipo: {root.other_values[1]}')
                elif key< root.value:
                    return __search(root.left,key)
                else:
                    return __search(root.right,key)
        
        return __search(self.root,key)

    
    def delete_node(self, key):  
        def __replace(root):
            if root.right is None:
                return root.left, root
            else:
                root.right, replace_node = __replace(root.right)
            return root, replace_node

        def __delete(root, key):
            value = None
            if root is not None:
                if key < root.value:
                    root.left, value = __delete(root.left, key)
                elif key > root.value:
                    root.right, value = __delete(root.right, key)
                else:
                    value = root.value
                    if root.left is None and root.right is not None:
                        return root.right, value
                    elif root.right is None and root.left is not None:
                        return root.left, value
                    elif root.left is None and root.right is None:
                        return None, value
                    else:
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value

            return root, value

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, key)
        return delete_value
    

    def contar(self, value):
        def __contar(root, value):
            count = 0
            if root is not None:
                if root.value == value:
                    count = 1
                count += __contar(root.left, value)
                count += __contar(root.right, value)
            return count

        return __contar(self.root, value)

    def contar_heroes(self, heroe):
        def __contar_heroes(root, heroe):
            count = 0
            if root is not None:
                if root.other_values is heroe:
                    count = 1
                count += __contar_heroes(root.left, heroe)
                count += __contar_heroes(root.right, heroe)
            return count

        return __contar_heroes(self.root, heroe)

    def separacion_de_arbol(self, arbol_superheroes, arbol_villanos):
        def __separacion_de_arbol(root, arbol_superheroes, arbol_villanos):
            if root is not None:
                __separacion_de_arbol(
                    root.left, arbol_superheroes, arbol_villanos)
                if root.other_values is True:
                    arbol_superheroes.insert_node(
                        root.value, root.other_values)
                if root.other_values is False:
                    arbol_villanos.insert_node(root.value, root.other_values)
                __separacion_de_arbol(
                    root.right, arbol_superheroes, arbol_villanos)

        __separacion_de_arbol(self.root, arbol_superheroes, arbol_villanos)

    def jedi_master(self, jedi):
        def __jedi_master(root, jedi):
            if root is not None:
                __jedi_master(root.left, jedi)
                if root.value == jedi:
                    pos = root.other_values
                    if pos:
                        print(get_value_from_file("TP5/jedis.txt", pos)[0])
                __jedi_master(root.right, jedi)

        __jedi_master(self.root, jedi)

    def maestros(self, fire):
        def __maestros(root):
            if root is not None:
                __maestros(root.left)

                if get_value_from_file(fire, root.other_values)[3] != '-':
                    get_value_from_file(fire, root.other_values)
                    print(get_value_from_file(fire, root.other_values))
                __maestros(root.right)
        __maestros(self.root)

    def Togruta_o_Cerean(self, fire):
        def __Togruta_o_Cerean(root):
            if root is not None:
                __Togruta_o_Cerean(root.left)

                if 'torguta' in get_value_from_file(fire, root.other_values)[2].lower() or 'cerean' in get_value_from_file(fire, root.other_values)[2].lower():
                    print(get_value_from_file(fire, root.other_values)[0])

                __Togruta_o_Cerean(root.right)
        __Togruta_o_Cerean(self.root)

    def nombresAoGuion(self, fire):
        def __nombresAoGuion(root):
            if root is not None:
                __nombresAoGuion(root.left)

                valor = get_value_from_file(fire, root.other_values)[0].lower()
                valor2 = valor[0]

                if 'a' == valor2 or '-' in get_value_from_file(fire, root.other_values)[0].lower():
                    print(get_value_from_file(fire, root.other_values)[0])

                __nombresAoGuion(root.right)
        __nombresAoGuion(self.root)

    

    def listado_inordencriaturas(self):
        def __listado_inordencriaturas(root):
            if root is not None:
                __listado_inordencriaturas(root.left)
                # continuar
                print(
                    f'Criatura: {root.value} Derrotado por: {root.other_values} Descripcion:{root.other_values3} Capturado por:{root.fourth_value} ')
                __listado_inordencriaturas(root.right)
        __listado_inordencriaturas(self.root)

    def inorden_ranking(self, ranking):
        def __inorden_ranking(root, ranking):
            if root is not None:
                __inorden_ranking(root.left, ranking)
                if root.other_values is not None:
                    if root.other_values not in ranking:
                        ranking[root.other_values] = 1
                    else:
                        ranking[root.other_values] += 1
                __inorden_ranking(root.right, ranking)
        __inorden_ranking(self.root, ranking)

    def criaturas_derrotadas_por_Heracles(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                if root.other_values == 'Heracles':
                    print(root.value)
                __inorden(root.right)
        __inorden(self.root)

    def Criaturas_no_derrotadas(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                if root.other_values == '-':
                    print(root.value)
                __inorden(root.right)
        __inorden(self.root)

    def search_by_criatura(self, value):
        def __search_by_coincidence(root, value):
            if root is not None:
                if root.value.startswith(value):
                    print(
                        f'Criatura: {root.value} Derrotado por: {root.other_values} Descripcion:{root.other_values3} Capturado por:{root.fourth_value} ')
                __search_by_coincidence(root.left, value)
                __search_by_coincidence(root.right, value)
        __search_by_coincidence(self.root, value)

    def caputrados_por_Heracles(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                if root.fourth_value == 'Heracles':
                    print(root.value)
                __inorden(root.right)
        __inorden(self.root)

    def contador_pokemon_electricos(self):
        def contar(root):
            cont=0
            if root is not None:
                if "Eléctrico" in root.value:
                    cont=1
                cont+= contar(root.left)
                cont+= contar(root.right)
            return cont
        return contar(self.root)

    def contador_pokemon_acero(self):
        def contar(root):
            cont=0
            if root is not None:
                if "Acero" in root.value:
                    cont=1
                cont+= contar(root.left)
                cont+= contar(root.right)
            return cont
        return contar(self.root)
    
# arbol = BinaryTree()

# for i in range(15):
#     arbol.insert_node(i)

# arbol.preorden()

# arbol.root = arbol.balancing(arbol.root)


# print(arbol.root)
# arbol.insert_node('F')
# arbol.insert_node('B')
# # arbol.insert_node('E')
# arbol.insert_node('K')
# arbol.insert_node('H')
# arbol.insert_node('J')
# arbol.insert_node('I')
# arbol.insert_node('R')

# arbol.preorden()

# print()
# deleted = arbol.delete_node('F')
# # if deleted:
# #     print('el valor fue eliminado', deleted)
# # print()
# arbol.preorden()
# deleted = arbol.delete_node('Z')
# print()
# arbol.preorden()
# deleted = arbol.delete_node('K')
# print()
# arbol.preorden()


# print()
# pos = arbol.search('Z')
# print(pos)
# if pos:
#     print('valor encontrado', pos.value)
