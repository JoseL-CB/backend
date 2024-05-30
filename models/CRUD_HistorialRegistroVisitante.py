from config.database import get_connection

class HistorialRegistroVisitanteConnection:
    def __init__(self):
        self.conn = get_connection()

    def read_all(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM "historialregistrovisitante"
            """)
            return cur.fetchall()

    def read_one(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM "historialregistrovisitante" WHERE idperfilusuario = %s
            """, (id,))
            return cur.fetchone()

    def write(self, data):
        try:
            with self.conn.cursor() as cur:
                cur.execute(""" 
                    INSERT INTO "historialregistrovisitante" (idperfilusuario, idregistrovisita)
                    VALUES (%(idperfilusuario)s, %(idregistrovisita)s)
                """, data)
            self.conn.commit()
        except Exception as e:
            print(f"Error executing query: {e}")
            self.conn.rollback()
            raise e

    def delete(self, idperfilusuario, idregistrovisita):
        with self.conn.cursor() as cur:
            cur.execute(""" 
                DELETE FROM "historialregistrovisitante" WHERE idperfilusuario = %s AND idregistrovisita = %s
            """, (idperfilusuario, idregistrovisita))
        self.conn.commit()

    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE "historialregistrovisitante" SET idregistrovisita = %(idregistrovisita)s
                WHERE idperfilusuario = %(idperfilusuario)s
            """, data)
        self.conn.commit()

    def __del__(self):
        if self.conn:
            self.conn.close()
