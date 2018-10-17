# Toktok

Stand-alone Python port of [Tok-Tok Tokenizer](https://github.com/jonsafari/tok-tok)


Install
====

```
pip install -U toktok
```

Usage
====

```python
>>> toktok = ToktokTokenizer()
>>> text = u'Is 9.5 or 525,600 my favorite number?'
>>> print (toktok.tokenize(text, return_str=True))
Is 9.5 or 525,600 my favorite number ?

>>> text = u'The https://github.com/jonsafari/tok-tok/blob/master/tok-tok.pl is a website with/and/or slashes and sort of weird : things'
>>> print (toktok.tokenize(text, return_str=True))
The https://github.com/jonsafari/tok-tok/blob/master/tok-tok.pl is a website with/and/or slashes and sort of weird : things

>>> text = u'\xa1This, is a sentence with weird\xbb symbols\u2026 appearing everywhere\xbf'
>>> expected = u'\xa1 This , is a sentence with weird \xbb symbols \u2026 appearing everywhere \xbf'
>>> toktok.tokenize(text, return_str=True) == expected
True
>>> toktok.tokenize(text)
[u'\xa1', u'This', u',', u'is', u'a', u'sentence', u'with', u'weird', u'\xbb', u'symbols', u'\u2026', u'appearing', u'everywhere', u'\xbf']


>>> text = u'This is a (some foo bar) sentence with lots of <brackets>, and sometimes [lists] and {sets
>>> toktok.tokenize(text, return_str=True)
This is a ( some foo bar ) sentence with lots of <brackets> , and sometimes [ lists ] and { sets }
```
