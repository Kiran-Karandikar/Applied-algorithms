# Applied algorithms Lab

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
