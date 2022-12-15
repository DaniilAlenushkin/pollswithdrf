from django.urls import path
from .apiviews import PollList, PollDetail

urlpatterns = [
    path("", PollList.as_view(), name="polls_list"),
    path("<int:pk>/", PollDetail.as_view(), name="polls_detail"),
]
