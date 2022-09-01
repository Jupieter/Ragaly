import pytest
from get_data import DB_questions


def test_html_transform():
    post_in = [
        [15, "Post 1", 25, "<p><strong>Hello World</strong></p>"], 
        [15, "Post 1", 25, "<!-- wp:tadv/classic-paragraph -->\n<p><strong>A versenyekről röviden</strong></p>\n<p>Nevezés:"]
        ]
    post_out = [
        [15, "Post 1", 25, "<p>[b]Hello World[/b]</p>"], 
        [15, "Post 1", 25, "<!-- wp:tadv/classic-paragraph -->\n<p>[b]A versenyekről röviden[/b]</p>\n<p>Nevezés:"]
        ]
    tr = DB_questions()
    test2 = tr.html_transform(post_in)
    print(test2)
    assert test2 == post_out
