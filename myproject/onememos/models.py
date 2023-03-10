from django.db import models

# Create your models here.

# 1. 데이터 모델
# idx(정수형)              X
# memo_text(문자형)        O
# published_date(날짜형)   O
# 2. 작성 후 admin 사이트에 반영 - admin.py 추가 작성

class Memo(models.Model):
    memo_text = models.CharField(max_length = 200) # 문자형
    published_date = models.DateTimeField(auto_now_add = True) # 날짜형

    def __str__(self):
        return self.memo_text