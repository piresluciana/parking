import subprocess
import logging

logging.basicConfig(filename='data.csv', level=logging.INFO)


def shell_cmd(cmd):
	result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	output = result.communicate()[0]
	return output


url = "http://www.dublincity.ie/dublintraffic/cpdata.xml"

cmd = "curl {0}".format(url)


result = shell_cmd(cmd).decode('utf-8').split("\n")
#print(result)
#result = result[0].split("\n")


for thing in result:
	if "Timestamp" in thing:
		timestamp = thing.split("<Timestamp>")[1].split(" ")[0]


for thing in result:
	if "carpark name=" in thing:
		var = thing.split("\"")
		print(var)		
		data_to_log = ',{0},{1},{2}'.format(str(var[1]), str(var[3]), str(timestamp))
		logging.info(data_to_log)
