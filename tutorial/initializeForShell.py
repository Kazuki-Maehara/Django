from queriesLearning.models import Entry
from queriesLearning.models import Blog
from queriesLearning.models import Author
from queriesLearning.models import Dog
from django.db.models import F
import datetime
from datetime import timedelta


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

print(Dog.objects.filter(data__breed='collie'))
print(Dog.objects.filter(data__owner__name='Bob'))
print(Dog.objects.filter(data__owner__other_pets__0__name='Fishy'))
print(Dog.objects.filter(data__owner__isnull=True))
