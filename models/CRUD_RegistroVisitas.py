from config.database import get_connection

class RegistroVisitasConnection:
    def __init__(self):
        self.conn = get_connection()

    def read_all(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT id, fecha_entrada, hora_entrada, idvisitante, idpaciente, fecha_salida, hora_salida FROM "registrovisitas"
            """)
            return cur.fetchall()

    def read_one(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT id, fecha_entrada, hora_entrada, idvisitante, idpaciente, fecha_salida, hora_salida FROM "registrovisitas" WHERE id = %s
            """, (id,))
            return cur.fetchone()

    def write(self, data):
        try:
            with self.conn.cursor() as cur:
                cur.execute(""" 
                    INSERT INTO "registrovisitas" (fecha_entrada, hora_entrada, idvisitante, idpaciente, fecha_salida, hora_salida)
                    VALUES (%(fecha_entrada)s, %(hora_entrada)s, %(idvisitante)s, %(idpaciente)s, %(fecha_salida)s, %(hora_salida)s)
                """, data)
            self.conn.commit()
        except Exception as e:
            print(f"Error executing query: {e}")
            self.conn.rollback()
            raise e

    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute(""" 
                DELETE FROM "registrovisitas" WHERE id = %s
            """, (id,))
        self.conn.commit()

    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE "registrovisitas" SET fecha_entrada = %(fecha_entrada)s, hora_entrada = %(hora_entrada)s,
                idvisitante = %(idvisitante)s, idpaciente = %(idpaciente)s, fecha_salida = %(fecha_salida)s, hora_salida = %(hora_salida)s
                WHERE id = %(id)s
            """, data)
        self.conn.commit()

    def __del__(self):
        if self.conn:
            self.conn.close()
