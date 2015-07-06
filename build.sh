#!/bin/bash
source ENV/bin/activate

all_lang=( "en" "ja" "zh" )
for i in "${all_lang[@]}"
do
    #sed -i "s/DEFAULT_LANG = u'[a-zA-Z]\{2\}'/DEFAULT_LANG = '$i'/g" pelicanconf.py
    echo "build ${i} ...."
    cp -pr pelicanconf_${i}.py pelicanconf.py
    #make html
    pelican content/${i} -o output -s pelicanconf.py
    rm -rf /var/www/html/linne_pelican/${i}
    cp -pr output /var/www/html/linne_pelican/${i}
    rm -rf output
done
