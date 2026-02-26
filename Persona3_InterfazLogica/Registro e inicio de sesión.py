# Registro e inicio de sesión
def validar_contraseña(clave):
    tiene_mayuscula = any(c.isupper() for c in clave)
    tiene_minuscula = any(c.islower() for c in clave)
    tiene_numero = any(c.isdigit() for c in clave)
    return tiene_mayuscula and tiene_minuscula and tiene_numero

def registrar_usuario():
    # ... [código completo de esta función]

def iniciar_sesion_cliente():
    # ... [código completo de esta función]

def iniciar_sesion_admin():
    # ... [código completo de esta función]
