from http.server import BaseHTTPRequestHandler
from urllib import parse
import json

import functions

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        s = self.path
        query = dict(parse.parse_qsl(parse.urlsplit(s).query))
        print('Query input:')
        print(query)

        start = query.get('start')
        end = query.get('end')
        days = query.get('days')

        if start and end:
            print('start and end provided:', start, end)
            res = functions.business_day_diff(start, end)

        elif start and days:
            print('start and business days provided:', start, days)
            res = functions.calculate_due_date(start, int(days))

        else:
            raise Exception('Invalid input provided')

        self.wfile.write(json.dumps({ "res": res }))
        return
