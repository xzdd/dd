#coding；utf-8

import smtplib
from email.mime.text import MIMEText

#-------1.跟发件有关的参数----------
smtpserver = "smtp.qq.com"      #发件服务器
port = 465                      #端口
sender = "1041468717@qq.com"    #账号
psw = "elkjtljbphckbfgh"        #密码
receiver = ["1041468758@qq.com","812816802@qq.com"]        #多个收件人 list 对象

#-------2.编辑邮件内容----------
subject = "小湿妹的问卷调查"               #标题
body ='<p>1.小湿妹多重呀..</p>'           #定义邮件正文html格式
msg = MIMEText(body,"html","utf-8")
msg['from'] = sender
msg['to'] = ";".join(receiver)           #多个收件人 list 转 str
msg['subject'] = subject

#---------3.发送邮件------------兼容163-qq发件方式代码
try:
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)                            #连接服务器
    smtp.login(sender,psw)
except:
    smtp = smtplib.SMTP_SSL(smtpserver, port)           #连接服务器
    smtp.login(sender, psw)                             # 登录
smtp.sendmail(sender, receiver, msg.as_string())        # 发送
smtp.quit()                                             # 关闭