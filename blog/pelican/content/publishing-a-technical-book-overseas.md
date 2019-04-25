Title: 海外で技術書をゼロから執筆・出版する方法
Date: 2018-10-24 00:00
Category: Natural Language Processing
slug: publishing-a-technical-book-overseas

本記事は、私が海外（アメリカ）で技術書 「実世界自然言語処理」"Real-World Natural Language Processing" (Manning Publications) をゼロから執筆、出版するまでを綴った日記です。本記事の執筆時点 (2018年12月) において、まだ書籍は未発表・執筆中ですので、進展がある毎に更新していく予定です。

なお、本書の入手・購入について、色々な方から問い合わせを受けるので。Manning Publication では、MEAP (Manning Early Access Program) といって、執筆中の書籍を未完成の段階で購入し、章が完成するごとに読みすすめられるという制度があります。本書も、最初の数章が完成した段階で MEAP で入手可能になります。現在のところ、2019年3月ごろを予定しています。

## まずはじめに - 技術書を執筆・出版したい人へ

私はこれまで、オライリー・ジャパンから２冊翻訳書を、翔泳社から１冊、共著で書いた本を出版した経験があります。技術書を出版するプロセスは、分野や出版社、著者によって大きく異なりますが、技術書の執筆に興味がある人には、以下のことをぜひ覚えておいて欲しいと思います。

- 技術書を執筆するのは非常に大変な作業です。週40時間フルタイムで作業しても、1年ほど時間がかかるのを覚悟しましょう。
- 金利的な報酬を目標にして技術書を執筆するのはやめましょう。書籍の売れ行きにもよりますが、ほとんどの技術書は数千部ほどしか売れず、その微々たる印税を時間単位に換算すると、おそらく最低賃金にも満たないのではないでしょうか。お金が必要であれば、コンビニでバイトでもしたほうがマシです。
- その代わり、金銭的な報酬の代わりの目標を立てましょう。人それぞれの目標があると思いますが、個人的には、本の執筆は、自分の専門家としての権威の確立と社会への還元、そして、本の執筆を通じて得られる学習効果が非常に大きいと思います。
- 出版社は通常、過去に本を出版した経験のある、信頼できる著者と仕事をしたがるものです。では、書籍をこれまでに出版したことの無い人は、どうやって取っ掛かりを見つければよいでしょうか。出版社にいきなり提案書を送っても、相手にしてもらえるでしょうか？これは一見、鶏と卵の問題に見えますが、方法はいくつかあります。１つ目は、ブログや自費出版などを通じて、実績を作ってしまう方法です。２つ目は、既に著書がいくつかある著者に仕事を紹介してもらうという方法です。著書が既にある人は、出版社や他の著者とのコネがあるので、人を紹介してくれたり、運が良ければ共著に加えてもらえるかもしれません。自分は、この２つ目の方法でまず翻訳書をいくつか出版して経験を積みました。
- 出版社は、常に良い本のネタを探しています。もし自分が得意な専門分野があり、本を書き上げる自信があれば、編集者に提案書を送ってみるのも手かもしれません（自分はやったことはないですが）。
- 技術書を出版するために、業界トップのエンジニアや研究者である必要は必ずしもありません。「専門家として業績を出す能力」と「大衆に受ける分かりやすい技術書を書き上げる能力」は、あまり相関が無い気がします。
- 共著で書籍を執筆する場合、共著者は慎重に選びましょう。これは、一緒に仕事をするチームメンバーを採用するのと同じです。可能であれば、過去に一緒に仕事をしたことがあり、信頼できる人を共著者に選びましょう。

以下、本を執筆するに至るまでのいきさつを時系列に書いていきます。

## 編集者からのメール

2018年8月中旬ごろ、Manning Publications の 獲得編集者 (適訳かどうか分からないが、 Acquisition Editor のこと) から1通のメールが届く。自然言語処理と深層学習について話を聞きたいというのだ。「話を聞きたい」というのはかなり漠然としているが、聞いてみるとどうやら本の著者を探しているらしい。面白そうなので１週間後に Skype で話す約束をする。

## 獲得編集者との Skype ミーティング  

次の週の月曜、獲得編集者と Skype で話す。前の日に中国旅行から帰ってきたばかりで、疲労と時差ボケでしんどかったのを思い出す。最初は天気や今居る場所 (彼は Boston で在宅で働いているようだ。時差が無いので楽だ、等) などの他愛もない話をする。自分の経歴や、今の業務内容などを簡単に話した後、すぐに書籍の執筆の話になる。簡単に言うと「書籍を執筆することに興味はないか」ということだった。なんとなく興味はあるということ、もし本を出版するとすれば、最新のトピックを取り入れた深層自然言語処理の本が良いのでは、などとなんとなくアドバイスする。自分は業務で深層自然言語処理のプロダクション・システムを実装したりしているが、いわゆる MLOps と呼ばれているような、機械学習の設計・実装・運用に関する情報を取り扱った本が無いことや、強化学習や GAN など、割と最近のトピックも書いたら面白いのでは、と話をすると、彼の興味とも一致したらしく、けっこう意気投合する。

その後、よく考えてみて、もし書籍の執筆に興味があるようであれば、次のステップ、すなわち、提案書の準備、に進んでみないか、という話になる。参考用に、Manning Publications で準備中の、関連するいくつかの技術書 ([Natural Language Processing in Action](https://www.manning.com/books/natural-language-processing-in-action), [Deep Reinforcement Learning in Action](https://www.manning.com/books/deep-reinforcement-learning-in-action), [GANs in Action](https://www.manning.com/books/gans-in-action)) の電子版を無料で読めるようにしてもらう。

## 提案書の作成

提案書の作成には、合計で２週間ほどかかった。Manning Publications の提案書のテンプレートはかなりボリュームがあり、

- なぜ自分がその本を書くに値する人間なのか
- その本を理解できる最低限のスキルを持った読者はどんな人か (これを Minimally Qualified Reader, MQR と呼んでいる)
- その本を読むことで、どういったタスクが達成できるようになるのか
- その本と類似した本はすでに市場に存在するか。もしそうなら、相違点は何か。
- 目次全体（章と節全て）

など全て書かなければいけない。(もし具体的なプロセスに興味があれば、[write for us](https://www.manning.com/write-for-us/) のページを見てみると良い。)

アメリカのスタートアップで叩き込まれた仕事の哲学に、成果物は未完成でも良いからとにかく早く関係者にシェアし、そこからフィードバックを得ながらすばやく改善していく、というものがある。ここでもその方法を最大限活用し、まだ荒削りの段階で上記の編集者のフィードバックを仰ぎながら改善していった。それが功を奏したのか、提案書の作成はスムーズに行ったと思う。

これと並行して、勤務先である Duolingo との交渉も始まった。まずは自分の上長に、続いて、その上の経営層に、「こういった本を、このぐらいの時間を使って書きたい。業務時間も少し使いたい」という旨の提案書を書く（まだ規模が小さいので、2層しかない）。スタートアップ（というか弊社）ならではのスピード感で、２日ぐらいで OK が出た。日本の大企業なら、きっと一人のハンコをもらうのに１週間ぐらいかかっていたと思う。

また、これもアメリカ企業では割と一般的だが、雇用形態が「社員が雇用期間中に作成した知財はすべて雇用主に属する」という形になっている。本を出版する場合それだと困るので、人事と話し、例外的に、執筆する本をこの対象から外してもらうよう、追加の契約書を作成してもらう。

## 提案書の承認

Manning Publication では、提案書はその後、数人の専門家からなる外部査読者に送られ、フィードバックが集められる。自分の場合は、８人ほどの NLP 研究者や開発者などに提案書が送られ、「想定読者や市場は本当に存在するか」「この内容の本があれば読んでみたいか」「この著者は本を完成するために必要な専門性があるか」などのフィードバックを集める。査読者のほとんどは自分の知らない人だったが、ほとんどの人が「この市場はこれから拡大する」「読んでみたい」と肯定的に思ってくれていたようだ。これらのフィードバックは、獲得編集者、および、Manning Publications の編集長（提案書の承認を権限を持つ）に全て転送される。

全てのフィードバックが集まって程なくして、提案書が承認されたとの知らせを受ける。

## 執筆契約書へのサイン

その後、獲得編集者との２回めのミーティング (Skype) をする。フィードバックが肯定的で、提案書が承認されて良かった点、これからのステップなどを話す。特に、書籍の執筆を始めるにあたってもっとも重要な、執筆契約書の内容について大まかな説明がある。書籍の内容と量、執筆のスケジュールや、印税の支払い、もし執筆できなかった場合の対応などが主な条項だ。印税の項目についてはここにどこまで書いていいか分からないが、今回の本は割と人気が出そうなので、印税のパーセンテージが売上部数にしたがって階段状に上がっていく契約にできるだろう、ということだった。書籍の３分の１が完成するたびにマイルストーンがあり、そのたびにある一定の金額が印税の頭金（cash advance）として著者に支払われる。

Skype ミーティングの後すぐに、執筆契約書が電子的に送られてくる。アメリカに来てから、こういった法務関係にかなり敏感になったと思う。契約に不利な内容が無いかどうか、一字一句、完全に理解できるまで10回ぐらい通して読んだ。また、契約書にサインする前に、技術書を出版するという同様の経験について書かれたブログ記事（[この記事](http://www.aristeia.com/authorAdvice.html)や[この記事](http://www.voidspace.org.uk/python/articles/technical-writing.shtml)が大変参考になった）を読みまくる。編集者といくつか質問などでやりとりした後、執筆契約書へサインする。

## キックオフ・ミーティング

執筆契約書にサインしてから２週間ほど経ったころ、獲得編集者、編集長、編集補佐 (Development Editor)、自分、の４人で、キックオフ・ミーティングをする。これは、Manning Publications の編集長 (Marjan Bace) と初めて話す機会になる。高圧的な人だったらどうしようかと少し緊張したが、とても物腰の柔らかそうな人で、今の仕事の内容や Duolingo など、本にあまり関係の無い雑談をけっこうしたりしてスムーズに進んだ。また、編集補佐（＝自分がこれから主にコンタクトを取る編集者）の紹介や、Manning の教え方の哲学などのオリエンテーション的な説明も受ける。Manning の編集者たちは基本的に在宅で仕事をしているようで、Skype で４者同時通話だったが、全員が米国東部時間なのでスケジューリング等はかなり楽だった。

この頃、同時進行して、本のウェブサイトとブログ ([www.realworldnlpbook.com](http://www.realworldnlpbook.com/)) を立ち上げる。書籍のウェブサイトを作ったり、ブログで本の内容をシェアするのも出版社としても推奨しているようで、これからもそちらで同時並行してブログ記事を書いていこうと思っている。

## 編集補佐との最初のミーティング

Manning Publication では、各書籍には編集補佐が割り当てられ、キックオフ・ミーティングの後は、著者は基本的にこの編集補佐を通じて出版社側とコミュニケーションする。キックオフ・ミーティングの数日後、この編集補佐と１：１でミーティングする。彼女はインディアナに住んでいるようで、地元の話をするなどして和んだ後、これからの予定等について一通りオリエンテーションを受ける。

このミーティングの約１ヶ月後に、Editorial Board Meeting (編集役員会) なるミーティングが開かれ、そこで本の構成、目次、想定読者層、第１章のドラフトなどがレビューされるので、それまでにこれらのドキュメントを完成させなければならない。

目次は、提案書に書いたものをベースとし、外部査読者のフィードバックなどを取り入れ、かつ各サブセクションに「重み」を割り振らなければならない。重みは、簡単なトピックから難しいトピックまで、１から１０の値で割り振る。それぞれの数字について、そのトピックを説明するために必要になるであろうページ数の目安が決まっている。８や９を割り振るような難しいトピックは、多くのページが必要になるので、それ自体、セクションではなく独立の章として書くことを推奨している。また、想定読者層 (MQR; Minimally Qualified Reader) については前述の通り提案書にも書いたが、ここで改めて独立のドキュメントとしてまとめ直す必要がある。

## 第１章の執筆と、編集役員会

その後、第1章の執筆が始まった。Thanksgiving の休暇を挟んだのでスケジュールが少し遅くなったが、編集委員会が開催されるまで約１ヶ月で完成させなければならない。

Manning Publication では、Microsoft Word, Asciidoc, Google Docなど、様々な方法で原稿を執筆できる。編集者を含め一番皆が慣れているという理由でおすすめの Word を選択した。Word なんて何年も使ったことが無かったが、最近の Microsoft の動きには個人的に色々と好感が持てるので、応援も兼ねて Office に課金して使っている。

執筆において一つ問題になるのが、イラスト・図表をどうするかだ。Manning Publication では、イラスト・図表のファイルの最終版まで自分で用意しなければならないという問題があって、これについては前に [Manning Publication で本を出版した著者のブログ](http://www.voidspace.org.uk/python/articles/technical-writing.shtml) で知っていたので、早めに対策を考えていた。もちろん、自分で全部描いてもいいのだが、量が大量になるので、外注することにした。具体的には、[fiverr](https://www.fiverr.com/) という $5 で色々なタスクを外注できるサイトで、質の高いイラストを作っているイラストレーターの人を探して、ノートに書いた自分の殴り書きからキレイな Illustrator 製のイラストに起こしてもらうという手だ。

例えば、ブログ記事でも使ったこの Elmo の図も、そうして作ってもらった。

<img src="http://www.realworldnlpbook.com/blog/images/elmo.png" />

自分で描いたらたぶん1時間ぐらいかかりそうなのを、10分で描いた殴り書きから $5 でイラストに起こしてもらえるので大変満足している。（そういえば、もしイラストが得意で、こういった仕事を受けたい方が居れば<a href="mailto:hagisan@gmail.com">私までご連絡ください</a>。おそらく全部で150枚を超えるイラストを発注することになるので、けっこうな額になると思います。）

約１か月後に、編集役員会が開かれる。ここでは、主に編集ディレクター (Editorial Director) から目次、想定読者層、第1章のドラフトについてコメントをもらうのが主な目的だ。彼はシアトルの郊外に住んでいて、エンジニアとして働いた経験があり自身も著者として技術書を出版した経験がある。想定読者層へのコメント（例えば、数学や機械学習の前提知識を仮定すると対象読者層が大幅に減るので、そこは完全な初心者を対象にした方がいいのではないか）や、章ごとにどこまで踏み込んで解説するか（[Bloom's Taxonomy](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/) というものをプログラミングに応用したフレームワークを教えてもらった）などについて、詳細にフィードバックをもらう。

目からウロコだったのが、「２つ以上の難しい概念を一度に教えようとしない」という原則。これ、一見当たり前のように見えるが、巷にあふれているプログラミングの参考書などを見てみると、この原則が破られている例がたくさんあることが分かる。最初に基礎的な概念をいくつか順に説明した後に、具体的になにかを作ってみるという構成のものが多いが、この具体例のところに突然難しい概念がいくつか出てきて、読者が面食らってしまう、というものだ。読者の立場になって書籍を書くことがいかに重要で、いかに難しいかを考えさせられる。

編集委員会の翌日、自分の編集補佐と個別に１：１でミーティングし、第１章の詳細なフィードバックをもらう。全体的に割と良く書けているということでほっと胸をなでおろす。章の内部構成について色々とアドバイスをもらうので、それに沿う形で２週間を目処に修正する予定。

以下、進捗があるたびに追記していきます。