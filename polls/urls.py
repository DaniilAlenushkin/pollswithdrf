from django.urls import path
from .apiviews import ChoiceList, CreateVote, PollViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', PollViewSet, basename='polls')

urlpatterns = [
    path("<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote")
]

urlpatterns += router.urls
