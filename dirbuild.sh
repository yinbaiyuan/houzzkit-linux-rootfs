#!/bin/bash

backup()
{
	find ./ubuntu-rootfs/ -type d -empty > emptydirlist.txt
	getfacl -R ./ubuntu-rootfs > permission.txt

}

restore()
{
	for line in $(cat emptydirlist.txt)
	do
		mkdir -p $line
	done
	cp permission.txt ubuntu-rootfs/
	setfacl --restore=permission.txt
	rm ubuntu-rootfs/permission.txt
}

if [ "$1" == "backup" ]
then
	backup
elif [ "$1" == "restore" ]
then
	restore
else
	echo ""
	echo "Parameters were missing"
	echo "1'st parameter can be one of these: backup , restore "
	echo "backup   --Create empty directory list file and acl permission file"
	echo "restore  --Restore empty directory list file and acl permission file"
fi
