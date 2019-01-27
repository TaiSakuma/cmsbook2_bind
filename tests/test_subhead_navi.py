# Tai Sakuma <tai.sakuma@gmail.com>
import pytest

from cmsbook2.subhead_navi import make_subhead_navi, make_subhead_navi_item
from cmsbook2.subhead_navi import _expand_item

##__________________________________________________________________||
params = [
    pytest.param(
        [ ], 'cmsbook_home', [ ], id='empty'),
    pytest.param(
        [dict(head = 'Conferences', localonly = True, parentdir = 'conferences', href = '../../conferences/s0000_index_001'), ],
        'cmsbook_home',
        ['<a href="../../conferences/s0000_index_001"><i class="fas fa-home fa-xs"></i>&nbsp;Conferences</a>',],
        id='one-item'),
    pytest.param(
        [
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
        ],
        'cmsbook_home',
        [
            '<a href="../../conferences/s0000_index_001"><i class="fas fa-home fa-xs"></i>&nbsp;Conferences</a>',
            '<span> // </span>',
            '<a href="../../publications/s0000_index_001"><i class="fas fa-home fa-xs"></i>&nbsp;Publications</a>',
            '<span> // </span>',
            '<a href="../../meetings/s0000_index_001"><i class="fas fa-home fa-xs"></i>&nbsp;Meetings</a>',
            '<span> // </span>',
            '<a href="../../Seminars/s0000_index_001"><i class="fas fa-home fa-xs"></i>&nbsp;Seminars</a>',
            '<span> // </span>',
            '<a href="../../CV/s0000_index_001"><i class="fas fa-home fa-xs"></i>&nbsp;CV</a>',
            '<span> // </span>',
            '<a href="../../references/s0000_index_001"><i class="fas fa-home fa-xs"></i>&nbsp;References</a>',
            '<span style="float:right">',
            '<a href="../../help/s0000_index_001"><i class="fas fa-cog"></i></a>',
            '<span> // </span>',
            '<a href="../../scratch/s0000_index_001"><i class="fas fa-inbox"></i></a>',
            '</span>',
        ],
        id='full-example'),
]

@pytest.mark.parametrize('topcontents, parentdir, expected', params)
def test_make_subhead_navi(topcontents, parentdir, expected):
    assert expected == make_subhead_navi(topcontents, parentdir)

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
    pytest.param(dict(separator=True), 'dir0', dict(separator=True), id='separator'),
    pytest.param(dict(linebreak=True), 'dir0', dict(linebreak=True), id='linebreak'),
    pytest.param(
        dict(separator=True, linebreak=True),
        'dir0',
        dict(separator=True, linebreak=True),
        id='separator-linebreak'),
]

@pytest.mark.parametrize('item, path, expected', params)
def test_expand_item(item, path, expected):
    _expand_item(item, path)
    assert expected == item


    pytest.param(
        dict(br=True),
        'cmsbook_home',
        '<br />',
        id='br'),
    pytest.param(
        dict(separator=True, br=True),
        'cmsbook_home',
        '<br />', # separator ignored
        id='br-separator'),
]

@pytest.mark.parametrize('item, parentdir, expected', params)
def test_make_subhead_navi_item(item, parentdir, expected):
    assert expected == make_subhead_navi_item(item, parentdir)

##__________________________________________________________________||
