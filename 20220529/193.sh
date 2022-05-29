#!/bin/bash  

# Read from the file file.txt and output all valid phone numbers to stdout.
find_phone_number() {
    value=$(<file.txt)  
echo "$value"  
}

find_phone_number

grep -E "(?[0-9]{3})?[-]?\s?[0-9]{3}[-]?\s?[0-9]{4}" file.txt