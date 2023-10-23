import sqlite3

CONN = sqlite3.connect('lib/')
CURSOR = CONN.cursor()
    
class Customer:

    def __init__(self, first_name="Chuck", last_name="Nicks"):
        self.id = None
        self.fname = first_name
        self.lname = last_name
    
    
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS customer(
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
        
    def save(self):
        sql = """
            INSERT INTO dogs (name, breed)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.breed))
        CONN.commit()
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM dogs").fetchone()[0]
    
        
    def given_name(self)
        return f'Customer: {self.fname}.'
    
    def family_name(self)
        return f"Customer's family name: {self.lname}."
    
    def full_name(self)
        return f"Customer's Full name: {self.fname} {self.lname}."
    
    
    
    
    
        
        
        
    
