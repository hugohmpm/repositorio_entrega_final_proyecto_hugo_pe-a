import sqlite3
import random

# FUNCIONES


def mostrar_camion(camion: dict):
    print(f"Serial del motor: {
          camion[0]} - Modelo: {camion[1]} - Patente: {camion[2]} - Kilometraje: {camion[3]}")


def cargar_nuevo_camion():
    # CARGA DE DATOS
    print("Cargar nuevo camion")
    modelo_camion = str(input("Ingrese el modelo del camion: "))
    patente_camion = str(input("Ingrese la patente incluyendo el guion: "))
    kilometraje_camion = int(input("Ingrese el kilometraje del camion: "))
    serial_motor_camion = abs(random.randint(1, 100000000000))

    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO flota_camiones (serial_motor, modelo, patente, kilometraje) values (?, ?, ?, ?)                   
    """, (serial_motor_camion, modelo_camion, patente_camion, kilometraje_camion))

    conexion.commit()
    cursor.close()

    print("Camion agregado exitosamente")


def mostrar_flota():
    print("Flota de camiones")
    cursor = conexion.cursor()
    cursor.execute(
        "SELECT serial_motor, modelo, patente, kilometraje FROM flota_camiones")
    flota_camiones_db = cursor.fetchall()

    for camion in flota_camiones_db:
        mostrar_camion(camion)

    cursor.close()


def borrar_camion():
    patente = str(
        input("Ingrese la patente del camion que desea eliminar incluyendo el guion: "))

    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM flota_camiones where patente=?", (patente,))

    patentes_encontradas = cursor.fetchall()

    if len(patentes_encontradas) == 0:
        print("La patente no fue encontrada")
        return

    cursor.execute(
        "DELETE FROM flota_camiones WHERE patente=?", (patente,))
    conexion.commit()
    cursor.close()
    print("Camion eliminado con exito")


def editar_kilometraje_camion():
    patente = str(
        input("Ingrese la patente del camion a modificar incluyendo el guion: "))

    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM flota_camiones where patente=?", (patente,))

    patentes_encontradas = cursor.fetchall()

    if len(patentes_encontradas) == 0:
        print("La patente no fue encontrada")
        return

    kilometros = int(input("Indique los kilometros actualizados: "))

    cursor.execute(
        "UPDATE flota_camiones SET kilometraje=? where patente=?", (kilometros, patente))
    conexion.commit()
    cursor.close()
    print("Kilometraje actualizado con exito")


def reporte_mantenimiento_preventivo():
    kilometraje_mantenimiento = int(
        input("Ingrese el kilometraje al cual se requiere mantenimiento preventivo: "))

    cursor = conexion.cursor()
    cursor.execute(
        "SELECT serial_motor, modelo, patente, kilometraje FROM flota_camiones where kilometraje >= ?", (kilometraje_mantenimiento,))

    flota_camiones_db = cursor.fetchall()

    if len(flota_camiones_db) == 0:
        print("Por el momento no hay ningun camion que requiera mantenimiento preventivo")
        return

    print("Los siguientes camiones requieren mantenimiento preventivo: ")
    for camion in flota_camiones_db:
        mostrar_camion(camion)

    cursor.close()


def buscar_por_patente():
    patente_a_buscar = str(
        input("Ingrese la patente del vehiculo a consultar incluyendo el guion: "))
    encontramos_patente = False

    cursor = conexion.cursor()
    cursor.execute(
        "SELECT serial_motor, modelo, patente, kilometraje FROM flota_camiones where patente=?", (patente_a_buscar,))

    patentes_halladas = cursor.fetchall()

    if len(patentes_halladas) == 0:
        print("La patente no fue encontrada")
        return
    for camion in patentes_halladas:
        print("Detalles del camion consultado: ")
        mostrar_camion(camion)


# INICIA LA APLICACION:

conexion = sqlite3.connect("flota_camiones_db.db")

listado_productos = []
opcion = "in"

# MENU PRINCIPAL
while opcion != "0":
    print("""
    Menú control de flota:
          1 - Agregar un camion a la flota
          2 - Mostrar flota
          3 - Buscar por patente
          4 - Editar kilometraje de un camion
          5 - Eliminar camion de la flota
          6 - Reporte de mantenimiento preventivo
          0 - Salir
    """)
    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        cargar_nuevo_camion()
    elif opcion == "2":
        mostrar_flota()
    elif opcion == "3":
        buscar_por_patente()
    elif opcion == "4":
        editar_kilometraje_camion()
    elif opcion == "5":
        borrar_camion()
    elif opcion == "6":
        reporte_mantenimiento_preventivo()
    elif opcion == "0":
        print("Gracias por usar la app")

        conexion.close()
    else:
        print("Oops, seleccionaste una opcion invalida.")
