#!/bin/sh

export PATH=$PATH:/usr/local/bin

# exit if NTP hasn't set computer clock
[ `ntpdc -c sysinfo | awk '/stratum:/ {print $2}'` -ge 10 ] && exit

pidfile=/var/run/pywws.pid
datadir=/home/robert/jrWH1080/data
logfile=/home/robert/jrWH1080/logs/pywws.log

# exit if process is running
[ -f $pidfile ] && kill -0 `cat $pidfile` && exit

# email last few lines of the logfile to see why it died
#14.01.17: t.b.d

# restart process
pywws-livelog-daemon -v -p $pidfile $datadir $logfile start
