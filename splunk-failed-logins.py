#!/usr/bin/python
import sys
import splunklib.results as results
import splunklib.client as client
import splunklib.binding as binding
import argparse

# Default settings

HOST = "localhost"
PORT = 8089
USERNAME = "admin"   # please chenge to your default username
PASSWORD = "none"    # please change to your default password
FIELDS = "timestamp user info src host"
TIME = "-1w"
LIMIT= 100



def main():
    sys.stdout.flush()
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "-H", "--host", help="Splunk server Host Name", default=HOST)
    parser.add_argument(
        "-U", "--user", help="Username to use when connecting to a Splunk server", default=USERNAME)
    parser.add_argument(
        "-P", "--password", help="Username to use when connecting to a Splunk server", default=PASSWORD)
    parser.add_argument(
        "-p", "--port", help="Port to use when connecting to a Splunk server", default=PORT, type=int)
    parser.add_argument(
        "-f", "--fields", help="Set of fields to return.", default=FIELDS)
    parser.add_argument(
        "-l", "--limit", help="Set number of lines to return.", type=int, default=LIMIT)
    parser.add_argument(
        "-t", "--time", help="Timeframe to search. Default: -1 week. Options: -t=-1minute, -t=-1day, -t=-1year", default=TIME)
    args = parser.parse_args()

    # Creating connection to the Splunk server.
    
    try:
        service = client.connect(
            host=args.host, port=args.port, username=args.user, password=args.password)
    
    except binding.AuthenticationError:
        print "CONNECTION ERROR:\nConnection to Splunk Server on \nhost : '" + args.host + "', username : '" + args.host + \
            "', password : '" + args.password + \
            "'\ncould not be establised.\nPlease check your settings.\nPlease use 'python " + \
            sys.argv[0] + " -h' for help"
        sys.exit(1)
        
    # Make Search on Splunk Server 
    
    raw = results.ResultsReader(service.jobs.export(
        "search index=_audit action=\"login attempt\" info=failed earliest=" + args.time + " | head " + str(args.limit) + " | fields " + args.fields))
    
    # Parsing and printing results
    
    try: 
        for result in raw:
            if isinstance(result, dict):
                for key in args.fields.split(" "):
                    print key+"="+str(result[key])+'\t',
                print '\n',
    except KeyError:
        print "Please check fields requested : '" + args.fields + "'\nPlease use 'python " + sys.argv[0] + " -h' for help"
        sys.exit(1)
        


if __name__ == '__main__':
    main()
