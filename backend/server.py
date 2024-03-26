
import json
from read import Read
from htmlparser import HtmlParser


from flask_restful.utils import cors



from flask import Flask, request#, render_template, abort

from flask_restful import Resource, Api, reqparse
from flask_caching import Cache


from flask_cors import CORS

config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}
app = Flask(__name__)
CORS(app)
# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)
api = Api(app)

parser = reqparse.RequestParser()


class Parse(Resource):
    @cors.crossdomain(origin='*')
    def post(self):
        data = request.get_json(force=True)
        print(data["type"])
        if data["type"] == "alt":
            #alt text
            print("do alt text")
        html = html = Read.read_web_page(data["website"])
       # print(html)
        parse = HtmlParser(html)
        errors = parse.check_alt_text()
        #print(errors)
        return {"problems":errors }

    def get(self):
        return "hello world"
     

@app.route('/')
def hello_world():  # put application's code here
    return "hello"


api.add_resource(Parse, "/api/parse")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, threaded=True)
