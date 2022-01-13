import sqlite3 
from helper import resource_path 
def create_connection(name): 
    db = sqlite3.connect(resource_path('databases\\data.sqlite')) 
def load_responce(index): 
    db = sqlite3.connect(resource_path('databases\\responces.sqlite')) 
    c = db.cursor() 
    c.execute(F"SELECT * FROM answers_data;")
    x = filter(lambda x: x[1] == str(index), c.fetchall()) 
    for i in x: 
        responce = i[0] 
    return responce