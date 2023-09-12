#!/bin/bash

### BEGIN INIT INFO
# Provides:          rongpin
# Required-Start:    
# Required-Stop:     
# Should-Stop:       
# Default-Start:     
# X-Start-Before:    
# Default-Stop:      
# Short-Description: Rongpin platform scripts
### END INIT INFO


# resize filesystem
mt_blk=$(lsblk | grep "/$" | sed 's/ .*$//g' | sed 's/^.*[^a-z0-9]//g');resize2fs /dev/$mt_blk


# defalut host mode
# echo 1 > /sys/devices/platform/usb0/dwc3_mode

BOARD=`cat /proc/device-tree/compatible`
# npu
if [[ "${BOARD}" =~ "3399pro" ]];then
	# gpu config
	ln -sf libmali-midgard-t86x-r18p0.so /usr/lib/aarch64-linux-gnu/libmali.so.1.9.0

	echo "rpdzkj, npu frimware dowload..." > /dev/console
	npu-image.sh > /dev/null
	sleep 5s 
	npu_transfer_proxy 

	#default host mode
	echo 1 > /sys/devices/platform/usb0/dwc3_mode

elif [[ "${BOARD}" =~ "rk3399" ]];then
	# gpu config
	ln -sf libmali-midgard-t86x-r14p0.so /usr/lib/aarch64-linux-gnu/libmali.so.1.9.0

	#usbmode config
	echo 1 > /sys/devices/platform/usb0/dwc3_mode

elif [[ "${BOARD}" =~ "rk1808" ]];then

	#npu driver load
	echo "rpdzkj, load npu driver..." > /dev/console
        /lib/npu_modules/rk1808/NPU_init.sh start

	#default host mode
	echo 1 > /sys/devices/platform/usb/dwc3_mode
	
	#wifi driver load
	insmod /lib/wifi_modules/rk1808/bcmdhd.ko

elif [[ "${BOARD}" =~ "rk356" ]];then
	#insmod /lib/wifi_modules/rk3568/bcmdhd.ko
	#insmod /lib/npu_modules/rk3568/rknpu.ko
	#/lib/npu_modules/rk3568/rknpu.sh &
	sleep 5 && insmod /lib/npu_modules/rk3568/rknpu.ko
	/usr/bin/restart_rknn.sh
fi



#config sound
#amixer cset numid=1 2 > /dev/null
