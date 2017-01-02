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

I had a problem with xapian library - my linux only had an old xapian.
I used a ppa to get a later xapian:

    sudo add-apt-repository ppa:xapian-backports/ppa
    sudo apt-get update
    sudo synaptic
    sudo apt-get install xapian-tools
    sudo apt-get install libxapian-dev
    xapian-config --version

Now I can install it:

    # as per https://github.com/wikimedia/openzim/tree/master/zimwriterfs
    sudo apt-get install liblzma-dev libmagic-dev zlib1g-dev libgumbo-dev 
    cd ../zimlib && ./autogen.sh && ./configure && make && cd ../zimwriterfs
    # ...
    ./autogen.sh
    ./configure CXXFLAGS=-I../zimlib/include LDFLAGS=-L../zimlib/src/.libs
    make

This made zimwriterfs which I've copied to this directory.

