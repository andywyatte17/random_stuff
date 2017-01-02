#!/bin/bash

mkdir openenglishbible
cd openenglishbible
for x in index b{001..069}
do 
  # echo $x
  wget --page-requisites http://openenglishbible.org/oeb/2016.1/read/$x.html
done
cd ..

