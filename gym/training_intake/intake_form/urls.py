# urls.py
from django.urls import path
from .views import intake_form_view, success_view, view_submitted_requests, submission_detail, index
from .views import signup, user_login, user_logout
urlpatterns = [
    path('', index, name='index'),
    path('create/', intake_form_view, name='intake_form'),
    path('success/', success_view, name='success'),
    path('submitted-requests/', view_submitted_requests, name='submitted_requests'),
    path('submission/<int:submission_id>/', submission_detail, name='submission_detail'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]