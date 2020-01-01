alias autopep8="/home/runner/.local/bin/autopep8  --in-place --aggressive --aggressive --indent-size 2"
alias pytest="/home/runner/.local/bin/pytest"

cp gitignore .gitignore
cd tests
/home/runner/.local/bin/pytest
