# how to run:
# FLASK_APP=cmsbook2/cmsbook2.py FLASK_DEBUG=1 flask run
# http://127.0.0.1:5000/
import os
from flask import Flask, render_template
import importlib.util

from .chapter import load_chapter_lists
from .subhead_navi import make_subhead_navi
from .pagemenu import make_pagemenu

app = Flask(__name__)

cmsbook_path = '/Users/sakuma/Dropbox/cmsbook'

##__________________________________________________________________||
def load_section_lists(chapter_path):
    path = os.path.join(cmsbook_path, chapter_path, 'cmsbook2_chapter', 'sections.py')
    spec = importlib.util.spec_from_file_location('sections', path)
    sections = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sections)
    return sections.sections

@app.route('/')
def index():
    chapters = load_chapter_lists(cmsbook_path)
    subheadernavi = ''.join(make_subhead_navi(chapters, ''))
    return render_template('index.html', subheadernavi=subheadernavi)

@app.route('/<path:path>')
def page(path):
    path_items = path.split('/')
    chapter_path = path_items[0]
    chapters = load_chapter_lists(cmsbook_path, chapter_path)
    print(chapters)
    subheadernavi = ''.join(make_subhead_navi(chapters, chapter_path))
    pagemenutitle = '<a href="../../references/s0000_index_001" class="selected">References</a>'
    thisfile = ''
    sections = load_section_lists(chapter_path)
    pagemenu = ''.join(make_pagemenu(sections, chapter_path, thisfile))
    return render_template(
        'page.html',
        subheadernavi=subheadernavi,
        pagemenutitle=pagemenutitle,
        pagemenu=pagemenu
    )

##__________________________________________________________________||
