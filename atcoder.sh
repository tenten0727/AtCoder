#/usr/bin/bash

start_atcoder () {
    mkdir -p "$1"
    cd "$1"
    shift
    for N in "$@";do
        touch "$N.py"
    done
}

#if文の[]の空白注意！

file=()
if [ "$3" = "" ]; then
    file=("A" "B" "C" "D")
else
    for N in "${@:3}";do
        file+=($N)
    done
fi

if [ "$1" = "abc" ]; then
    start_atcoder "AtCoder Beginner Contest $2" ${file[@]}
elif [ "$1" = "arc" ]; then
    start_atcoder "AtCoder Regular Contest $2" ${file[@]}
else
    echo '第一引数が間違ってるー'
fi