# how to run:
# FLASK_APP=cmsbook.py FLASK_DEBUG=1 flask run
# http://127.0.0.1:5000/
from flask import Flask, render_template

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
    return render_template(
        'page.html',
        subheadernavi=subheadernavi,
        pagemenutitle=pagemenutitle,
        pagemenu=pagemenu
    )

pagemenu = """
        <ul>
            <li class=""><div><a href="../inbox/md.php?md=web.md">&nbsp;&nbsp;inbox (unsorted)</a></div></li>
            <li class=""><div><a href="../CMS/md.php?md=web.md">&nbsp;&nbsp;CMS</a></div></li>
            <li class=""><div><a href="../ATLAS/md.php?md=web.md">&nbsp;&nbsp;ATLAS</a></div></li>
            <li class=""><div><a href="../LHC/md.php?md=web.md">&nbsp;&nbsp;LHC</a></div></li>
            <li class=""><div><a href="../PDG/md.php?md=web.md">&nbsp;&nbsp;PDG</a></div></li>

            <li class=" has_subcontents"><div><a href="../statistics/md.php?md=web.md">&nbsp;&nbsp;Statistics</a></div><ul>
                <li class=""><div><a href="../statistics/md.php?md=asimov.md">&nbsp;&nbsp;Asimov</a></div></li>
            </ul>
            </li>
            <li class=""><div><a href="../LPCC/md.php?md=web.md">&nbsp;&nbsp;LPCC LHC WGs</a></div></li>
            <li class=""><div><a href="../LHCHXSWG/md.php?md=web.md">&nbsp;&nbsp;LHC Higgs Xsec WG</a></div></li>
            <li class=""><div><a href="../SUSY/md.php?md=web.md">&nbsp;&nbsp;SUSY</a></div></li>
            <li class=""><div><a href="../DarkMatter/md.php?md=web.md">&nbsp;&nbsp;Dark Matter</a></div></li>
            <li class=" selected"><div><a href="../MachineLearning/md.php?md=web.md" class="selected">&nbsp;&nbsp;Machine Learning</a></div></li>
        </ul>
"""

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
