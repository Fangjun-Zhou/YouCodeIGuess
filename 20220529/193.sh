# Read from the file file.txt and output all valid phone numbers to stdout.
find_phone_number() {
    input="file.txt"
    while read -r line; 
    do 
    echo "$line"
    done <"$input"
}

find_phone_number

grep -E "(?[0-9]{3})?[-]?\s?[0-9]{3}[-]?\s?[0-9]{4}" file.txt