# how to run:
# FLASK_APP=cmsbook2/cmsbook2.py FLASK_DEBUG=1 flask run
# http://127.0.0.1:5000/
from flask import Flask, render_template
import importlib.util

from .pagemenu import make_pagemenu
from .subhead_navi import make_subhead_navi

app = Flask(__name__)

def load_chapter_lists():
    path = '/Users/sakuma/Dropbox/cmsbook/cmsbook2_config/chapters.py'
    spec = importlib.util.spec_from_file_location('chapters', path)
    chapters = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chapters)
    return chapters.chapters

def load_section_lists():
    path = '/Users/sakuma/Dropbox/cmsbook/references/cmsbook2_chapter/sections.py'
    spec = importlib.util.spec_from_file_location('sections', path)
    sections = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sections)
    return sections.sections

@app.route('/')
def index():
    chapters = load_chapter_lists()
    subheadernavi = ''.join(make_subhead_navi(chapters, ''))
    return render_template('index.html', subheadernavi=subheadernavi)

@app.route('/<path:path>')
def page(path):
    chapters = load_chapter_lists()
    path_items = path.split('/')
    parentdir = path_items[0]
    subheadernavi = ''.join(make_subhead_navi(chapters, parentdir=parentdir))
    pagemenutitle = '<a href="../../references/s0000_index_001" class="selected">References</a>'
    thisfile = ''
    sections = load_section_lists()
    pagemenu = ''.join(make_pagemenu(sections, parentdir, thisfile))
    return render_template(
        'page.html',
        subheadernavi=subheadernavi,
        pagemenutitle=pagemenutitle,
        pagemenu=pagemenu
    )

##__________________________________________________________________||
