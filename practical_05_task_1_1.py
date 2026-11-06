"""Скрипт перевірки середовища розробки."""

import sys
import importlib


def check_python_version():
    """Перевіряє версію Python (потрібна >= 3.10)."""
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro}")
    if version < (3, 10):
        print("  ⚠ ПОПЕРЕДЖЕННЯ: Рекомендовано використовувати Python 3.10 або новіше!")
    else:
        print("  ✓ Версія Python відповідає вимогам (>= 3.10)")


def check_package(package_name: str) -> bool:
    """Перевіряє, чи встановлено пакет, і виводить його версію."""
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, '__version__', 'невідома')
        print(f"  {package_name}: {version} ✓")
        return True
    except ImportError:
        print(f"  {package_name}: НЕ ВСТАНОВЛЕНО ✗")
        return False


def main():
    check_python_version()

    print("\nВстановлені пакети:")
    packages = ['django', 'flask']
    results = {pkg: check_package(pkg) for pkg in packages}

    installed_count = sum(results.values())
    missing_count = len(packages) - installed_count

    print(f"\nПідсумок: встановлено {installed_count}/{len(packages)} пакетів.")
    
    if missing_count > 0:
        missing_pkgs = [pkg for pkg, status in results.items() if not status]
        print("\nДля встановлення відсутніх пакетів виконайте команду:")
        print(f"  pip install {' '.join(missing_pkgs)}")


if __name__ == "__main__":
    main()