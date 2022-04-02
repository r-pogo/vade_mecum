# I/O Redirections
## stdin, stdout and stderr
In computing, the term stream refers to something that can transfer data. Here, all three streams carry text as the data.
Similar to water streams, data streams also have two endpoints. There are a source and an outflow. 
Whatever command you’re running in the terminal will be at either point of the stream. Using the stream, 
you can connect two terminal windows, two different commands, and even files!

stdin: Stands for standard input. It takes text as input.
stdout: Stands for standard output. The text output of a command is stored in the stdout stream.
stderr: Stands for standard error. Whenever a command faces an error, the error message is stored in this stream.
In Linux, almost all the streams are treated as if they were files. Just like you can read/write a file, you can read/write data from these streams.

An easy way to access any file is by using the unique file descriptor number associated with it. 
In the case of these streams, there are unique values assigned to each one of them.

0: stdin  
1: stdout  
2: stderr `ls -l /bin/usr 2> ls-error.txt`  

The `>` symbol is used for output (stdout) redirection. when using > the target file is always completely overwritten.
`ls -l  /usr/bin > ls-output.txt`

Using a redirection operator without any previous command will empty the contents of an existing file or create a new empty file.
`> ls-output.txt`

To add more content to an existing file, then you should use `>>` operator.
To redirect both stdout and sterr:
`ls -l /bin/usr &> ls-outpu.txt`

Getting rid of messages use /dev/null
`ls -l /bin/usr 2> /dev/null`

The `<` symbol is used for input(stdin) redirection
___
## Pipe
The Pipe is a command in Linux that lets you use two or more commands such that output of one command serves as input to the next.  
In short, the output of each process directly as input to the next one like a pipeline. The symbol ‘|’ denotes a pipe.
`ls -l | less`

Linux has a lot of filter commands like awk, grep, sed, spell, and wc. A filter takes input from one command, 
does some processing, and gives output.

When you pipe two commands, the “filtered” output of the first command is given to the next.
`ls file | sort | less`
___
