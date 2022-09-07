# music-market

## Запуск бека

### Версия python: 3.9.7

 1. **Запуск виртуального окружения**

	### Linux
	    source ./server/venv/bin/activate

	### Windows
	    .\server\venv\Scripts\activate

 2. **Установка зависимостей**
 

	    
	    python -m pip install -r ./server/requirements.txt

3. **Запуск сервера**

	    python ./server/market_service/manage.py runserver
