import datetime as dt

from flask import abort, flash, request

from .database import db
from .model import Memos

class Service():

    # メモの一覧を取得する
    @staticmethod
    def get_memo_list():
        return Memos.query.order_by('create_at').all()

    # 引数のIDのメモを取得する
    @staticmethod
    def get_memo(id):
        memo = Memos.query.filter(Memos.id == id).first()

        if memo is None:
            abort(404, f"Memo id {id} doesn't exist.")
        else:
            return memo

    # メモを新規作成する
    @staticmethod
    def create_memo():
        contents = request.form['contents']

        if contents is None:
            flash("The contents doesn't exist.")
            return False
        else:
            memo = Memos(contents=contents, create_at=dt.datetime.now(), delete_flg=False)
            db.session.add(memo)
            db.session.commit()
            return True

    # 引数のIDのメモをフォームの内容で更新する
    @staticmethod
    def update_memo(id):
        memo = Memos.query.filter(Memos.id == id).first()

        if memo is None:
            abort(404, f"Memo id {id} doesn't exist.")
            return False

        contents = request.form['contents']

        if contents is None:
            flash('Contents is missing.')
            return False
        else:
            memo.contents = contents
            db.session.commit()
            return True

    # 引数のIDのメモを削除する
    @staticmethod
    def delete_memo(id):
        query = Memos.query.filter(Memos.id == id)
        memo = query.first()

        if memo is None:
            abort(404, f"Memo id {id} doesn't exist.")
            return False

        query.delete()
        db.session.commit()
        return True
