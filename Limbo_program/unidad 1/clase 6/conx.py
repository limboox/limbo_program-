import mysql.connector

try:
    # Datos de conexión
    conexion = mysql.connector.connect(
        host="localhost",      # Servidor
        user="root",           # Usuario de MySQL
        password="",           # Contraseña (en XAMPP suele estar vacía)
        database="persona",  # Tu base de datos
        port=3306              # Puerto (por defecto 3306)
    )

    if conexion.is_connected():
        print("✅ Conexión exitosa a la base de datos")
        cursor = conexion.cursor()
        print("📋 Tablas disponibles:")
        for tabla in cursor:
            print(tabla)

except Exception as e:
    print("❌ Error de conexión:", e)

finally:
    if 'conexion' in locals() and conexion.is_connected():
        conexion.close()
        print("🔌 Conexión cerrada")
