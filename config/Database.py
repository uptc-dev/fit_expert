#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb

class Database:
    connection = ""
    cursor = ""
    def __init__(self, db_host, db_user, db_pass, db_name):
        self.db_host = db_host
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_name = db_name
        # Conexion automatica con la base de datos.
        if self.connect():
            print("Database connected.")
        else:
            print("Can't connect to database.")

    def connect(self):
        # Establece conexion con la base de datos.
        try:
            self.connection = MySQLdb.connect(self.db_host, self.db_user, self.db_pass, self.db_name)
            return True
        except:
            return False

    def executeQuery(self, query):
        # Creacion de un cursor.
        self.cursor = self.connection.cursor()
        # Ejecucion de una consulta.
        self.cursor.execute(query)
        if query.upper().startswith('SELECT'):
            # Seleccion de datos.
            data = self.cursor.fetchone()
        else:
            # Guarda cambios en la base de datos.
            self.connection.commit()
            data = None
        # Cierra el cursor
        self.cursor.close()
        return data
