# 徵音梅林Web
徵音梅林 Website on Github.io [https://projectmeilin.github.io/](https://projectmeilin.github.io/)

![Alt text](top.png "Optional title")

## 開發環境 (environment)
- Docker 4.6.0 above
- Debian 11
- Pelican 4.7.2

## 設定開發環境 (setup environment)
1. Pull repo
```bash
git clone https://github.com/ProjectMeilin/ProjectMeilin.github.io.git
```

2. Build docker images and run
```bash
cd ProjectMeilin.github.io
docker-compose up -d --build
```

3. Enter development container
```bash
docker-compose exec project_meillin_wiki /bin/bash

## now you are in container
root@4f062e1e7cc3:/work/src#
```

4. setup python3 virtualenv and install packages
```bash
## run in container
virtualenv ENV
source ENV/bin/activate

## you will enter venv
(ENV) root@4f062e1e7cc3:/work/src#

## then install python3 needed packages
pip install -r requirements.txt
```

Congrats! Now you are ready for development!

## 如何開發 (how to development)
1. 新增/修改 `contents/zh/*.md` (有三種語言：zh, ja, en)

2. metadata格式 必須填入`Lang`, `Category`, `Slug`. 會產生對應頁面 如`/$LANG/$Category/$Slug.html`

3. Mardown檔案編輯完畢後，執行 `./build.sh` ，就會自動產生 `output` 資料夾

## 測試 (testing)
- build all pages
```
./build.sh
```
- Test in local. [http://localhost:8000](http://localhost:8000)
```
make serve-global
```

## Deploy new pages into gh-pages

如何把gh-pages branch的output推到github page上

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
