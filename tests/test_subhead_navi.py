# Tai Sakuma <tai.sakuma@gmail.com>
import pytest

from cmsbook2.subhead_navi import make_subhead_navi
from cmsbook2.subhead_navi import _render_item

##__________________________________________________________________||
params = [
    pytest.param(
        [ ], [ ], id='empty'),
    pytest.param(
        [dict(title='AAA', path='aaa', urlpath='aaa', selected=False, localonly=False, lock=False), ],
        ['<a href="aaa">AAA</a>',],
        id='one-item'),
    pytest.param(
        [
            dict(title='AAA', path='aaa', urlpath='aaa', selected=False, localonly=False, lock=False),
            dict(title='BBB', path='bbb', urlpath='bbb', selected=False, localonly=False, lock=False)
        ],
        ['<a href="aaa">AAA</a>', '<span> // </span>', '<a href="bbb">BBB</a>'],
        id='two-items-separator'),
    pytest.param(
        [
            dict(title='AAA', path='aaa', urlpath='aaa', selected=False, localonly=False, lock=False),
            dict(title='BBB', path='bbb', urlpath='bbb', selected=False, localonly=False, lock=False),
            dict(linebreak=True),
            dict(title='CCC', path='ccc', urlpath='ccc', selected=False, localonly=False, lock=False),
            dict(title='DDD', path='ddd', urlpath='ddd', selected=False, localonly=False, lock=False),
        ],
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
            dict(title='AAA', path='aaa', urlpath='aaa', selected=False, localonly=False, lock=False),
            dict(title='BBB', path='bbb', urlpath='bbb', selected=False, localonly=False, lock=False),
	        dict(right=True),
            dict(title='CCC', path='ccc', urlpath='ccc', selected=False, localonly=False, lock=False),
            dict(title='DDD', path='ddd', urlpath='ddd', selected=False, localonly=False, lock=False),
            dict(linebreak=True),
            dict(title='EEE', path='eee', urlpath='eee', selected=False, localonly=False, lock=False),
	        dict(right=True),
            dict(title='FFF', path='fff', urlpath='fff', selected=False, localonly=False, lock=False),
        ],
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

@pytest.mark.parametrize('chapters, expected', params)
def test_make_subhead_navi(chapters, expected):
    assert expected == make_subhead_navi(chapters)

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
