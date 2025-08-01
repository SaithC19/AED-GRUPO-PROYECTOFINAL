def cargar_grafo_desde_archivo(nombre_archivo):
    grafo = Grafo()
    if not os.path.exists(nombre_archivo):
        print(f"⚠️ Archivo '{nombre_archivo}' no encontrado. El grafo estará vacío.")
        return grafo
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            if ":" in linea:
                origen, conexiones_str = linea.strip().split(":")
                conexiones = conexiones_str.split(";")
                for conexion in conexiones:
                    if conexion.strip():
                        partes = conexion.strip().split(",")
                        if len(partes) >= 2:
                            destino = partes[0].strip()
                            distancia = float(partes[1].strip())
                            costo = float(partes[2].strip()) if len(partes) > 2 else 0.0
                            grafo.agregar_arista(origen.strip(), destino, distancia, costo)
    return grafo

def guardar_grafo_en_archivo(nombre_archivo, grafo):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        for origen in grafo.vertices:
            conexiones = []
            for destino, datos in grafo.vertices[origen].items():
                conexiones.append(f"{destino},{datos['distancia']},{datos['costo']}")
            f.write(f"{origen}:{';'.join(conexiones)}\n")
