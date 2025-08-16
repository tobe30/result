from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student, Result
from core.forms import CheckResult
from django.contrib.auth.decorators import login_required
from core.utils import student_login_required



@student_login_required
def index(request):
    
    return render(request, "dashboard/index.html")

def student_login(request):
    if request.method == "POST":
        reg_number = request.POST.get("reg_number")
        password = request.POST.get("password")

        try:
            student = Student.objects.get(reg_number=reg_number, password=password)
            # Save session
            request.session["student_id"] = student.id
            request.session["student_name"] = student.name
            return redirect("core:index")  # redirect to dashboard
        except Student.DoesNotExist:
            messages.error(request, "Invalid Registration Number or Password")

    return render(request, "dashboard/login.html")


@student_login_required
def student_dashboard(request):
    student_id = request.session.get("student_id")
    student = Student.objects.get(id=student_id)

    return render(request, "dashboard/index.html", {"student": student})


@student_login_required
def check_result(request):
    if request.method == 'POST':
        form = CheckResult(request.POST)
        if form.is_valid():
            session = form.cleaned_data['session'].id
            semester = form.cleaned_data['semester'].id

            return redirect('core:result_page', session_id=session, semester_id=semester)
    else:
        form = CheckResult()

    return render(request, "dashboard/check_result.html", {'form': form})


@student_login_required
def my_result(request, session_id, semester_id):
    # get student from session
    student_id = request.session.get("student_id")
    if not student_id:
        return redirect("dashboard:student_login")

    student = Student.objects.get(id=student_id)

    results = Result.objects.filter(
        student=student,
        session_id=session_id,
        semester_id=semester_id
    ).select_related('course')

    if not results.exists():
        messages.error(request, "Result not found for the selected session and semester.")
        return redirect('core:check_result')

    context = {
        'results': results,
        'student': student,
        'session': results.first().session,
        'semester': results.first().semester,
    }
    return render(request, 'dashboard/result_page.html', context)


def student_logout(request):
    request.session.flush()
    return redirect("core:login")
