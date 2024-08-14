from flask import Flask, request
from .controller import Controller

def create_route(app: Flask):

    # メモ一覧の表示
    @app.get("/list")
    def show_list():
        return Controller.show_list()

    # メモの表示
    @app.get("/<int:id>")
    def show(id):
        return Controller.show(id)

    # メモの作成画面表示
    @app.get("/new")
    def new():
        return Controller.show_create_page()

    # メモの作成
    @app.post("/create")
    def create():
        return Controller.create()

    # メモの編集画面表示
    @app.get("/edit/<int:id>")
    def edit(id):
        return Controller.show_update_page(id)

    # メモの編集
    @app.post("/update/<int:id>")
    def update(id):
        if request.form.get('_method') == 'PATCH':
            return Controller.update(id)
        else:
            return "Method Not Allowed", 405

    # メモの削除
    @app.post("/delete/<int:id>")
    def delete(id):
        if request.form.get('_method') == 'DELETE':
            return Controller.delete(id)
        else:
            return "Method Not Allowed", 405
