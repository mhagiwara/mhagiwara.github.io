{"title": "Training an N-gram Language Model and Estimating Sentence Probability", "template": "page.html", "url": "training-an-n-gram-language-model-and-estimating-sentence-probability.html"}

# Training an N-gram Language Model and Estimating Sentence Probability

## Problem

A (statistical) language model is a model which assigns a probability to a sentence, which is an arbitrary sequence of words. In other words, a language model determines how likely the sentence is in that language. By far the most widely used language model is the n-gram language model, which breaks up a sentence into smaller sequences of words (n-grams) and computes the probability based on individual n-gram probabilities. Given a large corpus of plain text, we would like to train an n-gram language model, and estimate the probability for an arbitrary sentence.

## Solution

First, we need to prepare a plain text corpus from which we train a language model. We use the sample corpus from [COCA (Corpus of Contemporary American English)](http://corpus.byu.edu/coca/), which can be downloaded from [here](http://corpus.byu.edu/full-text/samples.asp). After downloading 'Word: linear text' → 'COCA: 1.7m' and unzipping the archive, we can clean all the uncompressed text files (`w_acad_1990.txt`, `w_acad_1991.txt`, ..., `w_spok_2012.txt`) using a [cleaning script](https://github.com/mhagiwara/nlproc-cookbook/blob/master/preprocessors/coca/clean.py) as follows (we assume the COCA text is unzipped under `text/` and this is run from the root directory of the Git repository):

```
cat text/*.txt | python coca/clean.py > text/coca_fulltext.clean.txt
```

We use [KenLM Language Model Toolkit](https://kheafield.com/code/kenlm/) to build an n-gram language model. KenLM is bundled with the latest version of [Moses machine translation system](http://www.statmt.org/moses/). We'll cover how to install Moses in a separate article. Let's say Moses is installed under `mosesdecoder` directory. Then we can train a trigram language model using the following command:

```
mosesdecoder/bin/lmplz -o 3 < text/coca_fulltext.clean.txt > text/coca_fulltext.clean.lm.arpa
```

This will create a file in the *ARPA format* for N-gram back-off models. You can compute the language model probability for any sentences by using the `query` command:

```
echo "I am a boy ." | mosesdecoder/bin/query text/coca_fulltext.clean.lm.arpa
```

which will output the result as follows (along with other information such as perplexity and time taken to analyze the input):

<pre>
I=486 2 -1.7037368
am=4760 3 -1.4910358
a=27 3 -1.1888235
boy=10140 2 -3.2120245
.=29 3 -0.6548149
&lt;/s&gt;=2 2 -1.335156
Total: -9.585592
OOV: 0
</pre>

The final number `-9.585592` is the *log* probability of the sentence. Since it's the logarithm, you need to compute the 10 to the power of that number, which is around 2.60 x 10<sup>-10</sup>.

## Discussion

KenLM uses a smoothing method called modified Kneser-Ney. Smoothing is a technique to adjust the probability distribution over n-grams to make better estimates of sentence probabilities. For example, any n-grams in a querying sentence which did not appear in the training corpus would be assigned a probability zero, but this is obviously wrong. We cannot cover all the possible n-grams which could appear in a language no matter how large the corpus is, and just because the n-gram didn't appear in a corpus doesn't mean it would *never* appear in any text. We are not going into the details of smoothing methods in this article. You can find [some good introductory articles](http://www.foldl.me/2014/kneser-ney-smoothing/) on Kneaser-Ney smoothing. KenLM is a very memory and time efficient implementation of Kneaser-Ney smoothing and officially distributed with Moses. You can find [a benchmark article](http://kheafield.com/code/kenlm/benchmark/) on its performance.

The file created by the `lmplz` program is in a format called `ARPA format` for N-gram back-off models. [This page](http://www.speech.sri.com/projects/srilm/manpages/ngram-format.5.html) explains the format in details, but it basically contains log probabilities and back-off weights of each n-gram. In order to compute the probability for a sentence, we look at each n-gram in the sentence from the beginning. If the n-gram is found in the table, we simply read off the log probability and add it (since it's the logarithm, we can use addition instead of product of individual probabilities). If the n-gram is not found in the table, we *back off* to its lower order n-gram, and use its probability instead, adding the back-off weights (again, we can add them since we are working in the logarithm land).

For example, suppose an excerpt of the ARPA language model file looks like the following:


<pre>
2-grams
-1.7037368      &lt;s&gt; I   -0.35425213
-3.1241505      a boy   -0.19261438
-1.9892355      am a    -0.08787394
-1.0562452      boy .   -0.19261438

3-grams
-1.4910358      &lt;s&gt; I am
-1.1888235      I am a
-0.6548149      a boy .
-1.1425415      . &lt;/s&gt;  0
</pre>

when we are looking at the trigram 'I am a' in the sentence, we can directly read off its log probability `-1.1888235` (which corresponds to log P('a' | 'I' 'am')) in the table since we do find it in the file. However, the trigram 'am a boy' is not in the table and we need to back-off to 'a boy' (notice we dropped one word from the context, i.e., the preceding words) and use its log probability `-3.1241505`. Since we backed off, we need to add the back-off weight for 'am a', which is `-0.08787394`. The sum of these two numbers is the number we saw in the analysis output next to the word 'boy' (`-3.2120245`). You can also find some explanation of the ARPA format on [the CMU Sphinx page](https://cmusphinx.github.io/wiki/tutoriallm/#building-a-grammar).
