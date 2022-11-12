# Руководство по работе с бэком

## Запуск бэка
---

### 1. Перейдите в директорию server

### 2. Активируйте виртуальное окружение
```bash
.\venv\Scripts\activate
```

### 3. Запустите сервер
```bash
python market_service/manage.py runserver
```

---

## Работа с админкой
---

### 1. Перейдите в директорию *server/market_service*

### 2. Создайте админа
```bash
python manage.py createsuperuser
```

### 3. Запустите сервер
```bash
python manage.py runserver
```

### 4. Перейдите по адресу http://127.0.0.1:8000/admin и пройдите авторизацию через созданного админа

### 5. Администратор по умолчанию
**login**: admin@admin.com
**password**: admin12345

---
