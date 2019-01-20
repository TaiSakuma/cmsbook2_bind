# Tai Sakuma <tai.sakuma@gmail.com>
import pytest

from cmsbook2.pagemenu import _copy_contents
from cmsbook2.pagemenu import _add_href_item
from cmsbook2.pagemenu import _add_thisfile_item
from cmsbook2.pagemenu import _add_thisfile_ancestor

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
