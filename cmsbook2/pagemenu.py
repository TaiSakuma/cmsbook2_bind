# Tai Sakuma <tai.sakuma@gmail.com>

##__________________________________________________________________||
def make_pagemenu(contents, thisdir, thisfile):

    contents = _expand_contents(contents, thisdir, thisfile)
    return _render_contents(contents)

def _expand_contents(contents, thisdir, thisfile):
    return contents

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
