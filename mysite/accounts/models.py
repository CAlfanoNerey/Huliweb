from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.
from django.dispatch import receiver
from django.shortcuts import reverse
from django.conf import settings

TITLE_STATES = [
    ('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('American Samoa', 'American Samoa'), ('Arizona', 'Arizona'), ('Arkansas', 'Arkansas'),
    ('California', 'California'), ('Colorado', 'Colorado'), ('Connecticut', 'Connecticut'), ('Delaware', 'Delaware'),
    ('District of Columbia', 'District of Columbia'), ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Guam', 'Guam'), ('Hawaii', 'Hawaii'),
    ('Idaho', 'Idaho'), ('Illinois', 'Illinois'), ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'),
    ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'),
    ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Minor Outlying Island', 'Minor Outlying Islands'),
    ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'), ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'),
    ('New Hampshire', 'New Hampshire'), ('New Jersey', 'New Jersey'), ('New Mexico', 'New Mexico'), ('New York', 'New York'),
    ('North Carolina', 'North Carolina'), ('North Dakota', 'North Dakota'), ('Northern Mariana Islands', 'Northern Mariana Islands'), ('Ohio', 'Ohio'),
    ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'), ('Pennsylvania', 'Pennsylvania'), ('Puerto Rico', 'Puerto Rico'),
    ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'), ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'),
    ('U.S. Virgin Islands', 'U.S. Virgin Islands'), ('Utah', 'Utah'), ('Vermont', 'Vermont'), ('Virginia', 'Virginia'),
    ('Washington', 'Washington'), ('West Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'), ('Wyoming', 'Wyoming'),

]





class User(AbstractUser):

    #name = models.CharField(max_length=200, default='')
    #
    #
    # address_line1 = models.CharField(max_length=200,default='')
    # address_line2 = models.CharField(blank=True, null=True, max_length=200,default='')
    # # state = models.ForeignKey('States', null=True, blank=True)
    # city = models.CharField(max_length=200,default='')
    # state_or_territory = models.CharField(max_length=40, choices=TITLE_STATES,default='')
    # # zipcode = models.PositiveIntegerField(blank=True, null=True)
    # zipcode = models.PositiveIntegerField(validators=[MaxValueValidator(99999)],default=0)
    #fax = models.IntegerField(blank=True, null=True,default=0)

    def __str__(self):
        return self.username


CATEGORY_CHOICES = [
    ('S', 'Shirt')
]

LABEL_CHOICES = [
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
]


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices= CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices= LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("accounts:productPage", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


# class Recipient(models.Model):
#
#     Requester = models.ForeignKey(Requester, on_delete=models.CASCADE)
#
#
#     name = models.CharField(max_length=200)
#     address_line1 = models.CharField(max_length=200)
#     address_line2 = models.CharField(blank=True, null=True,max_length=200)
#     city = models.CharField(max_length=200)
#     state_or_territory = models.CharField(max_length=40, choices=TITLE_STATES)
#     zipcode = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
#     email = models.CharField(max_length=200)
#     fax = models.IntegerField(blank=True, null=True)
#
#     def __str__(self):
#         return self.name



# this method is mainly to create new users inside of the django admin


# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         user_profile = UserProfile.objects.create(user=kwargs['instance'])
#         # user = Requester.objects.create(user=kwargs['instance'])
#
#
# post_save.connect(create_profile, sender=User)

# class States(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=96)
#     state_abbr = models.CharField(max_length=24, blank=True)
#
#     # Define the __unicode__ method, which is used by related models by default.
#     def __unicode__(self):
#         return self.state_abbr
