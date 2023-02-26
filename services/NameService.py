import os

from daos.NameDao import NameDao


class NameService(object):
    def __init__(self):
        self.nameDao = NameDao(
            os.getenv("DB_NAME"),
            os.getenv("DB_USER"),
            os.getenv("DB_PASS")
        )

    def get_name(self):
        return self.nameDao.get_name()

    def add_name(self, arg: str) -> bool:
        return self.nameDao.add_name(arg)
