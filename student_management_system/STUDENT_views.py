from django.shortcuts import render, redirect
from app.models import Student, StudentResult


def HOME(request):
    return render(request, 'STUDENT/home.html')


def VIEW_RESULT(request):
    student = Student.objects.get(admin=request.user.id)
    result = StudentResult.objects.filter(student_id=student)
    context = {
        'result': result,

    }
    return render(request, 'STUDENT/view_result.html', context)


def Hall_Ticket(request):

    # context = {
    #     'student': student,
    # }
    return render(request, 'STUDENT/hallticket.html')


def FEE_PAYMENT(request):
    return render(request, 'STUDENT/fee_payment.html')
