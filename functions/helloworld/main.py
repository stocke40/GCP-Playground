from flask import escape
import requests
from bs4 import BeautifulSoup

# GoogleCloudFunctions seems to expect that the cloud functions must exist in a source module named main.py 
# Trying multiple routines packaged in main.py

def hello_http(request):
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
    return 'Hello {}!'.format(escape(name))

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
    cr_html = r.text
    csoup = BeautifulSoup(cr_html, 'html.parser')

    # Assuming top table entry is the current futures contract.  
    # Perhaps we could change this to consume entire table and choose the
    # table entry with the highest volume.  Need more thought here.
    cEsPriorSettle = csoup.find_all(id="QuotesFuturesProductTable1_ESH1_priorSettle")

    return 'CME ES Prior Settle {}!'.format(escape(cEsPriorSettle))

# Another comment outside function    