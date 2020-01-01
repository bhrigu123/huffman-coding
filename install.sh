chmod 755 install.sh
pip3 install pytest
pip3 install autopep8

cp gitignore .gitignore

alias autopep8="/home/runner/.local/bin/autopep8  --in-place --aggressive --aggressive --indent-size 2"
alias pytest="/home/runner/.local/bin/pytest"

chmod 755 test.sh
