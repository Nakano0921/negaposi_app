### AIを活用したクチコミ分析
- [サービスURL](https://flask-scraping-app.herokuapp.com/)
- 特徴
  - webスクレイピングで某高級ホテルのクチコミサイトのデータを取得しそのクチコミデータを基にAIでネガティブポジティブの数値分析を行った。
- 構成技術
  - python3.9.0
  - selenium
  - oseti
  - Flask
  - pandas
  - numpy
  - jupyter notebook
  - Streamlit
- 開発期間：１ヶ月半
- 開発プロセス
  - 基礎的なpythonの学習とよく使うCUIの学習
  - selenium入門でseleniumの学習
  - 仮想環境（virtualenv）の反映
  - スクレイピングの結果をCSVに出力
  - requirements.txtでライブラリの管理
  - PRを初めて行う
  - 設定用ファイルを作成し、メインファイルから読み込み
  - git管理したくないファイルをgitignoreに入れる
  - blackの反映
  - Flaskの反映
  - Materializeの導入 
  - Herokuでスクレイピングを行えるにする
  - topページのクライアント側の調整
- 今後取り組もうと思っている事
  - フレームワークをStreamlitを使用し、総合評価を出し各項目との相関を出し、店舗の強みと弱みなどの分析
  - 店舗検索機能をつける
  - Herokuでのcsvファイルの保存
- 今後の課題
  - データサイエンティスト又は機械学習エンジニアを目指している為AWSの学習の優先度が低くなった