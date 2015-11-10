import urllib2


def validate_inspire_metadata(metadata):
    """validate metadata against INSPIRE metadata validation service"""

    host = 'http://inspire-geoportal.ec.europa.eu'
    endpoint = 'GeoportalProxyWebServices/resources/INSPIREResourceTester'

    url = '{}/{}'.format(host, endpoint)

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'text/plain'
    }
    request = urllib2.Request(url, data=metadata, headers=headers)
    response = urllib2.urlopen(request)
    return response.read()

if __name__ == '__main__':  # run interactively
    import sys

    if len(sys.argv) != 2:
        print('Usage: {} <metadata_xml_file>').format(sys.argv[0])
        sys.exit(1)

    with open(sys.argv[1]) as ff:
        print(validate_inspire_metadata(ff.read()))
