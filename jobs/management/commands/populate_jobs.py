from django.core.management.base import BaseCommand
from faker import Faker
from jobs.models import Job
import random

class Command(BaseCommand):
    help = 'Populate the Job model with dummy data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        num_jobs = 10000  # Number of dummy jobs to create

        for _ in range(num_jobs):
            job = Job(
                title=fake.job(),
                company_name=fake.company(),
                location=fake.city(),
                description=fake.text(max_nb_chars=200),
                skills_required=", ".join(fake.words(nb=5)),
                experience_required=f"{random.randint(1, 5)}-year(s)",
                education_required=fake.job(),
                salary_range=f"{random.randint(10, 30)}K - {random.randint(30, 60)}K",
                date_posted=fake.date_this_year(),
                job_url=fake.url()
            )
            job.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully populated {num_jobs} jobs'))
