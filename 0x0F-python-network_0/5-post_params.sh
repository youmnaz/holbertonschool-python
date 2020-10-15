#!/bin/bash
# Send POST request and display body
curl -s -X POST -L "$1" -d 'email=hr@holbertonschool.com&subject=I will always be here for PLD'
