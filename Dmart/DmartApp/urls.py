from django.conf.urls import url
import views

urlpatterns = [
    url('getusers/', views.showAllEmployees),
    url('createuser/', views.emp),
    

]