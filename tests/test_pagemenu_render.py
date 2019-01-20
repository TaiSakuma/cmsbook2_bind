# Tai Sakuma <tai.sakuma@gmail.com>
import pytest

from cmsbook2.pagemenu import _render_item

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
