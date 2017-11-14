import json
import requests
import sys

# run on some node in the network
# works with python3
# just give service name as an argument when you run the script

def main(service):
    req = requests.get('http://leader.mesos:8080/v2/apps/' + service, headers = {'Accept': 'application/json'}).text
    data = json.loads(req)['app']
    removeFields = ['tasks','lastTaskFailure','versionInfo','version','deployments',
        'uris','fetch','executor','tasksStaged','tasksHealthy','tasksRunning',
        'tasksUnhealthy','ipAddress','residency','secrets','requirePorts','user','args',
        'storeUrls','constraints']
    for field in removeFields:
        if field in data:
            del data[field]
    print(json.dumps(data, sort_keys=True, indent=2, separators=(',', ': ')))

if __name__ == "__main__":
    main(sys.argv[1])

