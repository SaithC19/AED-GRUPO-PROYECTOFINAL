def main():
    grafo = cargar_grafo_desde_archivo(RUTAS_TXT)
    while True:
        print("\n==== SISTEMA DE RUTAS ====")
        print("1. Registrarse como Cliente")
        print("2. Iniciar sesión como Cliente")
        print("3. Iniciar sesión como Administrador")
        print("4. Salir")
        opcion = input("Opción: ")

        # ... [resto de la función]
