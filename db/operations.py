from db.db import get_connection

def guardar_actividad(activity_data):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO todo (title, description) VALUES (%s, %s)",
                (activity_data["title"], activity_data["description"])
            )
        conn.commit()
        return True
    except Exception as e:
        print(f"Error al guardar actividad: {e}")
        conn.rollback()
        return False
    finally:
        conn.close()

def obtener_actividades():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
            SELECT id, title, description, 
                   TO_CHAR(created_at, 'DD/MM/YYYY') as fecha
            FROM todo 
            ORDER BY created_at DESC
            """)
            return cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener actividades: {e}")
        return []
    finally:
        conn.close()