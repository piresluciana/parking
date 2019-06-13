import subprocess
import logging
import time
import datetime

logging.basicConfig(format='%(message)s', filename='data.csv', level=logging.INFO)


def shell_cmd(cmd):
    result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = result.communicate()[0]
    return output


cmd = "curl http://www.dublincity.ie/dublintraffic/cpdata.xml"

while True:
    # get time 
    # format = 2017-03-06 16:00:04.159338
    # + timedelta because time is in UTC +0
    date_now = str(datetime.datetime.now() + datetime.timedelta(seconds=60*60))
    
    # get the xml as list and split by lines
    result = shell_cmd(cmd).decode('utf-8').split("\n")
    
    # get the current timestamp on xml
    for thing in result:
        if "Timestamp" in thing:
            timestamp = thing.split("<Timestamp>")[1].split(" ")[0]

    # get the results and append todata.csv
    # format = PARKING NAME, VALUE, XML TIMESTAMP, CURRENT DATETIME 
    for thing in result:
        if "carpark name=" in thing:
            var = thing.split("\"")
            data_to_log = '{0},{1},{2},{3}'.format(str(var[1]), str(var[3]), str(timestamp), date_now)
            logging.info(data_to_log)
    
    # wait 5 min and run again
    time.sleep(60*5)
