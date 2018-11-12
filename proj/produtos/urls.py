from django.urls import path
from .views import home, detalhe_produto

urlpatterns = [
    path('', home),
    path('produto/<int:codigo>/', detalhe_produto),
]

# request > url > view > model > response