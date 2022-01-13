import os 
import sys
def generate_paths(obj, vec='all'): 
    folder = f'{obj}\\{vec}' 
    names = os.listdir(folder) 
    paths = [os.path.join(folder, name) for name in names] 
    return paths 
def resource_path(relative_path):
    try: 
        base_path = sys._MEIPASS 
    except Exception: 
        base_path = os.path.abspath(".") 
    return os.path.join(base_path, relative_path) 
if __name__ =='__main__': 
    pass