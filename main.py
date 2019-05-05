from flask import make_response, request
from endpoint import fetch
import json


def scrape(request):
    """Scrape scheduled link previews.

    1. Set headers of fetch request.
    2. Call get_meta constructor.
    3. Convert metadata to JSON object.
    4. Return response.
    """
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
    target_url = request.args.get('url')
    previews = fetch.get_meta(target_url)
    response_body = json.dumps(previews)
    return make_response(str(response_body), 200, headers)
