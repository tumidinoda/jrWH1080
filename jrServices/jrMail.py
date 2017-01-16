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

        self.__mailFrom = 'SeyringWetter@a1.net'
        self.__mailTo = 'robert.jonas@gmx.at'
        secrets = netrc.netrc()
        self.__mail_user, self.__smtp_server, self.__mail_pw = secrets.authenticators('Mailprovider')

    # ------------------------------------------------------------------------------------------------------------------
    def sendMail(self, subject, inhalt):
        text = 'From: ' + self.__mailFrom + '\n'
        text += 'To: ' + self.__mailTo + '\n'
        text += 'Date: ' + time.ctime(time.time()) + '\n'
        text += 'Subject: ' + subject + '\n\n'
        text += inhalt

        self.myLogger.debug(text)

        # server = smtplib.SMTP_SSL(self.__smtp_server)
        server = smtplib.SMTP(self.__smtp_server)
        server.login(self.__mail_user, self.__mail_pw)
        server.sendmail(self.__mail_user, self.__mailTo, text)
        server.quit()
