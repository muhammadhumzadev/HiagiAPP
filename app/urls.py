from django.urls import path
<<<<<<< HEAD
from .views import fnBuildSecondBrain, fnQA, download_text
=======
from .views import fnBuildSecondBrain, fnQA
>>>>>>> main

urlpatterns = [
    path('buildbrain', fnBuildSecondBrain, name="buildBrain"),
    path('ask', fnQA, name="QA"),
<<<<<<< HEAD
    path('download-text', download_text, name='download_text'),
=======
>>>>>>> main
]
