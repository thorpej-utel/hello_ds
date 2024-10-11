#hello ds

Prerequisites
The following installations are required for the completion of this tutorial. Make sure to install them if you haven't already.

Visual Studio Code

The Python extension for VS Code and Jupyter extension for VS Code from the Visual Studio Marketplace. For more details on installing extensions, see Extension Marketplace. Both extensions are published by Microsoft.

Miniconda with latest Python

Note: If you already have the full Anaconda distribution installed, you don't need to install Miniconda. Alternatively, if you'd prefer not to use Anaconda or Miniconda, you can create a Python virtual environment and install the packages needed for the tutorial using pip. If you go this route, you will need to install the following packages: pandas, jupyter, seaborn, scikit-learn, keras, and tensorflow.


conda create -n myenv python=3.10 pandas jupyter seaborn scikit-learn keras tensorflow
conda install -n base ipykernel --update-deps --force-reinstall

