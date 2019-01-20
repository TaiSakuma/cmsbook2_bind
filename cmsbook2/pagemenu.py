# Tai Sakuma <tai.sakuma@gmail.com>

##__________________________________________________________________||
def make_pagemenu(contents, thisdir, thisfile):
    contents = _expand_contents(contents, thisdir, thisfile)
    return _render_contents(contents)

##__________________________________________________________________||
def _expand_contents(contents, thisdir, thisfile):
    contents = _copy_contents(contents)
    _add_href(contents)
    _add_thisfile(contents, thisdir, thisfile)
    _add_thisfile_ancestor(contents)
    return contents

def _copy_contents(contents):
    """return a copy of contents

    This function is used instead of the very slow copy.deepcopy().
    """
    ret = [i.copy() for i in contents]
    for item in ret:
        if 'subcontents' in item:
            item['subcontents'] = _copy_contents(item['subcontents'])
    return ret

def _add_href(contents):
    for item in contents:
        _add_href_item(item)

def _add_href_item(item):
    if 'href' not in item:
        if 'dir' in item:
            if 'file' in item:
                item['href'] = '../{}/{}'.format(item['dir'], item['file'])
            else:
                item['href'] = '../{}/'.format(item['dir'])
        elif 'file' in item:
                item['href'] = '../{}'.format(item['file'])

    if 'subcontents' in item:
        _add_href(item['subcontents'])

def _add_thisfile(contents, thisdir, thisfile):
    for item in contents:
        _add_thisfile_item(item, thisdir, thisfile)

def _add_thisfile_item(item, thisdir, thisfile):
    if 'dir' in item and 'file' in item:
        if item['dir'] == thisdir and item['file'] == thisfile:
            item['thisfile'] = True

    if 'subcontents' in item:
        _add_thisfile(item['subcontents'], thisdir, thisfile)

def _add_thisfile_ancestor(contents):
    for item in contents:
        if item.get('thisfile', False):
            return True
        if 'subcontents' in item:
            if _add_thisfile_ancestor(item['subcontents']):
                item['thisfile_ancestor'] = True
                return True
    return False

##__________________________________________________________________||
def _render_contents(contents):
    ret = [ ]
    ret.append('<ul>')
    for item in contents:
        ret.extend(_render_item(item))
    ret.append('</ul>')
    return ret

def _render_item(item):

    # li
    li_classes = [ ]

    if 'subcontents' in item:
        li_classes.append('has_subcontents')

    li_attributes = [ ]
    if li_classes:
        li_attributes.append('class="{}"'.format(' '.join(li_classes)))

    # label
    label = '&nbsp;&nbsp;{}'.format(item['head'])

    if 'href' in item:
        label = '<a href="{}">{}</a>'.format(item['href'], label)

    if not 'subcontents' in item:
        return [
            '<{}><div>{}</div></li>'.format(
                " ".join(['li'] + li_attributes), label
            )]

    ret = [ ]
    ret.append(
        '<{}><div>{}</div>'.format(
            " ".join(['li'] + li_attributes), label
        )
    )
    ret.extend(_render_contents(item['subcontents']))
    ret.append('</li>')
    return ret

##__________________________________________________________________||
