VER: v0.0.1

Pre-Requisites:

Install Python3

Ubuntu
From BASH Shell Execute

sudo bash apt-get python3

Install Python Packages

PyTest = https://docs.pytest.org/en/latest/getting-started.html  
Invoke = http://www.pyinvoke.org/installing.html

Logic:

To use this example, make sure that Invoke, PyTest, and a version of Python above 3.5 is installed on the localhost.

Once completed, to get running use the "invoke deps" command to install the dependencies and then "invoke test" to run the unit test.

NOTE: If this is run after stock trading hours the test will fail due to dynamic page content changing.
