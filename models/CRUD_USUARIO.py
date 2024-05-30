from config.database import get_connection


class UserConnection:
    def __init__(self):
        self.conn = get_connection()

    def read_all(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM "perfil_usuario"
            """)
            return cur.fetchall()

    def read_one(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM "perfil_usuario" WHERE id = %s
            """, (id,))
            return cur.fetchone()

    def write(self, data):
        try:
            with self.conn.cursor() as cur:
                cur.execute(""" 
                    INSERT INTO "perfil_usuario" (nombres, apellidos, fecha_nacimiento, cedula, email, password, sexo, roleid)
                    VALUES (%(nombres)s, %(apellidos)s, %(fecha_nacimiento)s, %(cedula)s, %(email)s, %(password)s, %(sexo)s, %(roleid)s) 
                """, data)
            self.conn.commit()
        except Exception as e:
            print(f"Error executing query: {e}")
            self.conn.rollback()
            raise e

    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute(""" 
                DELETE FROM "perfil_usuario" WHERE id = %s
            """, (id,))
        self.conn.commit()

    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE "perfil_usuario" SET nombres = %(nombres)s, apellidos = %(apellidos)s,
                fecha_nacimiento = %(fecha_nacimiento)s, cedula = %(cedula)s, email = %(email)s,
                password = %(password)s, sexo = %(sexo)s, roleid = %(roleid)s
                WHERE id = %(id)s
            """, data)
        self.conn.commit()

    def __del__(self):
        if self.conn:
            self.conn.close()

    def verify_credentials(self, cedula: int, password: str):
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    SELECT * FROM "perfil_usuario" WHERE cedula = %s AND password = %s
                """, (cedula, password))
                user = cur.fetchone()
                if user:
                    return user
                else:
                    return None
        except Exception as e:
            print(f"Error verifying credentials: {e}")
            raise
