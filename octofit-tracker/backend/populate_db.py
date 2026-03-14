"""
populate_db.py

Script to populate the database with test data for OctoFit Tracker.
Run with: python manage.py shell < populate_db.py
"""

from octofit_tracker import models
from django.contrib.auth.models import User

# Create test users
def create_users():
    users = [
        {"username": "alice", "email": "alice@example.com", "password": "testpass123"},
        {"username": "bob", "email": "bob@example.com", "password": "testpass123"},
        {"username": "carol", "email": "carol@example.com", "password": "testpass123"},
    ]
    for u in users:
        if not User.objects.filter(username=u["username"]).exists():
            user = User.objects.create_user(username=u["username"], email=u["email"], password=u["password"])
            print(f"Created user: {user.username}")
        else:
            print(f"User {u['username']} already exists.")

# Add more test data creation functions here as models are defined

def main():
    create_users()
    # Add calls to other test data creation functions here

if __name__ == "__main__":
    main()
