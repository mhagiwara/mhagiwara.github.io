{"title": "Building a Statistical Machine Translation System using Moses", "template": "page.html", "url": "building-a-statistical-machine-translation-system-using-moses.html"}


# Building a Statistical Machine Translation System using Moses

## Problem

A phrase-based statistical machine translation system translates foreign text by dividing the text into phrases (a phrase is just a sequence of one or more words,
not necessarily linguistically related) and by replacing them with phrases in the target language (e.g., English) and possibly by reordering them.
Given a large corpus of bilingual sentences (bitext), we would like to build a phrase-based machine translation system which translates text in one language to another.

## Solution

We will be using the [Moses machine translation system](http://www.statmt.org/moses/) to build our own machine translation system. Moses is a toolkit for building
statistical machine translation models given a parallel corpus (a large collection of bilingual sentences).

Specifically, we will be building a machine translation system which translates from English to [Lojban](https://en.wikipedia.org/wiki/Lojban) (a constructed syntactically unambiguous language).

After cloning [zmifanva git repository](https://github.com/mhagiwara/zmifanva) and installing Moses and GIZA++ under `mosesdecoder` and `giza-pp` respectively (see Moses's [Getting Started Guide](http://www.statmt.org/moses/?n=Development.GetStarted) for instruction), let's first prepare the training corpus by running:

    $ mkdir corpus
    $ mkdir lm
    $ python scripts/convert_solr_xml_to_bitext.py \
        docs/aspect.xml \
        docs/cll.xml \
        docs/conlang.xml \
        docs/jbowiki.xml \
        docs/phrasebook.xml \
        docs/tatoeba.xml \
        docs/teris.xml \
        docs/introduction.xml \
        docs/crashcourse1.xml \
        docs/crashcourse.jbo_eng_dict.xml \
        > corpus/train

This will create a file `corpus/train`, which is a collection of tab-separated lines of Lojban and English sentences. After this, we preprocess the training sentences by tokenizing and cleaning them:


    $ cat corpus/train | cut -f 1 | python scripts/tokenize_jbo.py > corpus/train.tok.jb
    $ cat corpus/train | cut -f 2 | mosesdecoder/scripts/tokenizer/tokenizer.perl -l en
        > corpus/train.tok.en

    $ mosesdecoder/scripts/training/clean-corpus-n.perl corpus/train.tok jb en corpus/train.clean 1 80


`clean-corpus-n.perl` is a script bundled with Moses, which filters out sentences which are either too long or too short (in this case, length is between 1 and 80 words)
or length of Lojban/English sentences is too unbalanced (by default, filters the sentence pair if the ratio of sentence length is greater than 9). This is because sentence pairs that are too long, too short, or too unbalanced, are not suited as part of training data since they may cause some difficulties, such as inaccurate word alignment.

Next, we need to build a language model. A statistical machine translation system uses a language model and a translation model to generate output in target language. A language model, as explained in [this article](/training-an-n-gram-language-model-and-estimating-sentence-probability.html), is what determines how likely (or fluent) a generated sentence (or a sentence that is being generated, which is called a *hypothesis*) in the target language.


    $ mosesdecoder/bin/lmplz -o 3 < corpus/train.clean.jb > lm/train.arpa.jb
    $ mosesdecoder/bin/build_binary lm/train.arpa.jb lm/train.blm.jb


We can give an arbitrary collection of text in order to build a language model. Here, we are just passing the Lojban part of the training corpus, although in practice a larger corpus separate from the training bilingual corpus is often used, which usually gives better results. Note that here we are binarizing the language model file so that Moses can load it faster.

Now we are ready to run the main training script of Moses as follows:

    $ mosesdecoder/scripts/training/train-model.perl \
        -root-dir train.en-jb -corpus corpus/train.clean \
        -f en -e jb -alignment grow-diag-final-and -reordering msd-bidirectional-fe \
        -lm 0:3:$PWD/lm/train.blm.jb:8 \
        -external-bin-dir mosesdecoder/tools


There seems to be a lot going on here, but the most important parameters are: `-corpus`, which specifies which training corpus it reads from (in this case, the preprocessed `corpus/train.clean.en` and `corpus/train.clean.jb` files), `-f` and `-e`, which determines the languages we are translating to and from (`f` means foreign, and `e` means English. In machine translation, by default we assume we are translating text in a foreign language to English, but in this case it's the other way), and `-root-dir`, which specifies the location where the output model is written.

After the training is finished, we can run Moses in an interactive mode by:


    $ mosesdecoder/bin/moses -f train.en-jb/model/moses.ini


We can type `Hello , everybody .` (note the tokenization --- Moses decoder itself is not responsible for tokenizing the text) and you can see the correct translation is generated by Moses as follows:


    Hello , everybody .
    Translating: Hello , everybody .
    Line 0: Initialize search took 0.000 seconds total
    Line 0: Collecting options took 0.000 seconds at moses/Manager.cpp:127
    Line 0: Search took 0.010 seconds
    coi ro do
    BEST TRANSLATION: coi ro do [1111]  [total=-6.115] core=(0.000,-3.000,2.000,-4.030,-8.843,...
    Line 0: Decision rule took 0.000 seconds total
    Line 0: Additional reporting took 0.000 seconds total
    Line 0: Translation took 0.011 seconds total


## Discussion

### Installing Moses

Installing Moses could be challenging depending which platform you are using.
Probably the easiest way is to use Ubuntu 14.04 LTS, on which you can first install all the dependencies using `sudo apt-get install`, and then Moses compiles beautifully.
As of the writing of this article (Dec. 2015), Ubuntu Server 14.04 is supported by AWS EC2 by default, so you can easily try Moses on an EC2 instance if you have an AWS account.

On Mac (OS X), You may need to install the boost library manually, as written in [this guide](http://www.statmt.org/moses/?n=Development.GetStarted).

### Behind the Scenes

There is a lot going on behind the `train-model.perl` script. At high level, what it does is:

* Run GIZA++ on the training corpus for both directions (`f` to `e` and `e` to `f`) and obtain word alignment. For the details of word alignment, see [this article](using-giza-to-obtain-word-alignment-between-bilingual-sentences.html).

* Extract phrases using both directions of word alignment. `-alignment grow-diag-final-and` option to the `train-model.perl` script specifies [the algorithm](http://homepages.inf.ed.ac.uk/pkoehn/publications/iwslt05-report.pdf) we use for this. Here, phrases are small chunks of text such as *Hello ||| coi* and *everybody ||| ro do*, that are used to compose the final translation output.

* Score phrases based on frequencies in the training corpus and lexical weights calculated from word alignment.

* Learn the reordering model. Reordering model determines how to put translated phrases in order. For example, when you are translating from Spanish ('la casa blanca') to English ('the white house'), you have to flip the order of nouns and adjectives. The `-reordering msd-bidirectional-fe` option the specific model to use for reordering.

If you are interested in the inner workings of phrase-based statistical machine translation, there are great tutorials (such as [this one](http://homepages.inf.ed.ac.uk/pkoehn/publications/tutorial2006.pdf)) and and a book ([Statistical Machine Translation](http://www.statmt.org/book/)).

### What's Next?

There could be a number of ways to improve the quality of machine translation over the baseline phrase-based model introduced here, including:

* Tuning - statistical machine translation uses a combination of sub models and features, such as language models and translation models, to come up with the best translation output. [Tuning](http://www.statmt.org/moses/?n=FactoredTraining.Tuning) tries to find the optimal weights to give to each of these sub-models, possibly boosting the translation performance.

* Syntactic Models - Moses also supports [hierarchical phrase-based models](http://www.statmt.org/moses/?n=Moses.SyntaxTutorial), which deal with grammatical rules such as `ne X1 pas -> not X1` (French-English) instead of plain phrases which are just sequences of words.

* [Sequence-to-Sequence Models](https://www.tensorflow.org/versions/master/tutorials/seq2seq/index.html) - this is a completely new paradigm for machine translation, which uses a variant of recurrent neural network called LSTM or GRU to train the mapping between input and output sequences. It is [reported](http://papers.nips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks.pdf) that this new, relatively simpler model outperforms the traditional phrase-based model.

