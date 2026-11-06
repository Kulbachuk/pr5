"""Views додатка pages."""

from django.http import HttpResponse


def index(request):
    """Головна сторінка."""
    html_content = """
    <!DOCTYPE html>
    <html lang="uk">
    <head><meta charset="UTF-8"><title>Головна</title></head>
    <body>
        <h1>Ласкаво просимо до нашого Django-сайту!</h1>
        <p>Це навчальний веб-проект, створений в рамках практичної роботи №5.</p>
        <h3>Основні розділи:</h3>
        <ul>
            <li><a href="/">Головна сторінка</a></li>
            <li><a href="/about/">Про проект</a></li>
            <li><a href="/contact/?name=Даниїл">Контакти (з параметром)</a></li>
        </ul>
    </body>
    </html>
    """
    return HttpResponse(html_content)


def about(request):
    """Сторінка 'Про проект'."""
    html_content = """
    <!DOCTYPE html>
    <html lang="uk">
    <head><meta charset="UTF-8"><title>Про проект</title></head>
    <body>
        <h1>Інформація про проект</h1>
        <p><strong>Назва курсу:</strong> Програмування (Python Web)</p>
        <p><strong>Номер практичної:</strong> Практична робота №5</p>
        <p><strong>Студент:</strong> Кульбачук Даниїл Сергійович</p>
        <p><strong>Група:</strong> ФІКб-1-24</p>
        <p><a href="/">← Повернутися на головну</a></p>
    </body>
    </html>
    """
    return HttpResponse(html_content)


def contact(request):
    """Контактна сторінка з підтримкою GET-параметрів."""
    name = request.GET.get('name')
    if name:
        greeting = f"<h2>Вітаємо, {name}! Дякуємо, що звернулися до нас.</h2>"
    else:
        greeting = "<h2>Вітаємо, Гість! Заповніть параметр ?name=ВашеІм'я у URL.</h2>"

    html_content = f"""
    <!DOCTYPE html>
    <html lang="uk">
    <head><meta charset="UTF-8"><title>Контакти</title></head>
    <body>
        <h1>Зворотний зв'язок</h1>
        {greeting}
        <p>Зв'яжіться з нами через електронну пошту або форму.</p>
        <p><a href="/">← На головну</a></p>
    </body>
    </html>
    """
    return HttpResponse(html_content)