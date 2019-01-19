# Tai Sakuma <tai.sakuma@gmail.com>
import pytest

from cmsbook2.pagemenu import make_pagemenu, _render_item
from cmsbook2.pagemenu import _copy_contents
from cmsbook2.pagemenu import _add_href_item
from cmsbook2.pagemenu import _add_thisfile_item
from cmsbook2.pagemenu import _add_thisfile_ancestor

##__________________________________________________________________||
params = [
    pytest.param(
        [
            dict(head="inbox (unsorted)", dir='inbox', file='md.php?md=web.md', lock=False),
            dict(head="CMS", dir='CMS', file='md.php?md=web.md', lock=False),
            dict(head="ATLAS", dir='ATLAS', file='md.php?md=web.md', lock=False),
            dict(head="LHC", dir='LHC', file='md.php?md=web.md', lock=False),
            dict(head="PDG", dir='PDG', file='md.php?md=web.md', lock=False),
            dict(head="Statistics", dir='statistics', file='md.php?md=web.md', lock=False,
                 subcontents=[
                     dict(head="Asimov", dir='statistics', file='md.php?md=asimov.md', lock=False),
                 ]
            ),
            dict(head="LPCC LHC WGs", dir='LPCC', file='md.php?md=web.md', lock=False),
            dict(head="LHC Higgs Xsec WG", dir='LHCHXSWG', file='md.php?md=web.md', lock=False),
            dict(head="SUSY", dir='SUSY', file='md.php?md=web.md', lock=False),
            dict(head="Dark Matter", dir='DarkMatter', file='md.php?md=web.md', lock=False),
            dict(head="Machine Learning", dir='MachineLearning', file='md.php?md=web.md', lock=False),
        ],
        'MachineLearning',
        'md.php?md=web.md',
        [
            '<ul>',
            '<li><div><a href="../inbox/md.php?md=web.md">&nbsp;&nbsp;inbox (unsorted)</a></div></li>',
            '<li><div><a href="../CMS/md.php?md=web.md">&nbsp;&nbsp;CMS</a></div></li>',
            '<li><div><a href="../ATLAS/md.php?md=web.md">&nbsp;&nbsp;ATLAS</a></div></li>',
            '<li><div><a href="../LHC/md.php?md=web.md">&nbsp;&nbsp;LHC</a></div></li>',
            '<li><div><a href="../PDG/md.php?md=web.md">&nbsp;&nbsp;PDG</a></div></li>',
            '<li class="has_subcontents"><div><a href="../statistics/md.php?md=web.md">&nbsp;&nbsp;Statistics</a></div>',
            '<ul>',
            '<li><div><a href="../statistics/md.php?md=asimov.md">&nbsp;&nbsp;Asimov</a></div></li>',
            '</ul>',
            '</li>',
            '<li><div><a href="../LPCC/md.php?md=web.md">&nbsp;&nbsp;LPCC LHC WGs</a></div></li>',
            '<li><div><a href="../LHCHXSWG/md.php?md=web.md">&nbsp;&nbsp;LHC Higgs Xsec WG</a></div></li>',
            '<li><div><a href="../SUSY/md.php?md=web.md">&nbsp;&nbsp;SUSY</a></div></li>',
            '<li><div><a href="../DarkMatter/md.php?md=web.md">&nbsp;&nbsp;Dark Matter</a></div></li>',
            '<li class=" selected"><div><a href="../MachineLearning/md.php?md=web.md" class="selected">&nbsp;&nbsp;Machine Learning</a></div></li>',
            '</ul>',
        ]
    )
]

@pytest.mark.parametrize('contents, thisdir, thisfile, expected', params)
def test_make_pagemenu(contents, thisdir, thisfile, expected):
    assert expected == make_pagemenu(contents, thisdir, thisfile)

##__________________________________________________________________||
params = [
    pytest.param(
        dict(head="inbox (unsorted)", dir='inbox', file='md.php?md=web.md', lock=False),
        ['<li><div><a href="../inbox/md.php?md=web.md">&nbsp;&nbsp;inbox (unsorted)</a></div></li>']
    ),
    pytest.param(
        dict(head="Statistics", dir='statistics', file='md.php?md=web.md', lock=False,
             subcontents=[
                 dict(head="Asimov", dir='statistics', file='md.php?md=asimov.md', lock=False),
             ]
        ),
        [
            '<li class="has_subcontents"><div><a href="../statistics/md.php?md=web.md">&nbsp;&nbsp;Statistics</a></div>',
            '<ul>',
            '<li><div><a href="../statistics/md.php?md=asimov.md">&nbsp;&nbsp;Asimov</a></div></li>',
            '</ul>',
            '</li>',
        ]
    )
]

@pytest.mark.parametrize('item, expected', params)
def test_render_item(item, expected):
    assert expected == _render_item(item)


##__________________________________________________________________||
params = [
    pytest.param([dict(head="AAA")], id='simple'),
    pytest.param(
        [dict(head="AAA", subcontents=[dict(head="BBB")])],
        id='nested-1'),
    pytest.param(
        [dict(head="AAA", subcontents=[
            dict(head="BBB", subcontents=[dict(head="CCC")])
        ]
        )],
        id='nested-2'),
]

@pytest.mark.parametrize('contents', params)
def test_copy_contents(contents):
    copy = _copy_contents(contents)
    assert copy is not contents
    for item_copy, item_original in zip(copy, contents):
        assert item_copy is not item_original
        if 'subcontents' in item_original:
            assert item_copy['subcontents'] is not item_original['subcontents']
            for item_copy2, item_original2 in zip(item_copy['subcontents'], item_original['subcontents']):
                assert item_copy2 is not item_original2
                if 'subcontents' in item_original2:
                    assert item_copy2['subcontents'] is not item_original2['subcontents']

##__________________________________________________________________||
params = [
    pytest.param(
        dict(head="AAA", dir='dirA', file='fileA'),
        dict(head="AAA", dir='dirA', file='fileA', href='../dirA/fileA'),
        id='simple'),
    pytest.param(
        dict(head="AAA", dir='dirA', file='fileA', href='hrefA'),
        dict(head="AAA", dir='dirA', file='fileA', href='hrefA'),
        id='href-exist'),
    pytest.param(
        dict(head="AAA", dir='dirA'),
        dict(head="AAA", dir='dirA', href='../dirA/'),
        id='dir-only'),
    pytest.param(
        dict(head="AAA", file='fileA'),
        dict(head="AAA", file='fileA', href='../fileA'),
        id='file-only'),
    pytest.param(
        dict(head="AAA"),
        dict(head="AAA"),
        id='no-dir-or-file'),
    pytest.param(
        dict(head="AAA", href='hrefA'),
        dict(head="AAA", href='hrefA'),
        id='href-only'),
]

@pytest.mark.parametrize('item, expected', params)
def test_add_href_item(item, expected):
    _add_href_item(item)
    assert expected == item

params = [
    pytest.param(
        dict(head="AAA", subcontents=[
            dict(head="111", dir='dir1', file='file1'),
            dict(head="222", dir='dir1', file='file2'),
        ]),
        dict(head="AAA", subcontents=[
            dict(head="111", dir='dir1', file='file1', href='../dir1/file1'),
            dict(head="222", dir='dir1', file='file2', href='../dir1/file2'),
        ]),
        id='subcontents'),
    pytest.param(
        dict(head="AAA", subcontents=[ ]),
        dict(head="AAA", subcontents=[ ]),
        id='empty'),
    pytest.param(
        dict(head="AAA", subcontents=[
            dict(head="111", dir='dir1', file='file1'),
            dict(head="222", dir='dir1', file='file2'),
            dict(head="aaaa", dir='dir2', file='file3', subcontents=[
                dict(head="333", dir='dir3', file='file4'),
            ]),
        ]),
        dict(head="AAA", subcontents=[
            dict(head="111", dir='dir1', file='file1', href='../dir1/file1'),
            dict(head="222", dir='dir1', file='file2', href='../dir1/file2'),
            dict(head="aaaa", dir='dir2', file='file3', href='../dir2/file3', subcontents=[
                dict(head="333", dir='dir3', file='file4', href='../dir3/file4'),
            ]),
        ]),
        id='nested'),
]

@pytest.mark.parametrize('item, expected', params)
def test_add_href_item_subcontents(item, expected):
    _add_href_item(item)
    assert expected == item

##__________________________________________________________________||
params = [
    pytest.param(
        dict(head="AAA", dir='dirA', file='fileA'),
        'dirA', 'fileA',
        dict(head="AAA", dir='dirA', file='fileA', thisfile=True),
        id='simple-true'),
    pytest.param(
        dict(head="AAA", dir='dirA', file='fileA'),
        'dirA', 'fileB',
        dict(head="AAA", dir='dirA', file='fileA'),
        id='simple-false-1'),
    pytest.param(
        dict(head="AAA", dir='dirA', file='fileA'),
        'dirB', 'fileA',
        dict(head="AAA", dir='dirA', file='fileA'),
        id='simple-false-2'),
    pytest.param(
        dict(head="AAA", subcontents=[
            dict(head="111", dir='dir1', file='file1'),
            dict(head="222", dir='dir1', file='file2'),
            dict(head="aaaa", dir='dir2', file='file3', subcontents=[
                dict(head="333", dir='dir3', file='file4'),
            ]),
        ]),
        'dir3', 'file4',
        dict(head="AAA", subcontents=[
            dict(head="111", dir='dir1', file='file1'),
            dict(head="222", dir='dir1', file='file2'),
            dict(head="aaaa", dir='dir2', file='file3', subcontents=[
                dict(head="333", dir='dir3', file='file4', thisfile=True),
            ]),
        ]),
        id='nested'),
]

@pytest.mark.parametrize('item, thisdir, thisfile, expected', params)
def test_add_thisfile_item(item, thisdir, thisfile, expected):
    _add_thisfile_item(item, thisdir, thisfile)
    assert expected == item

##__________________________________________________________________||
params = [
    pytest.param(
        [
            dict(head="AAA", subcontents=[
                dict(head="111", dir='dirA', file='file111'),
                dict(head="222", dir='dirA', file='file222'),
                dict(head="333", dir='dirA', file='file333', subcontents=[
                    dict(head="333 a", dir='dirA', file='file333_a', thisfile=True),
                ]),
            ]),
            dict(head="BBB", dir='dirA', file='file111')
        ],
        [
            dict(head="AAA", thisfile_ancestor=True, subcontents=[
                dict(head="111", dir='dirA', file='file111'),
                dict(head="222", dir='dirA', file='file222'),
                dict(head="333", dir='dirA', file='file333', thisfile_ancestor=True, subcontents=[
                    dict(head="333 a", dir='dirA', file='file333_a', thisfile=True),
                ]),
            ]),
            dict(head="BBB", dir='dirA', file='file111')
        ],
    ),
]

@pytest.mark.parametrize('contents, expected', params)
def test_add_thisfile_ancestor(contents, expected):
    _add_thisfile_ancestor(contents)
    assert expected == contents

##__________________________________________________________________||
