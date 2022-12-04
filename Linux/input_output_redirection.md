# I/O Redirections
## stdin, stdout and stderr
In computing, the term stream refers to something that can transfer data. Here, all three streams carry text as the data.
Similar to water streams, data streams also have two endpoints. There are a source and an outflow. 
Whatever command you’re running in the terminal will be at either point of the stream. Using the stream, 
you can connect two terminal windows, two different commands, and even files!

`stdin`: Stands for standard input. It takes text as input.  
`stdout`: Stands for standard output. The text output of a command is stored in the stdout stream.  
`stderr`: Stands for standard error. Whenever a command faces an error, the error message is stored in this stream.  

In Linux, almost all the streams are treated as if they were files. Just like you can read/write a file, you can read/write data from these streams.

#### File descriptors (FD)
An easy way to access any file, remember everything is a file (regular files, directories, and even Devices are files!) is by using the unique file descriptor number associated with it. 
Your screen also has a File Descriptor. When a program is executed the output is sent to File Descriptor of the screen, and you see program output on your monitor.
In the case of streams, there are unique values assigned to each one of them.

| File | File Descriptor |
|------|-----------------|
| stdin | 0
| stdout | 1
| stderr | 2
___

The `>` symbol is used for output (stdout) redirection. when using > the target file is always completely overwritten.
`ls -l  /usr/bin > ls-output.txt`

Using a redirection operator without any previous command will empty the contents of an existing file or create a new empty file.
`> ls-output.txt`

To add more content to an existing file, then you should use `>>` operator.
`ls -l /usr/bin >> ls-output.txt`
If the file doesn't exists it will be created, the same happens with `>`

The `<` symbol is used for input(stdin) redirection
___
## Standard error stream redirection
Redirection is a feature in Linux which can be used to change the standard input device (e.g.keyboard) or standard output device (e.g.screen) during the execution of a command. 
The basic process of any Linux command is that it takes an input and gives output but the standard/input and output can be changed using the redirection technique. 

The redirection operator `(command > file)` only redirects standard output and hence, the standard error is still displayed on the terminal. The default standard error is the screen.
Error redirection is routing the errors to a file other than the screen.

`ls -l /bin/usr 2> ls-error.txt`

To redirect both stdout and stderr:
`ls -l /bin/usr &> ls-outpu.txt`
`&>` allows to redirect stdout and stderr to file ls-outpu.txt
`&>>`allows to append stdout and stderr to file ls-outpu.txt

Getting rid of messages use /dev/null:
`ls -l /bin/usr 2> /dev/null`
`dev/null` is a system tool  called also `bit bucket` that that does not perform any operations on the input.
___
## Pipe
The Pipe is a command in Linux that lets you use two or more commands such that output of one command serves as input to the next.  
In short, the output of each process directly as input to the next one like a pipeline. The symbol ‘|’ denotes a pipe.
`ls -l | less`

Linux has a lot of filter commands like awk, grep, sed, spell, and wc. A filter takes input from one command, 
does some processing, and gives output.

When you pipe two commands, the “filtered” output of the first command is given to the next.
`ls file | sort | less`

Remember!!! `>` links a command with a file, `|` links the output of a command with the entrance of the second command.
___

## Sources
- W. Shotts, The Linux Command Line, 2nd Edition: A Complete Introduction, No Starch Press 2019
- M. Brent, Guru99, Input Output Redirection in Linux/Unix Examples, https://www.guru99.com/linux-redirection.html