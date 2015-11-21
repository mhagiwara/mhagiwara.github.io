Title: Using GIZA++ to Obtain Word Alignment Between Bilingual Sentences
Date: 2015-11-20 12:00
Category: NLProc Cookbook
Tags: Machine Translation, Word Alignment

## Problem

Word alignment is mapping of words between two sentences that have the same meaning in two different languages.
Let's say we have an English and a Spanish sentence:

```
I saw a white bird on my way home.
Vi un pájaro blanco camino a casa.
```

Then words 'I saw' <-> 'Vi', 'white' <-> 'blanco', 'bird' <-> 'pájaro', etc. correspond between two sentences.
Notice that words do not correspond one-to-one. For example, 'on my way' in English is translated as 'camino' in Spanish.
Also, word order may also be different across languages, e.g., 'white bird' in English becomes 'pájaro blanco' in Spanish
since Spanish adjectives are put after nouns. Given a large corpus of bilingual sentences (bitext), we would like to
compute this word alignment automatically.

## Solution

[GIZA++](https://github.com/moses-smt/giza-pp) is a toolkit to train word alignment models. GIZA++ supports IBM Model 1 to 5, now classic but most widely used unsupervised word alignment models to date. Let's use bilingual sentences from [Tatoeba project](http://tatoeba.org/) to begin with. We can use the [Tatoeba.org preprocessing script](https://github.com/mhagiwara/nlproc-cookbook/blob/master/preprocessors/tatoeba/create_bitext.py) to extract bilingual sentences from sentence and link dumps downloaded from their [downlaod page](http://tatoeba.org/eng/downloads):

```
python preprocessors/tatoeba/create_bitext.py --languages spa_eng --sentences sentences.csv --links links.csv > tatoeba_es_en.tsv
```

We extract bilingual sentences in Spanish (source language) and English (target language). We use the script bundled with [Moses machine translation system](http://www.statmt.org/moses/) to tokenize text in each language (We'll cover Moses in another article):

```
cut -f3 tatoeba_es_en.tsv | mosesdecoder/scripts/tokenizer/tokenizer.perl -l es > tatoeba_es_en.tsv.es
cut -f6 tatoeba_es_en.tsv | mosesdecoder/scripts/tokenizer/tokenizer.perl -l en > tatoeba_es_en.tsv.en
```

Then go to directory `giza-pp/GIZA++-v2` and run:

```
./plain2snt.out tatoeba_es_en.tsv.es tatoeba_es_en.tsv.en
```

which will generate vcb (vocabulary) files and snt (sentence) files, containing the list of vocabulary and aligned sentences, respectively.

IBM Model 4 and 5 use word classes to model *distortion* - a concept to model how word order changes across languages, as shown
under giza-pp/mkcls-v2

```
./mkcls -ptatoeba_es_en.tsv.es -Vtatoeba_es_en.tsv.es.vcb.classes
./mkcls -ptatoeba_es_en.tsv.en -Vtatoeba_es_en.tsv.en.vcb.classes
```

    train word classes by using a maximum-likelihood-criterion.

    See http://www.aclweb.org/anthology/E99-1010 (Section 1) for the details.

## Discussion

You may need to change the makefile to compile GIZA++. 

Before:
```
CFLAGS_OPT = $(CFLAGS) -O3 -funroll-loops -DNDEBUG -DWORDINDEX_WITH_4_BYTE -DBINARY_SEARCH_FOR_TTABLE -DWORDINDEX_WITH_4_BYTE
```
After:
```
CFLAGS_OPT = $(CFLAGS) -O3 -funroll-loops -DNDEBUG -DWORDINDEX_WITH_4_BYTE
```
(Not sure why `-DWORDINDEX_WITH_4_BYTE` is duplicated. )

http://catherinegasnier.blogspot.com/2014/04/install-giza-107-on-mac-osx-1092.html

Line 321:
-      alignfile = Prefix + ".A3." + number ;
+      alignfile = Prefix + ".VA3." + number ;
conflicts with '.a.'

Here are some details of input/output file format for GIZA++:

* vcb (vocabulary) file
From GIZA++'s manual:'
    Each entry is stored on one line as follows:

     uniq_id1 string1 no_occurrences1
     uniq_id2 string2 no_occurrences2
     uniq_id3 string3 no_occurrences3
     ....

    Here is a sample from an English vocabulary file:

    627 abandon 10
    628 abandoned 17
    629 abandoning 2
    630 abandonment 12
    631 abatement 8
    632 abbotsford 2

* snt (entence alignment) file

    Each sentence pair is stored in three lines. The first line
    is the number of times this sentence pair occurred. The second line is
    the source sentence where each token is replaced by its unique integer
    id from the vocabulary file and the third is the target sentence in
    the same format.

* T-tables (.ti.) file

T-tables (lexical translation probability) t(e|f)
        [prefix].actual.ti.final inverse table
        actual tokens instead of unique IDs
        inverse -> t(f|e)  sum_f t = 1

* A (.A3.) file

Alignment File ([prefix].A3.final)

    viterbi alignment
        the most probable alignment (the one that maximizes the alignment probability)
    alignment source <- target
    "These numbers represent the positions of the target words to which this source word is connected, according to the alignment."
    alignment score (probability)
        something called 'viterbi_score'
        in model1, product of word_best_score (max of t(e|f))
            -> max_a P(e, a|f)
            I saw a white bird on my way home.
            NULL ({ 6 }) Vi ({ 1 2 }) un ({ 3 }) pájaro ({ 5 }) blanco ({ 4 }) camino ({ 7 8 }) a ({ }) casa ({ 9 }) . ({ 10 })
