# flake8: noqa
import re
import sys

from colorama import init, Fore

init()

MODULE_REGEX = r"^[_a-zA-Z][-_a-zA-Z0-9]+$"
DNS_REGEX = r"^[\-a-zA-Z]+$"

project_slug_name = "{{cookiecutter.project_name_slug}}"
project_dsn_name = "{{cookiecutter.project_name_dns}}"

if not re.match(MODULE_REGEX, project_slug_name):
      print(re.search(MODULE_REGEX, project_slug_name))     
      print(Fore.RED +
            f"ERROR: Project slug name ({project_slug_name}) must not have any special character."
      )

      # Exit to cancel project
      sys.exit(1)

if not re.match(DNS_REGEX, project_dsn_name):
      print(Fore.RED +
            f"ERROR: Project DNS name ({project_dsn_name}) must not have underscore (_) or numbers."
      )
      # Exit to cancel project
      sys.exit(1)
