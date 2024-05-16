from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('', include('courses_app.urls')),
    path('', include('members_app.urls'))
]