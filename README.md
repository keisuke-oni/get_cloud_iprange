# cloud_iprange

各種クラウドサービスが利用しているIPアドレスレンジをCSVで収集するスクリプトです。

ネットワーク解析などでの利用を想定しています。

## 対応クラウドサービス
- Amazon Web Service
- Microsoft Azure
- Google Cloud Platform

## スクリプトの説明
### awsiprange_json2text.py
AWSのサイトからIPアドレスを収集してきます。
### azureiprange_xml2text.py
AzureのサイトからIPアドレスを収集してきます。<br />
最新版の日付を自動収集する機能はないので、確認して修正してください。
### find_gcp_iprange.py (https://github.com/keisuke-oni/find_gcp_iprange)
GCPのドメインからDNSを再帰的に引いてIPアドレスを収集してきます。
### cloud_ipranges_marge.py
すべてのクラウドサービスのIPを1つのCSVファイルにまとめます。

## 使い方
順番は問わないので、aws, azure, gcpの3つのスクリプトを実行して各クラウドサービスのIPアドレスを収集します。

- aws_ipranges.csv
- azure_ipranges.csv
- gcp_ipranges.csv

上記3つのCSVが作成されます。

3つのCSVが作成されているのが確認できたら、同じフォルダー内でcloud_ipranges_marge.pyを実行します。

- cloud_ipranges.csv

上記CSVが生成されてるのが確認できたら完了です。

## データ構造
### aws_ipranges.csv, azure_ipranges.csv, gcp_ipranges.csv
IPレンジ
### cloud_ipranges.csv
IPレンジ,クラウドベンダー名
