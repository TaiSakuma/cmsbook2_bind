# Tai Sakuma <tai.sakuma@gmail.com>

##__________________________________________________________________||
def make_pagemenu(contents):
    return _render_contents(contents)

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

    if item.get('thisfile', False):
        li_classes.append('selected')

    li_attributes = [ ]
    if li_classes:
        li_attributes.append('class="{}"'.format(' '.join(li_classes)))

    # label
    label = '&nbsp;&nbsp;{}'.format(item['head'])

    if 'href' in item:
        a_classes = [ ]
        if item.get('thisfile', False):
            a_classes.append('selected')
        a_attributes = [ ]
        a_attributes.append('href="{}"'.format(item['href']))
        if a_classes:
            a_attributes.append('class="{}"'.format(' '.join(a_classes)))
        label = '<{}>{}</a>'.format(
            " ".join(['a'] + a_attributes), label)

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
