import sqlite3

CONN = sqlite3.connect('lib/')
CURSOR = CONN.cursor()
    
class Customer:

    all = []
    
    def __init__(self, first_name="Chuck", last_name="Nicks"):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
    
    
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS customers(
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()
        
        
    def save(self):
        sql = """
            INSERT INTO customers (first_name, last_name)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.first_name, self.last_name))
        CONN.commit()
        self.id = CURSOR.execute("SELECT last_insert_rowid() FROM customers").fetchone()[0]
    
    @classmethod
    def create(cls, ):
        customer = Customer(name, first_name, last_name)
        customer.save()
        return customer
    
    @classmethod
    def new_from_db(cls, row):
         = cls(row[1], row[2])
        customer.id = row[0]
        return customer
    
    def given_name(self):
        return f'Customer: {self.first_name}.'
    
    def family_name(self):
        return f"Customer's family name: {self.last_name}."
    
    def full_name(self):
        firstname = self.first_name 
        lastname= self.last_name
        return firstname + " " + lastname
    
    @classmethod
    def all(cls):
        sql = """
            SELECT *
            FROM customers
        """
        all = CURSOR.execute(sql).fetchall()
        
        cls.all = [cls.new_from_db(row) for row in all]
        return cls.all
    
    
    
    
        
        
        
    
