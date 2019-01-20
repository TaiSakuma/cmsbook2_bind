# Tai Sakuma <tai.sakuma@gmail.com>
import pytest

from cmsbook2.pagemenu import _render_item

##__________________________________________________________________||
params = [
    pytest.param(
        dict(head="headAAA", href='hrefAAA', lock=False),
        ['<li><div><a href="hrefAAA">&nbsp;&nbsp;headAAA</a></div></li>'],
        id='simple'),
    pytest.param(
        dict(head="headAAA", lock=False),
        ['<li><div>&nbsp;&nbsp;headAAA</div></li>'],
        id='no-href'),
    pytest.param(
        dict(head="headAAA", href='hrefAAA', lock=False,
             subcontents=[
                 dict(head="headBBB", href='hrefBBB', lock=False),
             ]
        ),
        [
            '<li class="has_subcontents"><div><a href="hrefAAA">&nbsp;&nbsp;headAAA</a></div>',
            '<ul>',
            '<li><div><a href="hrefBBB">&nbsp;&nbsp;headBBB</a></div></li>',
            '</ul>',
            '</li>',
        ],
        id='subcontents-href'),
    pytest.param(
        dict(head="headAAA", lock=False,
             subcontents=[
                 dict(head="headBBB", href='hrefBBB', lock=False),
             ]
        ),
        [
            '<li class="has_subcontents"><div>&nbsp;&nbsp;headAAA</div>',
            '<ul>',
            '<li><div><a href="hrefBBB">&nbsp;&nbsp;headBBB</a></div></li>',
            '</ul>',
            '</li>',
        ],
        id='subcontents-no-href'),
]

@pytest.mark.parametrize('item, expected', params)
def test_render_item(item, expected):
    assert expected == _render_item(item)

##__________________________________________________________________||
