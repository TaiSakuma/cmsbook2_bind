# Tai Sakuma <tai.sakuma@gmail.com>

##__________________________________________________________________||
def make_subhead_navi(chapters, dirpath):

    chapters = _copy(chapters)

    for item in chapters:
        _expand_item(item, dirpath)

    ret = [ ]
    right = False
    for item in chapters:
        if 'right' in item and item['right']:
            if right:
                continue
            right = True
            ret.append('<span style="float:right">')
            continue
        ret.append(_render_item(item))

    if right:
            ret.append('</span>')

    return ret

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

    if 'separator' in item:
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
def _render_item(item):

    if not item:
        return ''

    if 'linebreak' in item and item['linebreak']:
        return '<br />'

    if 'separator' in item and item['separator']:
        return '<span> // </span>'

    icons = [ ]
    if item['localonly']:
        icons.append('<i class="fas fa-home fa-xs"></i>&nbsp;')
    if item['lock']:
        icons.append('<i class="fas fa-lock fa-xs"></i>&nbsp;')
    icons = ''.join(icons)
    label = '{icons}{head}'.format(icons=icons, head=item['title'])

    attributes = [ ]
    attributes.append('href="{}"'.format(item['urlpath']))
    if item['selected']:
        attributes.append('class="selected"')
    attributes = ' '.join(attributes)

    ret = '<a {}>{}</a>'.format(attributes, label)

    return ret

##__________________________________________________________________||
