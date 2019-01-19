# Tai Sakuma <tai.sakuma@gmail.com>

##__________________________________________________________________||
def make_pagemenu(contents, thisdir, thisfile):
    contents = _expand_contents(contents, thisdir, thisfile)
    return _render_contents(contents)

##__________________________________________________________________||
def _expand_contents(contents, thisdir, thisfile):
    contents = _add_href(contents)

def _add_href(contents):
    return [_add_href_item(i) for i in contents]

def _add_href_item(item):
    item = item.copy()
    if 'href' not in item:
        if 'dir' in item:
            if 'file' in item:
                item['href'] = '../{}/{}'.format(item['dir'], item['file'])
            else:
                item['href'] = '../{}/'.format(item['dir'])
        elif 'file' in item:
                item['href'] = '../{}'.format(item['file'])

    if 'subcontents' in item:
        item['subcontents'] = _add_href(item['subcontents'])
    return item

##__________________________________________________________________||
def _render_contents(contents):
    ret = [ ]
    ret.append('<ul>')
    for item in contents:
        ret.extend(_render_item(item))
    ret.append('</ul>')
    return ret

def _render_item(item):

    # label
    label = '&nbsp;&nbsp;{}'.format(item['head'])

    # li
    li_classes = [ ]

    if 'subcontents' in item:
        li_classes.append('has_subcontents')

    li_attributes = [ ]
    if li_classes:
        li_attributes.append('class="{}"'.format(' '.join(li_classes)))

    # a
    href = '../{}/{}'.format(item['dir'], item['file'])

    if not 'subcontents' in item:
        return [
            '<{}><div><a href="{}">{}</a></div></li>'.format(
                " ".join(['li'] + li_attributes), href, label
            )
        ]

    ret = [ ]
    ret.append(
        '<{}><div><a href="{}">{}</a></div>'.format(
            " ".join(['li'] + li_attributes), href, label
        )
    )
    ret.extend(_render_contents(item['subcontents']))
    ret.append('</li>')
    return ret

##__________________________________________________________________||
