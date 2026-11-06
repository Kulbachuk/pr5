"""Аналізатор конфігурації Django-проекту."""

import os
import sys
import re


def analyze_settings(settings_path: str) -> dict:
    """Аналізує файл settings.py та повертає ключові параметри."""
    config = {}
    with open(settings_path, 'r', encoding='utf-8') as f:
        content = f.read()

    debug_match = re.search(r'^DEBUG\s*=\s*(True|False)', content, re.MULTILINE)
    config['DEBUG'] = debug_match.group(1) if debug_match else 'Не знайдено'

    lang_match = re.search(r"^LANGUAGE_CODE\s*=\s*['\"]([^'\"]+)['\"]", content, re.MULTILINE)
    config['LANGUAGE_CODE'] = lang_match.group(1) if lang_match else 'Не знайдено'

    tz_match = re.search(r"^TIME_ZONE\s*=\s*['\"]([^'\"]+)['\"]", content, re.MULTILINE)
    config['TIME_ZONE'] = tz_match.group(1) if tz_match else 'Не знайдено'

    if 'django.db.backends.sqlite3' in content:
        config['DATABASE_ENGINE'] = 'SQLite3'
    else:
        config['DATABASE_ENGINE'] = 'Custom / Other'

    apps_match = re.search(r'INSTALLED_APPS\s*=\s*\[(.*?)\]', content, re.DOTALL)
    if apps_match:
        apps_raw = apps_match.group(1)
        apps_list = [app.strip().strip("'\"") for app in apps_raw.split(',') if app.strip()]
        config['INSTALLED_APPS'] = apps_list
    else:
        config['INSTALLED_APPS'] = []

    return config


def check_security(settings_path: str) -> list[str]:
    """Перевіряє базову безпеку конфігурації Django."""
    warnings = []
    with open(settings_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if re.search(r'^DEBUG\s*=\s*True', content, re.MULTILINE):
        warnings.append("DEBUG = True увімкнено! Це небезпечно для production.")

    if re.search(r"^SECRET_KEY\s*=\s*['\"]django-insecure-", content, re.MULTILINE):
        warnings.append("SECRET_KEY використовує дефолтний секретний ключ розробки.")

    if re.search(r'^ALLOWED_HOSTS\s*=\s*\[\s*\]', content, re.MULTILINE):
        warnings.append("ALLOWED_HOSTS порожній! Для запуску на сервері вкажіть домени.")

    return warnings


def main():
    settings_path = os.path.join('mysite', 'mysite', 'settings.py')
    if not os.path.exists(settings_path):
        print(f"Файл {settings_path} не знайдено!")
        sys.exit(1)

    config = analyze_settings(settings_path)
    print("=== Аналіз конфігурації Django ===\n")
    for key, value in config.items():
        if isinstance(value, list):
            print(f"  {key}:")
            for item in value:
                print(f"    - {item}")
        else:
            print(f"  {key}: {value}")

    print("\n=== Перевірка безпеки ===\n")
    warnings = check_security(settings_path)
    if warnings:
        for w in warnings:
            print(f"  ⚠ {w}")
    else:
        print("  ✓ Попереджень не знайдено")


if __name__ == "__main__":
    main()