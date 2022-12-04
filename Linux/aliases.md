#### My aliases
TODO zrobic oddzielny plik z aliasami i skryptami
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