#!/bin/sh
# file-poke - tell us stuff about files

files=`ls`
for i in $files
do
	echo -n "$i"
	grep $i $i
done
