# how to run:
# FLASK_APP=cmsbook2/cmsbook2.py FLASK_DEBUG=1 flask run
# http://127.0.0.1:5000/
import os
from flask import Flask, render_template

from .chapter import load_chapter_lists
from .subhead_navi import make_subhead_navi
from .section import load_section_lists
from .pagemenu import make_pagemenu

app = Flask(__name__)

cmsbook_path = '/Users/sakuma/Dropbox/cmsbook'

##__________________________________________________________________||
@app.route('/')
def index():
    chapters = load_chapter_lists(cmsbook_path)
    subheadernavi = ''.join(make_subhead_navi(chapters))
    return render_template('index.html', subheadernavi=subheadernavi)

@app.route('/<path:path>')
def page(path):
    path_items = path.split('/')
    chapter_path = path_items[0]
    chapters = load_chapter_lists(cmsbook_path, chapter_path)
    path_title_dict = dict([(i['path'], i['title']) for i in chapters if 'path' in i])
    subheadernavi = ''.join(make_subhead_navi(chapters))
    pagemenutitle = '<a href="{}">{}</a>'.format(chapter_path, path_title_dict[chapter_path])
    thisfile = ''
    sections = load_section_lists(cmsbook_path, chapter_path, thisfile)
    pagemenu = ''.join(make_pagemenu(sections))
    content = ''
    return render_template(
        'page.html',
        subheadernavi=subheadernavi,
        pagemenutitle=pagemenutitle,
        pagemenu=pagemenu,
        content=content
    )

##__________________________________________________________________||
