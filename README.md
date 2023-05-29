# Higher Level Languages - Python🐍
🤖 Holberton Foundations Part 2
________
### Install PEP8
Pycodestyle is now the new standard of Python style code, but at school we will use *PEP8, version 1.7.* * Don’t worry, pycodestyle is based on pep8. The hardest part now is to install it for Python 3: Regular Ubuntu 14.04 install

`$ sudo apt-get install python3-pep8`

Using Pip3 Install Pip3

`$ sudo apt-get install python3-pip`

Install Pep8

`$ pip3 install pep8`

Make sure you have the right version

`$ pep8 --version`
`1.7`
`$`

If it’s not the case, it means PEP8 is installed but not linked in your PATH. You should look at these folders to find where it has been installed:

`*/usr/local/lib/python3*/dist-packages/pep8.py*`
`*/usr/lib/python3*/dist-packages/pep8.py*`

Don’t hesitate to delete /usr/bin/pep8 and replace by one of those pep8.py:

`*cp pep8.py /usr/bin/pep8*`

`*chmod u+x /usr/bin/pep8*`

Finally, if you can’t make it work, please use the “container-on-demand” tool to “PEP8” your files in a pre-configured container.
