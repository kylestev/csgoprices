def obj_str(obj):
    attrs = []
    for attr in dir(obj):
        if attr[0] == '_':
            continue
        attrs.append('{}={}'.format(attr, getattr(obj, attr)))
    return '<{} {}>'.format(type(obj).__name__, ', '.join(attrs))

