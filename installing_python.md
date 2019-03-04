# Installing Python

The very first thing you will need to do in order to use Python is installing it. There are several ways of doing so depending on the operative system (OS) you use and how advanced you are as a user. The simplest way to get started with Python-based scientific computing is using **Anaconda**. 

Anaconda is a Python distribution that includes, as standard, the main packages useful for most research-related task. It also has an easy to use interface to install new packages, a couple of tools for development (Spyder and Jupyter) and a terminal for the more impatient users. 

To download Anaconda, simply click in the following link:

[Download Anaconda](https://www.anaconda.com/download)

You should be offered with the correct version for your OS. During this course, we will use **Anaconda 2018.12** (the newest at the time of writing this gide) with **Python 3.7**. Make sure you click in the correct download button.

The default settings during the installation should be fine in most cases, as long as you do not have other Python 3 already installed in your sistem. If you are using Windows or Mac OS, chances are this is your first Python 3. In some Linux distributions, Python 3 might be installed already, but hopefully Anaconda will not create any conflict. 

## What comes with Anaconda?

Of course, the basic Python 3.7 distribution with all the basic tools you find normally in Python, but also:

- [**Numpy**](http://www.numpy.org): This is the fundamental package for numerical analysis of any kind. Basically, *all* packages that aim to do *any* type of numerical analysis or using *any* type of large data structures, uses it. All the packages mentioned below do so. Among many other things, it provides the ```array``` type of data: esentially vectors and matrices. 

- [**Scipy**](https://docs.scipy.org/doc/scipy/reference/): This package provides the tools and algorithms to solve mathematical problems, ranging from linear and non-linear algebra, differential equations, optimization, etc... 

- [**Matplotlib**](https://matplotlib.org): This is *THE* Python plotting library, incredibly flexible and able of producing almost any type of graph with publication quality. Simply, have a look at the [galery](https://matplotlib.org/tutorials/introductory/sample_plots.html).  

- [**Pandas**](http://pandas.pydata.org): This is a data analysis library, pretty much created to do the same things that *R* does... but in Python. Copying from the documentation "it provides fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive."  

...and many other we do not care, for now. 

## How do I get started?

Anaconda itself is not a piece of software, but rather a bundle of different tools conveniently packed together. To develop Python applications, we will use [Jupyter notebooks](https://jupyter.org). The material for the course are actually Jupyter notebooks that you can open and edit.  

To launch Jupyter notebooks, there are several options depending on your OS:

- **Windows**: There should be an entry called Jupyter in the Windows menu, probably inside an entry grouping all Anaconda applications. 
- **Linux and Mac OS X**: Here you can:
    - Fast way: open a terminal, write "jupyter notebook" and hit "enter".
    - The visual way: open the Anaconda Navigator, which should appear somewhere in your Applications folder or menu, and then lunch Jupyter when given the option.   

**Note**: by default, any graph will appear within the Jupyter notebook window, which is rather small and not interactive. To make it appear as a separate window and be able to interact with it, run anywhere within a notebook, and before doing anythin else ```%matplotlib tk``` .
