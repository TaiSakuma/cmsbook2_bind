# Tai Sakuma <tai.sakuma@gmail.com>
import pytest

from cmsbook2.subhead_navi import make_subhead_navi
from cmsbook2.subhead_navi import _copy
from cmsbook2.subhead_navi import _expand_item
from cmsbook2.subhead_navi import _render_item

##__________________________________________________________________||
params = [
    pytest.param(
        [ ], 'cmsbook_home', [ ], id='empty'),
    pytest.param(
        [dict(title='AAA', path='aaa'), ],
        'cmsbook_home',
        ['<a href="aaa">AAA</a>',],
        id='one-item'),
    pytest.param(
        [dict(title='AAA', path='aaa'), dict(title='BBB', path='bbb')],
        'cmsbook_home',
        ['<a href="aaa">AAA</a>', '<span> // </span>', '<a href="bbb">BBB</a>'],
        id='two-items-separator'),
    pytest.param(
        [
            dict(title='AAA', path='aaa'),
            dict(title='BBB', path='bbb'),
            dict(linebreak=True),
            dict(title='CCC', path='ccc'),
            dict(title='DDD', path='ddd'),
        ],
        'cmsbook_home',
        [
            '<a href="aaa">AAA</a>',
            '<span> // </span>',
            '<a href="bbb">BBB</a>',
            '<br />',
            '<a href="ccc">CCC</a>',
            '<span> // </span>',
            '<a href="ddd">DDD</a>',
        ],
        id='linebreak'),
    pytest.param(
        [
            dict(title='AAA', path='aaa'),
            dict(title='BBB', path='bbb'),
	        dict(right=True),
            dict(title='CCC', path='ccc'),
            dict(title='DDD', path='ddd'),
            dict(linebreak=True),
            dict(title='EEE', path='eee'),
	        dict(right=True),
            dict(title='FFF', path='fff'),
        ],
        'cmsbook_home',
        [
            '<a href="aaa">AAA</a>',
            '<span> // </span>',
            '<a href="bbb">BBB</a>',
            '<span style="float:right">',
            '<a href="ccc">CCC</a>',
            '<span> // </span>',
            '<a href="ddd">DDD</a>',
            '</span>',
            '<br />',
            '<a href="eee">EEE</a>',
            '<span style="float:right">',
            '<a href="fff">FFF</a>',
            '</span>',
        ],
        id='linebreak-right'),
]

@pytest.mark.parametrize('chapters, dirpath, expected', params)
def test_make_subhead_navi(chapters, dirpath, expected):
    assert expected == make_subhead_navi(chapters, dirpath)

##__________________________________________________________________||
params = [
    [ ],
    [dict(A="AAA", B="BBB"), ],
    [dict(A="AAA", B="BBB"), dict()],
    [dict(A="AAA", B="BBB"), dict(A="aaa", B="bbb"), ],
]

@pytest.mark.parametrize('items', params)
def test_copy(items):
    copy = _copy(items)
    assert copy == items
    assert copy is not items
    for item_copy, item_original in zip(copy, items):
        assert item_copy == item_original
        assert item_copy is not item_original

##__________________________________________________________________||
params = [

    ###
    pytest.param(
        dict(path='chapter_1'),
        'dir0',
        dict(title='chapter_1', path='chapter_1', urlpath='chapter_1',
             selected=False,
             localonly=False, lock=False),
        id='path-only'),
    pytest.param(
        dict(title='Chapter 1'),
        'dir0',
        dict(title='Chapter 1', path=None, urlpath=None,
             selected=False,
             localonly=False, lock=False),
        id='title-only'),
    pytest.param(
        dict(title='Chapter 1', path='chapter_1'),
        'dir0',
        dict(title='Chapter 1', path='chapter_1', urlpath='chapter_1',
             selected=False,
             localonly=False, lock=False),
        id='typical'),
    pytest.param(
        dict(title='Chapter 1', path='chapter_1', urlpath='ch1'),
        'dir0',
        dict(title='Chapter 1', path='chapter_1', urlpath='ch1',
             selected=False,
             localonly=False, lock=False),
        id='urlpath'),
    pytest.param(
        dict(title='Chapter 1', urlpath='ch1'),
        'dir0',
        dict(title='Chapter 1', path=None, urlpath='ch1',
             selected=False,
             localonly=False, lock=False),
        id='title-urlpath-only'),
    pytest.param(
        dict(urlpath='ch1'),
        'dir0',
        dict(title='ch1', path=None, urlpath='ch1',
             selected=False,
             localonly=False, lock=False),
        id='urlpath-only'),

    ###
    pytest.param(
        dict(title='Chapter 1', path='chapter_1'),
        'chapter_1',
        dict(title='Chapter 1', path='chapter_1', urlpath='chapter_1',
             selected=True,
             localonly=False, lock=False),
        id='selected'),
    pytest.param(
        dict(title='Chapter 1', path='chapter_1', urlpath='ch1'),
        'chapter_1',
        dict(title='Chapter 1', path='chapter_1', urlpath='ch1',
             selected=True,
             localonly=False, lock=False),
        id='selected-urlpath'),
    pytest.param(
        dict(title='Chapter 1', path='chapter_1', urlpath='ch1'),
        'ch1',
        dict(title='Chapter 1', path='chapter_1', urlpath='ch1',
             selected=False,
             localonly=False, lock=False),
        id='selected-urlpath-false'),

    ###
    pytest.param(
        dict(title='Chapter 1', path='chapter_1', localonly=True),
        'dir0',
        dict(title='Chapter 1', path='chapter_1', urlpath='chapter_1',
             selected=False,
             localonly=True, lock=False),
        id='localonly-True'),
    pytest.param(
        dict(title='Chapter 1', path='chapter_1', localonly=False),
        'dir0',
        dict(title='Chapter 1', path='chapter_1', urlpath='chapter_1',
             selected=False,
             localonly=False, lock=False),
        id='localonly-false'),

    ###
    pytest.param(
        dict(title='Chapter 1', path='chapter_1', lock=True),
        'dir0',
        dict(title='Chapter 1', path='chapter_1', urlpath='chapter_1',
             selected=False,
             localonly=False, lock=True),
        id='lock-True'),
    pytest.param(
        dict(title='Chapter 1', path='chapter_1', lock=False),
        'dir0',
        dict(title='Chapter 1', path='chapter_1', urlpath='chapter_1',
             selected=False,
             localonly=False, lock=False),
        id='lock-false'),

    ###
    pytest.param(dict(), 'dir0', dict(), id='empty'),
    pytest.param(dict(linebreak=True), 'dir0', dict(linebreak=True), id='linebreak'),
]

@pytest.mark.parametrize('item, path, expected', params)
def test_expand_item(item, path, expected):
    _expand_item(item, path)
    assert expected == item

##__________________________________________________________________||
params = [

    ###
    pytest.param(
        dict(title='Chapter 1', path='chapter_1', urlpath='chapter_1',
             selected=False,
             localonly=False, lock=False),
        '<a href="chapter_1">Chapter 1</a>',
        id='typical'),
    pytest.param(
        dict(title='Chapter 1', path='chapter_1', urlpath='chapter_1',
             selected=True,
             localonly=False, lock=False),
        '<a href="chapter_1" class="selected">Chapter 1</a>',
        id='selected'),
    pytest.param(
        dict(title='Chapter 1', path='chapter_1', urlpath='chapter_1',
             selected=False,
             localonly=True, lock=False),
        '<a href="chapter_1"><i class="fas fa-home fa-xs"></i>&nbsp;Chapter 1</a>',
        id='localonly'),
    pytest.param(
        dict(title='Chapter 1', path='chapter_1', urlpath='chapter_1',
             selected=False,
             localonly=False, lock=True),
        '<a href="chapter_1"><i class="fas fa-lock fa-xs"></i>&nbsp;Chapter 1</a>',
        id='lock'),
    pytest.param(
        dict(title='Chapter 1', path='chapter_1', urlpath='chapter_1',
             selected=False,
             localonly=True, lock=True),
        '<a href="chapter_1"><i class="fas fa-home fa-xs"></i>&nbsp;<i class="fas fa-lock fa-xs"></i>&nbsp;Chapter 1</a>',
        id='localonly-lock'),

    ###
    pytest.param(dict(), '', id='empty'),
]

@pytest.mark.parametrize('item, expected', params)
def test_render_item(item, expected):
    actual = _render_item(item)
    assert expected == actual

##__________________________________________________________________||
