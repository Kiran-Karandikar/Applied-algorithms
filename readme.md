# Applied algorithms Lab

### Jupyter Notebook and Virtual Environment

- [How to activate virtual env in conda](https://towardsdatascience.com/manage-your-python-virtual-environment-with-conda-a0d2934d5195)

#### List of packages installed
``
conda list
``
#### Create and activate virtual Env
``
conda env create --name appalg python=3.8.8
conda activate appalg
``

#### Install Required packages for juptyer Notebook
``
conda install pywin32
conda install ipykernel
conda install juptyer
``
####  Attach Kernel to the venv
``
python -m ipykernel install --name=appalg
``

##### Temp Stuff -->

``
pip install --user ipykernel; pip install jupyter;
``
> Add your virtual environment to Jupyter

Replace `appalg` with name of your virtual environment

``
python -m ipykernel install --name=appalg
``

conda env list

conda create --name appalg

conda activate appalg

conda list to list the packages inside of venv

