from config.database import get_connection

class HospitalizacionConnection:
    def __init__(self):
        self.conn = get_connection()

    def read_all(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT id, fecha_hospitalizacion, hora_hospitalizacion, idpaciente, idhabitacion, fecha_alta, hora_alta FROM "hospitalizacion"
            """)
            return cur.fetchall()

    def read_one(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT id, fecha_hospitalizacion, hora_hospitalizacion, idpaciente, idhabitacion, fecha_alta, hora_alta FROM "hospitalizacion" WHERE id = %s
            """, (id,))
            return cur.fetchone()

    def write(self, data):
        try:
            with self.conn.cursor() as cur:
                cur.execute(""" 
                    INSERT INTO "hospitalizacion" (fecha_hospitalizacion, hora_hospitalizacion, idpaciente, idhabitacion, fecha_alta, hora_alta)
                    VALUES (%(fecha_hospitalizacion)s, %(hora_hospitalizacion)s, %(idpaciente)s, %(idhabitacion)s, %(fecha_alta)s, %(hora_alta)s)
                """, data)
            self.conn.commit()
        except Exception as e:
            print(f"Error executing query: {e}")
            self.conn.rollback()
            raise e

    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute(""" 
                DELETE FROM "hospitalizacion" WHERE id = %s
            """, (id,))
        self.conn.commit()

    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE "hospitalizacion" SET fecha_hospitalizacion = %(fecha_hospitalizacion)s, hora_hospitalizacion = %(hora_hospitalizacion)s,
                idpaciente = %(idpaciente)s, idhabitacion = %(idhabitacion)s, fecha_alta = %(fecha_alta)s, hora_alta = %(hora_alta)s
                WHERE id = %(id)s
            """, data)
        self.conn.commit()

    def __del__(self):
        if self.conn:
            self.conn.close()
