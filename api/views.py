# В данном файле находятся все обрабочтики запросов

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Book
from .serializer import BookSerializer


# Получение всех книг
@api_view(["GET"])  # Тип запроса принемаемых функцией(в данном случае GET)
def get_books(request):
    books = Book.objects.all()  # Получение всех книг
    serializer = BookSerializer(books, many=True)  # Сериализация полученных данных

    return Response({'data': serializer.data, 'code': 200})  # Отправка ответа пользователю


@api_view(["POST"])
def add_book(request):
    serialized_data = BookSerializer(data=request.data)  # Сериализация данных отправленных пользователем
    if serialized_data.is_valid():  # Проверка правильности стркутуры и самих данных отправленних пользователем
        serialized_data.save()  # Сохранение данных в БД

        return Response({'data': {'message': "product added", 'code': 201}})  # Отправка ответа пользователю
    return Response({'error': serialized_data.errors})  # Отправка ответа пользователю при выявлении ошибок


@api_view(["GET"])
def remove_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)  # Получение объекта по его id (pk - это то что указывает польхователь в URL адресе запроса)
    except:
        return Response({"error": "Not found", "code": 404})  # Ответ в случае необнаружения объекта с указанным id

    book.delete()  # Удаление

    return Response({'data': {'message': 'product removed', 'code': 200}})


@api_view(["GET"])
def title_search(request, pk):
    try:
        book = Book.objects.filter(title=pk)  # Получение одного или множества объектов с подходящими названиями
    except:
        return Response({"error": "Not found", "code": 404})

    serialized_data = BookSerializer(book, many=True)

    return Response({"data": serialized_data.data, "code": 200})


@api_view(["GET"])
def author_search(request, pk):
    try:
        book = Book.objects.filter(author=pk)
    except:
        return Response({"error": "Not found", "code": 404})

    serialized_data = BookSerializer(book, many=True)

    return Response({"data": serialized_data.data, "code": 200})


@api_view(["GET"])
def year_search(request, pk):
    try:
        book = Book.objects.filter(year=pk)  #
    except:
        return Response({"error": "Not found", "code": 404})

    serialized_data = BookSerializer(book, many=True)

    return Response({"data": serialized_data.data, "code": 200})


# В данной функции происходит почти тоже самое что и в add_book
@api_view(["PATCH"])  # Запрос на изменение данных
def status_change(request, pk):
    try:
        book = Book.objects.get(pk=pk)  # Получение книги по её id
    except:
        return Response({"error": "Not found", "code": 404})

    serialized_data = BookSerializer(book, data=request.data, partial=True)

    if serialized_data.is_valid():
        serialized_data.save()

        return Response({'data': serialized_data.data, 'code': 200})
    return Response({'error': serialized_data.errors})
