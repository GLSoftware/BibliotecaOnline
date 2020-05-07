from django.shortcuts import render
from django.views import generic
from catalogo.models import Book, Author, Genre, Format
import django_filters
from django.http import HttpResponse


def index(request):

    num_books = Book.objects.all().count()
    books = Book.objects.all()
    myFilter = BookFilter(request.GET, queryset=books)
    context = {
        'num_books': num_books,
        'books': books,
        'myFilter': myFilter,
    }
    return render(request, 'index.html', context=context)


class BookDetailView(generic.DetailView):
    model = Book


class AuthorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Nombre', lookup_expr='icontains')

    class Meta:
        model = Author
        fields = ['name']


def author_list(request):
    authors = Author.objects.all()
    filtroautor = AuthorFilter(request.GET, queryset=authors)
    authors = filtroautor.qs
    context = {'filtroautor': filtroautor, 'authors': authors}
    return render(request, 'catalogo/author_list2.html', context)


class AuthorDetailView(generic.DetailView):
    model = Author


class BookFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(label='Título', lookup_expr='icontains')
    author__name = django_filters.CharFilter(label='Autor', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'author__name', 'format']


def book_list(request):
    books = Book.objects.all()
    myFilter = BookFilter(request.GET, queryset=books)
    books = myFilter.qs
    context = {'myFilter': myFilter, 'books': books}
    return render(request, 'catalogo/book_list2.html', context)
