from tortoise import Model, fields

class Url(Model):
    id = fields.CharField(pk=True, unique=True, max_length=60)
    redirect = fields.TextField()
    created_on = fields.TimeField(auto_now=False)

class Admin(Model):
    id = fields.CharField(pk=True, unique=True, max_length=30)
    username = fields.TextField()
    password = fields.TextField()