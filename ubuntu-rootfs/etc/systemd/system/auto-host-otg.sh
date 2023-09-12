#!/bin/bash

otgMode()
{
        echo otg > /sys/devices/platform/fe8a0000.usb2-phy/otg_mode
	echo 5 > /sys/class/gpio/export
	echo out > /sys/class/gpio/gpio5/direction
	echo 0 > /sys/class/gpio/gpio5/value
	echo 5 > /sys/class/gpio/unexport
}

hostMode()
{
        echo host > /sys/devices/platform/fe8a0000.usb2-phy/otg_mode
        echo 5 > /sys/class/gpio/export
        echo out > /sys/class/gpio/gpio5/direction
        echo 1 > /sys/class/gpio/gpio5/value
        echo 5 > /sys/class/gpio/unexport

}

main()
{
        if [ $1 == "otg" ];then
                otgMode "$2"
                #do_mount
        elif [ $1 == "host" ];then
                hostMode "$2"
        fi
}

main $1 $2

