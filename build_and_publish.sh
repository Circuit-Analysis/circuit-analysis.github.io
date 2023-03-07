jupyter-book build -W -n .
ghp-import -n -p -f _build/html
git_hash=`cat includes/git_hash.txt`
git tag -d published
git push origin :refs/tags/published
git tag published $git_hash
git push origin published


