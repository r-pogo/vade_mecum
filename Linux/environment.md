# Environment

| Command | Action |
|---------|--------|
| env | allows you to run another program in a custom environment without modifying the current one. When used without an argument it will print a list of the current environment variables.
| printenv | prints all or the specified environment variables.
| set | sets or unsets shell variables. When used without an argument it will print a list of all variables including environment and shell variables, and shell functions.
| unset | deletes shell and environment variables.
| export |  sets environment variables.
| alias | listing or creating aliases.
___

## Environment Variables and Shell Variables
Environment variables are available system-wide and are inherited by all spawned child processes and shells.  
Shell variables apply only to the current shell instance.  


Variables have the following format:
````
# environment variables should have UPPER CASE names
KEY=value # no space around = symbpol
KEY="Some other value"
KEY=value1:value2 # When assigning multiple values to the variable they must be separated by the colon : characte
````
___
## Viewing the environment
If you run the `printenv` or `env` command without any arguments it will show a list of all environment variables.  
If you want to get a list of all variables,  environment and shell use `set`
Listing environment variables:
```
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶printenv | less
```
`printenv` also allows you to display the value of a specific variable:
```
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶printenv USER
elski
```
You can use also `echo`:
```
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶echo $USER
elski
```
___
# Setting up the environment
Bash reads and executes commands from a set of startup files. What files are read depends upon whether the shell is invoked as an interactive login or non-login shell  

Login shell - is the one where we are asked for a username and password, for example when a user login to the terminal either remotely via ssh or locally, or when Bash is launched with the --login option.  
Non-Login shell - takes place when we run a shell in a graphical environment.  

Login shell startup files:
Bash looks for the `/etc/profile` file, and if the file exists, it runs the commands listed in the file. Then Bash searches for `~/.bash_profile`, `~/.bash_login`, and `~/.profile` files, in the listed order, and executes commands from the first readable file found.

| File | Content |
|---------|--------|
| /etc/profile | a global configuration script that applies to all users
| ~/.bash_profile | user startup file. It can be used to extend or overwrite the settings in the global configuration script
| ~/.bash_login | if ~/.bash_profile is not found, bash will try to read this script
| ~/.profile | if neither ~/.bash_profile nor ~/.bash_login is found, bash tries to read this script. This is the default behavior on Debian based distributions like Ubuntu

Non-Login shell startup files:
In this case Bash reads and executes commands from `~/.bashrc`, if that file exists, and it is readable.

| File | Content |
|---------|--------|
| /etc/bash.bashrc | A global configuration script that applies to all users 
| ~/.bashrc | User startup file. It can be used to extend or overwrite the settings in the global configuration script
___
## Modifying the environment

As a general rule of thumb, if you want to add directories to the `PATH` variable or define additional environment variables - commands that should run only once, 
you should put those changes in the `.bash_profile file` (or its equivalent, e.g. `.profile` for Ubuntu). 
All other changes - commands that should run every time you launch a new shell, should be placed in the `.bashrc` file.

To apply you modification use the text editor of your choice:

```
# for vscode
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶code ~/.bashrc
```
After that force bash to read `.bashrc` again (generally is read only once at the beginning of the session):

```
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶source ~/.bashrc
```
___
### Setting variables
To create a new shell variable just type:
```
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶NEW_VARIABLE='stuff'

elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶set | grep NEW_VARIABLE
NEW_VARIABLE=stuff
```
To create an environment variable you need to use `export`:

```
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶export NEW_VARIABLE

elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶printenv NEW_VARIABLE
stuff
```
Environment variables created in this way are available only in the current session.  
If you open a new shell or if you log out all variables will be lost.

To make environment variables persistent you need to define those variables in the bash configuration files.

`/etc/environment` - This file is used to set up system-wide environment variables.
`/etc/profile` - Variables set in this file are loaded whenever a bash login shell is entered. When declaring environment variables in this file you need to use the export command:
```
export PATH_STUFF="/path/to/stuff/home"
export PATH=$PATH:$PATH_STUFF/bin
```
Per-user shell specific configuration files. For example, if you are using Bash, you can declare the variables in the `~/.bashrc`:

`export PATH="$HOME/bin:$PATH"`
___
## Sources
- W. Shotts, The Linux Command Line, 2nd Edition: A Complete Introduction, No Starch Press 2019
- Linuxize, How to Set and List Environment Variables in Linux, https://linuxize.com/post/how-to-set-and-list-environment-variables-in-linux/#
- Linuxize, .bashrc vs .bash_profile, https://linuxize.com/post/bashrc-vs-bash-profile/


