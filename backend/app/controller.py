from flask import (
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for
)

from .service import Service

class Controller():

    # メモ一覧の表示
    @staticmethod
    def show_list():
        memos = Service.get_memo_list()
        print(memos)
        return render_template('list.html', memos=memos)

    # メモの表示
    @staticmethod
    def show(id):
        memo = Service.get_memo(id)
        return render_template('show.html', memo=memo)

    # メモの作成ページ表示
    @staticmethod
    def show_create_page():
        return render_template('create.html')

    # メモの作成
    @staticmethod
    def create():
        isSuccess = Service.create_memo()

        if isSuccess:
            return Controller.show_list()
        else:
            return render_template('create.html')

    # メモの編集ページ表示
    @staticmethod
    def show_update_page(id):
        memo = Service.get_memo(id)
        return render_template('update.html', memo=memo)

    # メモの編集ページ表示
    @staticmethod
    def update(id):
        Service.update_memo(id)
        return Controller.show_update_page(id)

    # メモの削除(削除結果を返却)
    @staticmethod
    def delete(id):
        Service.delete_memo(id)
        return Controller.show_list()
