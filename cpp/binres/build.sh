#!/bin/sh

echo "1.py" && python binres-builder.py $1 > binres-$1.cpp
echo "1.ls" && ls -l -h binres-$1.cpp
echo "1.clang++" && time clang++ --std=c++11 binres-$1.cpp -o binres-$1
echo "1.binres" && echo "" && ./binres-$1 && echo ""

echo "2.py" && python binres-builder2.py $1 > binres2-$1.cpp
echo "2.ls" && ls -l -h binres2-$1.cpp
echo "2.clang++" && time clang++ --std=c++11 binres2-$1.cpp -o binres2-$1
echo "2.binres" && echo "" && ./binres2-$1 && echo ""
