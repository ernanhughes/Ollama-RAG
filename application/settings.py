from application.models import db, Setting

@staticmethod
def save_setting(key, value):
    setting = Setting.query.filter_by(key=key).first()
    if setting:
        setting.value = value
    else:
        setting = Setting(key=key, value=value)
        db.session.add(setting)
    db.session.commit()

@staticmethod
def load_setting(key):
    setting = Setting.query.filter_by(key=key).first()
    return setting.value if setting else None
