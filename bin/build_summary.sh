#!/bin/bash

cd ..
echo "# Summary" > SUMMARY_AUTO.md
ls src/*.md | while read i; do

	grep  "^\#" "$i"
	grep  "^\#" "$i" | while read j; do
		TITLE=$(echo $j | sed -e "s/#### /        * \[/g" | sed -e "s/### /    * \[/g" | sed -e "s/## /  * \[/g" | sed -e "s/# /* \[/" )
		echo "$TITLE]($i)" >> SUMMARY_AUTO.md
	done 
done
