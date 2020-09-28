file=~/regex

while read -r line; do
	echo "$line|"
done < $file
