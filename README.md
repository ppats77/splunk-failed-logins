# Splunk failed logins
Connects to the Splunk server and makes a request to prints the list of failed login attemts to the Splunk Search Head Server.
By default it use settings to connect to the localy running Splunk

## Instalation
1. Clone the project: ```git clone https://github.com/ppats77/splunk-failed-logins``` 
2. Install Splunk SDK: ```[sudo] pip install splunk-sdk```
3. Configure connection settings to the Splunk Server
   - inside the file
   - using command-line arguments
   
## Usage
```
usage: splunk-failed-logins.py [-h] [-H HOST] [-U USER] [-P PASSWORD]
                               [-p PORT] [-f FIELDS] [-t TIME]

optional arguments:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  Splunk server Host Name (default: localhost)
  -U USER, --user USER  Username to use when connecting to a Splunk server
                        (default: admin)
  -P PASSWORD, --password PASSWORD
                        Username to use when connecting to a Splunk server
                        (default: none)
  -p PORT, --port PORT  Port to use when connecting to a Splunk server
                        (default: 8089)
  -f FIELDS, --fields FIELDS
                        Set of fields to return. Default: timestamp user info
                        src host (default: timestamp user info src host)
  -t TIME, --time TIME  Timeframe to search. Default: -1 week. Options:
                        -t=-1minute, -t=-1day, -t=-1year (default: -1w )
```

## Example 
```
testuser$ python splunk-failed-logins.py -H=mydockerhost -U=admin -P="*********"
timestamp=10-10-2019 22:49:48.555	user=admin	info=failed	src=127.0.0.1	host=wpad.local
timestamp=10-10-2019 22:32:55.298	user=admin	info=failed	src=127.0.0.1	host=wpad.local
timestamp=10-10-2019 22:07:07.294	user=gmax	info=failed	src=127.0.0.1	host=wpad.local
timestamp=10-10-2019 22:05:50.746	user=gmax	info=failed	src=127.0.0.1	host=wpad.local
timestamp=10-10-2019 16:37:16.111	user=admin	info=failed	src=127.0.0.1	host=wpad.local
```
