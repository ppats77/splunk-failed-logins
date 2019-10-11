# splunk-failed-logins
Connects to the Splunk server and makes a request to prints the list of failed login attemts to the Splunk Search Head Server.
By default it use settings to connect to the localy running Splunk:

optional arguments:
		-h, --help show this help message and exit
		-H HOST, --host Splunk server Host Name
		-U USER, --user Username to use when connecting to a Splunk server
		-P PASSWORD, --password Username to use when connecting to a Splunk server
		-p PORT, --port Port to use when connecting to a Splunk server
		-f FIELDS, --fields Set of fields to return. Default: timestamp user info
                        src host
		-t TIME, --time Timeframe to search. Default: -1 week. Options:
                        -t=-1minute, -t=-1day, -t=-1year
