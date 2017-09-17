#!/bin/sh

if grep "Delilah" sample_file.txt > /dev/null
then
	echo "It's there"
else
	echo "No!"
fi
