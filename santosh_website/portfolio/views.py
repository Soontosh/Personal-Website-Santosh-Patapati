from django.shortcuts import render
from django.http import Http404, HttpResponse

# Create your views here.

def home(request):
    """
    Render the main portfolio page (index_formatted.html equivalent)
    """
    response = render(request, 'portfolio/index.html')
    response['X-Robots-Tag'] = 'noindex, nofollow, noarchive, nosnippet'
    return response

def robots_txt(request):
    """
    Serve robots.txt to prevent search engine indexing
    """
    content = """User-agent: *
Disallow: /

# Prevent all search engines from indexing this site
User-agent: Googlebot
Disallow: /

User-agent: Bingbot
Disallow: /

User-agent: Slurp
Disallow: /

User-agent: DuckDuckBot
Disallow: /
"""
    return HttpResponse(content, content_type="text/plain")

def custom_404(request, exception=None):
    """
    Custom 404 page with stylized design matching the portfolio
    """
    return render(request, 'portfolio/404.html', status=404)
