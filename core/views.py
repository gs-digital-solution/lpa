from django.shortcuts import render, get_object_or_404
from .models import SiteSettings, Service, AboutBlock

def home(request):
    lang_param = request.GET.get('lang')
    if lang_param in ['fr', 'en']:
        request.session['lang'] = lang_param
        request.session.modified = True
    current_lang = request.session.get('lang', 'en')

    return render(request, 'home.html', {
        'settings': SiteSettings.load(),
        'services': Service.objects.filter(is_active=True),
        'about_blocks': AboutBlock.objects.all(),
        'lang': current_lang,
    })

def service_detail(request, slug):
    lang_param = request.GET.get('lang')
    if lang_param in ['fr', 'en']:
        request.session['lang'] = lang_param
        request.session.modified = True
    current_lang = request.session.get('lang', 'en')

    service = get_object_or_404(Service, slug=slug, is_active=True)

    return render(request, 'service_detail.html', {
        'settings': SiteSettings.load(),
        'service': service,
        'lang': current_lang,
    })

def about(request):
    return render(request, 'about.html', {
        'about_blocks': AboutBlock.objects.all(),
    })
    # Note : settings et lang sont gérés par le context processor maintenant !