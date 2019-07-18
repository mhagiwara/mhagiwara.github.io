Title: 拙著『実世界自然言語処理』の事前予約が可能になりました 
Date: 2019-07-09 00:00
Category: Research
slug: real-world-nlp-book-meap
Cover: images/rwnlp-meap.png

昨年の夏ほどから執筆を開始した拙著『実世界自然言語処理 (Real-World Natural Language Processing)』の事前予約が可能になった。

この事前予約、正確には MEAP (Manning Early Access Program) と言い、購入すると、執筆中の書籍の執筆が完了した章から順番に読めるようになり、最後に完成した書籍が手に入る、というもの。執筆中のため、誤りがあったり校正がまだ整っていなかったりする可能性もあるものの、完成した書籍を後から買うよりも安価に購入できるというメリットがある。興味のある方は、以下のリンクを参照して欲しい。

<figure style="text-align: center">
    <a href="https://www.manning.com/books/real-world-natural-language-processing">
	<img src="images/rwnlp-meap.png" style="width: 240px;"/>
	<figcaption>『実世界自然言語処理 (Real-World Natural Language Processing)』</figcaption>
    </a>
</figure>

本書籍は、昨年の夏ごろ、Manning の編集者から連絡があり、執筆を開始していたものだ。全編英語で、しかも単著で書籍をイチから執筆するということで、色々と大変なこともあったが、とりあえず一つのマイルストーンまで辿り着けたことでほっと胸をなでおろしている。執筆を開始したいきさつについては、以下の記事に詳しく書いたので、興味のある方はこちらもどうぞ。

[海外で技術書をゼロから執筆・出版する方法](http://masatohagiwara.net/blog/publishing-a-technical-book-overseas.html)

## 本書の特徴

本書は、他の自然言語処理や機械学習の教科書や入門書とは一味違ったものになっていると自負している。一般の教科書では、「ニューロンとは」「活性化関数とは」みたいな入門的な概念から始まり、「排他的論理和を計算するニューラルネットを作る」など簡単な例を経て、少しずつ難しいタスクを解いていく。言い換えると、教え方がボトムアップなのである。

ニューロンや活性化関数などの概念は、深層学習や（現代の）自然言語処理において非常に大切な概念なのは間違いない。しかし、この「ボトムアップ式」の問題は、「学習に途中で挫折した時に、何も有用なことが達成できなくて終わる」という点である。

一方、本書では、第１章で基礎的な概念を説明した後、第２章でいきなり「感情分析システムを作ってみよう」という例から入る。RNNや線形レイヤーなど、既存のコンポーネントを繋ぎ合わせることによって、個別の概念を完全に理解しなくても、上から下まで動くものをまず作り、必要に応じて概念を詳しく学んでいく、という「トップダウン式」を採用している。

この「トップダウン式」を採用したのは、２つの要因があった。一つは、特に海外で絶対的な人気を誇る [fast.ai の深層学習のコース](https://course.fast.ai/) が、このトップダウン式を採用しているということである。自分もコースを一通り見てみたが、フレームワーク等を駆使して Lesson 1 からいきなり動くものを作り、そこから必要に応じて概念を掘り下げていく Jeremy Howard の教え方には定評がある。もう一つの要因は、ここ数年で自然言語処理の分野で多大な人気を博している [AllenNLP](https://allennlp.org/) の登場である。AllenNLP を使うと、自然言語処理向けに抽象化されたモジュールを組み合わせることで、実に多様なタスクを簡単に解くことができる。本書では、ほぼ全ての章でこの AllenNLP をフル活用し、「まず動くものを作り、概念を必要に応じて解説する」というトップダウンな教え方を可能にしていた。

そのため、本書には数式がほぼ登場しない。数学やコンピュータ・サイエンスの知識が無くても、Python 等の知識のみで実際に動く自然言語処理システムを作れるようになる、というのが売りだ。

また、自分が機械学習エンジニアとして、実サービス向けの機械学習・自然言語処理システムに関わったこれまでの経験を活かし、教科書などではあまり触れられない、自然言語処理・機械学習の実サービスをいかに設計・開発・運用するかといった、エンジニアリング、MLOps 寄りの内容もカバーする予定である。

## 執筆

[前回の記事](http://masatohagiwara.net/blog/publishing-a-technical-book-overseas.html) を執筆してから、[勤めていたスタートアップを退職し、機械学習エンジニアとして独立](http://masatohagiwara.net/blog/leaving-startup-and-becoming-independent.html) し、米国の東海岸から西海岸まで引っ越しの準備をするなど、色々と私生活ではバタバタとしていたが、本書の執筆については、各章を執筆し、編集者にチェックしてもらう、という流れが確立しつつあり、順調に進んでいた。現時点で、第5章までは執筆がほぼ終わっているため、来年の春には書籍の全体が完成する予定である（ので、興味があれば安心して予約注文していただければと思う）。

本書で取り上げるタスクについては、全て[こちらの Github リポジトリ](https://github.com/mhagiwara/realworldnlp)からサンプルコードを参照でき、Google Colab で動かせるようにしてあるので、実際に動くコードに興味のある方はそちらを直接参照していただければと思う。