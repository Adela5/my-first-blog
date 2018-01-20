from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):   #tabulka s příspěvky v řádcích, ve sloupci bude autor, titulek etc
    author = models.ForeignKey(   #ForeignKey odkazuje na nějakou cizí tabulku
    'auth.User',
    on_delete = models.CASCADE) #když se smaže autor, smažou se i jeho příspěvky kaskádovitě
    title = models.CharField(max_length=200) #titulek bude text/řetězec o max délce 200
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)  #null říká, že políčko může být prázdné - příspěvek jsem ještě nepublikoval a neukáže se na stránce

def publish(self):      #metoda umožňující pracovat s argumenty třídy. self zavolá právě ten, na kterém pracuji
        self.published_date = timezone.now()    #aby se post publikoval, publish date nebude prázdný ale bude mít aktuální datum timezone.now
        self.save() #ulož to do databáze; metoda save se dědí z modelu (je už připravená)

def __str__(self):  #speciální metoda s podtržítky, říká, jak se bude příspěvek převádět na řetězec - jednoduše vypíše titulek
        return self.title
