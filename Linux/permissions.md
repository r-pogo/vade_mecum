# Permissions
| Abbreviation | Effect |
|--------------|--------|
| id | Print user and group information for the specified USER
| chmod | allows you to change the permissions on a file using either a symbolic or numeric mode or a reference file
| umask |  assign the default file permission sets for newly created folders and files
| su |  allows you to run commands with another user's privileges, by default the root user.
| sudo | SuperUser DO and is used to access restricted files and operations
| chown | The chown command allows you to change the user and/or group ownership of a given file, directory, or symbolic link
| chgrp | chgrp command in Linux is used to change the group ownership of a file or directory.
| passwd | passwd command changes passwords for user accounts. · passwd also changes the account or associated password validity period
___
## Linux File Ownership
Every file and directory on Unix/Linux system is assigned 3 types of owner: 

`User`: a user is the owner of the file. By default, the person who created a file becomes its owner. 
Hence, a user is also sometimes called an owner.  

`Group`: a user- group can contain multiple users. All users belonging to a group will have the 
same Linux group permissions access to the file. 
Suppose you have a project where a number of people require access to a file. 
Instead of manually assigning permissions to each user, you could add all users to a group, 
and assign group permission to file such that only this group members and no one else can read or 
modify the files.  

`World`: any other user who has access to a file. This person has neither created the file, nor he 
belongs to a usergroup who could own the file. Practically, it means everybody else. 
___
## Linux file Permissions
`-rwxrwxrwx 1 cookieMonster cookieMonster      392 Mar 25 08:03  englishWord.txt*`

`-rwx-rw-r--`  
First sign indicates file type, next 3 are for user, next 3 for group, next 3 for world 
````
drwxr-xr-x 12 linuxize users 4.0K Apr  8 20:51 dirname
|[-][-][-]    [------] [---]
| |  |  |        |       |       
| |  |  |        |       +-----------> Group
| |  |  |        +-------------------> Owner
| |  |  +----------------------------> Others Permissions
| |  +-------------------------------> Group Permissions
| +----------------------------------> Owner Permissions
+------------------------------------> File Type
````

| Attribute | File type |
|------------|----------|
| – | regular file
| d | directory
| c | character device file
| b | block device file
| s | local socket file
| p | named pipe
| l | symbolic link

| Attribute | Effect |
|------------|-------|
| r | read permission
| w | write permission
| x | execute permission
| – | no permission
___
## chmod
`chmod` command stands for "change mode". Using the command, we can set permissions (read, write, execute) on 
a file/directory for the owner, group and the world.

`chmod permissions filename`

### Absolute(Numeric) Mode in Linux
In this mode, file permissions are not represented as characters but a three-digit octal number.

| Number | Permission Type | Symbol |
|--------|-----------------|--------|
| 0 | No Permission | ---
| 1 | Execute | --x
| 2 | Write | -w-
| 3 | Execute + Write| -wx
| 4 | Read | r--
| 5 | Read + Execute | r-x
| 6 | Read +Write | rw-
| 7 | Read + Write + Execute | rwx

### Symbolic Mode in Linux
In the Absolute mode, you change permissions for all 3 owners. In the symbolic mode, you can modify permissions of a specific owner. 
It makes use of mathematical symbols to modify the Unix file permissions.

| Operator | Description |
|----------|-------------|
| + | Adds a permission to a file or directory
| - | Removes the permission
| = | Sets the permission and overrides the permissions set earlier.

| Symbol | Meaning |
|--------|---------|
| u | user/owner
| g | group
| o | other/world
| a | all
___
## umsak
The default creation permissions can be modified using the `umask` utility.
The default creation permissions for files are 666 and for directories 777. To calculate the permission 
bits of the new files, subtract the umask value from the default value.  

For example, to calculate how umask 022 will affect newly created files and directories, use:  

Files: 666 - 022 = 644. The owner can read and modify the files. Group and others can only read the files.  

Directories: 777 - 022 = 755.The owner can cd into the directory, and list, read, modify, create or delete the files in the directory. Group and others can cd into the directory and list and read the files.
You can also display the mask value in symbolic notation using the -S option:  
`umask -S`  
`u=rwx,g=rx,o=rx`
___
## su
The `su` (short for substitute or switch user) utility allows you to run commands with another user’s 
privileges, by default the root user.
When invoked without any option, the default behavior of su is to run an interactive shell as root:  
`su`  

You will be prompted to enter the root password, and if authenticated, the user running the command temporarily becomes root.
To confirm that the user is changed, use the whoami command:  
`whoami`  

The command will print the name of the user running the current shell session:  
`root`  

The most commonly used option when invoking su is - (-l, --login). This makes the shell a login shell with an 
environment very similar to a real login and changes the current directory:  
`su -`  

After we are done just use `exit`.  

If you want to run a command as the substitute user without starting an interactive shell, use the -c, --command option  
`su -c`  

To switch to another user account, pass the user name as an argument to su. For example, to switch to the user cookieMonster you would type:
`su cookieMonster`  

On some Linux distributions like Ubuntu, the root user account is disabled by default for security reasons.  
This means that no password is set for root, and you cannot use su to switch to root.  
One option to change to root would be to prepend the su command with sudo and enter the currently logged-in user password:  
`sudo su -`  

The sudo command allows you to run programs as another user, by default the root user.

If the user is granted with sudo assess, the su command is invoked as root. Running `sudo su -` and then typing the 
user password has the same effect the same as running `su -` and typing the root password.

When used with the `-i` option, sudo run an interactive login shell with the root user’s environment:
`sudo -i`  
`sudo -i` is basically the same as running `su -`.
___
## sudo
The sudo command allows you to run programs as another user, by default the root user
To use sudo, simply prefix the command with sudo:  
`sudo command`
___
## chown
For changing the ownership of a file/directory, you can use the following command:  
`chown user filename`  

In case you want to change the user as well as group for a file or directory use the command:  

`chown user:group filename`  
`chown :group filename` changes only group  
`chown user: filename`  changes user and group to the user default login group
___
## chgrp
In case you want to change group-owner only, use the command:  
`chgrp group_name filename`  

Tip:
- The file /etc/group contains all the groups defined in the system
- You can use the command “groups” to find all the groups you are a member of
- You can use the command newgrp to work as a member a group other than your default group
- You cannot have 2 groups owning the same file.
- You do not have nested groups in Linux. One group cannot be sub-group of other
- x- eXecuting a directory means Being allowed to “enter” a dir and gain possible access to sub-dirs
- There are other permissions that you can set on Files and Directories which will be covered in a later advanced tutorial
___
## Sources
- W. Shotts, The Linux Command Line, 2nd Edition: A Complete Introduction, No Starch Press 2019
- M. Brent, Guru99, File Permissions in Linux / Unix: How to Read, Write & Change?, https://www.guru99.com/file-permissions.html#:~:text=Linux%20divides%20the%20file%20permissions,ownership%20of%20a%20file%2Fdirectory. 
- Linuxize, Umask Command in Linux, https://linuxize.com/post/umask-command-in-linux/#
- Linuxize, Su Command in Linux (Switch User), https://linuxize.com/post/su-command-in-linux/



