# how to run:
# FLASK_APP=cmsbook.py FLASK_DEBUG=1 flask run
# http://127.0.0.1:5000/
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
