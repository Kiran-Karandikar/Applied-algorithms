# Applied algorithms

> Python version 3.8

`pip install -r requirements.txt`


---

- [ ] re-arrange below stuff

- ### Jupyter Notebook and Virtual Environment
	
	- [How to activate virtual env in conda](https://towardsdatascience.com/manage-your-python-virtual-environment-with-conda-a0d2934d5195)

> ! Do not use `pip` for installation inside conda environment use `conda install`.

- #### List of packages installed
  ``
  conda list
  ``
- #### Create and activate virtual Env
  ``
  conda env create --name appalg python=3.8.8 conda activate appalg
  ``

- #### Install Required packages for jupyter Notebook
  ``
  conda install pywin32 conda install ipykernel conda install juptyer
  ``
- #### Attach Kernel to the venv
  Here replace `appalg` with name of virtual Environment.
  ``
  python -m ipykernel install --name=appalg
  ``

##### Temp Stuff -->

`python [environment path]/Scripts/pywin32_postinstall.py -install`

# To create a requirements.txt file:

conda list #Gives you list of packages used for the environment

conda list -e > requirements.txt #Save all the info about packages to your
folder

# To export environment file

activate <environment-name>
conda env export > <environment-name>.yml

# For other person to use the environment

conda env create -f <environment-name>.yml