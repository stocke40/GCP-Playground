from flask import escape
import requests
from bs4 import BeautifulSoup
from google.cloud import logging

# GoogleCloudFunctions seems to expect that the cloud functions must exist in a source module named main.py
# imports must be declared in requirements.txt in the same directory as these are pip installed when the 
#   funtion is deployed to google cloud run time Python 3.7.
#   See https://cloud.google.com/functions/docs/writing/specifying-dependencies-python#python37 for more info.

def CME_quote_ES(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'

    CME_ES_url = 'https://www.cmegroup.com/trading/equity-index/us-index/e-mini-sandp500_quotes_globex.html'

    cr = requests.get(CME_ES_url,timeout=2.5)
    cr_html = cr.text
    print("HTML: {}".format(cr.text))
    #logging.warn(RuntimeError('HTML: '+cr.text+'(logging.warn)'))
    csoup = BeautifulSoup(cr_html, 'html.parser')

    # Assuming top table entry is the current futures contract.  
    # Perhaps we could change this to consume entire table and choose the
    # table entry with the highest volume.  Need more thought here.
    cEsPriorSettle = csoup.find_all(id="QuotesFuturesProductTable1_ESH1_priorSettle")

    return 'CME ES Prior Settle {}!'.format(escape(cEsPriorSettle))

# Another comment outside function    