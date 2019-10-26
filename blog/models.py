from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # models.ForeignKey :他モデルのリンク
    title = models.CharField(max_length=200)
    # models.CharFiled :文字数制限ありのテキストを定義するフィールド
    text = models.TextField()
    # models.CharFiled :文字数制限なしのテキストを定義するフィールド
    created_date = models.DateTimeField(default=timezone.now)
    # models.DataTimeFiled :日付・時間を定義するフィールド
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        # 特殊メソッド ｓｔｒ型を返す
        return self.title
