# Static website generator

## Description

The scope of the project was to create an application that could turn simple
markdown files into html files to be served on the web. </br> </br>
Currently, it takes all markdown files in _content_ directory and directories nested in it, turns them in valid html files and copies everything in a public directory from where the site will be served on the web.
CSS files and images are served separately from the static directoy and are also copied in _public_.
</br> </br>

## Get started

As an example I've already put a markdown file used for a school project. To start the application use `./main.sh` from the root of the project, it should run the _main.py_ script and then host the _public_ directory on local, port 8888 </br>
To pass any markdown file you want, simply remove everything that is already in _content_ and add your own files. Make sure to add any necessary files in _static_.
