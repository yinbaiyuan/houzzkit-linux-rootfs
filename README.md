# houzzkit-linux-rootfs

此仓库为HOUZZkit硬件项目的根文件系统构建工程，本项目目前可以构建出 Ubuntu 18.04 版本的根文件系统。

欢迎大家提交PR，让 HOUZZkit 硬件支持更多的Linux发行版。

### **注意**

>1. 不能放在虚拟机的共享文件夹中编译！
>2. SDK的编译环境建议使用 ubuntu 18.04 或更高版本。


### 构建环境依赖包

安装命令：
```bash
sudo apt-get install acl schroot qemu-user-static -y
```
若还有其他缺少的依赖包，请根据报错信息自行安装。

### 构建步骤

1. 将本仓库 clone 到本地。
2. sudo -i 进入 root 用户，以root权限执行后续操作。
3. 执行以下脚本，重建空目录并修复目录和文件权限。
    ```bash
    ./dirbuild.sh restore
    ```
4. 执行以下脚本，生成根文件系统镜像文件。
    ```bash
    ./rfsbuild.sh make
    ```
