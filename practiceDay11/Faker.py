# App1/faker.py

import os
import django
import random
from faker import Faker

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practiceDay11.settings')
django.setup()

from App1.models import Trainee

fake = Faker()

def create_fake_trainees(n=10):
    for _ in range(n):
        name = fake.name()
        email = fake.unique.email()
        age = random.randint(18, 40)

        Trainee.objects.create(
            name=name,
            email=email,
            age=age
        )

    print(f"{n} fake trainees created successfully!")

if __name__ == '__main__':
    create_fake_trainees()
