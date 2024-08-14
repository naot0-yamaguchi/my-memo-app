from .database import db

# メモエンティティのクラス
class Memos(db.Model):
    __tablename__ = 'memos'

    id = db.Column(db.Integer, primary_key=True)
    contents = db.Column(db.String, nullable=True)
    create_at = db.Column(db.DateTime, nullable=False)
    update_at = db.Column(db.DateTime, nullable=True)
    delete_at = db.Column(db.DateTime, nullable=True)
    delete_flg = db.Column(db.Boolean, nullable=False)
