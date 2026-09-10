This is the repository of the course on Declarative Programming taught at the Computer 
Science Degree of the University Rey Juan Carlos. 


# Content 

The course material basically includes several notebooks on the following topics:

* PF-1
  * Topic 1. [Introduction & schedule](PF-1/Intro.pdf) (spanish, URJC specifics)
  * Topic 2. Strongly-typed languages and Scala
* PF-2
  * Topic 3. Algebraic data types
  * Topic 4. [The Curry-Howard correspondence](https://github.com/jserranohidalgo/curry-howard-game)
* PF-3
  * Topic 5. Recursive functions and data types
  * Topic 6. Higher-order functions and modular programming
  * Topic 7. Applications

# The Curry-Howard Game

Topic 4 comes with a game: [__The Curry-Howard Game__](https://github.com/jserranohidalgo/curry-howard-game).
Given a proposition, the goal is to construct a proof of it — or to establish that no proof exists —
by building, step by step, the program that inhabits the corresponding type. It runs in the browser,
with nothing to install; see its repository for the details.

# Launching notebooks

To access these notebooks you need first to install [git](https://git-scm.com/) and clone this repository in your local drive: 

`> git clone https://github.com/jserranohidalgo/urjc-pd.git pd`

Then, install `jupyter` (see instructions below) and run the program:

`jupyter notebook`  or `jupyter lab`

in the root directory of the repository.

Alternatively, you can skip the manual installation of `jupyter`
and run it through [docker](https://hub.docker.com/editions/community/docker-ce-desktop-windows) as follows:

`docker run -it --rm -p 8888:8888 -p 4040:4040 -m 4g -v "$PWD":/home/jovyan/work almondsh/almond:latest` (LINUX)

`docker run -it --rm -p 8888:8888 -p 4040:4040 -m 4g -v <<c:/path/to/downloaded/folder>>:/home/jovyan/work almondsh/almond:latest` (WINDOWS)

(also in the root directory of the repository)

Finally, note that `jupyter` is already installed in the virtual environment MyApps (just for URJC users).

# Installing jupyter and the Scala kernel

To install jupyter and run Scala notebooks, follow these steps:

* Install the package manager [`conda`](https://docs.conda.io/en/latest/miniconda.html), or use `pip`, the python package manager.
* Install [`jupyter`](https://jupyter.org/install) itself
* Alternatively, you can also find jupyter notebooks for free when installing [anaconda](https://www.anaconda.com/products/individual-d).
* Install [Java 8](https://docs.oracle.com/javase/8/docs/technotes/guides/install/install_overview.html#A1096936). Take into account whether your architecture is 32-bit or 64-bit.
* Install the Scala plugin [`almond`](https://almond.sh/docs/quick-start-install). 

For the last step, in order to install the Scala 3 version of the almond kernel, choose the following options: 

`./coursier launch --fork almond:0.14.0-RC14 --scala 3.3.1 -- --install --id scala33 --display-name "Scala 3.3"`

### Possible problems when installing almond

* On windows, I can't download the installation scripts of the `almond` Scala kernel through:

	> bitsadmin /transfer downloadCoursierCli https://git.io/coursier-cli "Í%%coursier"
	> ...

Likely, you are using powershell; use simple `cmd` instead. 

Possibly, you will also need to use administration privileges (i.e., run CMD as admin).


* In the thir step (".\coursier launch --fork ..."), the following error pops up:

Exception in thream "main" java.lang.Exception: Unrecognized CPU architecture: x86. 

Likely, you need a java version for 64 bits, but you installed one for 32 bits. Check which java version you have by typing: "java -d64 -version".

* Now, the installation command hangs (most likely, on windows)

Execute the installation command with the verbose option enabled (`-v -v`):

        .\coursier launch --fork almond -M almond.ScalaKernel -v -v -- --install

When the program hangs, stop it (C-c C-c). Most likely, the last command that was attempted was something like "Running java ...". Copy-paste that java invocation and run it manually:

        java -Dscala-kernel.version=<...> -jar <...> --install

Luckily, this will complete the installation of the almond kernel.

* "Cannot find default main class. Specify one with -M or --main-class" (most likely, on linux)

Add the option `-M almond.ScalaKernel`  to the installation command, i.e.

        ./coursier launch --fork almond -M almond.ScalaKernel -- --install

# Git branches

The course material lives in two forms: full notebooks, and a _template_ version of each
one. Theory classes — except for the very first, presentation session — don't use slides:
instead, I go through the template notebooks and fill them in live, explaining concepts by
writing illustrative examples as we go. What ends up in a template is usually close to its
corresponding full notebook, but classroom discussion often leads to extra examples that
aren't in it.

After each class, I push the updated templates to the branch of your course (`MOS-26-27` or
`VIC-26-27`), so that everyone has access to what was written in class.

You are encouraged to bring your laptop and fill in the templates along with me as the
class goes. To do so, create a personal branch off the course branch and work there —
__don't commit directly to `MOS-26-27`/`VIC-26-27`__, or your changes will conflict with the
ones I push after class. Your personal branch is your own version of the course branch.

Practice classes work the same way, except there is no template version of the problem
sets: I fill in the actual exercise notebooks directly, and push the changes to the course
branch just as with the theory notebooks. You should do the same on your personal branch.

### Setting up your personal branch

Create it once, off the course branch (`VIC-26-27` in this example), and switch to it:

```sh
git checkout VIC-26-27
git checkout -b <your-branch-name>
```

### Saving your changes after each class

Commit what you filled in during the session, with a message that identifies the class:

```sh
git add -A
git commit -m "Class 1/10/26"
```

### Updating your local course branch

Before switching branches, make sure your own changes are committed (see above). Then,
to bring in the templates I pushed after class:

```sh
git checkout VIC-26-27
git pull
```

and switch back to your personal branch to keep working:

```sh
git checkout <your-branch-name>
```

This is enough git to follow the course, but it's only a thin slice of what git can do. If
you want to go deeper, [_Pro Git_](https://git-scm.com/book/en/v2) is the reference: free,
thorough, and available online.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
