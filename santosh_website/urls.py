"""
URL configuration for santosh_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Removed admin import for Vercel deployment
# from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

def redirect_to_home(request, path=''):
    """Redirect any unmatched URL to the home page"""
    return redirect('portfolio:home', permanent=False)

urlpatterns = [
    # Removed admin URL for Vercel deployment
    # path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    # Catch-all pattern - this should be last
    re_path(r'^.*/$', redirect_to_home),
]

handler404 = 'portfolio.views.custom_404'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
