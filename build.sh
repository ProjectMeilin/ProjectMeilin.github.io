#!/bin/bash
source ENV/bin/activate

rm -rf output

all_lang=( "en" "ja" "zh" )
for i in "${all_lang[@]}"
do
    #sed -i "s/DEFAULT_LANG = u'[a-zA-Z]\{2\}'/DEFAULT_LANG = '$i'/g" pelicanconf.py
    echo "build ${i} ...."
    cp -pr pelicanconf_${i}.py pelicanconf.py
    mkdir -p output/${i} && pelican content/${i} -o output/${i} -s pelicanconf.py
    rm -rf /var/www/html/linne_pelican/${i}
    cp -pr output/${i} /var/www/html/linne_pelican/${i}
done

cp index.html output/index.html
cp -pr output/ja/theme output/theme
