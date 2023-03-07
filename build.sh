touch chapter-1.md
jupyter-book build . --builder linkcheck
jupyter-book build -W -n .

git_hash=`cat includes/git_hash.txt`
for f in ./_build/html/*.html; 
do 
	echo "Adding git hash to $f"
	f_base=`basename $f`
	sed -e "s/<\!--.*-->//g" $f > /tmp/$f_base.updated
	echo "<!-- $git_hash -->" >> /tmp/$f_base.updated
	cp /tmp/$f_base.updated $f
done

