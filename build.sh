echo '<!-- Content begin -->' > .tmp
pygmentize -v -f formatter.py -x content.py >> .tmp
echo '<!-- Content end -->' >> .tmp
sed -e '/<!-- Content begin -->/{:a; N; /\n<!-- Content end -->$/!ba; r .tmp' -e 'd;}' index.html > .tmp2
cat .tmp2 > index.html
rm .tmp .tmp2
