from Flask_Todo_list_app import db


class Todo(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key = True)
    task_Name = db.Column(db.String, nullable = False)
    is_Completed = db.Column(db.Boolean())


    def __init__ (self, task_Name):
        self.task_Name = task_Name
        self.is_Completed = False





