from multiprocessing import context
from django.shortcuts import render, redirect

from app.models import Staff, Subject, Session_Year, Student, Attendance, Attendance_Report, StudentResult


def HOME(request):
    return render(request, 'STAFF/home.html')


def STAFF_TAKE_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin=request.user.id)

    subject = Subject.objects.filter(staff=staff_id)
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session_year = None
    students = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')
            get_subject = Subject.objects.get(id=subject_id)
            get_session_year = Session_Year.objects.get(id=session_year_id)
            subject = Subject.objects.filter(id=subject_id)
            for i in subject:
                student_id = i.course.id
                students = Student.objects.filter(course_id=student_id)
    context = {
        'subject': subject,
        'session_yaer': session_year,
        'get_subject': get_subject,
        'get_session_year': get_session_year,
        'action': action,
        'students': students,

    }
    return render(request, 'STAFF/take_attendance.html', context)


def STAFF_SAVE_ATTENDANCE(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        attendance_date = request.POST.get('attendance_date')
        student_id = request.POST.getlist('student_id')
        get_subject = Subject.objects.get(id=subject_id)
        get_session_year = Session_Year.objects.get(id=session_year_id)
        attendance = Attendance(
            subject_id=get_subject,
            attendance_date=attendance_date,
            session_year_id=get_session_year
        )
        attendance.save()
        for i in student_id:
            stud_id = i
            int_stud = int(stud_id)

            p_students = Student.objects.get(id=int_stud)
            attendance_report = Attendance_Report(
                student_id=p_students,
                attendance_id=attendance,
                session_year_id=session_year_id
            )
            attendance_report.save()
    return redirect('staff_take_attendance')


def STAFF_VIEW_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff_id=staff_id)
    action = request.GET.get('action')
    get_subject = None
    attendance_date = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            attendance_date = request.POST.get('attendance_date')
            get_subject = Subject.objects.get(id=subject_id)
    context = {
        'staff_id': staff_id,
        'subject': subject,
        'attendance_date': attendance_date,
        'action': action,
        'get_subject': get_subject,
    }
    return render(request, 'STAFF/view_attendance.html', context)


def STAFF_ADD_ATTENDANCE(request):
    return render(request, 'STAFF/add_attendance.html')


def STAFF_ADD_RESULT(request):
    staff = Staff.objects.get(admin=request.user.id)

    subjects = Subject.objects.filter(staff_id=staff)
    session_year = Session_Year.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session = None
    students = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            session_year_id = request.POST.get('session_year_id')

            get_subject = Subject.objects.get(id=subject_id)
            get_session = Session_Year.objects.get(id=session_year_id)

            subjects = Subject.objects.filter(id=subject_id)
            for i in subjects:
                student_id = i.course.id
                students = Student.objects.filter(course_id=student_id)

    context = {
        'subjects': subjects,
        'session_year': session_year,
        'action': action,
        'get_subject': get_subject,
        'get_session': get_session,
        'students': students,
    }

    return render(request, 'Staff/add_result.html', context)


def STAFF_SAVE_RESULT(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        session_year_id = request.POST.get('session_year_id')
        student_id = request.POST.get('student_id')
        assignment_mark = request.POST.get('assignment_mark')
        Exam_mark = request.POST.get('Exam_mark')

        get_student = Student.objects.get(admin=student_id)
        get_subject = Subject.objects.get(id=subject_id)

        check_exist = StudentResult.objects.filter(
            subject_id=get_subject, student_id=get_student).exists()
        if check_exist:
            result = StudentResult.objects.get(
                subject_id=get_subject, student_id=get_student)
            result.assignment_mark = assignment_mark
            result.exam_mark = Exam_mark
            result.save()
            # messages.success(request, "Successfully Updated Result")
            return redirect('staff_add_result')
        else:
            result = StudentResult(student_id=get_student, subject_id=get_subject, exam_mark=Exam_mark,
                                   assignment_mark=assignment_mark)
            result.save()
            # messages.success(request, "Successfully Added Result")
            return redirect('staff_add_result')
