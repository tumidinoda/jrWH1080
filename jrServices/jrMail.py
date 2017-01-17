# -*- encoding: utf-8 -*-
import logging
import netrc
import smtplib
import time


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
        text = 'From: ' + self.__mail_from + '\n'
        text += 'To: ' + self.__mail_to + '\n'
        text += 'Date: ' + time.ctime(time.time()) + '\n'
        text += 'Subject: ' + subject + '\n\n'
        text += inhalt

        self.myLogger.debug(text)

        # server = smtplib.SMTP_SSL(self.__smtp_server)
        server = smtplib.SMTP(self.__smtp_server)
        server.login(self.__mail_user, self.__mail_pw)
        server.sendmail(self.__mail_from, self.__mail_to, text)
        server.quit()
