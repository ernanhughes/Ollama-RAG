from application.database import db

class Setting(db.Model):
    id = db.Column(db.BigInteger(), primary_key=True)
    key = db.Column(db.Text(), unique=True, nullable=False)
    value = db.Column(db.Text(), nullable=False)

class ChatQuery(db.Model):
    id = db.Column(db.BigInteger(), primary_key=True)
    prompt = db.Column(db.Text(), nullable=False)
    model = db.Column(db.Text(), nullable=False)
    created_time = db.Column(db.DateTime, nullable=False, default=db.func.now())

class ChatResponse(db.Model):
    id = db.Column(db.BigInteger(), primary_key=True)
    response = db.Column(db.Text(), nullable=False)
    prompt = db.Column(db.Text(), nullable=False)
    model = db.Column(db.Text(), nullable=False)
    created_time = db.Column(db.DateTime, nullable=False, default=db.func.now())


