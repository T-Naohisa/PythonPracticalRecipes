from dateutil.relativedelta import relativedelta
from datetime import datetime


now = datetime.now()
print(now)
# 1カ月後の計算にはrelativedeltaを使用する
print(now + relativedelta(months=+1))
