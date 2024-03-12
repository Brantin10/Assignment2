Pig 🐷 Dice game
======================


Pig, is a fun and simple dice game perfect for playing with family and friends. The game requires only two dice and a strong appetite for risk-taking! Here is a basic description of how it works:

**Player:** Two people against each other.

**The goal:** To reach 100 points first.

**Rules:**

1. The player / computer rolls the  dice.
2. If the player rolls a one on the dice, they lose all points collected during the round and it is the next player's turn.
3. If the player does not roll a one, the sum of the dice is added to their score for the round.
4. The player can choose to either roll the dice again to increase their score for the round, or stay and add the score to their total score for the game.
5. If the player decides to stay, control passes to the next player.
6. First player to reach 100 points wins the game.

**Strategy:**

- The risk of continuing to roll the dice increases the chance of getting a one and losing all points for the round.
- It is important to weigh the risk and reward when deciding to continue or stay.
- A common strategy is to accumulate points slowly by stopping at each safe sum to avoid losing everything in a single turn.

Good luck, let´s play! 🎲

![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/Brantin10/Assignment2/total?style=for-the-badge&logo=docusign&logoColor=%2340AEF0color=%2340AEF0)
![GitHub License](https://img.shields.io/github/license/Brantin10/Assignment2?style=for-the-badge)
![GitHub Release](https://img.shields.io/github/v/release/Brantin10/Assignment2?include_prereleases&sort=date&display_name=tag&style=for-the-badge)


Table of Contents 📃
----------------------
Click on the link to get to the section!

- [Get started](#clone-repositorie)

  - [Clone Repositorie](#clone-repositorie) 🖨️
 
  - [Check Python version](#check-python-version) <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" alt="Python" width="15" height="15" />


  - [Install Python virtual environment and activate it](#install-python-virtual-environment-and-activate-it) <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" alt="Python" width="15" height="15" />


  - [Install the dependencies 💾](#install-the-dependencies)

  - [Run the code 🏃](#run-the-code)
    
- [Test code](#run-the-validators)
  
  - [Run the validators 🏃](#run-the-validators)

  - [Codestyle with black  ⏺](#codestyle-with-black)

  - [Run the unittests 🏃](#run-the-unittests)

  - [Run parts of the testsuite 🏃](#run-parts-of-the-testsuite)

- [More targets in the Makefile 📄](#more-targets-in-the-makefile)

- [Remove generated files 🗑️](#remove-generated-files)

<a name = "clone-repositorie"></a> Clone Repositorie 🖨️
--------------------------------------------------------
Here is a guide how to clone the repositorie -->
[Clone repositorie](https://www.youtube.com/watch?v=S1rDpn5fk5s&list=PLEtyhUSKTK3iTFcdLANJq0TkKo246XAlv&index=4).

Https://
```
git clone https://github.com/Brantin10/Assignment2
```
SSH
```
git clone git@github.com:Brantin10/Assignment2.git
```
Then go inside the Assignment2 map with
```
cd Assignment2
```

<a name = "check-python-version"></a> Check Python version <img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" alt="Python" width="20" height="20" />
-----------------------------------------------------------------------------------------------------------------------------
Check what version of Python you have. The Makefile uses `PYTHON=python` as default.
```
make version
```
If you have another naming of the Python executable then you can solve that using an environment variable. This is common on Mac and Linux.

Set the environment variable to be your python executable
```
export PYTHON=python3
```
```
make version
```
> [!TIP]
> Read more on [GNU make](https://www.gnu.org/software/make/manual/make.html).


<a name = "install-python-virtual-environment-and-activate-it"></a> Install a Python virtual environment and activate it <img 
src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="20" height="20" alt="Python" /></a></p>
------------------------------------------------------------------------------------------------------------------------------------------
Here is a guide how to install the Python virtual environment --> [Create the virtual environment](https://www.youtube.com/watch?v=UsmNyNxndv4)
### Create
Create a .venv on Windows 🪟
```
python -m venv .venv
```
Create a .venv on Linux / Mac 🍏
```
python3 -m venv .venv
```
### Open
Open the .venv
```
make venv
```
### Activate
Activate on Windows 🪟
```
. .venv/Scripts/activate
```

Activate on Linux / Mac 🍏
```
. .venv/bin/activate
```
### Deactivate
When you are done you can leave the venv using the command 🙅🏼
```
deactivate
```
> [!TIP]
> Read more on [Python venv](https://docs.python.org/3/library/venv.html).


<a name="install-the-dependencies"></a> Install the dependencies 🪢
---------------------------------------------------------------------
Install the PIP packages that are dependencies to the project and/or the development environment. The dependencies are documented in the `requirements.txt`.

Do not forget to check that you have an active venv.

To install them
```
make install
```
Check what is installed in .venv
```
make installed
```
> [!TIP]
> Read more on [Python PIP](https://pypi.org/project/pip/).


<a name="run-the-code"></a> Run the code 👩‍💻 
-------------------------------------------
The program can be started like this.

Execute the main program
```
python PigDiceGame/main.py
```
All code is stored below the directory `PigDiceGame/`.

Good Luck! 😀


<a name="run-the-validators"></a> Run the validators ✅
-------------------------------------------------------
You can run the static code validators like this. They check the sourcecode and exclude the testcode.

Run each at a time
```
make flake8
```
```
make pylint
```
Run all on the same time
```
make lint
```
Read more on:

> [!TIP]
> * [flake8](https://flake8.pycqa.org/en/latest/)
> * [pylint](https://pylint.org/)


<a name="codestyle-with-black"></a> Codestyle with black ⚫
-----------------------------------------------------------
You can unify the codestyle using black. Running black will change your source code to have a codestyle according to black codestyle.

Same same, different names
```
make black
```
> [!TIP]
> Read more on [black](https://pypi.org/project/black/).


<a name="run-the-unittests"></a> Run the unittests 🏃
--------------------------------------------------------
You can run the unittests like this. The testfiles are stored in the `test/` directory.

Run unittests without coverage
```
make unittest
```
Run unittests with coverage
```
make coverage
```

Run the linters and the unittests with coverage
```
make test
```

Copy and insert in terminal to open the web browser to inspect the code coverage as a generated HTML report.

On windows 🪟

```
start htmlcov/index.html
```
On linux / Mac 🍏
```
open htmlcov/index.html
```

Read more on:

> [!TIP]
> * [unittest](https://docs.python.org/3/library/unittest.html)
> * [coverage](https://coverage.readthedocs.io/)

<a name="run-parts-of-the-testsuite"></a> Run parts of the testsuite   🏃
-------------------------------------------------------------------------
You can also run parts of the testsuite, for examples files or methods in files.

You can run all tests from a testfile.

Run a testfile
```
python -m unittest test.test_game
```

You can also run a single testcase from a file.

Run a test method, in a class, in a testfile
```
python -m unittest test.test_game.TestGameClass.test_init_default_object
```


<a name="more-targets-in-the-makefile"></a> More targets in the Makefile 📄
---------------------------------------------------------------------------
The makefile contains more targets, for example these.

to generate documentation from the code.
```
make doc
```

to generate class and package diagrams from the code base.
```
make pyreverse
```
Open with:

On windows 🪟
```
start doc/pyreverse/classes.png && start doc/pyreverse/packages.png
```
on Mac (add xdg-, before if you have linux)
```
open doc/pyreverse/classes.png && open doc/pyreverse/packages.png
```


<a name="remove-generated-files"></a> Remove generated files 🗑️
---------------------------------------------------------------
You can remove all generated files by this.

Remove files generated for tests or caching
```
make clean
```

Do also remove all you have installed
```
make clean-all
```
