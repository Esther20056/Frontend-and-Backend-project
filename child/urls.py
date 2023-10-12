from django.urls import path
from .views import getALLArticles, getArticles, signup, Login, createArticle



urlpatterns = [
    path('getarticles/', getALLArticles),
    path('getarticle/<int:id>', getArticles ),
    path('signup/', signup),
    path('login/', Login),
    path('createarticle/', createArticle)
    
]
