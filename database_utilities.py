from abc import ABC, abstractmethod
from typing import TypeAlias, Any

sandbox_submission: TypeAlias = [bool, Any]

def sandbox(func) -> sandbox_submission:
    def execute(*args, **kwargs):
        try:
            return True, func(*args, **kwargs)
        except Exception as e:
            return False, str(e) # option to log here
            
    return execute

class Database(ABC):
    @staticmethod
    def execute(fxn_ptr, *args, **kwargs):
        try:
            return True, fxn_ptr(*args, **kwargs)
        except Exception as e:
            return False, str(e)
    
    def __init__(self, database_path: str, connection_pool: int):
        self.database_path = database_path
        self.connection_pool = connection_pool
        # self.conn = self.get_connection()
        # self.cursor = self.get_cursor()
        # self.create_tables()
        
    # @sandbox
    @abstractmethod
    def get_connection(self):
        # return sqlite3.connect(self.database_path)
        pass
      
    # @sandbox
    @abstractmethod      
    def get_cursor(self):
        pass # return self.conn.cursor()
        
    # @sandbox
    @abstractmethod
    def load_connection_pool(self):
        pass
        
    # Lookup type of sql query/queries
    # Need to instantiate conn and cursor in subclasses
    @sandbox
    def execute(self, query: str, data: tuple = (), many: bool = False, _return: bool = False) -> Any:
        if many:
            if _return:
                return self.cursor.executemany(query, data)
            else:
                self.cursor.executemany(query, data)
        else:
            if _return:
                return self.cursor.execute(query, data)
            else:
                if len(data):
                    self.cursor.execute(query, data)
                else:
                    self.cursor.execute(query)
                    
        self.conn.commit()
        
    # insertion or creation
    def insert(self, query: str, data: tuple = ()) -> Any:
        if len(data):
            self.execute(query, data)
        else:
            self.execute(query)
        
    def search(self, query) -> Any:
        return self.execute(query)
  
    def delete(self, query):
        self.execute(query)
        
    @sandbox
    def __del__(self):
        self.cursor.close()
        
class SQLite(Database):
    def __init__(self, database_path: str):
        super().__init__(database_path)
        
        self.conn = self.get_connection()
        self.cursor = self.get_cursor()
        
    # Look up type here!
    @sandbox
    def get_connection(self):
        return sqlite3.connect(self.database_path)
        
    @sandbox
    def get_cursor(self):
        return self.conn.cursor()
        
    @sandbox
    def load_connection_pool(self):
        pass
    
