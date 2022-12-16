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
| top |  dynamic real-time view of a running system refreshed every 3 seconds
| pstree | Display processes in form of a tree
| vmstat | Display system resource usage information
| xload | graphic program drawing a graph of system load over time
| tload | similar to xload however, it draws a graph in the terminal
## Control Processes
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
___
## Killall
To send a signal toi many processes.  
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
| halt    |
| poweroff |
| reboot  |
| shutdown |

## Sources
- W. Shotts, The Linux Command Line, 2nd Edition: A Complete Introduction, No Starch Press 2019
- A. Kili, All You Need To Know About Processes in Linux [Comprehensive Guide], https://www.tecmint.com/linux-process-management/


