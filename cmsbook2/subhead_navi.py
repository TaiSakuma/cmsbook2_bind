# Tai Sakuma <tai.sakuma@gmail.com>
from .chapter import _copy, _expand_item

##__________________________________________________________________||
def make_subhead_navi(chapters, dirpath):

    chapters = _copy(chapters)

    for item in chapters:
        _expand_item(item, dirpath)

    ret = [ ]
    right = False
    need_separator = False
    for item in chapters:
        if item.get('right', False):
            if right:
                continue
            right = True
            ret.append('<span style="float:right">')
            need_separator = False
            continue
        if item.get('linebreak', False):
            if right:
                ret.append('</span>')
                right = False
            ret.append('<br />')
            need_separator = False
            continue
        if need_separator:
            ret.append('<span> // </span>')
        ret.append(_render_item(item))
        need_separator = True

    if right:
            ret.append('</span>')

    return ret

##__________________________________________________________________||
def _render_item(item):

    if not item:
        return ''

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
