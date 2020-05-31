from django.http import HttpResponse, Http404

def home(request):
    return HttpResponse("""
        <h1>Bienvenue sur DW Games</h1>
    """)
