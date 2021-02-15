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

    page = requests.get(CME_ES_url,timeout=2.5)
    #cr_content = cr.content
    # print("HTML: {}".format(cr.text)) - definietely getting HTML
    #logging.warn(RuntimeError('HTML: '+cr.text+'(logging.warn)'))
    soup = BeautifulSoup(page.content, 'html.parser')

    # need div first?
    # See https://www.dataquest.io/blog/web-scraping-tutorial-python/

    # Assuming top table entry is the current futures contract.  
    # Perhaps we could change this to consume entire table and choose the
    # table entry with the highest volume.  Need more thought here.
    prior_settle = soup.find(id="quotesFuturesProductTable1_ESH1_priorSettle").get_text()
    print(prior_settle)
    #print('bs_cEsPriorSettle: ')
    #print(bs_cEsPriorSettle)
    #cEsPriorSettle = list(bs_cEsPriorSettle)[0]
    #priorSettleText = bs_cEsPriorSettle.text
    #print('priorSettleText: ')
    #print(priorSettleText)

    return 'CME ES Prior Settle: {}!'.format(escape(prior_settle))

# Another comment outside function    