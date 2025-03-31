import sqlite3

# Database class to interact with SQLite database
class QuizDatabase:
    def __init__(self, db_name="quiz.db"):
        self.db_name = db_name
        self.initialize_db()

    # Establish a connection to the SQLite database
    def connect(self):
        return sqlite3.connect(self.db_name)
