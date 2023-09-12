#!/bin/sh

case "$1" in
	start)
		printf "insmod NPU modules: "
		cp /usr/lib/npu_modules/rk1808/cl_*.h /tmp/
		insmod /lib/npu_modules/rk1808/galcore.ko contiguousSize=0x400000 gpuProfiler=1
		unset MAX_FREQ
		read  MAX_FREQ < /sys/class/devfreq/ffbc0000.npu/max_freq
		echo  $MAX_FREQ > /sys/class/devfreq/ffbc0000.npu/userspace/set_freq
		[ $? = 0 ] && echo "OK" || echo "FAIL"
		
		chmod 666 /dev/galcore
		ln -sf /lib/npu_modules/rk1808/librknn_runtime.so /usr/lib/librknn_runtime.so

		#start_rknn.sh 
		;;
	stop)
		;;
	restart|reload)
		$0 stop
		$0 start
		;;
	*)
		echo "Usage: $0 {start|stop|restart}"
		exit 1
esac
exit 0
