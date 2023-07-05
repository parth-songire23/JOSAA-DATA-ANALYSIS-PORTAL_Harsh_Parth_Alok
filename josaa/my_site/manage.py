#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# #!/usr/bin/env python
# """Django's command-line utility for administrative tasks."""
# import os
# import sys


# def main():
#     """Run administrative tasks."""
#     os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site.settings')
#     try:
#         if sys.argv[1] == 'runserver':
#             from django.core.management.commands.runserver import Command as runserver
#             runserver.default_addr = "0.0.0.0"
#             runserver.default_port = "8000"
#             runserver.default_ipv6 = False
#             runserver.use_ipv6 = False
#             runserver.default_ssl_certificate = None
#             runserver.default_ssl_private_key = None
#             runserver.default_threading = False
#             runserver.default_wsgi_apps = False
#             runserver.default_max_age = None
#             sys.argv[1] = 'runserver'
#             from django.core.management import execute_from_command_line
#         else:
#             from django.core.management import execute_from_command_line
#     except ImportError as exc:
#         raise ImportError(
#             "Couldn't import Django. Are you sure it's installed and "
#             "available on your PYTHONPATH environment variable? Did you "
#             "forget to activate a virtual environment?"
#         ) from exc
#     execute_from_command_line(sys.argv)


# if __name__ == '__main__':
#     main()
