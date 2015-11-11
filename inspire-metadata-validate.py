# =================================================================
#
# Authors: Tom Kralidis <tomkralidis@gmail.com>
#
# Copyright (c) 2015 Tom Kralidis
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

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

    if 'ResourceReportResource' in json_data['value']:
        success = False
        LOGGER.error('Validation failed')
    elif 'PullBatchReportResource' in json_data['value']:
        success = False
        LOGGER.error('Validation failed')
    else:
        success = True
        LOGGER.info('Validation passed')

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
