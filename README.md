# music-market

## Запуск бека

### Версия python: 3.9.7

1. **Создание виртуального окружения**
	

	    pip install virtualenv
	    cd ./server
	    python -m virtualenv venv
2. **Запуск виртуального окружения**

	### Linux
	    source ./venv/bin/activate

	### Windows
	    .\venv\Scripts\activate

 3. **Установка зависимостей**
 

	    
	    python -m pip install -r requirements.txt

3. **Запуск сервера**

	    python ./market_service/manage.py runserver
