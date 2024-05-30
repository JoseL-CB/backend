from config.database import get_connection

class EstadoPacienteConnection:
    def __init__(self):
        self.conn = get_connection()

    def read_all(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM "estadopaciente"
            """)
            return cur.fetchall()

    def read_one(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM "estadopaciente" WHERE id = %s
            """, (id,))
            return cur.fetchone()

    def write(self, data):
        try:
            with self.conn.cursor() as cur:
                cur.execute(""" 
                    INSERT INTO "estadopaciente" (nombre)
                    VALUES (%(nombre)s)
                """, data)
            self.conn.commit()
        except Exception as e:
            print(f"Error executing query: {e}")
            self.conn.rollback()
            raise e

    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute(""" 
                DELETE FROM "estadopaciente" WHERE id = %s
            """, (id,))
        self.conn.commit()

    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE "estadopaciente" SET nombre = %(nombre)s
                WHERE id = %(id)s
            """, data)
        self.conn.commit()

    def __del__(self):
        if self.conn:
            self.conn.close()
