# Blockchain Interoperability

## Usage

```python
from api import store, retrieve, migrate, Blockchain

tx_hash = store('Some Data', Blockchain.STELLAR)    

data = retrieve('[Transaction_Hash]')    

tx_hash = migrate('[Transaction_Hash]', Blockchain.ETHEREUM)
```

Or use the CLI:
```python
source venv/bin/activate

python3 cli.py
```




## Setup

Python 3.6.6 (also tested with 3.6.5) was used for this project. It is compatible with Mac, Linux and Windows.

### Install Docker
(Linux) Follow [this](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04) or [this](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1) manual and then do `sudo apt-get install docker-compose` or follow [this](https://linuxize.com/post/how-to-install-and-use-docker-compose-on-ubuntu-18-04/)    

(Mac) Install from https://docs.docker.com/docker-for-mac/install/

### How to use venv
Install (only needed on Linux):    
`apt-get install python3-venv`    
Create environment:    
`python3 -m venv venv`    
Activate environment:    
`source venv/bin/activate`    
The python version of the environment will be the one with which the environment is created.    
Deactivate environment:    
`(venv) $ deactivate`    
  
### Import/Export and install dependencies
First, upgrade pip: `pip install --upgrade pip`

Export: `venv/bin/pip freeze > requirements.txt`    
Import/Install: `venv/bin/pip install -r requirements.txt`

*Installation problems on linux:*
You may have to do the following installs:    
`sudo apt-get install build-essential autoconf libtool pkg-config python-opengl python-pyrex python-pyside.qtopengl idle-python2.7 qt4-dev-tools qt4-designer libqtgui4 libqtcore4 libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus python-qt4 python-qt4-gl libgle3 python-dev libssl-dev`

*Upgrade pip on <3.6:*    
Use this command if upgrading pip fails due to SSL cert error:    
`curl https://bootstrap.pypa.io/get-pip.py | python`


### Database Setup
Install sqlite(not needed on linux, TEST on mac):        
`pip install sqlite`

Run the database setup:    
```python
import db.database
db.database.setup()
```

Calling the `setup` function of the [`database`](database.py) module will:

1. drop `credentials` and `transactions` tables if they already exist
2. create tables for storing `credentials` and `transactions`
3. seed the `credentials` table with credentials 
4. seed the `transactions` table with input transactions

Seed values are read from the [`config`](config.py) module.

### Blockchain Setup

See descriptions in [SETUP.md](SETUP.md) for instruction to setup the local nodes.

#### Hyperledger Sawtooth Adapter
The Hyperledger Sawtooth adapter does not support python 3.6.      
It was therefore removed from the requirements.txt.     
To use the Sawtooth Hyperledger adapter either use Python 3.5 (refactor adapter accordingly i.e. `f"{}"`) or use the workaround listed in setup.md (only tested on MacOS).

### Useful docker commands 
Stop and remove all docker container:     
`docker rm -f $(docker ps -a -q)`    
Delete all images:    
`docker rmi $(docker images -q)`     
