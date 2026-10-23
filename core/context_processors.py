from .models import SiteSettings

def global_context(request):
    # Gestion de la langue
    lang_param = request.GET.get('lang')
    if lang_param in ['fr', 'en']:
        request.session['lang'] = lang_param
        request.session.modified = True
    current_lang = request.session.get('lang', 'en')

    return {
        'settings': SiteSettings.load(),
        'lang': current_lang,
    }