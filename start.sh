#!/bin/bash

cd ~/dotfiles/
chmod +x sync_git/scripts/fetch_class.py
./sync_git/scripts/fetch_class.py
./sync_git/scripts/get_gits.sh