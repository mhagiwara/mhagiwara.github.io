Title: NLTK Japanese Corpora - NLTKで使える日本語コーパス
Date: 2016-12-10 00:00
Category: Personal
save_as: nltk-japanese-corpus.html
url: nltk-japanese-corpus.html

NLTK (Natural Language Toolkit) is an excellent toolkit which you can use for natural language processing and text mining experiments and learning. Unfortunately it doesn't include Japanese large corpora and this makes it relatively difficult to try some experiments using Japanese linguistic resources. Here I introduce two Japanese freely available corpora, along with their corpus reader modules. By using corpus readers, you can easily access the corpora with the unified interface.

NLTK (Natural Language Toolkit) は、自然言語処理やテキストマイニングの実験や実習用の素晴らしツールキットですが、残念ながら現時点で日本語の大規模コーパスが含まれておらず、日本語の言語資源を用いた実験を気軽に試すハードルが高くなってしまっています。ここでは、自由に利用可能な日本語のコーパスを２つ紹介し、それらに対応した CorpusReader を配布しています。これによって、他のコーパスと同様のインターフェースによって簡単にコーパスにアクセスできるようになります。

## 1. KNB Corpus (Annotated blog corpus) KNB (解析済みブログ)コーパス

### Corpus Introduction - コーパスについて

KNB Corpus is a re-distributable, annotated Japanese blog corpus, which consists of 249 articles and 4186 sentences. Its annotation includes morphology, dependency, case, omission, anaphora, and review information.

KNB コーパスは、再配布可能な日本語タグ付きブログコーパスで、249記事、4,189文から成ります。形態素、構文、格・省略・照応、評判情報を含んでいます。

### Download and Usage - ダウンロードおよび使用法

First, download the [KNB corpus](http://nlp.ist.i.kyoto-u.ac.jp/kuntt/#ga739fe2) distribution file from here:  [解析済みブログコーパス (KNBC_v1.0_090925.tar.bz2; 4.2MB)](http://nlp.ist.i.kyoto-u.ac.jp/kuntt/KNBC_v1.0_090925.tar.bz2), and put the decompressed files under NLTK's data directly (nltk_data by default).

まず [KNB コーパス](http://nlp.ist.i.kyoto-u.ac.jp/kuntt/#ga739fe2) の配布ファイルをこちらからダウンロードしてください: [解析済みブログコーパス (KNBC_v1.0_090925.tar.bz2; 4.2MB)](http://nlp.ist.i.kyoto-u.ac.jp/kuntt/KNBC_v1.0_090925.tar.bz2)。 ファイルを解凍し、NLTKのデータディレクトリ (デフォルトでは nltk_data) の下に置いてください。

Next, download the source code of the corpus reader from here: [knbc.py](https://github.com/mhagiwara/nltk/blob/master/jpbook/knbc.py). KNB Corpus reader is distributed under the same license as NLTK itself ([Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)).

次に、コーパスリーダーのソースコードを [knbc.py](https://github.com/mhagiwara/nltk/blob/master/jpbook/knbc.py) からダウンロードしてください。 このコーパスリーダーは、NLTK と同じライセンス ([Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)) の元で再配布可能です。</p>

For the basic usage, please refer to the demo() function in the source file. Firstly, you can find the data directory where you put the files by nltk.data.find() and then list up all the corpus files as fileids:

基本的な使い方については、ソースコードの demo() 関数を参照してください。まず、コーパスが格納されているディレクトリを nltk.data.find() によって取得し、コーパスを構成するファイルを fileids として列挙します:


    root = nltk.data.find('corpora/knbc/corpus1')
    fileids = [f for f in find_corpus_fileids(FileSystemPathPointer(root), ".*")
               if re.search(r"\d\-\d\-[\d]+\-[\d]+", f)]

Then you can sort fileids and pass all of them to the KNBCorpusReader constructor as below. All the fileids can be obtained by the corpus reader's fileids() method.

次に、fileids を番号順にソートし、 KNBCorpusReader のコンストラクタにリストとして全て渡します。全ての fileid は、コーパスリーダーの fileids() メソッドによって取得できます。


    def _knbc_fileids_sort(x):
        cells = x.split('-')
        return (cells[0], int(cells[1]), int(cells[2]), int(cells[3]))

    knbc = LazyCorpusLoader('knbc/corpus1', KNBCorpusReader,
                            sorted(fileids, key=_knbc_fileids_sort), encoding='euc-jp')
    print knbc.fileids()
    -> ['KN001_Keitai_1/KN001_Keitai_1-1-1-01',
    'KN001_Keitai_1/KN001_Keitai_1-1-2-01',
    'KN001_Keitai_1/KN001_Keitai_1-1-3-01',
    'KN001_Keitai_1/KN001_Keitai_1-1-4-01',
    'KN001_Keitai_1/KN001_Keitai_1-1-5-01', ...


Now you're ready to use the corpus. You can iterate over words by words() method:

これで、コーパスを使う準備は整いました。全ての単語について繰り返すには words() メソッドを使います:

    print ''.join(knbc.words()[:100])
    -> ［携帯電話］プリペイドカード携帯布教。もはや’今さら’だが、という接頭句で
	始めるしかないほど今さらだが、私はプリペイド携帯をずっと使っている。犯罪に用い
	られるなどによりかなり...

You can also access dependency trees by parsed_sents() method:

係り受け関係を表現した表現の木構造にアクセスするには、parsed_sents() を使います。

    print '\n\n'.join('%s' % tree for tree in knbc.parsed_sents())
    -> (布教/。
         (電話/］ ［/携帯)
         (携帯 (カード プリペイド)))

       (使って/いる/。
         (今さら/だ/が/、
           (ほど
             (始める/しか/ない
               もはや
               (接頭句/で (いう ’/今さら/’/だ/が/、/と)))))
        私/は
        (携帯/を プリペイド)
        ずっと)

he tree representation can be customized by the morphs2str parameter of the KNBCorpusReader constructor, or you can directly access morphs2str variable:

なお、木構造のノード表現の文字列は、 KNBCorpusReader のコンストラクタの morphs2str パラメータ、もしくは morphs2str メンバに直接アクセスすることによってカスタマイズできます。


    knbc.morphs2str = lambda morphs: '/'.join("%s(%s)" % (m[0], m[1][2])
        for m in morphs if m[0] != 'EOS').encode('utf-8')

    print '\n\n'.join('%s' % tree for tree in knbc.parsed_sents())
    -> (布教(名詞)/。(特殊)
           (電話(名詞)/］(特殊) ［(特殊)/携帯(名詞))
           (携帯(名詞) (カード(名詞) プリペイド(名詞))))

        (使って(動詞)/いる(接尾辞)/。(特殊)

          (今さら(副詞)/だ(判定詞)/が(助詞)/、(特殊)
            (ほど(名詞)
              (始める(動詞)/しか(助詞)/ない(形容詞)
                もはや(副詞)
                (接頭句(名詞)/で(助詞)
                  (いう(動詞)

                    ’(特殊)/今さら(副詞)/’(特殊)/だ(判定詞)/が(助詞)/、(特殊)/と(助詞))))))
          私(名詞)/は(助詞)
          (携帯(名詞)/を(助詞) プリペイド(名詞))
          ずっと(副詞))

### TO DO - 今後の予定

Currently the KNB corpus reader doesn't support other information except for morphology and dependency, such as case and anaphora.

KNB コーパスリーダーは、現段階では、形態素情報と係り受け以外の情報、例えば格や照応の情報はサポートしていません。


### Acknowledgement - 謝辞

I thank Mr. Steven Bird and other developers of NLTK. I also thank Prof. Sadao Kurohashi for allowing the redistribution of KNB Corpus for NLTK.

Steven Bird さんをはじめ NLTK の開発者の皆さまに感謝します。また、NLTK 用に KNB コーパスの再配布を許可して下さった黒橋禎夫教授に特に感謝いたします。*


## 2. JEITA Public Morphologically Tagged Corpus (in ChaSen format) - JEITA 形態素解析済み コーパス (ChaSen 形式)

### About this corpus - 本コーパスについて

This corpus, JEITA Public Morphologically Tagged Corpus (in ChaSen format), is a public, automatically tagged (morphologically analyzed) corpus of [Project Sugita Genpaku](http://www.genpaku.org/) and [Aozora Bunko](http://www.aozora.gr.jp/), which themselves are freely available text collections like Project Gutenberg. The corpus data was originally distributed as "JEITA Public Morphologically Tagged Corpus".

本コーパス 「JEITA 形態素解析済みコーパス (ChaSen 形式)」は、[プロジェクト杉田玄白](http://www.genpaku.org/) と[青空文庫](http://www.aozora.gr.jp/) のテキストを自動で形態素解析した、フリーで利用可能なタグ付きコーパスです。本コーパスは、本来、「JEITA 形態素解析済みコーパス」として配布されていたデータに基づいています。

However, the files included in this corpus are not the original distribution data of JEITA Public Morphologically Tagged Corpus but the ones which are converted into ChaSen's file formats for easier program access. For more information on the ChaSen morphological analyzer, you can refer to [ChaSen's official site](http://chasen-legacy.sourceforge.jp/).

ただし、本コーパスに含まれているファイルは上記JEITA 形態素解析済みコーパスの配布データそのものではなく、プログラムからのアクセスを容易にするために ChaSen のファイル形式に変換してあります。ChaSen の詳細については[ChaSen のオフィシャルサイト](http://chasen-legacy.sourceforge.jp/)を参考にしてください。

### Access by NLTK (Natural Language Toolkit) Corpus Reader - NLTK のコーパスリーダーを使って読み込む

Since this corpus is in ChaSen's format, it can be easily accessed via ChaSen corpus reader for NLTK distributed here.

本コーパスは ChaSen 形式であるため、ここで配布しているNLTK のための ChaSen コーパスリーダーを用いると簡単にアクセスできます。

Firstly, download this corpus's distributed files, and decompress it under any directory (NLTK's data directly nltk_data is preferable)

まず、以下の配布ファイルをダウンロードし、任意のディレクトリ (NLTK のデータディレクトリ nltk_data が標準)に解凍します。


- JEITA Public Morphologically Tagged Corpus (in ChaSen format) for Project Sugita Genpaku<br/>
JEITA 形態素解析済みコーパス (ChaSen形式) プロジェクト杉田玄白<br/>
(Morphologically Tagged by ChaSen + IPADic)<br/>
(ChaSen と IPADic により形態素解析)<br/>
[jeita_genpaku.tar.bz2, 3.86 MB](/files/jeita_genpaku.tar.bz2)

- JEITA Public Morphologically Tagged Corpus (in ChaSen format) for Aozora Bunko <br />
JEITA 形態素解析済みコーパス (ChaSen形式) 青空文庫 <br />
(Morphologically Tagged by ChaSen + IPADic) <br />
(ChaSen と IPADic により形態素解析) <br />
[jeita_aozora.tar.bz2, 53.6 MB](/files/jeita_aozora.tar.bz2)


Next, the ChaSen corpus reader source file from here: [chasen.py](https://github.com/mhagiwara/nltk/blob/master/jpbook/chasen.py). ChaSen corpus reader is distributed under the same license as NLTK itself ([Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)).


次に, ChaSen コーパスリーダーのソースコードを [chasen.py](https://github.com/mhagiwara/nltk/blob/master/jpbook/chasen.py) からダウンロードしてください。このコーパスリーダーは、NLTK と同じライセンス ([Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)) の元で再配布可能です。


Now you can specify the path to the corpus and filename(s) to read to construct a ChasenCorpusReader object. Multiple filenames can be specified as a list in the second parameter of the constructor.

ここで、コーパスへのパスと、読み込むファイル名を指定して、ChasenCorpusReader のオブジェクトのコンストラクタを呼び出します。第２引数のファイル名の部分には、複数のファイル名をリストとして指定することができます。


    >>> from chasen_reader import *
    >>> genpaku = ChasenCorpusReader('/path/to/corpus/jeita_genpaku',
                                     '0014.chasen', encoding='utf-8')

The interface of ChaSen corpus reader is the same as the standard TaggedCorpusReader, which has raw() (returns raw strings), words() (list of words), sents() (list of sentences), paras() (list of paragraphs), tagged_words() (list of tagged words), tagged_sents() (list of tagged sentences), tagged_paras() (list of tagged paragraphs).

ChaSen コーパスリーダーのインターフェースは、標準の TaggedCorpusReader と同じで、raw() (生の文字列を返す), words() (単語のリスト), sents() (文のリスト), paras() (パラグラフのリスト), tagged_words() (タグ付き単語のリスト), tagged_sents() (タグ付き文のリスト), tagged_paras() (タグ付きパラグラフのリスト) の各メソッドをサポートしています。


    >>> print '/'.join( genpaku.words()[0:40] )
    I/./　/心地よい/ランプ/の/明かり/に/照らさ/れ/た/書斎/を/行き/つ/戻り/つ/し/て
    /い/た/ヒューバート/・/グラニス/は/、/足/を/止め/て/、/暖炉/の/上/の/置き時計
    /と/腕時計/を/くらべ

Note that the tags (the second element of tuples returned by tagged_xxx methods) are themselves tuples, whose elements are readings, lemmas, pos1, pos2, and Katsuyou form.
なお、タグ情報 (tagged_xxx メソッドで返されるタプルの第２要素) はそれ自体がタプルになっていて、読み, 原形, 品詞1, 品詞2, 活用形の情報が含まれます。


    >>> print '\nEOS\n'.join(['\n'.join("%s/%s" % (w[0],w[1][2]) for w in sent)
                              for sent in genpaku.tagged_sents()[0:2]])
    I/記号-アルファベット
    ./記号-句点

    EOS
    　/記号-空白
    心地よい/形容詞-自立
    ランプ/名詞-一般
    の/助詞-連体化
    明かり/名詞-一般

    に/助詞-格助詞-一般
    照らさ/動詞-自立
    れ/動詞-接尾
    た/助動詞
    ...

By default, the sentence segmentation is done only by the "EOS" information given by ChaSen. Additional sentence segmentation function can be specified by the sent_splitter parameter of ChaSen Corpus reader.

デフォルトでは、文分割は、ChaSen によって出力された "EOS" の情報のみを用いていますが、ChaSen コーパスリーダーのコンストラクタの sent_splitter によって、追加で文分割関数を指定することもできます。

    >>> genpaku = ChasenCorpusReader('/path/to/jeita/corpus',
                                       '0014.chasen', encoding='utf-8',
                                       sent_splitter=lambda w:w[0]==u'。')
    >>> print '\n'.join([''.join(w for w in sent) for sent in sugita.sents()[2:4]])
    八時三分前。
    もう三分もすれば、著名な法律事務所アスカム・アンド・ペティローのピーター・
    カム弁護士が、時間きっかりにアパートの呼び鈴を押すことだろう。


### Acknowledgement - 謝辞

I thank the members of JEITA 言語資源分科会, especially the leader Prof. Hitoshi Isahara for allowing the conversion and redistributon of their Morphologically Tagged Corpus. I also thank the members of Project Sugita Genpaku and Aozora bunko, and the developers of ChaSen morphological analyzer.

本コーパスの元となった JEITA 形態素解析済みコーパスの変換および再配布の許可をいただいたJEITA 言語資源分科会の皆さま、特に委員長の井佐原均教授に感謝いたします。また、プロジェクト杉田玄白・青空文庫の公開、そして ChaSen の開発に携わる皆さまに感謝いたします。

