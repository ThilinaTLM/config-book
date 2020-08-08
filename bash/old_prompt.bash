
# Arguments
# 1 - Text
# 2 - Foreground
# 3 - Background
# function __f() {
#     if [ $1 ]; then 
#         text=$1
#     else
#         text=""
#     fi
#     if [ $2 ]; then 
#         fg=$2
#     else
#         fg=255
#     fi
#     if [ $3 ]; then 
#         bg=$3
#     else
#         bg=0
#     fi
#     echo "$(tput setaf $fg)$(tput setab $bg)${text}$(tput setaf 255)$(tput setab 0)"
# }


# function __isGit() {
#     if [ -d .git ]; then
#         echo 1
#     else
#         echo 0
#     fi
# }

# function __gitBranch() {
#     local BG=56
#     local FG=255
#     if [ $(__isGit) -eq 1 ]; then
#         echo "$(__f " $(echo -e \\uf322) " $FG $BG)$(__f "$(git branch --show-current) " $FG $BG)"
#     else
#         echo ""
#     fi
# }

# HOSTNAME="$(__f " TLM " 255 1)"

# PS1="${HOSTNAME}$(__gitBranch)"
# echo $PS1


function _GIT() {
    local isgit=$(git rev-parse --is-inside-work-tree)
    if [ $? == 0 ]
    then
        echo -ne "$(tput setaf 255)$(tput setab 166)"
        echo -ne -e " \uf322 "
        echo -ne "$(git branch --show-current) "
        echo -ne "$(tput sgr0)"
    else
        echo " "
    fi
}

function _PROMPT() {
    echo -ne "$(tput setaf 1)"
    echo -ne -e "\n\u2cb6 "
    #echo -ne -e "\n\ue285 "
    echo -ne "$(tput sgr0)"
}

function _CDIR() {
    echo -ne "$(tput setaf 26)"
    echo -ne -e "\w"
    #echo -ne -e "\n\ue285 "
    echo -ne "$(tput sgr0)"
}

_USER="$(setc 226)TLM"
_PSIGN="$(echo -ne -e \\u2cb6)"

export PS1="$_PSIGN $(_CDIR) $(_GIT)$(_PROMPT)$(tput sgr0)"