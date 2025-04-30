from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    """
    Middleware that redirects users to login if they're not authenticated,
    unless they're on login or register pages.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        # URLs that are allowed even if not logged in
        allowed_paths = [reverse('login'), reverse('register')]

        if not request.user.is_authenticated and path not in allowed_paths:
            return redirect('login')

        response = self.get_response(request)
        return response