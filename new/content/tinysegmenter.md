Title: TinySegmenter in Python
Date: 2016-12-02 00:00
Category: Personal


# TinySegmenter in Python

## What is this?

"TinySegmenter in Python" is a Python re-implementation of [TinySegmenter](http://chasen.org/~taku/software/TinySegmenter/), which is an extremely compact (23KB) Japanese tokenizer originally written in JavaScript by Mr. Taku Kudo. It works on Python 2.5 or above.

The interface of "TinySegmenter in Python" is compatible with [NLTK](http://www.nltk.org/)'s TokenizerI, although the distribution file below does not directly depend on NLTK. If you'd like to use it as a tokenizer in NLTK, you have to modify the first few lines of the code as below:


    import nltk
    import re
    from nltk.tokenize.api import *

    class TinySegmenter(TokenizerI):

## Download and Usage

Download the source code from [here](https://github.com/mhagiwara/nltk/blob/master/jpbook/tinysegmenter.py). TinySegmenter in Python is freely distributable under the terms of a new BSD license. </p>

No need to install it - just copy it anywhere, import it, and use it as the follow example:


    from tinysegmenter import *

    segmenter = TinySegmenter()
    print ' | '.join(segmenter.tokenize(u"私の名前は中野です"))

    私 | の | 名前 | は | 中野 | です


### Features (from the original TinySegmenter)


- Around 95% segemntation precision for Japanese news articles.
- Segmentation units are compatible with [MeCab + IPADic](http://taku910.github.io/mecab/)
- Only 23KB of source code. Just copy it anywhere and no other things are required.
-  No dependency on any dictionaries - character-based segmentation (Features: character, character N-grams, character types).
- Feature selection by L1-norm regularization [Boosting](http://en.wikipedia.org/wiki/AdaBoost).


### A Better Alternative

If you are interested in more accurate analysis of Japanese and Chinese text in JavaScript,  check out my other open source project [Rakuten MA](https://github.com/rakuten-nlp/rakutenma), which is an open source morphological analyzer written in 100% JavaScript, supporting PoS tagging in Japanese and Chinese.

### Acknowledgment

I thank Mr. Kudo for his effort on this kind of wonderful software.

