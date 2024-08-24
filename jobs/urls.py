from django.urls import path

from jobs.views import HomeView, JobView

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path('jobs/', JobView.as_view(), name='jobs'),

]