from registro_login import registrar_usuario, iniciar_sesion
from menus import menu_cliente, menu_administrador

def main():
    while True:
        print("\n==== Sistema de Rutas ====")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            usuario = iniciar_sesion()
            if usuario:
                if "admin" in usuario:  # Ejemplo: si el usuario tiene "admin" en su correo
                    menu_administrador()
                else:
                    menu_cliente(usuario)
        elif opcion == "3":
            break
        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()
