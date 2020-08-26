git add *

echo "mensaje para el commit:"
read TXT
git commit -m "$TXT"
git push origin master