# 邮箱类
## 现实了邮箱的创建
```python
from emailclass import bt_api

'''
调用此类创建一个新邮箱
'''
mybt = bt_api()
new_email = mybt.set_mail()
if new_email == None:
    print("邮箱生成失败")
else:
    print(new_email)
'''
调用此类读取某个邮箱的邮件

'''
```