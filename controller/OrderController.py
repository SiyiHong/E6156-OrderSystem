from flask import Flask, Response, request
import json
from OrderDB import OrderDB
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello World'


@app.get("/api/health")
def get_health():
    t = str(datetime.now())
    msg = {
        "name": "F22-Starter-Microservice",
        "health": "Good",
        "at time": t
    }

    # DFF TODO Explain status codes, content type, ... ...
    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result

@app.route("/api/record/all", methods=["GET"])
def get_all_record():

    result = OrderDB.get_all()

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/record/insert/", methods=["POST"])
def insert_record():

    id = int(request.args.get("id"))
    seller_id = int(request.args.get("seller_id"))
    product_id = int(request.args.get("product_id"))
    buyer_id = int(request.args.get("buyer_id"))

    result = OrderDB.insert_record(id, seller_id, product_id, buyer_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/record/seller/<seller_id>", methods=["GET"])
def get_by_sellerId(seller_id):

    result = OrderDB.get_by_sellerId(seller_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/record/buyer/<buyer_id>", methods=["GET"])
def get_by_buyerId(buyer_id):

    result = OrderDB.get_by_buyerId(buyer_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/record/delete/", methods=["POST"])
def delete_by_orderId():
    order_id = int(request.args.get("order_id"))
    result = OrderDB.delete_by_orderId(order_id)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

if __name__ == '__main__':
    app.run()
