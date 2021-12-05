from queriesLearning.models import Entry
from queriesLearning.models import Blog
from queriesLearning.models import Author
from django.db.models import F
import datetime

print(Entry.objects.filter(number_of_comments__gte=F("number_of_pingbacks") * 2))
