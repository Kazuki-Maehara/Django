from django.shortcuts import render
from django.views import generic
from .models import Book, Author, BookInstance, Genre
# Create your views here.


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects.
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(
        status__exact='a'
    ).count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_book_contains_javascript = Book.objects.filter(
        title__icontains="javascript"
    ).count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_book_contains_javascript': num_book_contains_javascript,
    }

    # Render the HTML template index.html
    # with the data in the context variable.
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 3
    # your own name for the list as a template variable
    # context_object_name = 'my_book_list'
    # Get 5 books containing the title "javascript"
    # queryset = Book.objects.filter(title__icontains='javascript')[:5]
    # Specify your own template name/location
    # template_name = 'books/my_arbitrary_template_name_list.html'


class BookDetailView(generic.DetailView):
    model = Book
