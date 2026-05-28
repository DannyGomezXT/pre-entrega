# Lista principal que ahora contiene DICCIONARIOS: [{"nombre": ..., "categoria": ..., "precio": ...}]
productos = []

def mostrar_menu():
    """Imprime el menú visual en la consola."""
    print("\n========================================")
    print("      SISTEMA DE INVENTARIO")
    print("========================================")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("========================================")

def imprimir_tabla_productos(lista_a_mostrar, usar_indices_originales=False):
    """Función auxiliar para reutilizar el diseño de la tabla."""
    print(f"\n{'ID':<5} | {'NOMBRE':<20} | {'CATEGORÍA':<20} | {'PRECIO'}")
    print("-" * 65)
    
    for idx, prod in enumerate(lista_a_mostrar):
        # Si filtramos en búsquedas, el diccionario tendrá una clave "id_original"
        if usar_indices_originales:
            id_mostrar = prod["id_original"]
        else:
            id_mostrar = idx
            
        print(f"{id_mostrar:<5} | {prod['nombre']:<20} | {prod['categoria']:<20} | ${prod['precio']}")

def desea_repetir(accion):
    """Pregunta si se desea repetir una acción. Solo acepta 's' o 'n'."""
    while True:
        respuesta = input(f"\n¿Desea {accion} otro producto? (s/n): ").strip().lower()
        if respuesta == 's':
            return True
        elif respuesta == 'n':
            return False
        else:
            print("❌ Opción inválida. Por favor, ingrese solo 's' para Sí o 'n' para No.")

def agregar_producto():
    """Valida y añade nuevos productos (como diccionarios) en bucle."""
    while True:
        nombre = input("\nNombre del producto: ").strip()
        while not nombre:
            print("❌ El nombre no puede estar vacío.")
            nombre = input("Nombre del producto: ").strip()
        
        categoria = input("Categoría: ").strip()
        while not categoria:
            print("❌ La categoría no puede estar vacía.")
            categoria = input("Categoría: ").strip()
        
        while True:
            precio_input = input("Precio (solo números enteros): ").strip()
            if not precio_input:
                print("❌ El precio no puede estar vacío.")
            elif precio_input.isdigit():
                precio_num = int(precio_input)
                if precio_num > 0:
                    precio = precio_num
                    break
                else:
                    print("❌ El precio debe ser mayor a cero.")
            else:
                print("❌ Error: Ingrese solo números enteros.")
        
        # MIGRACIÓN: Guardamos como diccionario
        nuevo_producto = {
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio
        }
        productos.append(nuevo_producto)
        print(f"✅ Producto '{nombre}' agregado correctamente.")
        
        if not desea_repetir("agregar"):
            break

def mostrar_productos():
    """Muestra todos los productos actuales."""
    if not productos:
        print("\n❌ El inventario está vacío.")
        return
    imprimir_tabla_productos(productos)

def buscar_producto():
    """Busca coincidencias parciales por nombre en bucle."""
    while True:
        if not productos:
            print("\n❌ El inventario está vacío.")
            break
            
        busqueda = input("\nNombre a buscar: ").strip().lower()
        coincidencias = []
        
        for i, prod in enumerate(productos):
            if busqueda in prod["nombre"].lower():
                # Creamos una copia del diccionario y le anexamos el ID original
                prod_con_id = prod.copy()
                prod_con_id["id_original"] = i
                coincidencias.append(prod_con_id)
                
        if not coincidencias:
            print(f"❌ No se encontraron productos llamados '{busqueda}'.")
        else:
            imprimir_tabla_productos(coincidencias, usar_indices_originales=True)
            print("-" * 65)
            print(f"La cantidad de coincidencias encontradas: {len(coincidencias)}")
            
        if not desea_repetir("buscar"):
            break

def eliminar_producto():
    """Muestra el inventario y elimina elementos por su ID en bucle."""
    while True:
        if not productos:
            print("\n❌ El inventario está vacío.")
            break
            
        imprimir_tabla_productos(productos)
        id_input = input("Ingrese el ID del producto a eliminar: ")
        
        try:
            id_p = int(id_input) 
            if 0 <= id_p < len(productos):
                # MIGRACIÓN: Acceso claro mediante nombres de claves
                prod_a_eliminar = productos[id_p]
                print(f"\n¿Eliminar '{prod_a_eliminar['nombre']}' de la categoría '{prod_a_eliminar['categoria']}'?")
                confirmar = input("Presiona 's' para confirmar (o cualquier otra tecla para cancelar): ").lower()
                
                if confirmar == 's':
                    eliminado = productos.pop(id_p)
                    print(f"✅ Producto '{eliminado['nombre']}' eliminado.")
                else:
                    print("❌ Operación cancelada.")
            else:
                print("❌ ID fuera de rango (el ID no existe en la lista).")
                
        except ValueError:
            print("❌ Error: El ID debe ser un número entero válido (sin letras).")
            
        if not desea_repetir("eliminar"):
            break


# BUCLE PRINCIPAL
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-5): ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        buscar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("❌ La opción ingresada NO es válida.")
