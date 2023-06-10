# Data carriers
| Command | Action |
|---------|--------|
| mount | mounts the file system
| umount | detaches (unmounts) the mounted file system
| fsck | checks and repairs the file system
| fdisk |
| mkfs |
| dd |
| genisoimage (mkisofs) |
| wodim (cdrecord) |
| md5sum |
___
## Mounting and unmounting storage devices
Mounting is a process that enables the device to be included in the operating system.
The devices, usually hard disk partitions, to be mounted at boot time are stored in a file called `/etc/fstab` short for file system table.
___
### Listing Mounted File Systems
When used without any argument, the mount command will display all currently attached file systems:
```
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶mount
/dev/sdb on / type ext4 (rw,relatime,discard,errors=remount-ro,data=ordered)
tmpfs on /mnt/wsl type tmpfs (rw,relatime)
tools on /init type 9p (ro,relatime,dirsync,aname=tools;fmask=022,loose,access=client,trans=fd,rfd=6,wfd=6)
none on /dev type devtmpfs (rw,nosuid,relatime,size=3187928k,nr_inodes=796982,mode=755)
sysfs on /sys type sysfs (rw,nosuid,nodev,noexec,noatime)
proc on /proc type proc (rw,nosuid,nodev,noexec,noatime)
...
```
The list format is `device name` (e.g: /dev/sdb) on `directory type `(e.g: /) of 
`filesystem type` (e.g: ext4 (rw,relatime,discard,errors=remount-ro,data=ordered))  
To display only certain file systems use the -t option:
`mount -t ext4`
___
### Mounting a File System
To mount a file system in a given location (mount point), use the mount command in the following form:
`mount [OPTION...] DEVICE_NAME DIRECTORY`  
For example, to mount the /dev/sdb1 file system to the /mnt/media directory you would use:  
`sudo mount /dev/sdb1 /mnt/media`  
Use the -t option to specify the file system type:
`mount -t TYPE DEVICE_NAME DIRECTORY`
Use the -o option for additional options (provided as a comma-separated list, no space after a comma):
`mount -o OPTIONS DEVICE_NAME DIRECTORY`

Example:
```
# Create new mount point
mkdir /mnt/cdrom

# Mounting CD-ROM in the new point
mount -t iso9660 /dev/sdc /mnt/cdrom
```
___
### Checking the name of the device
/dev directory is the root folder that contains all devices files:

| Path Pattern | Device |
|---------|--------|
| /dev/fd* | floppy drives
| /dev/hd* | ?
| /dev/lp* | printers
| /dev/sd* | hard disk ?
| /dev/sr* | CD/DVD readers and writers

If our system does not automatically mount removable devices, 
we can determine the name of the device when connected using the following technique:

1. previewing the file: `/var/log/messages` or `/var/log/syslog`
`sudo tail -f /var/log/messages`
2. Now connect your device


### Mounting a File System using /etc/fstab 
When providing just one parameter (either directory or device) to the mount command, it will read the content of the /etc/fstab configuration file to check whether the specified file system is listed or not

If the /etc/fstab contains information about the given file system, the mount command uses the value for the other parameter and the mount options specified in the fstab file.

The /etc/fstab file contains a list of entries in the following form:
[File System] [Mount Point] [File System Type] [Options] [Dump] [Pass]
SKONCZYC Z  KSIAZKA

### Mounting USB Drive
Create the mount point:
sudo mkdir -p /media/usb

Assuming that the USB drive uses the /dev/sdd1 device you can mount it to /media/usb directory by typing:
sudo mount /dev/sdd1 /media/usb

To find the device and filesystem type, you can use any of the following commands:
fdisk -l
ls -l /dev/disk/by-id/usb*
dmesg
lsblk

To mount exFAT formatted USB drives, install the free FUSE exFAT module and tools .

### Mounting ISO Files

You can mount an ISO file using the loop device which is a special pseudo-device that makes a file accessible as a block device.

Start by creating the mount point, it can be any location you want:

sudo mkdir /media/iso
Copy
Mount the ISO file to the mount point by typing the following command:

sudo mount /path/to/image.iso /media/iso -o loop
Copy
Don’t forget to replace /path/to/image.iso with the path to your ISO file.

### Mounting NFS
To mount an NFS share you’ll need to have the NFS client package installed on your system.

Install NFS client on Ubuntu and Debian:

sudo apt install nfs-common
Copy
Install NFS client on CentOS and Fedora:

sudo yum install nfs-utils
Copy
Use the steps below to mount a remote NFS directory on your system:

Create a directory to serve as the mount point for the remote filesystem:

sudo mkdir /media/nfs
Copy
Generally, you will want to mount the remote NFS share automatically at boot. To do so open the /etc/fstab file with your text editor :

sudo nano /etc/fstab
Copy
Add the following line to the file, replacing remote.server:/dir with the NFS server IP address or hostname and the exported directory:

/etc/fstab
# <file system>    <dir>       <type>   <options>   <dump>	<pass>
remote.server:/dir /media/nfs  nfs      defaults    0       0
Copy
Mount the NFS share by running the following command:

sudo mount /media/nfs
Copy
### Unmounting a File System
To detach a mounted file system, use the umount command followed by either the directory where it has been mounted (mount point) or the device name:

umount DIRECTORY
umount DEVICE_NAME
CopyCopy
If the file system is in use the umount command will fail to detach the file system. In those situations, you can use the fuser command to find out which processes are accessing the file system:

fuser -m DIRECTORY
Copy
Once you determine the processes you can stop them and unmount the file system.

Lazy unmount
Use the -l (--lazy) option to unmount a busy file system as soon as it is not busy anymore.

umount -l DIRECTORY
Copy
Force unmount
Use the -f (--force) option to force an unmount. This option is usually used to unmount an unreachable NFS system.

umount -f DIRECTORY
Copy
Generally not a good idea to force unmount as it may corrupt the data on the file system.


https://linuxize.com/post/how-to-mount-and-unmount-file-systems-in-linux/


