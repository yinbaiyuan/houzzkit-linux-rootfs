#!/bin/bash

. $HOME/ybashrc/command-common.sh

backupDirectory()
{
    commandInput "Yes no skip" "是否备份 文件夹系统空目录结构和所有文件的权限信息？"
    result="$GLOBAL_INPUT_RESULT"
    echo ""
    case $result in
        yes ) cmdExecute "./dirbuild.sh backup"
            ;;
        no ) echoYellow "未进行备份操作！"
            exit 1
            ;;
        skip )
	    echoYellow "跳过备份操作！"
	    ;;
        * ) echoRed "命令错误！"
            exit 1
    esac

}

backupDirectory


