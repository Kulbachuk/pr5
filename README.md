# Практична робота №5: Створення та конфігурація веб-проєктів на Django і Flask

**Студент:** Кульбачук Даниїл Сергійович  


---

## 📌 Опис проєкту

Проєкт містить виконання усіх завдань з Практичної роботи №5, присвяченої створенню, конфігурації, порівняльному аналізу та налаштуванню веб-проєктів на Python за допомогою двох найпопулярніших фреймворків: **Django** (монолітний підхід «batteries-included») та **Flask** (мікрофреймворк з паттерном *Application Factory*).

---

## 📁 Структура проєкту

```text
пр5/
├── practical_05_task_1_1.py  # Скрипт перевірки Python та встановлених пакетів
├── practical_05_task_1_2.py  # Генератор requirements.txt та перевірка залежностей
├── practical_05_task_2_2.py  # Аналізатор settings.py та перевірка безпеки Django
├── practical_05_task_3_2.py  # Порівняльний аналізатор дерев та файлових статистик
├── requirements.txt          # Точний список фіксованих версій пакетів
│
├── mysite/                   # Проєкт на Django
│   ├── manage.py
│   ├── mysite/
│   │   ├── settings.py       # Головна конфігурація (змінено мову, timezone, apps)
│   │   └── urls.py           # Кореневий роутинг з підключенням pages
│   └── pages/                # Додаток Django
│       ├── views.py          # View-функції: index, about, contact (GET name)
│       └── urls.py           # Локальні маршрути додатка
│
└── myflaskapp/               # Проєкт на Flask
    ├── config.py             # Класи конфігурацій (Development, Production)
    ├── app.py                # Реалізація Application Factory (create_app)
    ├── static/               # Статичні файли (style.css)
    └── templates/            # HTML-шаблони
```

---

## 🚀 Налаштування та запуск

### 1. Створення та активація віртуального середовища

Віндовс (PowerShell):
```powershell
py -m venv venv
.\venv\Scripts\activate
```

### 2. Встановлення залежностей

```powershell
py -m pip install --upgrade pip
pip install -r requirements.txt
```

### 3. Запуск перевірочних та аналітичних скриптів

- **Перевірка наявності фреймворків (Task 1.1):**
  ```powershell
  py practical_05_task_1_1.py
  ```

- **Перевірка відтворюваності requirements.txt (Task 1.2):**
  ```powershell
  py practical_05_task_1_2.py
  ```

- **Аналіз налаштувань та безпеки Django (Task 2.2):**
  ```powershell
  py practical_05_task_2_2.py
  ```

- **Порівняльний аналіз Django та Flask проєктів (Task 3.2):**
  ```powershell
  py practical_05_task_3_2.py
  ```

---

## 🌐 Запуск Dev-серверів

### 🟢 Запуск Django-сервера
```powershell
cd mysite
py manage.py runserver
```
*Сервер буде доступний за адресою:* `http://127.0.0.1:8000/`

---

### 🔵 Запуск Flask-сервера
```powershell
cd myflaskapp
py app.py
```
*Сервер буде доступний за адресою:* `http://127.0.0.1:5000/`

---

## 📊 Результати порівняльного аналізу (Django vs Flask)

| Характеристика | Django (`mysite`) | Flask (`myflaskapp`) |
| :--- | :---: | :---: |
| **Файли Python (`.py`)** | 14 | 2 |
| **Кількість каталогів** | 4 | 1 |
| **Загальний розмір файлів** | ~8.2 КБ | ~1.7 КБ |
| **Архітектурний підхід** | Batteries-Included (Моноліт) | Microframework (Application Factory) |
| **Маршрутизація** | Декларативна у `urls.py` | Декоратори `@app.route()` |