from src.gql_query_utils import converter


def test_query_simple_fields():
    result = converter.query_to_json("""
        {
            a
            b
        }
    """)
    assert result == {'query': {'a': True, 'b': True}}


def test_query_field_sets():
    result = converter.query_to_json("""
        {
            a
            b {
                c
            }
        }
    """)
    assert result == {'query': {'a': True, 'b': {'c': True}}}


def test_query_field_arguments():
    result = converter.query_to_json("""
        query {
            a
            b (id: 50) {
                c
            }
        }
    """)
    assert result == {'query': {'a': True, 'b': {'c': True, '__args': {'id': '50'}}}}
