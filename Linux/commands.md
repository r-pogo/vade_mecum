# Commands
What are commands?
- executable program: like all files in /usr/bin. Programs in form of compiled binary code
- built-in command in the shell itself: like `cd`
- shell functions: Miniature scripts included in the environment
- aliases: a command that you can define yourself on the basis of other commands
## Navigation
| Abbreviation | Effect |
|--------------|--------|
| pwd | Print the name of the current working directory.
| cd | Change the working directory. Just `cd` changes to home dir.`cd -` goeas to the previous dir. `cd ~user` changes to home dir of a specific user.
| j foo | autojump is a faster way to navigate your filesystem. It works by maintaining a database of the directories you use the most from the command line. link for gihub https://github.com/wting/autojump. Need to add `. /usr/share/autojump/autojump.sh` to your bashrc file.  
____
## System overview
| Abbreviation | Effect |
|--------------|--------|
| ls | List information about the files. cool aliases: `ll='ls -alF'`; `la='ls -A'`; `l='ls -CF'`
| file | Determine type of FILEs. In linux the filenames do not necessarily reflect the contents!
| fzf | It's an interactive Unix filter for command-line that can be used with any list; files, command history, processes, hostnames, bookmarks, git commits, etc. https://github.com/junegunn/fzf
| less | displays the contents of a file or a command output, one page at a time

#### Less commands
| Command | Action |
|---------|--------|
| PAGE UP or b | One page up
| PAGE DOWN or space bar | One page down
| Arrow up | One line up
| Arrow down | One line down
| G | End of the file
| 1G or g | Beginning of the file
| /symbol | Looks for the next `symbol`
| n | looks for the next occurrence of the previous occurrence
| h | help
| q | quit less
___
## Manipulating files and directories
| Abbreviation | Effect |
|--------------|--------|
| cp | Copies files and directories to another location.
| mv | Move and rename files and directories. mv item1 item2, if item2 doesn't exists item1 will be renamed as item2, if item2 exist item1 will be moved to item2   
| mkdir | Make new directories. mkdir dir1 dir2 dir3 makes 3 directories
| rm | Remove files and directories. No going back, if using wildcards good idea is first to test it with `ls` instead of `rm`
| ln | Creating links between files. By default, the ln command creates hard links. To create a symbolic link, use the -s (--symbolic) option

#### Links
`Hard links`: You can think a hard link as an additional name for an existing file. 
Hard links are associating two or more file names with the same inode. 
You can create one or more hard links for a single file. 
Hard links cannot be created for directories and files on a different filesystem or partition.  

`Soft or symbolic links`: A soft link is something like a shortcut in Windows. It is an indirect pointer to a file or directory. 
Unlike a hard link, a symbolic link can point to a file or a directory on a different filesystem or partition.

`ln -s [OPTIONS] FILE LINK`  

If both the FILE and LINK are given, ln will create a link from the file specified as the first argument (FILE) to the file specified as the second argument (LINK).  

If only one file is given as an argument or the second argument is a dot (.), ln will create a link to that file in the current working directory.
The name of the symlink will be the same as the name of the file it points to.

`ln -s source_file symbolic_link` or directories `ln -s /mnt/my_drive/mydir ~/my_dir`

Replace source_file with the name of the existing file for which you want to create the symbolic link and symbolic_link 
with the name of the symbolic link.  

The symbolic_link parameter is optional. If you do not specify the symbolic link, the ln command will create a new link in your current directory.

To overwrite the destination path of the symlink, use the -f (--force) option.
`ln -sf my_file.txt my_link.txt`

To delete/remove symbolic links use either the unlink or rm command.
`unlink symlink_to_remove` or `rm symlink_to_remove`

No matter which command you use, when removing a symbolic link not append the / trailing slash at the end of its name.
If you delete or move the source file to a different location, the symbolic file will be left dangling (broken) and should be removed.

#### Wildcards
| Wildcard | Meaning |
|--------------|--------|
| * | any character
| ? | any single character
| [characters] | groups
| [!characters] | negation of group
| [[:alnum:]] | alphanumeric char
| [[:alpha:]] | letters
| [[:digit:]] | numbers
| [[:lower:]] | lower case letters
| [[:upper:]] | upper case letters

Examples

| Template | Matches |
|----------|--------|
| * | all files
| g* | any file starting with g
| b*.txt | files that starts with b then any char and end with.txt
| Data???| files with Data and 3 characters
| [abc]* | any file that stars with either a or b or c
|backup.[0-9][0-9][0-9] | backup. and ther numbers from 0 to 9
| [[:upper]] | any file starting with upper case 
| [![:digit]] | files that don't start with numbers
| *[[:lower]123] | any file that ends with alower case letter or 1,2,3
#### Example of cp
| Command | Action |
|---------|--------|
| cp file1 file2 | Copies file one to file2, if file2 doesn't exists it will be created 
| cp -i file1 file2 | If file2 exists the user will be asked if he is sure about overwriting it
| cp file1 file2 dir1 | Copies file1 and fil2 to dir1. dir1 must already exists
| cp dir1/* dir2 | All files from dir1 copied to dir2. dir2 must exists
| cp -r dir 1 dir2 | dir1 copied to dir2. If dir2 doesn't exists it will be created same as dir1

## Getting information
| Abbreviation | Effect |
|--------------|--------|
| type | Display information about command type.
| which | Linux which command is used to identify the location of a given executable that is executed when you type the executable name (command) in the terminal prompt. The command searches for the executable specified as an argument in the directories listed in the PATH environment variable
| help |  Display information about builtin commands.
| man | Used to display the user manual of any executable that we can run on the terminal
| apropos | apropos command helps the user when they don’t remember the exact command but knows a few keywords related to the command that define its uses or functionality. It searches the Linux man page with the help of the keyword provided by the user to find the command and its functions
| whatis | Used to get a one-line manual page descriptions
| info | Reads documentation in the info format. It will give detailed information for a command when compared with the man page
| alias | displays a list of all aliases

#### My aliases
````
alias st='git status'
alias co='git checkout'
alias ci='git commit'
alias br='git branch'
alias df='git diff'
alias dfc='git diff --color-words'
alias ..='cd ..'
alias ..2='cd ../..'
alias ..3='cd ../../../'
alias ..4='cd ../../../../'
alias ..5='cd ../../../../..'
alias bf='git checkout $(git branch | fzf)'
alias pf="fzf --preview='less {}' --bind shift-up:preview-page-up,shift-down:preview-page-down"
````
SKOCZYC liste!!!
____
## I/O commands
| Abbreviation | Effect |
|--------------|--------|
| cat | The cat (short for “concatenate“). cat command allows us to create single or multiple files, view content of a file, concatenate files and redirect output in terminal or files.
| uniq | The uniq command in Linux is a command-line utility that reports or filters out the repeated lines in a file. In simple words, uniq is the tool that helps to detect the adjacent duplicate lines and also deletes the duplicate lines. uniq filters out the adjacent matching lines from the input file(that is required as an argument) and writes the filtered data to the output file.
| wc | word count
| grep | allows to search patterns in files
| head(tail) | beginnig and ending of a file
| tee | tee command reads the standard input and writes it to both the standard output and one or more files. The command is named after the T-splitter used in plumbing. It basically breaks the output of a program so that it can be both displayed and saved in a file. It does both the tasks simultaneously, copies the result into the specified files or variables and also display the result
