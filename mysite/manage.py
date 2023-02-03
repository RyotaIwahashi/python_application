#!/usr/bin/env python
"""
Django プロジェクトに対する様々な操作を行うためのコマンドラインユーティリティ
`django-admin startproject mysite`を実行すると生成される。

- シェルでDjangoと対話型で、インポートなどの処理を行う
`python manage.py shell`
- Djangoアプリケーションを起動する(第1引数でポート指定可能)
`python manage.py runserver`
- Djangoアプリケーションを新たに作成する
`python manage.py startapp <app名>`
- adminサイトにログインできるユーザを作成する
`python manage.py createsuperuser`
"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
