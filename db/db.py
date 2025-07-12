import psycopg2
from psycopg2 import OperationalError

DB_CONFIG = {
    "dbname": "postgres",  
    "user": "postgres",
    "password": "Arturo27",
    "host": "localhost",
    "port": "5432"
}

def create_database():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        conn.autocommit = True 
        cursor = conn.cursor()
        
        cursor.execute("SELECT 1 FROM pg_database WHERE datname='actividades'")
        if not cursor.fetchone():
            cursor.execute("CREATE DATABASE actividades")
            print("Base de datos 'actividades' creada exitosamente")
        
        cursor.close()
    except OperationalError as e:
        print(f"\n¡Error de conexión inicial!\nVerifica que:")
        print(f"1. PostgreSQL esté corriendo")
        print(f"2. El usuario y contraseña sean correctos")
        print(f"3. No haya bloqueo de firewall\n")
        raise e
    finally:
        if 'conn' in locals():
            conn.close()

def get_connection():
    config = DB_CONFIG.copy()
    config["dbname"] = "actividades"
    try:
        return psycopg2.connect(**config)
    except OperationalError as e:
        print(f"\n¡Error al conectar a 'actividades'!\n")
        raise e

def init_db():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS todo (
                id SERIAL PRIMARY KEY,
                title VARCHAR(100) NOT NULL,
                description TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """)
            cursor.execute("""
            ALTER TABLE todo DROP COLUMN IF EXISTS activity_date;
            """)
        conn.commit()
        print("Tabla 'todo' configurada correctamente")
    except Exception as e:
        print(f"Error al inicializar DB: {e}")
        conn.rollback()
    finally:
        conn.close()