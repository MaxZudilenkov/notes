from django.urls import path

from mainapp.views import RegisterUserView, show_main_page

urlpatterns = [
    path('registration/', RegisterUserView.as_view(), name='registration', ),
    path('', show_main_page, name='main', )

]
