from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def update_profile(request):
    if request.method == 'POST':
        if request.POST.get('csrftoken') != get_token(request):
            return HttpResponse("CSRF token mismatch", status=403)
        return HttpResponse("Profile updated")
    else:
        token = get_token(request)
        return HttpResponse(f"CSRF token: {token}")