# Tai Sakuma <tai.sakuma@gmail.com>

##__________________________________________________________________||
def _copy(items):
    """return a copy of a list of dicts

    This function is used instead of the very slow copy.deepcopy().
    """
    return [i.copy() for i in items]

##__________________________________________________________________||
def _expand_item(item, path):

    if not item:
        return

    if 'linebreak' in item:
        return

    default = dict(
        title=None, path=None, urlpath=None,
        selected=False,
        localonly=False, lock=False,
    )
    for k, v in default.items():
        item[k] = item.get(k, v)

    if item['title'] is None:
        item['title'] = item['path']

    if item['title'] is None:
        item['title'] = item['urlpath']

    if item['urlpath'] is None:
        item['urlpath'] = item['path']

    if path == item['path']:
        item['selected'] = True

##__________________________________________________________________||
