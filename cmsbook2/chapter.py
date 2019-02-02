# Tai Sakuma <tai.sakuma@gmail.com>
import os
import importlib.util

##__________________________________________________________________||
def load_chapter_lists(cmsbook_path):
    path = os.path.join(cmsbook_path, 'cmsbook2_config', 'chapters.py')
    spec = importlib.util.spec_from_file_location('chapters', path)
    chapters = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chapters)
    return chapters.chapters

##__________________________________________________________________||
def _copy(items):
    """return a copy of a list of dicts

    This function is used instead of the very slow copy.deepcopy().
    """
    return [i.copy() for i in items]

##__________________________________________________________________||
def _expand_item(item, path):

    if not item:
        return

    if 'linebreak' in item:
        return

    default = dict(
        title=None, path=None, urlpath=None,
        selected=False,
        localonly=False, lock=False,
    )
    for k, v in default.items():
        item[k] = item.get(k, v)

    if item['title'] is None:
        item['title'] = item['path']

    if item['title'] is None:
        item['title'] = item['urlpath']

    if item['urlpath'] is None:
        item['urlpath'] = item['path']

    if path == item['path']:
        item['selected'] = True

##__________________________________________________________________||
