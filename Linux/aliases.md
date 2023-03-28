# My aliases and functions
````
alias st='git status'  
alias co='git checkout'  
alias ci='git commit'  
alias br='git branch'
alias gdf='git diff'
alias dfc='git diff --color-words'
alias pierdole='rm -rf /mnt/c/Users/r.pogorzelsk/AppData/Roaming/Bixby\ Studio/*'
alias ..='cd ..'
alias ..2='cd ../..'
alias ..3='cd ../../../'
alias ..4='cd ../../../../'
alias ..5='cd ../../../../..'
alias brf='git checkout $(git branch | fzf)'
alias brd='git branch -d $(git branch | fzf)'
alias brD='git branch -D $(git branch | fzf)'
alias cdf='cd $(ls | fzf)'
alias pf="fzf --preview='less {}' --bind shift-up:preview-page-up,shift-down:preview-page-down"
alias cbashrc="code ~/.bashrc"
alias sbashrc="source ~/.bashrc "
````
___
# Fzf bash scripts (you need to install fzf first!) 
After installation paste them  in your bashrc
````
# fda - for interactivly cd, including hidden directories
fda() {
  local dir
  dir=$(find ${1:-.} -type d 2> /dev/null | fzf +m) && cd "$dir"
}
````
````
# cf - fuzzy cd from anywhere
# ex: cf word1 word2 ... (even part of a file name)
# zsh autoload function
cf() {
  local file

  file="$(locate -Ai -0 $@ | grep -z -vE '~$' | fzf --read0 -0 -1)"

  if [[ -n $file ]]
  then
     if [[ -d $file ]]
     then
        cd -- $file
     else
        cd -- ${file:h}
     fi
  fi
}
````
````
# fd - cd to selected directory
fd() {
  local dir
  dir=$(find ${1:-.} -path '*/\.*' -prune \
                  -o -type d -print 2> /dev/null | fzf +m) && cd "$dir"
}
````
````
# fe [FUZZY PATTERN] - Open the selected file with the default editor
#   - Bypass fuzzy finder if there's only one match (--select-1)
#   - Exit if there's no match (--exit-0)
fe() {
  IFS=$'\n' files=($(fzf-tmux --query="$1" --multi --select-1 --exit-0))
  [[ -n "$files" ]] && ${EDITOR:-code} "${files[@]}"
}
````
___
# Autojump
After installation paste the following line in your bashrc
`. /usr/share/autojump/autojump.sh`