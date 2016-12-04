#!/usr/bin/env bash

URL=http://www.regles-donjons-dragons.com

wget --mirror $URL \
    --no-host-directories \
    --directory-prefix=dnd.docset/Contents/Resources/Documents

function download_tree_gif() {
    echo $1
    wget "$URL/Res/tree/$1" -O dnd.docset/Contents/Resources/Documents/Res/tree/$1
}

download_tree_gif base.gif
download_tree_gif folder.gif
download_tree_gif folderopen.gif
download_tree_gif page.gif
download_tree_gif pagesel.gif
download_tree_gif empty.gif
download_tree_gif plus.gif
download_tree_gif minus.gif
download_tree_gif empty.gif

./create_index.py
