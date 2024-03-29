# Splunk failed logins
The python script designed to connect to a local or remote Splunk search head server and make a search request for the failed logins. 
By default, the script uses settings to connect to the locally running Splunk instance in port 8089. The username and password need to be provided.

## Instalation
1. Clone the project: ```git clone https://github.com/ppats77/splunk-failed-logins``` 
2. Install required packages: ```[sudo] pip install -r requirements.txt```
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
                        Set of fields to return. (default: timestamp user info
                        src host)
  -l LIMIT, --limit LIMIT
                        Set number of lines to return. (default: 100)
  -t TIME, --time TIME  Timeframe to search. Default: -1 week. Options:
                        -t=-1minute, -t=-1day, -t=-1year (default: -1w)
```

## Example 
```
ppats77$ python splunk-failed-logins.py -H=mydockerhost -U=admin -P="*********"
timestamp=10-10-2019 22:49:48.555	user=admin	info=failed	src=127.0.0.1	host=ppats77.macbook
timestamp=10-10-2019 22:32:55.298	user=admin	info=failed	src=127.0.0.1	host=ppats77.macbook
timestamp=10-10-2019 22:07:07.294	user=ppats77	info=failed	src=127.0.0.1	host=ppats77.macbook
timestamp=10-10-2019 22:05:50.746	user=ppats77	info=failed	src=127.0.0.1	host=ppats77.macbook
timestamp=10-10-2019 16:37:16.111	user=admin	info=failed	src=127.0.0.1	host=ppats77.macbook
```
