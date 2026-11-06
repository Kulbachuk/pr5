"""Порівняльний аналіз структури Django та Flask проектів."""

import os


def scan_directory(path: str, prefix: str = '') -> list[str]:
    """Рекурсивно сканує каталог та повертає дерево файлів."""
    tree = []
    ignored_items = {'__pycache__', 'venv', 'venv2', '.git', '.idea', 'db.sqlite3'}

    try:
        items = sorted(os.listdir(path))
    except PermissionError:
        return tree

    items = [item for item in items if item not in ignored_items and not item.endswith('.pyc')]

    for index, item in enumerate(items):
        is_last = (index == len(items) - 1)
        connector = '└── ' if is_last else '├── '
        full_path = os.path.join(path, item)

        if os.path.isdir(full_path):
            tree.append(f"{prefix}{connector}{item}/")
            new_prefix = prefix + ('    ' if is_last else '│   ')
            tree.extend(scan_directory(full_path, new_prefix))
        else:
            tree.append(f"{prefix}{connector}{item}")

    return tree


def analyze_project(path: str) -> dict:
    """Аналізує проект та збирає статистику."""
    stats = {
        'py_files': 0,
        'html_files': 0,
        'css_files': 0,
        'total_size': 0,
        'directories': [],
    }

    ignored_dirs = {'__pycache__', 'venv', 'venv2', '.git', '.idea'}

    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        stats['directories'].append(root)

        for file in files:
            if file.endswith('.pyc'):
                continue

            filepath = os.path.join(root, file)
            stats['total_size'] += os.path.getsize(filepath)

            if file.endswith('.py'):
                stats['py_files'] += 1
            elif file.endswith('.html'):
                stats['html_files'] += 1
            elif file.endswith('.css'):
                stats['css_files'] += 1

    stats['directories_count'] = len(stats['directories'])
    return stats


def compare_projects(django_path: str, flask_path: str):
    """Порівнює два проекти та виводить порівняльну таблицю."""
    print("=" * 60)
    print("ПОРІВНЯННЯ СТРУКТУРИ ПРОЕКТІВ")
    print("=" * 60)

    print(f"\n--- Django ({django_path}) ---")
    django_tree = scan_directory(django_path)
    for line in django_tree:
        print(line)
    django_stats = analyze_project(django_path)

    print(f"\n--- Flask ({flask_path}) ---")
    flask_tree = scan_directory(flask_path)
    for line in flask_tree:
        print(line)
    flask_stats = analyze_project(flask_path)

    print("\n" + "=" * 60)
    print(f"| {'Характеристика':<25} | {'Django':<12} | {'Flask':<12} |")
    print("|" + "-" * 27 + "|" + "-" * 14 + "|" + "-" * 14 + "|")
    print(f"| {'Файли Python (.py)':<25} | {django_stats['py_files']:<12} | {flask_stats['py_files']:<12} |")
    print(f"| {'Шаблони (.html)':<25} | {django_stats['html_files']:<12} | {flask_stats['html_files']:<12} |")
    print(f"| {'Стилі (.css)':<25} | {django_stats['css_files']:<12} | {flask_stats['css_files']:<12} |")
    print(f"| {'Кількість каталогів':<25} | {django_stats['directories_count']:<12} | {flask_stats['directories_count']:<12} |")
    print(f"| {'Розмір (байт)':<25} | {django_stats['total_size']:<12} | {flask_stats['total_size']:<12} |")
    print("=" * 60)


def main():
    django_path = 'mysite'
    flask_path = 'myflaskapp'

    if not os.path.isdir(django_path) or not os.path.isdir(flask_path):
        print("Каталоги не знайдено!")
        return

    compare_projects(django_path, flask_path)


if __name__ == "__main__":
    main()