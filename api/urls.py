# Все URL адреса приложения

from django.urls import path
from . import views

urlpatterns = [
    path("books", views.get_books),  # Первый аргумент это адрес (books) при переходе на который будет вызыватся функция указанная во втором аргументе(views.get_books)
    path("add_book", views.add_book),
    path("remove_book/<int:pk>", views.remove_book),  # <int:pk> в переменную pk мы поместим значение типа Integer после его примет указанная во втором аргументе функция
    path("title_search/<str:pk>", views.title_search),  # Тоже самое только вместо Integer мы поместим значение тима String
    path("author_search/<str:pk>", views.author_search),
    path("year_search/<int:pk>", views.year_search),
    path("status_change/<int:pk>", views.status_change),
]
