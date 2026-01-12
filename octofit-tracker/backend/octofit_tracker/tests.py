from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        self.assertEqual(team.name, 'Marvel')

    def test_user_creation(self):
        team = Team.objects.create(name='DC', description='DC Superheroes')
        user = User.objects.create(name='Superman', email='superman@dc.com', team=team)
        self.assertEqual(user.name, 'Superman')

    def test_activity_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        user = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=team)
        activity = Activity.objects.create(user=user, type='Running', duration=30, calories=300, date='2026-01-12')
        self.assertEqual(activity.type, 'Running')

    def test_workout_creation(self):
        team = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        workout = Workout.objects.create(name='Cardio Blast', description='Intense cardio workout')
        workout.suggested_for.add(team)
        self.assertEqual(workout.name, 'Cardio Blast')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='DC', description='DC Superheroes')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)
