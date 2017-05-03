#!/bin/bash
source ENV/bin/activate

rm -rf output
mkdir output

all_lang=( "en" "ja" "zh" )
for i in "${all_lang[@]}"
do
    echo "build ${i} ...."
    pelican content/${i} -o output_${i} -s pelicanconf_${i}.py
    mv output_${i} output/${i}
done

cp index.html output/index.html
cp -pr output/ja/theme output/theme
cp -pr output/ja/theme/img/favicon.ico output/
cp -pr theme/pelican-cait-custom/static/img/markdown/* output/
cp README.md output/README.md
rm -rf *.pyc
