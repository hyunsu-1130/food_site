from django.db import models
from chinese.models import Category, Food

# 장바구니
class Cart(models.Model):
  # 고객정보 - 필수지만 다음번에 로그인과 연동해서
  # 구매완료 - 정책 -> 완료되면 table에서 삭제 or '기록 완료' 표시 남기기

  food = models.ForeignKey(Food, on_delete=models.DO_NOTHING)
  amount = models.IntegerField(default=0)
