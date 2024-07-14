# 1. How to install LHAPDF

One can get LHAPDF from hepforge as follow:
```
current_location=$PWD
wget https://lhapdf.hepforge.org/downloads/?f=LHAPDF-6.5.3.tar.gz -O LHAPDF-6.5.3.tar.gz
tar xf LHAPDF-6.5.3.tar.gz
mkdir lhapdf
cd LHAPDF-6.5.3/
./configure --prefix=${current_location}/lhapdf
make
make install
cd ${current_location}
```
You should have python3, python3-pip, python3-venv, matplotlib, and lhapdf-venv if not run
```
sudo apt-get install python3-pip python3-venv
pip install matplotlib
```
and then do
```
mkdir test
cd test
python3 -m venv lhapdf-venv
```

Configure correct paths in your bash script.
Add these lines in your bash scripts.
```
### LHAPDF ###
export PATH=<current_location>/lhapdf/bin:$PATH
export LD_LIBRARY_PATH=<current_location>/lhapdf/lib:$LD_LIBRARY_PATH
export PYTHONPATH=<current_location>/lhapdf/lib/python3.8/site-packages/:$PYTHONPATH
alias run-lhapdf='source <current_location>/test/lhapdf-venv/bin/activate && printf "To run the code, do\n$ cd <current_location>/test && python3 *.py\n"'
### --- ###
```
Note <current_location> means the starting location that was set at the first time with `current_location=$PWD`.

Now activate lhapdf with
```
source lhapdf-venv/bin/activate
```
This will run the LHAPDF.
If you already set the alias `run-lhapdf` correctly, then you don't need to activate but just do run-lhapdf.
You can deactivate LHAPDF with `deactivate`.

If you already did these steps but do not remember which lhapdf version you have, then do
```
lhapdf-config --version
```

# 2. How to get new PDF sets

When you want to use new PDF sets, you should download it, e.g.
```
lhapdf install CT18NLO
```

# 3. How to draw PDF plots

```
git clone <This git>
cd ${current_location}/test
python3 plot.py
```
This will generate png files.




