#!/usr/bin/python
import sys
from time import sleep
import splunklib.results as results
import splunklib.client as client
from argparse import ArgumentParser

# Default settings

HOST = "localhost"
PORT = 8089
USERNAME = "gmax"
PASSWORD = "..."
FIELDS = "timestamp user info src host"
TIME = "-1w "


def main():
    sys.stdout.flush()
    parser = ArgumentParser(description='Search Failed Login attempts.')
    parser.add_argument(
        "-H", "--host", help="Splunk server Host Name", default=HOST)
    parser.add_argument(
        "-U", "--user", help="Username to use when connecting to a Splunk server", default=USERNAME)
    parser.add_argument(
        "-P", "--password", help="Username to use when connecting to a Splunk server", default=PASSWORD)
    parser.add_argument(
        "-p", "--port", help="Port to use when connecting to a Splunk server", default=PORT, type=int)
    parser.add_argument(
        "-f", "--fields", help="Set of fields to return. Default: timestamp user info src host", default=FIELDS)
    parser.add_argument(
        "-t", "--time", help="Timeframe to search. Default: -1 week. Options: -t=-1minute, -t=-1day, -t=-1year", default=TIME)
    args = parser.parse_args()

    # Creating connection to the Splunk server.

    service = client.connect(
        host=args.host,
        port=args.port,
        username=args.user,
        password=args.password)
    raw = results.ResultsReader(service.jobs.export(
        "search index=_audit action=\"login attempt\" info=failed earliest="+args.time+" | fields " + args.fields))
    for result in raw:
        if isinstance(result, dict):
            for key in args.fields.split(" "):
                print key+"="+str(result[key]),


if __name__ == '__main__':
    main()
