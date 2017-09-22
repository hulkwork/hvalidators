from utils import validators



def get_input_form(fields):
    tmp = '<input name="{name}">{name}</input>'
    if "type" in fields:
        tmp = '<input name="{name}" type="{type}">{name}</input>'
    if "required" in fields and fields["required"]:
        tmp = '<input name="{name}" type="{type} required">'
    return tmp.format(**fields)

def get_template_from_schema(schema,submit="Echo"):
    print schema
    res = ['<form action="http://localhost:5000/setParams_form" method="POST">']
    if "properties" in schema:
        for key in schema["properties"]:
            tmp_dict = {"name":key}
            tmp_dict.update(schema["properties"][key])
            res.append(get_input_form(tmp_dict))
    res.append('<input name="{submit}" type="submit">{submit}</input>'.format(**{"submit":submit}))
    res.append('</form>')
    return "\n".join(res)
