""" Tests """

from parse_rint import grfactor

class TestClass:
    def setUp(self):
        pass

    def test_1_iv_re(self):
        """ Parse a model with one independent variable and one random
        effect"""
        result = grfactor("xtmixed weight week || id: , var")
        assert result['iv'] == ['week']
        assert result['dv'] == 'weight'
        assert result['level-2-sub'] == 'id'

    def test_multiple_ivs_re(self):
        """ do we pick up multiple iv's"""
        result = grfactor("xtmixed weight week height farm || id: , var")
        assert result['iv'] == 'week height farm'.split()
        assert result['dv'] == 'weight'
        assert result['level-2-sub'] == 'id'

    def test_long_names(self):
        """ What if we have a really long dv or level-2 subject factor?"""

        result = grfactor("xtmixed weight12345678 week height farm || id: , var")
        assert result['dv'] == 'weight12345678'

        result = grfactor("xtmixed weight12345678 week height farm || pigident12345678: , var")
        assert result['level-2-sub'] == 'pigident12345678'
