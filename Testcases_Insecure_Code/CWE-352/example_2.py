from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def update_profile(request):
    if request.method == 'POST':
        # Update profile without CSRF protection
        return HttpResponse("Profile updated")
    return HttpResponse("GET request received")