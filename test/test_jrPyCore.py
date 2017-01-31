import sys

sys.path.append("..")
from jrPyCore.jrMail import JrMail

my_mail = JrMail()
my_mail.send('TestSubject', 'TestContent')
