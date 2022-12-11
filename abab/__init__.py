#初期化処理
from flask import Flask
app=Flask(__name__)
import abab.main #mainをインポート
from abab import db
db.create_books_table()