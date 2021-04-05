import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'tango_with_django_project.settings')

import django
django.setup()
from bakery.models import Category, Page

def populate():

    bakerys = [
    {'title': '___',
    'url':'___'},
    ]

    user_accounts = [
    {'title':'___',
    'url':'___'},
    ]

    other_pages = [
    {'title':'___',
    'url':'___'},
    ]

    cats = {'Bakerys': {'pages': bakerys},
    'User Accounts': {'pages': user_accounts},
    'Other Pages': {'pages': other_pages} }

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print('Starting bakery population script...')
    populate()