# Santosh Portfolio - Django

A personal portfolio website built with Django, optimized for Vercel deployment.

## Features

- Responsive design with modern UI
- Search engine indexing prevention (noindex, robots.txt)
- Static file optimization for Vercel
- Custom 404 handling
- Automatic redirects to home page

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the development server:
   ```bash
   python manage.py runserver
   ```

3. Visit `http://127.0.0.1:8000/`

## Deployment to Vercel

1. Push your code to a Git repository (GitHub, GitLab, etc.)

2. Connect your repository to Vercel:
   - Go to [vercel.com](https://vercel.com)
   - Import your repository
   - Vercel will automatically detect the Django configuration

3. The deployment will:
   - Install Python dependencies from `requirements.txt`
   - Run the build script (`build_files.sh`)
   - Collect static files
   - Deploy the application

## Configuration Files

- `vercel.json` - Vercel deployment configuration
- `requirements.txt` - Python dependencies
- `build_files.sh` - Build script for static files
- `.gitignore` - Git ignore rules

## SEO Prevention

This site is configured to prevent search engine indexing:
- Meta robots tags in HTML
- X-Robots-Tag HTTP headers
- robots.txt file
- No meta description tags
