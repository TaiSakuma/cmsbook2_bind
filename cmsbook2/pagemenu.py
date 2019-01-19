# Tai Sakuma <tai.sakuma@gmail.com>

##__________________________________________________________________||
def make_pagemenu(contents, thisdir, thisfile):

    ret = [ ]
    ret.append('<ul>')
    for item in contents:
        ret.extend(make_pagemenu_item(item))
    ret.append('</ul>')
    return ret

def make_pagemenu_item(item):
    ret = [ ]
    label = '&nbsp;&nbsp;{}'.format(item['head'])
    href = '../{}/{}'.format(item['dir'], item['file'])
    print('subcontents' in item)
    ret.extend(['<li class=""><div><a href="{}">{}</a></div></li>'.format(href, label)])
    return ret

##__________________________________________________________________||
