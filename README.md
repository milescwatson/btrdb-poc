# BTrDB POC App

# Documentation

## VM setup
Distro: Ubuntu 20.10

un: admin
pw: btrdb123

Working GIT directory: `/projects/btrdb-poc`

## Environment setup (Smartgrid Store)
git: https://github.com/BTrDB/smartgridstore
After cloning, install dependencies:
* Docker: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04
* Kubernetes: `sudo snap install kubectl --classic`

### Launch Server
To launch server, go to directory:
`/projects/btrdb-poc/smartgridstore`
and run
```
source ./environment.sh
sudo -E ./start_devmachine.sh
```
#### Close Server:
`source ./environment.sh sudo -E ./teardown_devmachine.sh`

### Administer Server
`ssh admin@127.0.0.1 -p 2222`
password: `sgs-default-admin-password`

### MrPlotter
site: 127.0.0.1:8888
un: `admin`
pw: `sgs-default-admin-password`

## Setup SQL Server
`sudo apt install mysql-server`
`sudo mysql_secure_installation`
*Credentials*
database: restaurants
user: btrdb
password: btrdb123

## Info
```
Plotter is on https://127.0.0.1:8888
Console is on ssh://127.0.0.1:2222
BTrDB GRPC api is on 127.0.0.1:4410
BTrDB HTTP api is on http://127.0.0.1:9000
BTrDB HTTP swagger UI is on http://127.0.0.1:9000/swag
```

## Python btrdb API

Install specific version: `pip3 install btrdb==4.15.9`
Import using `import btrdb4`
Note: use 'uu' instead of 'uuid' as the docs show to create streams

Upon installing, it is necceary to modify the `create` function, replacing it with the code from the newest btrdb python code
`/usr/local/lib/python3.8/dist-packages/btrdb4/endpoint.py`

# Links
## Repos
https://github.com/BTrDB/mr-plotter
https://github.com/BTrDB/btrdb-server
https://github.com/BTrDB/smartgridstore
## Guides
https://github.com/BTrDB/btrdb-server/issues/64
https://www.alibabacloud.com/blog/all-about-btrdb-berkeleys-tree-database_595170
https://btrdb.readthedocs.io/en/latest/working.html
https://btrdb.readthedocs.io/en/latest/explained.html

https://web.archive.org/web/20190410134756/https://docs.smartgrid.store/installation.html#startup

## Influx
https://docs.influxdata.com/influxdb/v1.8/query_language/continuous_queries/
https://docs.influxdata.com/influxdb/v1.8/concepts/time-series-index/