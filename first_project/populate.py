import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()


import random
from first_app.models import AccessRecord, Website, Topic
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #get the topic for entry
        top = add_topic()

        #create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the new Website entry
        web = Website.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        #create a fake AccessRecord entry
        access = AccessRecord.objects.get_or_create(name=web, date=fake_date)[0]


if __name__ == '__main__':
    print('populating models....')
    populate(10)
    print('populating complete!')

