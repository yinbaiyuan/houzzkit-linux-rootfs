#!/bin/bash

MOUNT_ROOT="/media/"
DEVICE="$2"
FP_DEVICE="/dev/$2"
MOUNT_POINT=$(mount | grep ${FP_DEVICE} | awk '{ print $3}')

mountAction()
{
	if [[ -n "${MOUNT_POINT}" ]];then
		echo "[WARNING] ${FP_DEVICE} is already mounted at ${MOUNT_POINT}."
		exit 0
	fi

        devLabel=$(lsblk $FP_DEVICE -lno LABEL)
	if [[ -z "${devLabel}" ]];then
		devLabel=$DEVICE
	fi

        fsType=$(lsblk $FP_DEVICE -lno FSTYPE)
	

        if [ -z "$fsType" ];then
		echo "[ERROR] File system format type is null."
               	exit 0
        fi
	
	MOUNT_POINT="/media/${devLabel}"
	OPTS="rw,relatime,users"

	if [ ! -d "${MOUNT_POINT}" ];then
                mkdir -p "${MOUNT_POINT}"
        fi
	
	if ! mount -o "${OPTS}" ${FP_DEVICE} "${MOUNT_POINT}"; then
		echo "[FAILED] Mounting ${FP_DEVICE} failed. (errcode = $?)"
		rmdir "${MOUNT_POINT}"
		exit 0
	fi
        echo "[OK] Mount to ${MOUNT_POINT} successfully."
}

umountAction()
{
	if [[ -z ${MOUNT_POINT} ]]; then
		echo "[WARNING] ${FP_DEVICE} is not mounted."
		exit 0
	fi

	if ! umount -l ${MOUNT_POINT};then
		echo "[FAILED] Umounting ${MOUNT_POINT} failed.(errcode = $?)"
	fi
	rmdir ${MOUNT_POINT}
	echo "[OK] Umount from ${MOUNT_POINT} successfully."
}

main()
{
	case $1 in
		add )
		    	mountAction "$2"	
		    	;;
		remove )
			umountAction "$2"
		    	;;
		* )
		    	exit 1
	esac
}

main $1 $2

