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

        self.__smtpserver = 'mail.gmx.net'
        self.__mailTo = 'robert.jonas@gmx.at'
        secrets = netrc.netrc()
        self.__user, mail_account, self.__pw = secrets.authenticators(self.__smtpserver)

    # ------------------------------------------------------------------------------------------------------------------

    def sendMail(self, subject, inhalt):
        text = 'From: ' + self.__mailTo + '\n'
        text += 'To: ' + self.__mailTo + '\n'
        text += 'Date: ' + time.ctime(time.time()) + '\n'
        text += 'Subject: ' + subject + '\n\n'
        text += inhalt

        self.myLogger.debug(text)

        server = smtplib.SMTP_SSL(self.__smtpserver)
        server.login(self.__user, self.__pw)
        server.sendmail(self.__user, self.__mailTo, text)
        server.quit()
