# -*- coding: utf-8 -*-
"""
test_vpo
----------------------------------

Tests for `vpo` module.
"""
import pytest
import vpo.generators
from vpo.generators import usefull_lines

class TestGenerators(object):
    @classmethod
    def setup_class(cls):
        cls.lines = [u'Line1 is normal',
                     u'',
                     u'#Line3 is a comment',
                     u'Line4 is normal']
        
        cls.expected = [u'Line1 is normal',
                        u'Line4 is normal']

    def test_gen_usefull_lines(self):
        def gen_lines(aList):
            for line in aList:
                yield line

        res_lines = []
        for line in usefull_lines(gen_lines(TestGenerators.lines)):
            res_lines.append(line)
        assert res_lines == TestGenerators.expected

    @classmethod
    def teardown_class(self):
        pass
