# zim

Here are projects relating to working with the OpenZIM file format.

## zimwriterfs

*zimwriterfs* is a project using libzim that makes a zim file from html
content in a folder.

How I installed zimwriterfs on Linux Mint:

    sudo apt-get install libzim-dev
    mkdir /path/to/zimwriterfs_tmp
    cd /path/to/zimwriterfs_tmp
    git clone https://github.com/wikimedia/openzim
    cd openzim/zimwriterfs

    # as per https://github.com/wikimedia/openzim/tree/master/zimwriterfs
    sudo apt-get install liblzma-dev libmagic-dev zlib1g-dev libgumbo-dev 
    cd ../zimlib && ./autogen.sh && ./configure && make && cd ../zimwriterfs
    # ...
    ./autogen.sh
    ./configure CXXFLAGS=-I../zimlib/include LDFLAGS=-L../zimlib/src/.libs
    make
