# Processes
Process is a running instance of a program.  
Types of processes:
- `Foreground processes` (also known as interactive processes): executed or initiated by the user. Thy aren't initialized by system services
- `Background processes` (also known as non-interactive/automatic processes): are processes not connected to a terminal. They don’t expect any user input. 
- `Daemons`:special types of background processes that start at system startup and keep running forever as a service.  
They are started as system tasks, spontaneously. They can be controlled by a user via the init process.
___
## PID - process ID
In Linux different users can run various programs on the system, each running instance of a program must be identified uniquely by the kernel.
PID identifies each program and  it's parent processes ID (PPID).
- `Parent process`: processes that create other processes during run-time
- `Child processes`: processes created by other processes during run-time

`Init` process is the mother of all processes on the system. It’s the first program that is executed when the Linux system boots up.  
It manages all other processes on the system. It is started by the kernel itself, so in principle it does not have a parent process.  
The `init` process has always an ID of 1.
___
## How to View Processes
| Command | Action |
|---------|--------|
| ps | displays information about a selection of the active processes on the system
| top | dynamic real-time view of a running system refreshed every 3 seconds
| jobs | list all jobs on the system; active, stopped, or otherwise
| pstree | display processes in form of a tree
| vmstat | display system resource usage information
| xload | graphic program drawing a graph of system load over time
| tload | similar to xload however, it draws a graph in the terminal

### ps
```
$ ▶ps
  PID TTY          TIME CMD
   10 pts/0    00:00:00 bash
   83 pts/0    00:00:00 ps
```

`TTY` is short for “Teletype,” and refers to the controlling terminal for the process
`TIME` field is the amount of CPU time consumed by the process.

```
$ ▶ps x
  PID TTY      STAT   TIME COMMAND
   10 pts/0    Ss     0:00 -bash
   91 pts/0    R+     0:00 ps x
```
`x`  option (note that there is no leading dash) tells ps to show all of our processes regardless of what terminal (if any) they are controlled by
`STAT` is short for “state” and reveals the current status of the process:

| State | Meaning |
|-------|---------|
| R | Running. This means that the process is running or ready to run.
| S | Sleeping. The process is not running; rather, it is waiting for an event, such as a keystroke or network packet.
| D | Uninterruptible Sleep. Process is waiting for I/O such as a disk drive.
| T | Stopped. Process has been instructed to stop. More on this later.
| Z | A defunct or “zombie” process. This is a child process that has terminated, but has not been cleaned up by its parent.
| < | A high priority process. It's possible to grant more importance to a process, giving it more time on the CPU. This property of a process is called niceness. A process with high priority is said to be less nice because it's taking more of the CPU's time, which leaves less for everybody else.
| N | A low priority process. A process with low priority (a “nice” process) will only get processor time after other processes with higher priority have been serviced.

```
$ ▶ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         1  0.0  0.0    908   536 ?        Sl   13:19   0:00 /init
root         8  0.0  0.0    908    84 ?        Ss   13:19   0:00 /init
root         9  0.0  0.0    908    84 ?        S    13:19   0:00 /init
elski       10  0.0  0.0  10188  5064 pts/0    Ss   13:19   0:00 -bash
elski       99  0.0  0.0  10616  3300 pts/0    R+   13:24   0:00 ps aux
```
`aux` This set of options displays the processes belonging to every user.

BSD style ps column headers:

| Header | Meaning |
|--------|---------|
| USER | User ID. This is the owner of the process.
| %CPU | CPU usage in percent.
| %MEM | Memory usage in percent.
| VSZ | Virtual memory size.
| RSS | Resident Set Size. The amount of physical memory (RAM) the process is using in kilobytes.
| START | Time when the process started. For values over 24 hours, a date is used.

### top
The `top` program displays a continuously updating (by default, every 3 seconds) display 
of the system processes listed in order of process activity. The name “top” comes from 
the fact that the top program is used to see the “top” processes on the system. The top 
display consists of two parts: a system summary at the top of the display, followed by a 
table of processes sorted by CPU activity:

```
$ ▶top
 top - 14:59:20 up  6:30,  2 users,  load average: 0.07, 0.02, 0.00
 Tasks: 109 total,   1 running, 106 sleeping,   0 stopped,   2 zombie
 Cpu(s):  0.7%us,  1.0%sy,  0.0%ni, 98.3%id,  0.0%wa,  0.0%hi,  0.0%si
 Mem:    319496k total,   314860k used,     4636k free,    19392k buff
 Swap:   875500k total,   149128k used,   726372k free,   114676k cach
  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
 6244 me        39  19 31752 3124 2188 S  6.3  1.0  16:24.42 trackerd
 11071 me        20   0  2304 1092  840 R  1.3  0.3   0:00.14 top
 6180 me        20   0  2700 1100  772 S  0.7  0.3   0:03.66 dbus-dae
 6321 me        20   0 20944 7248 6560 S  0.7  2.3   2:51.38 multiloa
 4955 root      20   0  104m 9668 5776 S  0.3  3.0   2:19.39 Xorg
    1 root      20   0  2976  528  476 S  0.0  0.2   0:03.14 init
    2 root      15  -5     0    0    0 S  0.0  0.0   0:00.00 kthreadd
    3 root      RT  -5     0    0    0 S  0.0  0.0   0:00.00 migratio
    4 root      15  -5     0    0    0 S  0.0  0.0   0:00.72 ksoftirq
    5 root      RT  -5     0    0    0 S  0.0  0.0   0:00.04 watchdog
    6 root      15  -5     0    0    0 S  0.0  0.0   0:00.42 events/0
    7 root      15  -5     0    0    0 S  0.0  0.0   0:00.06 khelper
   41 root      15  -5     0    0    0 S  0.0  0.0   0:01.08 kblockd/
   67 root      15  -5     0    0    0 S  0.0  0.0   0:00.00 kseriod
  114 root      20   0     0    0    0 S  0.0  0.0   0:01.62 pdflush
  116 root      15  -5     0    0    0 S  0.0  0.0   0:02.44 kswapd0
```

| Row | Field | Meaning |
|-----|-------|---------|
| 1 | top | Name of program
| | 13:28:24 |  Current time of day
| | up 9 min |  This is called uptime. It is the amount of time since the machine was last booted. 
| | 0 users | There are 0 users logged in
| | load average: |  Load average refers to the number of processes  that are waiting to run, that is, the number of processes that are in a runnable state and are sharing the CPU. Three values are shown, each for a different period of time. The first is the average for the last 60 seconds, the next the previous 5 minutes, and finally the previous 15 minutes. Values under 1.0 indicate that the machine is not busy. 
| 2 |  Tasks: | This summarizes the number of processes and their various process states.
| 3 | Cpu(s): |  This row describes the character of the activities that the CPU is performing.
| | 0.7%us |  0.7% of the CPU is being used for user processes. This means processes outside of the kernel itself.
| | 1.0%sy | 1.0% of the CPU is being used for system (kernel) processes
| | 0.0%ni | 0.0% of the CPU is being used by “nice” (low priority) processes.
| | 98.3%id | 98.3% of the CPU is idle.
| |  0.0%wa | 0.0% of the CPU is waiting for I/O.
| 4 | Mem: | Shows how physical RAM is being used.
| 5 | Swap: |  Shows how swap space (virtual memory) is being used.

The `top` program accepts a number of keyboard commands. The two most interesting are 
`h`, which displays the program's help screen, and `q`, which quits top
___
## Control Processes
| Command | Action |
|---------|--------|
| bg | puts a program in the background 
| fg | brings a process back to the foreground
### Putting a process in the background
Suppose we want the prompt to return to the shell, but without stopping the process.  
To start the program and immediately put it in the background, after the command we type the ampersand sign `&`.

```
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶ someProgram &
[1] 28236  # The shell informs us that the task number is [1] and that it has a PID 28236
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶
```
The function of controlling shell tasks also allows us to display tasks launched from our terminal, with `jobs`.
``` 
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶jobs
[1]+  Running 28236                someProgram &
```
___
### Bring a process back to the foreground
Use `fg` command.
```
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶jobs
[1]+  Running 28236                someProgram &
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶fg %1  # jobspec (% + number) if in the back ground ther is only one programm jobspec is optional
```
___
### Stopping/pausing a process
Sometimes we want to stop a process without terminating it.  
For example, when we want to move the foreground process to the background. To stop the foreground process, use `Ctrl+Z`.
```
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶ someProgram
[1]+ Stopped               someProgram
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶
```
The program can be restored to the foreground, using the `fg` command, or put it in the background with the `bg` command:
``` 
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶bg %1
[1]+ someProgram &
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶
```
___
## Kill a process
| Command | Action |
|---------|--------|
| kill | "kills" the execution of a process

Most often used as:  
`kill -signal PID...`
```
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶ someProgram &
[1] 28236
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶ kill 28236  # can also use  jobspec (% + number) instead of PID number
[1]+ Terminated               someProgram
```
`kill` actually sends a signal to the process like in the cast of Ctrl+C (sends signal INT interrupt) or Ctrl+Z (sends signal TSTP Terminal stop). 
Programs have the ability to listen to those signals and react.  

Frequently used signals:

| Number | Name | Description
|---------|-----|-----------|
| 1       | HUP | Hung up. The foreground program running in the terminal will receive a signal and will terminate.
| 2       | INT | Interrupt same as Ctrl+C
| 9       | KILL | This signal is sent directly to the kernel which will stop the execution of the selected program. Should be used as last resource! 
| 15      | TERM | Terminate. Defoult signal sended by `kill`
| 18      | CONT | Continue. Resumes the program after it was stopped woth `STOP` or `TSTP`. This signal sends `fg` and `bg` commands.
| 19      | STOP | Stop. This signal causes the process to quit the action but not stop the work. Like `KILL` is sent directly to the kernel.
| 20      | TSTP | Terminal stop
| 3       | QUIT | Quit.
| 11      | SEGV | This signal is sent if the program uses the memory in an unauthorized way, i.e. when it is about to write data in a place to which it is not entitled
| 28      | WINCH | Change in window. This is the signal sent when you resize a window.

To access the full list:  
`kill -l`

```
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶ someProgram &
[1] 28236
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶ kill -1 28236
[1]+ Hnagup               someProgram

elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶ someProgram &
[1] 28236
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶ kill -INT 28236
[1]+ Interrupt               someProgram
```

List of other common signals:

| Number | Name | Meaning |
|--------|------|---------|
| 3 | QUIT | Quit.
| 11 | SEGV | Segmentation Violation. This signal is sent if a program makes illegal use of memory, that is, it tried to write somewhere it was not allowed to.
| 20 | TSTP | Terminal Stop. This is the signal sent by the terminal when the Ctrl-z key is pressed. Unlike the STOP signal, the TSTP signal is received by the program but the program may choose to ignore it.
| 28 | WINCH |  Window Change. This is a signal sent by the system when a window changes size. Some programs , like top and less will respond to this signal by redrawing themselves to fit the new window dimensions.
___
## Killall
To send a signal to many processes.  
`killall [-u user] [-signal] name...`

```
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶ someProgram &
[1] 28236

elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶ someProgram &
[1] 28240

elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶ killall someProgram
[1]- Terminated           someProgram
[2]+ Terminated           someProgram
```
___
## Shutting down the system
| Command | Action |
|---------|--------|
| halt    | instructs the hardware to stop all CPU functions
| poweroff | sends an ACPI signal which instructs the system to power down
| reboot  | instructs the system to reboot
| shutdown | shutting down or restarting

```
elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶ sudo reboot

elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶ sudo shutdown -h now # equivalent to --poweroff, overridden by --halt

elski @ DESKTOP-3T3MNOS: ~
└─ $ ▶ sudo shutdown -r now # reboot the machine
```
___
## Sources
- W. Shotts, The Linux Command Line, 2nd Edition: A Complete Introduction, No Starch Press 2019
- A. Kili, All You Need To Know About Processes in Linux [Comprehensive Guide], https://www.tecmint.com/linux-process-management/


