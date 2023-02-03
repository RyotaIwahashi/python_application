import datetime

from django.db import models
from django.utils import timezone

# modelファイルでスキーマ定義する。(migrationすることでcreate table文などを実行できる)
# また、pythonから各オブジェクトに接続するためのデータベースAPIを作成できる

# モデルクラス
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # このモデルのオブジェクトに対して str() を呼び出す度に、以下が呼び出される
    # Djangoは内部で結構 str(obj)を使用する。例えば、Django 管理サイトでオブジェクトを表示し、オブジェクトを表示するときにテンプレートに値を挿入する場合など。
    # そのため、__str__()メソッドで人間可読なモデル表現を返す必要がある。
    def __str__(self):
        return self.question_text

    # クラスメソッド
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
