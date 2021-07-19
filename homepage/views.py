from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils import translation

def home(request):
    LANG = translation.get_language().replace('-', '_')
    translation.activate(LANG)
    return render(request, 'homepage/home.html', {
        'lang':LANG,
        'is_login':request.session.get('is_login')
    })
