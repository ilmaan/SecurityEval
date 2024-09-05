from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def update_profile(request):
    if request.method == 'POST':
        # Django's CSRF middleware will handle token validation
        return HttpResponse("Profile updated")
    return HttpResponse("GET request received")