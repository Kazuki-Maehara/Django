# from queriesLearning.models import Entry
# from queriesLearning.models import Blog
# from queriesLearning.models import Author
# from queriesLearning.models import Dog
#
# from polls.models import Question
#
# from django.db.models import F
# from django.db.models import Q
# import datetime
# from datetime import timedelta


# ---- Retrieving objects ----

# print(Entry.objects.filter(number_of_comments__gte=F("number_of_pingbacks") * 2))
# print(
#     Entry.objects.filter(
#         rating__lt=F('number_of_comments') + F('number_of_pingbacks')
#     )
# )
# print(Entry.objects.filter(authors__name=F('blog__name')))
# print(Entry.objects.filter(mod_date__gte=F('pub_date') + timedelta(days=1)))


# print(
#     Blog.objects.filter(pk__in=[1, 3])
# )
#
# print(
#     Blog.objects.filter(pk__gte=2)
# )
#
# print(
#     Entry.objects.filter(blog__id=3)
# )
#
# queryset = Entry.objects.all()
# print([p.headline for p in queryset])
# print([p.pub_date for p in queryset])


# ---- Querying JSONField ----
# Dog.objects.create(name='Rufus', data={
#     'breed': 'labrador',
#     'owner': {
#         'name': 'Bob',
#         'other_pets': [{
#             'name': 'Fishy',
#         }],
#     },
# })
#
# Dog.objects.create(name='Meg', data={
#         'breed': 'collie', 'owner': None
#     }
# )

# print(Dog.objects.filter(data__breed='collie'))
# print(Dog.objects.filter(data__owner__name='Bob'))
# print(Dog.objects.filter(data__owner__other_pets__0__name='Fishy'))
# print(Dog.objects.filter(data__owner__isnull=True))

# ---- has_key ----
# print(Dog.objects.filter(data__has_key='owner'))
# print(Dog.objects.filter(data__has_keys=['owner', 'breed']))
# print(Dog.objects.filter(data__has_any_keys=['owner', 'breed']))


# ---- Complex lookups with Q objects ----
# print(
#     Question.objects.get(
#         Q(question_text__startswith='Wh')
#     )
# )


# ---- Deleting objects ----
# b = Blog.objects.create(name="Deleting test",
#                         tagline="test tagline for deleting method")
# print(b.delete())


# ------- About aggregation -------
from aggregationLearning.models import Author, Publisher, Store, Book
from django.db.models import Avg, Max, Min, Sum
from django.db.models import Count
from django.db.models import Q

# print(Book.objects.all().count())
# print(Book.objects.all().aggregate(Avg('price')))
# print(Book.objects.all().aggregate(Max('price')))
# print(Book.objects.all().aggregate(Min('price')))
#
# print(Book.objects.all())
#
# q = Book.objects.annotate(Count('authors'))
#
# for author in q:
#     print(author.name, ": ", author.authors__count)

#
# book = Book.objects.first()
# print(book)
#
# print(book.authors.count())
# print(book.store_set.count())
#
# q = Book.objects.annotate(Count('authors'), Count('store'))
# print(q[1])
# print(q[1].authors__count)
# print(q[1].store__count)
#
# q = Book.objects.annotate(
#     Count('authors', distinct=True), Count('store', distinct=True))
# print(q[1].authors__count)
# print(q[1].store__count)

# q = Store.objects.annotate(min_price=Min('books__price'),
#                            max_price=Max('books__price'))
# print(type(q))
# print(type(q[0]))
#
# for one in q:
#     print("in " + str(one) + ":")
#     print(" " * 2 + "Max price is " + str(one.max_price) + " "
#           + "and Min price is " + str(one.min_price))

# print(Store.objects.aggregate(min_price=Min(
#     'books__price'), max_price=Max('books__price')))
#
# print(Store.objects.aggregate(youngest_age=Min('books__authors__age')))


# q = Publisher.objects.annotate(Count('book'))
#
# for one in q:
#     print(one.book__count)

# q = Publisher.objects.aggregate(oldest_pubdate=Min('book__pubdate'))
# print(q)

# q = Author.objects.annotate(total_pages=Sum('book__pages'))
# for one in q:
#     print(one.total_pages)

# print(Author.objects.aggregate(average_rating=Avg('book__rating')))
#
# q = Author.objects.annotate(Avg('book__rating'))
# for one in q:
#     print(one.book__rating__avg)

# q = Book.objects.filter(name__startswith='Django').annotate(
#     num_authors=Count('authors'))
#
# for one in q:
#     print(one.num_authors)


# q = Book.objects.filter(name__startswith="Django").aggregate(Avg('price'))
# print(q)

# highly_rated = Count('book', filter=Q(book__rating__gte=7))
# q = Author.objects.annotate(num_books=Count(
#     'book'), highly_rated_books=highly_rated)
#
# for one in q:
#     print(str(one) + ": ")
#     print(one.num_books, one.highly_rated_books)


# ------- Search -------

# This is a very fragile solution as it requires the user to know an exact substring of the author's name.
# A better approach could be a case-insensitive match(icontains), but this is only marginally better.

print(Author.objects.filter(name__contains="Thomas"))
