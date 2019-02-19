import sqlite3
import logging
import sys
from sqlalchemy import create_engine

sys.path.append(".")



class DBStore:


    def __init__(self,DBFile='DB/SampleDB.db'):
        self.db=DBFile
        logging.debug('Connecting to DB : %s',self.db)
        self.conn=sqlite3.connect(self.db)

        #Sqlalchemy
        connection_string = 'sqlite:///'+DBFile
        self.engine = create_engine(connection_string)
        self.connection = self.engine.connect()
        self.engine.echo = False
        ###########

        self.curr=self.conn.cursor()

        logging.info("Opened database successfully")

    def info(self):
        print ('In between')
        pass

    def createTable(self,createString):
        '''
        Example:
        createString="CREATE TABLE COMPANY
                 (ID INT PRIMARY KEY     NOT NULL,
                 NAME           TEXT    NOT NULL,
                 AGE            INT     NOT NULL,
                 ADDRESS        CHAR(50),
                 SALARY         REAL);"

        :param createString:
        :return:
        '''
        logging.debug("Creating table with sql : %s",createString)
        self.conn.execute(createString)
        logging.info("Table created successfully")

    def saveIt(self,insertString):
        '''This can be used for insert, update and delete data '''
        logging.debug(" Updating DB with sql : %s", insertString)
        self.curr.execute(insertString)
        self.conn.commit()
        logging.info('DB updated')

    def find(self,searchString):
        logging.debug(" Searching DB with sql : %s",searchString)
        result=self.curr.execute(searchString)
        logging.info("Record found")
        return result
    def findChemy(self,searchString):
        logging.debug(" Searching DB with sql with sqlalchemy : %s", searchString)
        result = self.connection.execute(searchString)
        logging.debug("Record found")
        return result


    def remove(self,tableName):
        '''This can be used dropping any table if existes'''
        logging.debug("Dropping table : %s", tableName)
        self.curr.execute("DROP TABLE IF EXISTS "+tableName)
        self.conn.commit()
        logging.info('Table removed')

    def __del__(self):
        self.conn.close()
        self.connection.close()
        logging.info("Closed database successfully")

if __name__ == "__main__":

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s: %(levelname)s : %(message)s"
    )

    data=DBStore('./Test.db')
    data.info()
    # tbstring='''CREATE TABLE IF NOT EXISTS COMPANY
    #                  (ID INT PRIMARY KEY     NOT NULL,
    #                  NAME           TEXT    NOT NULL,
    #                  AGE            INT     NOT NULL,
    #                  ADDRESS        CHAR(50),
    #                  SALARY         REAL);'''
    # data.createTable(tbstring)
    # val=[3,'Abk',24,10000]
    #
    # # sql = "INSERT INTO COMPANY(id,name, age, salary) VALUES({}, '{}', {}, {})".format(*val)
    # # data.saveIt(sql)
    # sql="SELECT id, name, age, salary from COMPANY where id=8"
    # result=data.find(sql)
    # oneitem=result.fetchone()
    # # oneitem.count(0)
    # if oneitem:
    #     print ("got it")
    # for row in result:
    #     print (row)
