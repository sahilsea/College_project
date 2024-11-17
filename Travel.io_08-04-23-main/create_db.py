from tourism import app, db
from tourism.models import User, Post

# Create application context
with app.app_context():
    # Create all database tables
    db.create_all()
    print("Database tables created successfully!")