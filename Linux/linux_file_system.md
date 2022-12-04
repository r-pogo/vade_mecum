## Linux file system

| Directory | Explanation |
|--------------|--------|
| / | root directory
| /bin | Contains binaries essential for the OS
| /sbin | Essential executables for super user (root)
| /lib | Shared codes between binaries
| /boot | Files needed to boot the system like the Linux kernel itself
| /dev | Device files to interact with hardware or drivers 
| /etc | Config files + shell scripts that start system services at boot time
| /home | Home directory for the end user
| /lost+found | this directory contains any formatted partition or device that uses the linux filesystem. This directory is used for partial recovery in case of file system corruption
| /media | This directory contains subdirectories which are used as mount points for removeable media such as floppy disks, cdroms and zip disks
| /mnt | This is a generic mount point under which you mount your filesystems or devices. Mounting is the process by which you make a filesystem available to the system.
| /opt | For installing optional software 
| /proc | A virtual filesystem maintained by the Linux kernel, those "files" are created in memory to keep track of the processes
| /tmp | Temporary files that want be persistent between reboots
| /usr | Programs used by the end user
| /usr/bin | Contains non-essential binaries for the OS and intended for the end user.
| /usr/lib | Shared libraries for programs in the directory /usr/bin
| /usr/local | Contains system-wide executables not included in the distribution. Programs compiled from the source are usually installed in /usr/local/bin. On a newly installed Linux system this directory tree exists, but is empty until the system administrator puts some program in it. All the binaries get mapped together with `$PATH` variable
| /usr/sbin | This directory contains program binaries for system administration which are not essential for the boot process
| /usr/share | contains all shared data used by programs in the /usr/sbin directory 
| /usr/share/doc | documentation files collected into packages
| /var | Variable files that will change as the OS is being used. e.g.: user email, data bases ecc.
| /var/log | Contains log files recording various system activities. Important are `var/log/messages` and `var/log/syslog`
___
## Sources
- W. Shotts, The Linux Command Line, 2nd Edition: A Complete Introduction, No Starch Press 2019
