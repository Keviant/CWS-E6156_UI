import pymysql

import os


class ColumbiaStudentResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        usr = os.environ.get("root")
        pw = os.environ.get("Kevinsekai232323***")
        h = os.environ.get("localhost")

        conn = pymysql.connect(
            user='root',
            password='Kevinsekai232323***',
            host='localhost',
            port=3306,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(key):

        sql = "SELECT * FROM f22_databases.columbia_students where guid=%s";
        conn = ColumbiaStudentResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result

