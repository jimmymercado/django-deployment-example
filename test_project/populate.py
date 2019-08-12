import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','test_project.settings' )

import django
django.setup()

from test_app.models import User

from faker import Faker
fakegen = Faker()


def populate(N=10):
    for x in range(N):
        f = fakegen.first_name()
        l = fakegen.last_name()
        e = fakegen.email()

        user = User.objects.get_or_create(firstname=f, lastname=l, email=e)[0]

if __name__=='__main__':
    print('poputating DB')
    populate(10)
    print('populating complete!')