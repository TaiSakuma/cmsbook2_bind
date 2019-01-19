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
    ret = [ ]
    label = '&nbsp;&nbsp;{}'.format(item['head'])
    href = '../{}/{}'.format(item['dir'], item['file'])
    print('subcontents' in item)
    ret.extend(['<li class=""><div><a href="{}">{}</a></div></li>'.format(href, label)])
    return ret

##__________________________________________________________________||
