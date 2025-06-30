from django.shortcuts import render
from django.http import Http404

# Create your views here.

def home(request):
    """
    Render the main portfolio page (index_formatted.html equivalent)
    """
    return render(request, 'portfolio/index.html')

def custom_404(request, exception=None):
    """
    Custom 404 page with stylized design matching the portfolio
    """
    return render(request, 'portfolio/404.html', status=404)
