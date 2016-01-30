from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import date, datetime

@python_2_unicode_compatible
class Category(models.Model):
    DEFAULT_PK = 1
    
    name = models.CharField(max_length=50)
    
    created = models.DateTimeField(null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    #created_by = models.ForeignKey(User)
    
    def save(self):
        if not self.id:
            self.created = datetime.today()
        self.updated = datetime.today()
        super(Category, self).save()
    
    def __str__(self):
        return self.name
    
@python_2_unicode_compatible
class AccountingSystem(models.Model):
    INCOME = 'IN'
    EXPENSE = 'EX'
    TYPES_CHOICES = (
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    )
    
    type = models.CharField( max_length = 2,
                             choices = TYPES_CHOICES,
                             default = INCOME )
    amount = models.FloatField()
    category = models.ForeignKey( Category,
                                  default = Category.DEFAULT_PK,
                                  on_delete = models.SET_DEFAULT )
    date = models.DateTimeField('date published')
    note = models.CharField(max_length=200)
    
    created = models.DateTimeField(null=True, blank=True)
    updated = models.DateTimeField(null=True, blank=True)
    #created_by = models.ForeignKey(User)
    
    def save(self):
        if not self.id:
            self.created = datetime.today()
        self.updated = datetime.today()
        super(AccountingSystem, self).save()

    def __str__(self):
        return self.amount