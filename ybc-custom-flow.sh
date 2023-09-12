#!/bin/bash

. $HOME/ybashrc/command-common.sh

moveRootFsImg()
{
    if [ ! -f "ubuntu-rootfs.img" ];then
        echoRed "ubuntu-rootfs.img文件不存在！"
        exit 1
    fi

    if [ ! -d "../houzzkit-linux-bsp/ubuntu" ];then
        cmdExecute "mkdir -p ../houzzkit-linux-bsp/ubuntu"
    fi
    cmdExecute "mv ubuntu-rootfs.img ../houzzkit-linux-bsp/ubuntu/"
}

makeRootFs()
{
    cmdExecute "./rfsbuild.sh make"

    commandInput "Yes no" "要移动根文件系统镜像到bsp目录吗？"
    subResult="$GLOBAL_INPUT_RESULT"
    case $subResult in
        Yes ) 
            moveRootFsImg
            ;;
        no ) 
            echoYellow "未移动根文件系统镜像！"
            ;;
        * ) 
            echoRed "命令错误！"
            exit 1
    esac
}

restoreDirectory()
{
    commandInput "Yes skip cancel" "是否恢复 文件夹系统空目录结构和所有文件的权限信息？"
    result="$GLOBAL_INPUT_RESULT"
    case $result in
        Yes ) 
            cmdExecute "./dirbuild.sh restore"
            makeRootFs
            ;;
        skip ) 
            echoYellow "跳过恢复操作！"
            makeRootFs
            ;;
        skip ) 
            echoYellow "操作退出！"
            exit 1
            ;;
        * ) 
            echoRed "命令错误！"
            exit 1
    esac
}


customFlowStart()
{
    commandInput "Make chroot move" "请输入命令" "创建根文件系统镜像 进入根文件系统 移动根文件系统镜像"
    result="$GLOBAL_INPUT_RESULT"
    echo ""
    case $result in
        Make ) 
            restoreDirectory
            ;;
        chroot ) 
            cmdExecute "./rfsbuild.sh chroot"
            cmdExecute "./rfsbuild.sh exit"
            ;;
        move )
            moveRootFsImg
            ;;
        * ) 
            echoRed "命令错误！"
            exit 1
    esac
}

buildAction()
{
    cmdExecute "./dirbuild.sh restore"
	cmdExecute "./rfsbuild.sh make"
}

cpToBspAction()
{
    moveRootFsImg
}

main() 
{
    commandArr="build cpToBsp manual"
    commandDesc="生成根文件系统镜像 移动根文件系统镜像到bsp目录 手动操作"
    inputQuestion="请输入流程名称"
    command=""
    if [ -z $1 ];then  
        commandInput "$commandArr" "$inputQuestion" "$commandDesc"
        command="$GLOBAL_INPUT_RESULT"
    else
        command=${1,,}
    fi
    case $command in
        build ) 
            buildAction
            ;;
        cptobsp ) 
            cpToBspAction
            ;;
        manual ) 
            customFlowStart
            ;;
        * ) 
            echoRed "[ERROR] 流程名称错误!"
            exit 1
    esac
}

main $@