import sqlite3

# Cambia "tu_nombre" por tu nombre (sin espacios)
tu_nombre = "tu_nombre"
db_name = f"reto_{tu_nombre}.db"

events = [
    "Inicio sistema",
    "Carga completa",
    "Error detectado",
    "Conexión establecida",
    "Usuario autenticado",
    "Usuario desconectado",
    "Backup iniciado",
    "Backup finalizado",
    "Actualización disponible",
    "Actualización aplicada",
    "Reinicio programado",
    "Reinicio completado",
    "Lectura de sensor",
    "Escritura en disco",
    "Permiso denegado",
    "Permiso otorgado",
    "Archivo subido",
    "Archivo descargado",
    "Sesión expirada",
    "Sesión extendida",
    "Plugin instalado",
    "Plugin eliminado",
    "Prueba de integridad",
    "Integridad ok",
    "Integridad fallida",
    "Notificación enviada",
    "Notificación fallida",
    "Pool de conexiones lleno",
    "Pool de conexiones liberado",
    "Monitoreo activado",
]

conn = sqlite3.connect(db_name)
cur = conn.cursor()

# Crear tabla (reinicia si ya existía)
cur.execute("DROP TABLE IF EXISTS LOGS;")
cur.execute("""
CREATE TABLE LOGS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    evento TEXT NOT NULL
);
""")

cur.executemany("INSERT INTO LOGS (evento) VALUES (?);", [(e,) for e in events])
conn.commit()
conn.close()

print(f"Base de datos creada: {db_name} con {len(events)} filas en la tabla LOGS.")