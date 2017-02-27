# http://stackoverflow.com/questions/9710118/convert-multipage-pdf-to-png-and-back-linux

# convert -density 150x150 southbank-2016-17-classical__season-brochure.pdf .tmp/i%03d.png

cd .tmp
for file in i*.png
do
  filename="${file%.*}"
  echo convert $file -crop 2x1@ split-$filename-%02d.png
done
cd ..

convert                    \
  -density 50              \
  -page a4                 \
   .tmp/split-i*.png       \
  -scale 595x842\!         \
  -gravity North           \
   multipage.pdf


