"""
WSGI config for santosh_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

# Get the directory containing this file (santosh_website/)
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory (project root)
project_root = os.path.dirname(current_dir)

# Add project root to Python path
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'santosh_website.settings')

application = get_wsgi_application()

# Vercel expects either a handler or app variable
handler = application
app = application
