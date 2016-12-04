#!/usr/bin/env bash

wget --mirror http://www.regles-donjons-dragons.com \
    --no-host-directories \
    --directory-prefix=dnd.docset/Contents/Resources/Documents

./create_index.py
