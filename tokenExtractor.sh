#/bin/bash

awk -F\' 'BEGIN{ORS="," } {print "\x27" $2 "\x27"}' < lexer.py