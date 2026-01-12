from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Thor', email='thor@marvel.com', team=marvel),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='Running', duration=30, calories=300, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='Cycling', duration=45, calories=400, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='Swimming', duration=60, calories=500, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='Running', duration=25, calories=250, date=timezone.now().date())
        Activity.objects.create(user=users[4], type='Cycling', duration=35, calories=350, date=timezone.now().date())
        Activity.objects.create(user=users[5], type='Swimming', duration=55, calories=450, date=timezone.now().date())

        # Create Workouts
        cardio = Workout.objects.create(name='Cardio Blast', description='Intense cardio workout')
        strength = Workout.objects.create(name='Strength Training', description='Build muscle and power')
        cardio.suggested_for.add(marvel, dc)
        strength.suggested_for.add(marvel, dc)

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=1200)
        Leaderboard.objects.create(team=dc, points=1100)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
