# Tai Sakuma <tai.sakuma@gmail.com>
import os
import importlib.util

##__________________________________________________________________||
def load_section_lists(cmsbook_path, chapter_path, thisfile):
    sections = _load(cmsbook_path, chapter_path)
    sections = _expand(sections, chapter_path, thisfile)
    return sections

##__________________________________________________________________||
def _load(cmsbook_path, chapter_path):
    path = os.path.join(cmsbook_path, chapter_path, 'cmsbook2_chapter', 'sections.py')
    spec = importlib.util.spec_from_file_location('sections', path)
    sections = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sections)
    return sections.sections

##__________________________________________________________________||
def _expand(contents, thisdir, thisfile):
    contents = _copy_contents(contents)
    _add_href(contents)
    _add_thisfile(contents, thisdir, thisfile)
    _add_thisfile_ancestor(contents)
    return contents

##__________________________________________________________________||
def _copy_contents(contents):
    """return a copy of contents

    This function is used instead of the very slow copy.deepcopy().
    """
    ret = [i.copy() for i in contents]
    for item in ret:
        if 'subcontents' in item:
            item['subcontents'] = _copy_contents(item['subcontents'])
    return ret

def _add_href(contents):
    for item in contents:
        _add_href_item(item)

def _add_href_item(item):
    if 'href' not in item:
        if 'dir' in item:
            if 'file' in item:
                item['href'] = '../{}/{}'.format(item['dir'], item['file'])
            else:
                item['href'] = '../{}/'.format(item['dir'])
        elif 'file' in item:
                item['href'] = '../{}'.format(item['file'])

    if 'subcontents' in item:
        _add_href(item['subcontents'])

def _add_thisfile(contents, thisdir, thisfile):
    for item in contents:
        _add_thisfile_item(item, thisdir, thisfile)

def _add_thisfile_item(item, thisdir, thisfile):
    if 'dir' in item and 'file' in item:
        if item['dir'] == thisdir and item['file'] == thisfile:
            item['thisfile'] = True

    if 'subcontents' in item:
        _add_thisfile(item['subcontents'], thisdir, thisfile)

def _add_thisfile_ancestor(contents):
    for item in contents:
        if item.get('thisfile', False):
            return True
        if 'subcontents' in item:
            if _add_thisfile_ancestor(item['subcontents']):
                item['thisfile_ancestor'] = True
                return True
    return False

##__________________________________________________________________||
