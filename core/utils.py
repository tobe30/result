from django.shortcuts import redirect
from functools import wraps

def student_login_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if "student_id" not in request.session:
            return redirect("core:login")  # redirect if not logged in
        return view_func(request, *args, **kwargs)
    return wrapper
