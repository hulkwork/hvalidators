from importer import *
from utils import schema_validators
from utils import params_validators
from conf import metadata

KEY_REPONSE_TIME = 'response_time'
KEY_MESSAGE = 'msg'
KEY_ALL_PARAMS = "all-params-names"
KEY_PARAMS = 'params'
KEY_ERROR_PARAMS = "error-params"
KEY_META = 'meta'
KEY_SCHEMA = "schemas"
meta = metadata.copy()


def _params():
    t_now = datetime.now()
    meta['date'] = t_now.strftime("%Y-%m-%d %H:%M:%S")
    response_query = {}
    schema, errors = schema_validators.get_hazel_schema()
    params_available, errors_params = params_validators.get_hazel_params()

    res = {
        KEY_MESSAGE: "All params available",
        KEY_ALL_PARAMS: params_available.keys(),
        KEY_PARAMS: params_available,
        KEY_ERROR_PARAMS: errors_params,
        KEY_META: meta

    }
    schema_key = None
    if request.method == "GET":
        if request.args.get("name"):
            name = request.args.get("name")
            if name in params_available:
                res[KEY_MESSAGE] = "%s found " % name
                res[KEY_PARAMS] = params_available[name]
                res[KEY_REPONSE_TIME] = (t_now - datetime.now()).total_seconds()
                return jsonify(res), 200
            else:
                del res[KEY_ALL_PARAMS], res[KEY_PARAMS], res[KEY_ERROR_PARAMS]
                res[KEY_MESSAGE] = "< %s >not found " % name
                res[KEY_REPONSE_TIME] = (t_now - datetime.now()).total_seconds()
                return jsonify(res), 404
        else:
            res[KEY_REPONSE_TIME] = (t_now - datetime.now()).total_seconds()
            return jsonify(res), 200

    elif request.method == "POST":
        post_data = request.data.encode('utf-8')
        if request.args.get("name"):
            name = request.args.get("name")
            if name in schema:
                schema_key = schema[name]
            else:
                return jsonify({
                    KEY_MESSAGE:
                        "Make sure your %s is schema define " % name,
                    KEY_REPONSE_TIME: (t_now - datetime.now()).total_seconds()

                }), 404
        else:
            return jsonify({
                KEY_MESSAGE:
                    "Put a schema name ?name=<string>",
                KEY_REPONSE_TIME: (t_now - datetime.now()).total_seconds()

            }), 404
        try:
            post_data = json.loads(post_data)
            schema_validators.get_validate(post_data, schema_key)
            response_query['params'] = post_data
            response_query["meta"] = meta
            response_query[KEY_REPONSE_TIME] = (t_now - datetime.now()).total_seconds()
            return jsonify(response_query), 200

        except Exception, e:
            return jsonify({
                KEY_MESSAGE:
                    "Make sure your json ",
                "Exception":
                    str(e),
                KEY_REPONSE_TIME: (t_now - datetime.now()).total_seconds()
            }), 403

    return jsonify({}), 200


def _schema():
    t_now = datetime.now()
    meta['date'] = t_now.strftime("%Y-%m-%d %H:%M:%S")
    response_query = {KEY_META: meta}
    if request.method == "GET":
        schema, errors = schema_validators.get_hazel_schema()
        if request.args.get("name"):
            name = request.args.get("name")
            if name in schema:
                response_query.update({
                    KEY_MESSAGE:
                        "<%s> schema found" % name,
                    KEY_SCHEMA:
                        schema[name],
                    KEY_REPONSE_TIME: (t_now - datetime.now()).total_seconds()
                })
                return jsonify(response_query), 200
            else:
                response_query.update({
                    KEY_MESSAGE:
                        "You schema %s not found" % name,
                })
                if name in errors:
                    response_query[KEY_MESSAGE] = "You schema %s is in error" % name
                    response_query['error'] = errors[name]
                    response_query[KEY_REPONSE_TIME] = (t_now - datetime.now()).total_seconds()
                    return jsonify(response_query), 500
                else:
                    response_query[KEY_REPONSE_TIME] = (t_now - datetime.now()).total_seconds()
                    return jsonify(response_query), 404
        response_query.update({
            KEY_MESSAGE:
                "You try to get params",
            KEY_SCHEMA:
                schema,
            "error-schema": errors,
            KEY_REPONSE_TIME: (t_now - datetime.now()).total_seconds()

        })
        return jsonify(response_query), 200
    elif request.method == "POST":
        post_data_schema = request.data.encode('utf-8')
        if not request.args.get("name"):
            return jsonify({
                KEY_MESSAGE:
                    "Make sure you put ?name=<string> ",
                KEY_REPONSE_TIME: (t_now - datetime.now()).total_seconds()
            }), 403
        try:
            post_data_schema = json.loads(post_data_schema)
            schema_validators.Draft4Validator.check_schema(post_data_schema)
            response_query[KEY_SCHEMA] = post_data_schema
            response_query[KEY_REPONSE_TIME] = (t_now - datetime.now()).total_seconds()

            return jsonify(response_query), 200

        except Exception, e:
            response_query.update({
                KEY_MESSAGE:
                    "Make sure your json ",
                "Exception":
                    str(e),
                KEY_REPONSE_TIME: (t_now - datetime.now()).total_seconds()
            })
            return jsonify(response_query), 403
    response_query[KEY_REPONSE_TIME] = (t_now - datetime.now()).total_seconds()
    return jsonify(response_query), 200
