# Tai Sakuma <tai.sakuma@gmail.com>
import pytest

from cmsbook2.subhead_navi import make_subhead_navi
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
