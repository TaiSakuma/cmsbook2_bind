# how to run:
# FLASK_APP=cmsbook.py FLASK_DEBUG=1 flask run
# http://127.0.0.1:5000/
from flask import Flask, render_template
from cmsbook2.pagemenu import make_pagemenu

app = Flask(__name__)

@app.route('/')
def index():
    subheadernavi = ''.join(make_subhead_navi(topcontents, ''))
    return render_template('index.html', subheadernavi=subheadernavi)

@app.route('/<path:path>')
def page(path):
    path_items = path.split('/')
    parentdir = path_items[0]
    subheadernavi = ''.join(make_subhead_navi(topcontents, parentdir=parentdir))
    pagemenutitle = '<a href="../../references/s0000_index_001" class="selected">References</a>'
    thisfile = ''
    pagemenu = ''.join(make_pagemenu(contents, parentdir, thisfile))
    return render_template(
        'page.html',
        subheadernavi=subheadernavi,
        pagemenutitle=pagemenutitle,
        pagemenu=pagemenu
    )

contents = [
    dict(head="inbox (unsorted)", dir='inbox', file='md.php?md=web.md', lock=False),
    dict(head="CMS", dir='CMS', file='md.php?md=web.md', lock=False),
    dict(head="ATLAS", dir='ATLAS', file='md.php?md=web.md', lock=False),
    dict(head="LHC", dir='LHC', file='md.php?md=web.md', lock=False),
    dict(head="PDG", dir='PDG', file='md.php?md=web.md', lock=False),
    dict(head="Statistics", dir='statistics', file='md.php?md=web.md', lock=False,
         subcontents=[
             dict(head="Asimov", dir='statistics', file='md.php?md=asimov.md', lock=False),
         ]
    ),
    dict(head="LPCC LHC WGs", dir='LPCC', file='md.php?md=web.md', lock=False),
    dict(head="LHC Higgs Xsec WG", dir='LHCHXSWG', file='md.php?md=web.md', lock=False),
    dict(head="SUSY", dir='SUSY', file='md.php?md=web.md', lock=False),
    dict(head="Dark Matter", dir='DarkMatter', file='md.php?md=web.md', lock=False),
    dict(head="Machine Learning", dir='MachineLearning', file='md.php?md=web.md', lock=False),
]

topcontents = [
	dict(head='Conferences', localonly=True, parentdir='conferences', href='../../conferences/s0000_index_001'),
	dict(separator=True),
	dict(head='Publications', localonly=True, parentdir='publications', href='../../publications/s0000_index_001'),
	dict(separator=True),
	dict(head='Meetings', localonly=True, parentdir='meetings', href='../../meetings/s0000_index_001'),
	dict(separator=True),
	dict(head='Seminars', localonly=True, parentdir='seminars', href='../../Seminars/s0000_index_001'),
	dict(separator=True),
	dict(head='CV', localonly=True, parentdir='CV', href='../../CV/s0000_index_001'),
	dict(separator=True),
	dict(head='References', localonly=True, parentdir='references', href='../../references/s0000_index_001'),
	dict(right=True),
	dict(head='<i class="fas fa-cog"></i>', parentdir='help', href ='../../help/s0000_index_001'),
	dict(separator=True),
	dict(head='<i class="fas fa-inbox"></i>', parentdir='scratch', href ='../../scratch/s0000_index_001'),
]

def make_subhead_navi(topcontents, parentdir):
    ret = [ ]
    right = False
    for item in topcontents:
        if 'right' in item and item['right']:
            if right:
                continue
            right = True
            ret.append('<span style="float:right">')
            continue
        ret.append(make_subhead_navi_item(item, parentdir))

    if right:
            ret.append('</span>')

    return ret

def make_subhead_navi_item(item, parentdir):

    if 'br' in item and item['br']:
        return '<br />'

    if 'separator' in item and item['separator']:
        return '<span> // </span>'

    icons = [ ]
    if 'localonly' in item and item['localonly']:
        icons.append('<i class="fas fa-home fa-xs"></i>&nbsp;')
    if 'lock' in item and item['lock']:
        icons.append('<i class="fas fa-lock fa-xs"></i>&nbsp;')
    icons = ''.join(icons)
    label = '{icons}{head}'.format(icons=icons, head=item['head'])

    attributes = [ ]
    attributes.append('href="{}"'.format(item['href']))
    if parentdir == item['parentdir']:
        attributes.append('class="selected"')
    attributes = ' '.join(attributes)

    ret = '<a {}>{}</a>'.format(attributes, label)
    return ret

##__________________________________________________________________||