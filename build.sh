#!/bin/bash
source ENV/bin/activate

rm -rf output
mkdir output

all_lang=( "en" "ja" "zh" )
for i in "${all_lang[@]}"
do
    #sed -i "s/DEFAULT_LANG = u'[a-zA-Z]\{2\}'/DEFAULT_LANG = '$i'/g" pelicanconf.py
    echo "build ${i} ...."
    cp -pr pelicanconf_${i}.py pelicanconf.py
    pelican content/${i} -o output_${i} -s pelicanconf.py
    mv output_${i} output/${i}
    #rm -rf /var/www/html/linne_pelican/${i}
    #cp -pr output/${i} /var/www/html/linne_pelican/${i}
done

cp index.html output/index.html
cp -pr output/ja/theme output/theme
