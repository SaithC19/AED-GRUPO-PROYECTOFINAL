def menu_cliente(usuario):
    while True:
        print(f"\n👤 Cliente: {usuario}")
        print("1. Ver mapa (simulado)")
        print("2. Consultar ruta óptima (simulado)")
        print("3. Explorar lugares jerárquicos (simulado)")
        print("4. Seleccionar ciudades a visitar")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("🗺️ Mapa turístico...")
        elif opcion == "2":
            print("📍 Ruta óptima entre ciudades...")
        elif opcion == "3":
            print("🏞️ Lugares organizados por zonas...")
        elif opcion == "4":
            ciudades = input("Escribe las ciudades separadas por coma: ").split(",")
            guardar_seleccion(usuario, ciudades)
        elif opcion == "5":
            break
        else:
            print("❌ Opción inválida.")

def guardar_seleccion(usuario, ciudades):
    archivo = f"rutas_cliente/rutas-{usuario.replace('@', '_').replace('.', '_')}.txt"
    with open(archivo, "w") as f:
        for c in ciudades:
            f.write(c.strip() + "\n")
    print("✅ Selección guardada.")

def menu_administrador():
    while True:
        print("\n👤 Administrador")
        print("1. Agregar ciudad (simulado)")
        print("2. Listar ciudades (simulado)")
        print("3. Buscar ciudad (simulado)")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            print("➕ Ciudad agregada.")
        elif opcion == "2":
            print("📋 Listado de ciudades...")
        elif opcion == "3":
            print("🔍 Buscar ciudad...")
        elif opcion == "4":
            break
        else:
            print("❌ Opción inválida.")
