from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views, HOD_views, STAFF_views, STUDENT_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    # Login-Path
    path('', views.LOGIN, name='login'),
    path('doLogin/', views.doLogin, name='doLogin'),
    path('doLogout', views.doLogout, name='logout'),

    # HOD Panel URLS
    path('hod/home/', HOD_views.HOME, name='hod_home'),
    path('hod/student/add', HOD_views.ADD_STUDENT, name='add_student'),
    path('hod/student/view', HOD_views.VIEW_STUDENT, name='view_student'),
    path('hod/student/edit<str:id>', HOD_views.EDIT_STUDENT, name='edit_student'),
    path('hod/student/update', HOD_views.UPDATE_STUDENT, name='update_student'),
    path('hod/student/delete<str:admin>',
         HOD_views.DELETE_STUDENT, name='delete_student'),
    path('hod/course/add', HOD_views.ADD_COURSE, name='add_course'),
    path('hod/course/view', HOD_views.VIEW_COURSE, name='view_course'),
    path('hod/course/delete<str:id>',
         HOD_views.DELETE_COURSE, name='delete_course'),

    path('hod/staff/add', HOD_views.ADD_STAFF, name='add_staff'),
    path('hod/staff/view', HOD_views.VIEW_STAFF, name='view_staff'),
    path('hod/staff/edit<str:id>', HOD_views.EDIT_STAFF, name='edit_staff'),
    path('hod/staff/update', HOD_views.UPDATE_STAFF, name='update_staff'),
    path('hod/staff/delete<str:admin>',
         HOD_views.DELETE_STAFF, name='delete_staff'),

    path('hod/subject/add', HOD_views.ADD_SUBJECT, name='add_subject'),
    path('hod/subject/view', HOD_views.VIEW_SUBJECT, name='view_subject'),
    path('hod/subject/edit<str:id>', HOD_views.EDIT_SUBJECT, name='edit_subject'),
    path('hod/subject/update', HOD_views.UPDATE_SUBJECT, name='update_subject'),
    path('hod/subject/delete<str:id>',
         HOD_views.DELETE_SUBJECT, name='delete_subject'),
    path('hod/staff/send_notification', HOD_views.STAFF_SEND_NOTOFICATION,
         name='staff_send_notification'),
    # Staff Panel URLS
    path('Staff/home', STAFF_views.HOME, name='staff_home'),
    path('Staff/take_attendance', STAFF_views.STAFF_TAKE_ATTENDANCE,
         name='staff_take_attendance'),
    path('Staff/save_attendance', STAFF_views.STAFF_SAVE_ATTENDANCE,
         name='staff_save_attendance'),
    path('Staff/view_attendance', STAFF_views.STAFF_VIEW_ATTENDANCE,
         name='staff_view_attendance'),
    path('Staff/Add_Result', STAFF_views.STAFF_ADD_RESULT,
         name='staff_add_result'),
    path('Staff/Save_Result', STAFF_views.STAFF_SAVE_RESULT,
         name='staff_save_result'),

    # Student Panels URLS
    path('student/home', STUDENT_views.HOME, name='student_home'),
    path('student/view_result', STUDENT_views.VIEW_RESULT,
         name='student_view_result'),
    path('student/hall_ticket', STUDENT_views.Hall_Ticket,
         name='student_hall_ticket'),
    path('student/fee_payment', STUDENT_views.FEE_PAYMENT,
         name='student_fee_payment'),

    # Profile
    path('Profile', views.PROFILE, name='profile'),
    path('Profile/update', views.PROFILE_UPDATE, name='profile_update'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
