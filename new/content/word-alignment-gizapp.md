Title: Using GIZA++ to Obtain Word Alignment Between Bilingual Sentences
Date: 2015-11-20 12:00
Category: NLProc Cookbook
Tags: Machine Translation, Word Alignment

## Problem

Word alignment is mapping of words between two sentences that have the same meaning in two different languages.
Let's say we have an English and a Spanish sentence:

>
I saw a white bird on my way home. <br>
Vi un pájaro blanco camino a casa.


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

We extract bilingual sentences in Spanish (source language) and English (target language). In all the examples in this article, please replace file names with ones with appropriate path. We recommend creating a separate `work` directory to run GIZA++. Next, we use the script bundled with [Moses machine translation system](http://www.statmt.org/moses/) to tokenize text in each language (We'll cover Moses in another article):

```
cut -f3 tatoeba_es_en.tsv | mosesdecoder/scripts/tokenizer/tokenizer.perl -l es > tatoeba_es_en.tsv.es
cut -f6 tatoeba_es_en.tsv | mosesdecoder/scripts/tokenizer/tokenizer.perl -l en > tatoeba_es_en.tsv.en
```

Then go to directory `giza-pp/GIZA++-v2` and run:

```
./plain2snt.out tatoeba_es_en.tsv.es tatoeba_es_en.tsv.en
```

which will generate vcb (vocabulary) files and snt (sentence) files, containing the list of vocabulary and aligned sentences, respectively.

IBM Model 4 and 5 use word classes to model *distortion* - a concept to model how word order changes across languages, as in the 'white bird' and 'pájaro blanco' example. `mkcls` is a program to automatically infer word classes from a corpus using a maximum likelihood criterion, which can be run as follows (in the `giza-pp/mkcls-v2` directory):

```
./mkcls -ptatoeba_es_en.tsv.es -Vtatoeba_es_en.tsv.es.vcb.classes
./mkcls -ptatoeba_es_en.tsv.en -Vtatoeba_es_en.tsv.en.vcb.classes
```

See [the paper by Franz Och](http://www.aclweb.org/anthology/E99-1010) for the details of this word clustering.

Finally, use the following command to run GIZA++:

```
/GIZA++ -S tatoeba_es_en.tsv.es.vcb -T tatoeba_es_en.tsv.en.vcb -C tatoeba_es_en.tsv.es_tatoeba_es_en.tsv.en.snt -o [prefix] -outputpath [output]
```

Here, `[prefix]` and `[output]` are the prefix used for output files and the directory where output files are saved, respectively. This will generate a bunch of output files with cryptic names. Among them, probably the most important ones are `[prefix].A3.final` and `[prefix].ti.final`, which contain the actual Viterbi alignment and the lexical translation table, respectively.

## Discussion

If you see `ERROR: NO COOCURRENCE FILE GIVEN!` when running GIZA++, you may need to change `Makefile` to compile GIZA++

Before:
```
CFLAGS_OPT = $(CFLAGS) -O3 -funroll-loops -DNDEBUG -DWORDINDEX_WITH_4_BYTE -DBINARY_SEARCH_FOR_TTABLE -DWORDINDEX_WITH_4_BYTE
```
After:
```
CFLAGS_OPT = $(CFLAGS) -O3 -funroll-loops -DNDEBUG -DWORDINDEX_WITH_4_BYTE
```
(Not sure why `-DWORDINDEX_WITH_4_BYTE` is duplicated. )

Also, depending on your environment, you may need to modify some of the source files as written in [this article](http://catherinegasnier.blogspot.com/2014/04/install-giza-107-on-mac-osx-1092.html):

```
perl -pi -w -e 's/<tr1\//</g;' GIZA++-v2/* mkcls-v2/*
perl -pi -w -e 's/using namespace std::tr1;//g;' GIZA++-v2/* mkcls-v2/*
perl -pi -w -e 's/std::tr1:://g;' GIZA++-v2/* mkcls-v2/*
sed '36d' mkcls-v2/mystl.h > mkcls-v2/mystl.h.tmp
sed '50d' mkcls-v2/mystl.h.tmp > mkcls-v2/mystl.h
rm mkcls-v2/mystl.h.tmp
```

Finally, if you are using an operating system with a case-insensitive file system (e.g., Windows or OS X), you may need to modify Line 321 of `model3.cpp` as follows to prevent the `.A3.final` file from being overwritten by the `.a3.final` file:

```
-      alignfile = Prefix + ".A3." + number ;
+      alignfile = Prefix + ".VA3." + number ;      // "VA" from Viterbi alignment. Can be any file name.
```

Here are some details of input/output file format for GIZA++:

* vcb (vocabulary) file

    - This file contains a list of (uniq_id, string, number of occurrences) for each word.

* snt (entence alignment) file

    - This file contains a list of three lines - the number of times this sentence pair occurred, source sentence (with each token replaced with its uniq_id), and target sentence in the same format.

* T-tables (.ti.) file

    - This is the final inverse T-tables (lexical translation probability) trained by the model. Lexical translation probability t(e|f) is the probability that word f in the source language is translated to word e in the target language. Since this is the inverse T-tables, it contains t(f|e). The file with `actual` in its filename contains actual word strings instead of unique IDs. This is an excerpt of the `[prefix].actual.ti.final` file trained from the Tatoeba corpus:

```
bird alimentador 3.07873e-06
bird apariencias 0.00452353
bird ave 0.0917504
bird aves 0.00720495
bird jaula 0.00635498
bird madruga 0.00524571
bird madrugador 0.0061525
bird pajarito 0.00875974
bird pájaro 0.814385
bird pájaros 0.053743
bird reluce 0.0018736
bird área 3.86079e-06
```

Since it contains t(f|e), you can confirm that summing over the source (in this case, Spanish) words gives a probability 1.0.

* A (.A3.) file

    - This file contains *Viterbi Alignment*, which is the most probable alignment (the one that maximizes the alignment probability). One particular sentence pair of this file looks like:

```
# Sentence pair (8597) source length 8 target length 10 alignment score : 1.66432e-09
I saw a white bird on my way home.
NULL ({ 6 }) Vi ({ 1 2 }) un ({ 3 }) pájaro ({ 5 }) blanco ({ 4 }) camino ({ 7 8 }) a ({ }) casa ({ 9 }) . ({ 10 })
```

The first line shows the length (number of words) of the source (Spanish) and target (English) sentences, along with the Viterbi alignment score mentioned above.

The second line is the target sentence, and the third line is the source sentence annotated with alignment information. Each source word is annotated with the set of indices of target words that are aligned to that source word. Note that in IBM Models assume that one target word is aligned at most one source word. The first `NULL ({ 6 })` means the 6th target word ('on') is not aligned to any words, and `Vi ({ 1 2 })` means the first and second target words 'I saw' are aligned to 'Vi'.

