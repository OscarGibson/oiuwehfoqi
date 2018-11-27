from django.shortcuts import render

def login_required(f):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return render(request, 'default_pages/auth_required.html', {})
        return f(request, *args, **kwargs)
    return wrapper