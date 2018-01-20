from django.contrib import admin
from .models import Post    #tečka před models říká, že to importujeme ze souboru ve stejném adresáři
admin.site.register(Post)   #zaregistruje náš příspěvek, který jsme předtím naimportovali
# Register your models here.
