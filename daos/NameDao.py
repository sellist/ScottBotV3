import psycopg2


class NameDao(object):
    def __init__(self, db: str, username: str, password: str):
        self.connection = psycopg2.connect(dbname=db, user=username, password=password)

    def get_name(self):
        with (self.connection.cursor()) as curr:
            try:
                curr.execute("select name from names offset random() * (select count(*) from names) limit 2;")
                result = curr.fetchall()
                self.connection.commit()
            except Exception as e:
                print(e)
                self.connection.rollback()

        return " ".join([x[0] for x in result])

    def add_name(self, arg: str) -> bool:
        with (self.connection.cursor()) as curr:
            try:
                curr.execute("INSERT INTO names (name) VALUES (%s) RETURNING name_id", (arg,))
                result = curr.fetchall()[0][0]
                self.connection.commit()
            except Exception as e:
                print(e)
                self.connection.rollback()
        return result is not None
