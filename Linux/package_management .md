# Package management 
Different distributions use different package management systems, 
and generally a package for one distribution is not compatible with another distribution.

Most distributions fall into one of two groups of package management technologies:

| Package management system | Distributions (partial list) |
|---------|--------|
| Debian (.deb)| Debian, Ubuntu, Linux Mint, Raspbian
| Red Hat (.rpm) | Fedora, CentOS, Red Hat Enterprise Linux, OpenSUSE

Virtually all software for Linux can be found on the Internet. Most are provided 
by the distributor as `package files`, and the rest are available as source code that you can compile yourself.

`Package files`: The package files contain all of the necessary files, metadata, 
and instructions to implement a particular functionality or software application on your computer.  
In addition, many packages include pre-installation and post-installation scripts that perform pre-installation and post-installation configuration tasks.  

`Repositories`: Repositories are servers which contain sets of packages.

`Dependencies`: Dependencies are additional packages required by the principal package in order to function properly.
___
## High- and low-level package management tools
Package management systems usually consist of two types of tools:  
- low-level tools which handle tasks such as installing and removing package files  
- high-level tools that per- form metadata searching and dependency resolution

Example of tools:

| Distributions | low-level | high-level |
|---------|--------|-----------|
| Debian | dpkg | apt-get, aptitude
| Fedora, Red Hat, CentOS | rpm | yum, dnf
___
## Common package management tasks
### Looking for a package in the repository

| Distribution | Command |
|---------|--------|
| Debian | apt-get update; apt-cache search search_string OR sudo apt search package_name
| Red Hat | yum search search_string

About apt: The APT package index is basically a database that holds records of available packages from the repositories enabled in your system.  
`sudo apt update` updates the package index.  
**NB: Always update the package index before upgrading or installing new packages!**  

___
### Installing the package from the repository

| Distribution | Command |
|---------|--------|
| Debian | apt-get update; apt-get install package_name
| Red Hat | yum install package_name
___
### Installing a package using a package file
If the package file was downloaded from a source other than a repository, 
it can be installed directly (although without dependency resolution) using low-level tools.

| Distribution | Command |
|---------|--------|
| Debian | dpkg --install package_file
| Red Hat | rpm -i package_file
___
### Package removal

| Distribution | Command |
|---------|--------|
| Debian | apt-get remove package_name
| Red Hat | yum erase package_name

For `apt` the `remove` command will uninstall the given packages, but it may leave some configuration 
files behind. If you want to remove the package including all configuration files, use `purge`: `sudo apt purge package_name`  
**NB**: When the package is removed, the dependencies will stay on the system.  
This leftover packages are no longer used by anything else and can be removed: `sudo apt autoremove`
___
### Updating packages from the repository

| Distribution | Command |
|---------|--------|
| Debian | apt-get update; apt-get upgrade
| Red Hat | yum update

For `apt` there is also `full-upgrade` which will remove the installed packages if that is needed to upgrade the whole system.
___
### Upgrading packages with a package file

| Distribution | Command |
|---------|--------|
| Debian | dpkg -i package_file
| Red Hat | rpm -U package_file
___
### Listing installed packages

| Distribution | Command |
|---------|--------|
| Debian | dpkg -l
| Debian | sudo apt list
| Red Hat | rpm -qa

For `apt`: `sudo apt list | grep package_name`  
To list only the installed packages type: `sudo apt list --installed`  
Getting a list of the upgradeable packages may be useful before actually upgrading the packages: `sudo apt list --upgradeable`
___
### Checking if the package is installed

| Distribution | Command |
|---------|--------|
| Debian | dpkg -s package_name
| Red Hat | rpm -q package_name
___
### Displaying information about an installed package

| Distribution | Command |
|---------|--------|
| Debian | apt-cache show package_name
| Red Hat | yum info package_name

For `apt`: To retrieve information about a given package, use the show command: `sudo apt show package_name`
___
### Checking which package installed the file

| Distribution | Command |
|---------|--------|
| Debian | dpkg -S package_name
| Red Hat | rpm -qf package_name
___
## Sources
- W. Shotts, The Linux Command Line, 2nd Edition: A Complete Introduction, No Starch Press 2019
- Linuxize, apt Command in Linux, https://linuxize.com/post/how-to-use-apt-command/

