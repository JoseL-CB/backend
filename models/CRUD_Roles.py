from config.database import get_connection

class RolesConnection:
    def __init__(self):
        self.conn = get_connection()

    def read_all(self):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM "roles"
            """)
            return cur.fetchall()

    def read_one(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                SELECT * FROM "roles" WHERE id = %s
            """, (id,))
            return cur.fetchone()

    def write(self, data):
        try:
            with self.conn.cursor() as cur:
                cur.execute(""" 
                    INSERT INTO "roles" (namerol)
                    VALUES (%(namerol)s)
                """, data)
            self.conn.commit()
        except Exception as e:
            print(f"Error executing query: {e}")
            self.conn.rollback()
            raise e

    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute(""" 
                DELETE FROM "roles" WHERE id = %s
            """, (id,))
        self.conn.commit()

    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE "roles" SET namerol = %(namerol)s
                WHERE id = %(id)s
            """, data)
        self.conn.commit()

    def __del__(self):
        if self.conn:
            self.conn.close()
