import sqlite3

conexion = sqlite3.connect("flota_camiones_db.db")

cursor = conexion.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS flota_camiones (
    serial_motor INTEGER NOT NULL PRIMARY KEY,
    modelo TEXT,
    patente TEXT UNIQUE,
    kilometraje INTEGER
)
""")

cursor.execute("""
INSERT INTO flota_camiones (serial_motor, modelo, patente, kilometraje) VALUES
    (ABS(RANDOM()), 'Ford SUPER DUTY', 'ABC-1234', 200507),
    (ABS(RANDOM()), 'Chevrolet 350', 'XYZ-5678', 362014),
    (ABS(RANDOM()), 'Triton', '1AB-2345', 452020),
    (ABS(RANDOM()), 'Nissan Patrol', 'QRS-8765', 132015),
    (ABS(RANDOM()), 'Honda CBH', '3JK-4567', 92000),
    (ABS(RANDOM()), 'BMW CSV', 'JKL-3456', 72005),
    (ABS(RANDOM()), 'Audi A400', '5GH-6789', 472004),
    (ABS(RANDOM()), 'Mercedes-Benz PTY', '9IJ-1239', 111992),
    (ABS(RANDOM()), 'Volkswagen BTM', '7RT-7890', 82002),
    (ABS(RANDOM()), 'Tesla CyberTruck', 'ZZZ-1111', 32021);
""")

conexion.commit()

cursor.close()

conexion.close()
