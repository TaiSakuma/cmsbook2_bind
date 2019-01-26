# Tai Sakuma <tai.sakuma@gmail.com>
import pytest

from cmsbook2.subhead_navi import make_subhead_navi, make_subhead_navi_item

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
    pytest.param(
        dict(head='head', parentdir='parentdir', href='href'),
        'cmsbook_home',
        '<a href="href">head</a>',
        id='minimum'),
    pytest.param(
        dict(head='head', parentdir='parentdir', href='href'),
        'parentdir',
        '<a href="href" class="selected">head</a>',
        id='selected'),
    pytest.param(
        dict(head='head', localonly=True, parentdir='parentdir', href='href'),
        'cmsbook_home',
        '<a href="href"><i class="fas fa-home fa-xs"></i>&nbsp;head</a>',
        id='localonly'),
    pytest.param(
        dict(head='head', lock=True, parentdir='parentdir', href='href'),
        'cmsbook_home',
        '<a href="href"><i class="fas fa-lock fa-xs"></i>&nbsp;head</a>',
        id='lock'),
    pytest.param(
        dict(head='head', localonly=True, lock=True, parentdir='parentdir', href='href'),
        'cmsbook_home',
        '<a href="href"><i class="fas fa-home fa-xs"></i>&nbsp;<i class="fas fa-lock fa-xs"></i>&nbsp;head</a>',
        id='localonly-lock'),
    pytest.param(
        dict(head='Conferences', localonly=True, parentdir='conferences', href='../../conferences/s0000_index_001'),
        'cmsbook_home',
        '<a href="../../conferences/s0000_index_001"><i class="fas fa-home fa-xs"></i>&nbsp;Conferences</a>',
        id='one-item'),
    pytest.param(
        dict(separator=True),
        'cmsbook_home',
        '<span> // </span>',
        id='separator'),
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
