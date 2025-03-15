import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 创建邮件主体对象
email = MIMEMultipart()
# 设置发件人、收件人和主题
email["From"] = "xxxxxxxxx@126.com"
email["To"] = "yyyyyy@qq.com;zzzzzz@1000phone.com"
email["Subject"] = str(Header("上半年工作情况汇报", "utf-8"))
# 添加邮件正文内容
content = """据德国媒体报道，当地时间9日，德国火车司机工会成员进行了投票，
定于当地时间10日起进行全国性罢工，货运交通方面的罢工已于当地时间10日19时开始。
此后，从11日凌晨2时到13日凌晨2时，德国全国范围内的客运和铁路基础设施将进行48小时的罢工。"""
email.attach(MIMEText(content, "plain", "utf-8"))

# 创建SMTP_SSL对象（连接邮件服务器）
smtp_obj = smtplib.SMTP_SSL("smtp.126.com", 465)
# 通过用户名和授权码进行登录
smtp_obj.login("xxxxxxxxx@126.com", "邮件服务器的授权码")
# 发送邮件（发件人、收件人、邮件内容（字符串））
smtp_obj.sendmail(
    "xxxxxxxxx@126.com", ["yyyyyy@qq.com", "zzzzzz@1000phone.com"], email.as_string()
)
