# 徵音梅林Web
徵音梅林 Website on Github.io [https://projectmeilin.github.io/](https://projectmeilin.github.io/)

![](http://projectmeilin.github.io/theme/img/markdown/top.png)

## 開發環境 (environment)
- python2.7 or python3
- virtualenv
- pelican

## 設定開發環境 (setup environment)
- Mac
```bash
git checkout source
brew update
brew upgrade
brew install python
pip install virtualenv
virtualenv ENV
source bin/activate
pip install -r requirements.txt
```

- Debian / Ubuntu
```bash
git checkout source
apt-get update
apt-get upgrade
sudo apt-get install python-pip python-dev build-essential
sudo pip install --upgrade pip
sudo pip install --upgrade virtualenv
virtualenv ENV
source bin/activate
pip install -r requirements.txt
```

## 如何開發 (how to development)
- 新增/修改 `contents/zh/*.md`
- metadata格式 必須填入`Lang`, `Category`, `Slug`. 會產生對應頁面 如`/$LANG/$Category/$Slug.html`

## 測試 (testing)
- build all pages
```
./build.sh
```
- Test in local. [http://localhost:8000](http://localhost:8000)
```
make serve PORT=8000
```

## Deploy new pages into gh-pages
```bash
git checkout gh-pages
git fetch --all
git checkout origin/source -- output
cp -pr output/* ./ && rm -rf output
git add . && git commit -m "update new files to gh-pages"

git checkout master
git merge gh-pages
git push --all
```

## Contributors
- [kilfu0701](https://github.com/kilfu0701) (kilfu0701@gmail.com)
- [MGdesigner](https://github.com/MGdesigner)
- [atsushieno](https://github.com/atsushieno)
- [Yuan CHAO](https://github.com/yuanchao)

## License
MIT
