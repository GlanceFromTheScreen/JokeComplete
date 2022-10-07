from django.contrib import admin
from ListOfJokes.models import StartPhrases
from ListOfJokes.models import User
from ListOfJokes.models import Comments

admin.site.register(StartPhrases)
admin.site.register(User)
admin.site.register(Comments)
