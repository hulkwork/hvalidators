import json
from datetime import datetime
from flask import request, jsonify
from utils import validators
from conf import metadata

meta = metadata.copy()

def _params():
    meta['date'] = datetime.now().strptime("%Y-%m-%d %H:%M:%S")
    response_query = {}
    schema, errors = validators.get_all_valide_schema()
    params_available = {"default": {
        "price": 2000,
        "name": "Hulk"
    }}
    res = {
        "msg": "All params available",
        "params": params_available,
        "meta" : meta

    }
    schema_key = None
    if request.method == "GET":
        if request.args.get("name"):
            name = request.args.get("name")
            if name in params_available:
                res["msg"] = "%s found " % name
                res['params'] = params_available[name]
                return jsonify(res), 200
            else:
                res["msg"] = "< %s >not found " % name
                return jsonify(res), 404
        else:
            return jsonify(res), 200

    elif request.method == "POST":
        post_data = request.data.encode('utf-8')
        if request.args.get("name"):
            name = request.args.get("name")
            if name in schema:
                schema_key = schema[name]
            else:
                return jsonify({
                    "msg":
                        "Make sure your %s is schema define " % name,

                }), 404
        else:
            return jsonify({
                "msg":
                    "Put a schema name ?name=<string>",

            }), 404
        try:
            post_data = json.loads(post_data)
            validators.get_validate(post_data, schema_key)
            response_query['params'] = post_data
            response_query["meta"] = {
                "date":
                    datetime.now()
            }
            return jsonify({}), 200

        except Exception, e:
            return jsonify({
                "msg":
                    "Make sure your json ",
                "Exception":
                    str(e)
            }), 403

    return jsonify({}), 200


def _schema():
    meta['date'] = datetime.now().strptime("%Y-%m-%d %H:%M:%S")
    response_query = {"meta":meta}
    if request.method == "GET":
        schema, errors = validators.get_all_valide_schema()
        if request.args.get("name"):
            name = request.args.get("name")
            if name in schema:
                response_query.update({
                    "msg":
                        "<%s> schema found" % name,
                    "schemas":
                        schema[name]
                })
                return jsonify(response_query), 200
            else:
                response_query.update({
                    "msg":
                        "You schema %s not found" % name,
                })
                if name in errors:
                    response_query["msg"] = "You schema %s is in error" % name
                    response_query['error'] = errors[name]
                    return jsonify(response_query), 500
                else:
                    return jsonify(response_query), 404
        response_query.update({
            "msg":
                "You try to get params",
            "schemas":
                schema,
            "error-schema": errors
        })
        return jsonify(response_query), 200
    elif request.method == "POST":
        post_data_schema = request.data.encode('utf-8')
        if not request.args.get("name"):
            return jsonify({
                "msg":
                    "Make sure you put ?name=<string> "
            }), 403
        try:
            post_data_schema = json.loads(post_data_schema)
            validators.Draft4Validator.check_schema(post_data_schema)
            response_query['schema'] = post_data_schema

            return jsonify(response_query), 200

        except Exception, e:
            response_query.update({
                "msg":
                    "Make sure your json ",
                "Exception":
                    str(e)
            })
            return jsonify(response_query), 403

    return jsonify(response_query), 200
