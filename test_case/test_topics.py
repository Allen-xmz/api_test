from all_api.topics import Topics
import pytest

@pytest.mark.parametrize(
    "limit,tab",
    [(1, "ask"), (10, "share"),(20, "job")],
)
def test_index_page(limit,tab):
    url = "/topics"
    topics = Topics(url)
    print("-----------",topics.url)
    res = topics.get_index_topics(limit,tab)
    r = res.json()
    assert len(r['data']) == limit
    assert r['success'] == True
    assert res.status_code== 200
    all_data = r["data"]
    for data in all_data:
        assert  data["tab"] == tab

   