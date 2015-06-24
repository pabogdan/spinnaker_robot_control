# AlanProject

__The Imitation Game__ will be a major contemporary art exhibition curated by Clare Gannaway at Manchester
Art Gallery, UK, March-August 2016. Inspired by Manchesterís rich history of computer science, it will
feature eight international contemporary artists exploring the theme of machines and the imitation of life.
The exhibition will be part of the cultural programme for Manchesterís role as __European City of Science__ in
2016.

Artist Tove Kjellmark (Sweden) is making a new artwork for The Imitation Game exhibition, opening March
2016, in the form of two __human-like robots__ which will sit in leather armchairs in the gallery and converse
with each other on topics yet to be decided. They will __detect and acknowledge the presence of human
visitors__ to the gallery through __movement and speech__. Tove is currently working with staff and students at
KTH, Stockholm, to begin the building process, and she will also work collaboratively with academics and
students at The University of Manchester to embed SpiNNaker technology into the robots to affect their
behaviour.

## Requirements

The following should work on all operating systems:

+   [Python 2.7](https://www.python.org/download/releases/2.7/) with [pip](https://pip.pypa.io/en/stable/installing.html) installed

### Windows specific
+   [Microsoft Visual C++ Compiler for Python 2.7](http://www.microsoft.com/en-gb/download/details.aspx?id=44266)

## Installation

In a terminal run the following commands (might require administrator privilege):

`pip install numpy`
    
`pip install nengo_gui`

If you want to run simulations on SpiNNaker you will also need to install the SpiNNaker Nengo library

`pip install nengo_spinnaker`

## Running the software locally

In order to start the GUI you only need to type `nengo_gui` into the terminal as the previously installed package should be on the PATH already.

## Running the software on SpiNNaker

Please follow the guide on the [Nengo SpiNNaker Github repo](https://github.com/project-rig/nengo_spinnaker)

