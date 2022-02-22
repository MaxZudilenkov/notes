from django.urls import path

from mainapp.views import RegisterUserView, show_main_page, UserLoginView, user_logout, add_note

urlpatterns = [
    path('registration/', RegisterUserView.as_view(), name='registration', ),
    path('login/', UserLoginView.as_view(), name='login', ),
    path('logout/', user_logout, name='logout', ),
    path('add_note/', add_note, name='add_note', ),
    path('', show_main_page, name='main', )

]
