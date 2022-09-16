import peewee
from db_config import psql_db

class Ads(peewee.Model):
    class Meta:
        database = psql_db
    
    title = peewee.CharField(max_length=200)
    image = peewee.CharField(max_length=200)
    desc = peewee.TextField()
    location = peewee.CharField(max_length=200)
    beds = peewee.IntegerField()
    price = peewee.DecimalField(max_digits=10, decimal_places=2)
    date = peewee.DateTimeField()