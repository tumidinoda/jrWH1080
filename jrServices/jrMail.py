# -*- encoding: utf-8 -*-
import logging
import netrc
import smtplib
from email.mime.text import MIMEText


# noinspection PyPep8Naming
class JrMail:
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        self.myLogger = logging.getLogger('jrWetterstationLogger')
        self.myLogger.debug('Mail constructor')

        self.__mail_from = 'SeyringWetter@a1.net'
        self.__mail_to = 'robert.jonas@gmx.at'
        secrets = netrc.netrc()
        self.__mail_user, self.__smtp_server, self.__mail_pw = secrets.authenticators('Mailprovider')

    # ------------------------------------------------------------------------------------------------------------------
    def sendMail(self, subject, inhalt):
        msg = MIMEText(inhalt, 'plain', 'utf-8')
        msg['From'] = self.__mail_from
        msg['To'] = self.__mail_to
        msg['Subject'] = subject

        # server = smtplib.SMTP_SSL(self.__smtp_server)
        server = smtplib.SMTP(self.__smtp_server)
        server.login(self.__mail_user, self.__mail_pw)
        server.sendmail(self.__mail_from, self.__mail_to, msg.as_string())
        server.quit()
