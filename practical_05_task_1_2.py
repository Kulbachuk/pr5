"""Генератор requirements.txt з перевіркою залежностей."""

import json
import os
import subprocess
import sys


def get_installed_packages() -> list[dict]:
    """Повертає список встановлених пакетів з версіями."""
    result = subprocess.run(
        [sys.executable, '-m', 'pip', 'list', '--format=json'],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        return []
    return json.loads(result.stdout)


def generate_requirements(packages: list[dict], filename: str = 'requirements.txt'):
    """Записує пакети у файл requirements.txt."""
    system_packages = {'pip', 'setuptools', 'wheel'}
    filtered_packages = [
        pkg for pkg in packages if pkg['name'].lower() not in system_packages
    ]
    
    with open(filename, 'w', encoding='utf-8') as f:
        for pkg in filtered_packages:
            f.write(f"{pkg['name']}=={pkg['version']}\n")


def verify_requirements(filename: str = 'requirements.txt') -> bool:
    """Перевіряє наявність пакетів з requirements.txt."""
    if not os.path.exists(filename):
        print(f"Файл {filename} не знайдено!")
        return False

    installed_map = {pkg['name'].lower(): pkg['version'] for pkg in get_installed_packages()}
    all_ok = True

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '==' in line:
                name, req_version = line.split('==', 1)
                name_key = name.lower()
                if name_key not in installed_map:
                    print(f"  ✗ Пакет {name} відсутній")
                    all_ok = False
                elif installed_map[name_key] != req_version:
                    print(f"  ⚠ Розбіжність версії {name}: {installed_map[name_key]} != {req_version}")
                    all_ok = False
    return all_ok


def main():
    packages = get_installed_packages()
    print(f"Знайдено {len(packages)} встановлених пакетів\n")

    for pkg in packages[:10]:
        print(f"  {pkg['name']}=={pkg['version']}")
    if len(packages) > 10:
        print(f"  ... та ще {len(packages) - 10}")

    generate_requirements(packages)
    print(f"\nФайл requirements.txt оновлено")

    ok = verify_requirements()
    print(f"Перевірка залежностей: {'✓ Усе OK' if ok else '✗ Є розбіжності'}")


if __name__ == "__main__":
    main()