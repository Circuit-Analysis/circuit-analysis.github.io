jupyter-book build -W -n .
ghp-import -n -p -f _build/html
git_hash=`cat includes/git_hash.txt`
git tag published $git_hash
git push origin published


