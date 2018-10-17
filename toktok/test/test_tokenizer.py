
# -*- coding: utf-8 -*-

"""
Tests for toktok Tokenizer
"""

import unittest

from toktok.tokenize import Tokenizer

class TestTokenzier(unittest.TestCase):
    def test_toktok_tokenize(self):
        # Tokenize a sentence.
        toktok = Tokenizer()
        text = u'Is 9.5 or 525,600 my favorite number?'
        expected_str = u'Is 9.5 or 525,600 my favorite number ?'
        tokenized_text_str = toktok.tokenize(text, return_str=True)
        assert tokenized_text_str == expected_str

    def test_toktok_tokenize_url(self):
        # Test sentence with url.
        toktok = Tokenizer()
        text = u'The https://github.com/jonsafari/tok-tok/blob/master/tok-tok.pl is a website with/and/or slashes and sort of weird : things'
        expected_str = u'The https://github.com/jonsafari/tok-tok/blob/master/tok-tok.pl is a website with/and/or slashes and sort of weird : things'
        tokenized_text_str = toktok.tokenize(text, return_str=True)
        assert tokenized_text_str == expected_str

    def test_toktok_tokenize_weird_symbols(self):
        # Test sentence with weird symbols.
        toktok = Tokenizer()
        text = u'\xa1This, is a sentence with weird\xbb symbols\u2026 appearing everywhere\xbf'
        expected_str = u'\xa1 This , is a sentence with weird \xbb symbols \u2026 appearing everywhere \xbf'
        expected_tokens = [u'\xa1', u'This', u',', u'is', u'a', u'sentence', u'with', u'weird', u'\xbb', u'symbols', u'\u2026', u'appearing', u'everywhere', u'\xbf']

        tokenized_text_str = toktok.tokenize(text, return_str=True)
        assert tokenized_text_str == expected_str

        tokenized_text = toktok.tokenize(text)
        assert tokenized_text == expected_tokens

    def test_combined_open_close_punct(self):
        # Test sentence with open and close punctuation.
        # Note: Angular brackets are kept.
        toktok = Tokenizer()
        text = u'This is a (some foo bar) sentence with lots of <brackets>, and sometimes [lists] and {sets}'
        expected_str = u'This is a ( some foo bar ) sentence with lots of <brackets> , and sometimes [ lists ] and { sets }'
        tokenized_text_str = toktok.tokenize(text, return_str=True)
        assert tokenized_text_str == expected_str
