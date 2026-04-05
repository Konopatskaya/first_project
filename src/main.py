print('Hello from repository! All is good!')

from dotenv import load_dotenv 
import os  
def print_author():
    # Загружаем переменные из файла .env
    
    load_dotenv(dotenv_path='C:/Kat/DataMining/work_terminal/project2/.env')
	    
    # Получаем значение переменной AUTHOR и присваиваем его переменной author
    author = os.getenv('AUTHOR')
    
    print(f"Автор проекта: {author}")
	
# Вызов функции для проверки её работы
print_author()
