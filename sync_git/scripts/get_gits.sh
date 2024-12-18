#!/bin/bash

cd ~/dotfiles/sync_git
csv_file="GIT.csv"
while IFS=, read -r column1 column2 column3
do  
    cd ~/CLASS
    mkdir -p $column1
    cd $column1
    git init > /dev/null 2>&1
    git remote add origin git@github.com:$column2 > /dev/null 2>&1 

    git pull origin "${column3%?}" > /dev/null 2>&1 
    git fetch

done < "$csv_file"