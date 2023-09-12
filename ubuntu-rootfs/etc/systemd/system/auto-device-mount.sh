#!/bin/bash

add()
{
        echo "add"
}

remove()
{
        echo "remove"
}

main()
{
        if [ $1 == "add" ];then
                add "$2"
        elif [ $1 == "remove" ];then
                remove "$2"
        fi
}

main $1 $2

