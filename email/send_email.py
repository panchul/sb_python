import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_addr='from_somebody@somedomain.com'
to_addr=['somebody1@somedomain.com','somebody2@somedomain.com']

msg=MIMEMultipart()
msg['From']=from_addr
msg['To']=" ,".join(to_addr)
msg['subject']='you signed up for this'

body='here goes email body with spam links and dividing rhetoric'

msg.attach(MIMEText(body,'plain'))

email='somesecretemail'
password='somesecretpassword'

# better yet, use local smtp instead
mail=smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)

text=msg.as_string()
mail.sendmail(from_addr,to_addr,text)

# or don't quit, but do more harm to the subscribers instead.
mail.quit()

