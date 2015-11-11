import json
import logging
import urllib2

LOGGER = logging.getLogger(__name__)


def validate_inspire_metadata(metadata):
    """validate metadata against INSPIRE metadata validation service"""

    success = None

    host = 'http://inspire-geoportal.ec.europa.eu'
    endpoint = 'GeoportalProxyWebServices/resources/INSPIREResourceTester'

    url = '{}/{}'.format(host, endpoint)

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'text/plain'
    }
    LOGGER.info('Performing validation')
    request = urllib2.Request(url, data=metadata, headers=headers)
    response = urllib2.urlopen(request)
    report = response.info().getheader('Location')

    json_data = json.loads(response.read())
    completeness_indicator = json_data['value']['CompletenessIndicator']
    LOGGER.info('Completeness Indicator %r', completeness_indicator)

    if completeness_indicator == 100:
        success = True
        LOGGER.info('Validation passed')
    else:
        success = False
        LOGGER.error('Validation failed')

    return {
        'success': success,
        'report': report
    }

if __name__ == '__main__':  # run interactively
    import sys

    if len(sys.argv) != 2:
        print('Usage: {} <metadata_xml_file>').format(sys.argv[0])
        sys.exit(1)

    with open(sys.argv[1]) as ff:
        RESULT = validate_inspire_metadata(ff.read())

    if not RESULT['success']:
        print('Validation failed: see {} for report'.format(RESULT['report']))
    else:
        print('Validation passed')
