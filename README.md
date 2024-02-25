
# SkywardLease 

Skywardlease is a platform designed to facilitate the rental and management of Unmanned Aerial Vehicles (UAVs), also known as drones.

## Table of Contents

- [SkywardLease](#skywardlease)
  - [Table of Contents](#table-of-contents)
  - [Quick Start](#quick-start)
- [How to install WSL on windows](#how-to-install-wsl-on-windows)
  - [Enable WSL](#enable-wsl)
  - [WSL 2](#wsl-2)
  - [Install WSL Ubuntu](#install-wsl-ubuntu)
  - [Install Docker to WSL](#install-docker-to-wsl)
  - [References](#references)



## Quick Start

Use terminal and navigate to the project root. 

- Clone the repository with the following command:

```bash
git clone https://github.com/sualpemre/skywardlease.git
```

- Then  open a command prompt, then navigate to the location where you cloned the project using the command prompt

- Then run : <code>wsl</code> on project folder location

- Note : If you don't have WSL and Docker installed on your machine, [👉 click](#how-to-install-wsl-on-windows) here to learn how to install them.



# How to install WSL on windows

## Enable WSL 
        
- Open Turn Windows features on or off and check Windows Subsystem for Linux
    ![Wsl Open](assets/wsl-1.png)

- On the first enablement of WSL, Windows will download required packages and will prompt to restart for completing the installation

## WSL 2

- Windows, by default, installs WSL 1. However, we need WSL 2 to run docker containers.

- Open elevated Powershell and run:
    <code>dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart</code>

- Then run in cmd or powershell
    <code>wsl --update</code> 

- after completed, set wsl version to 2 by running
    <code>wsl --set-default-version 2</code>

## Install WSL Ubuntu

<code>wsl --install -d ubuntu</code>
- Important: Save password that you set during the installation. For administrative commands, you will need to enter that password

- After install, it will login into ubuntu. To check the WSL version, type exit to leave WSL and run:
    <code>wsl -l -v</code>

- If you see version 2, we are good to install docker into WSL
    
    ![Wsl Shell](assets/wsl-2.png)

## Install Docker to WSL

- You can login to WSL Ubuntu by:
    <code>wsl</code>

- On the very first login, run the following for security updates:
    <code>sudo apt update && sudo apt upgrade</code>

- Important
  - To avoid any potential conflicts with using WSL 2 Docker Engine, you must uninstall any previous versions of Docker Engine and CLI installed directly  through Linux distributions or Docker Desktop.

- Install Dependencies(ignore temporary warnings/errors during installation)

    <code>sudo apt install -y \
        apt-transport-https \
        ca-certificates \
        curl \
        software-properties-common</code>

- Add Docker GPG Key
    <code>curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg</code>

- Note

  - If above command does not run and throws error as "Could not resolve host: download.docker.com", its because network connectivity issues [can happen](https://github.com/microsoft/WSL/issues?q=is%3Aissue+label%3Anetwork) with WSL 2, and tweaking the DNS settings often resolves these problems by running the following(skip if does not fail)
    <code>echo -e "[network]\ngenerateResolvConf = false" | sudo tee -a /etc/wsl.conf sudo unlink /etc/resolv.conf echo nameserver 1.1.1.1 | sudo tee /etc/resolv.conf</code>
    
- Add the Docker repository to your APT sources
    <code>echo "deb [signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null</code>

- Update the package list again
    <code>sudo apt update</code>

- Install the Docker engine
    <code>sudo apt install -y docker-ce docker-ce-cli containerd.io</code>

- when done, check the docker service status by
    <code>sudo systemctl status docker</code>
- or check the version
    <code>docker --version</code>

- Manage Docker as a Non-root User (Optional):
    <code>sudo usermod -aG docker $USER 
    newgrp docker</code>


## References

- [https://learn.microsoft.com/en-us/windows/wsl/install](https://learn.microsoft.com/en-us/windows/wsl/install)
- [https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-3---enable-virtual-machine-feature](https://learn.microsoft.com/en-us/windows/wsl/install-manual#step-3---enable-virtual-machine-feature)
- [https://dev.to/bowmanjd/install-docker-on-windows-wsl-without-docker-desktop-34m9](https://dev.to/bowmanjd/install-docker-on-windows-wsl-without-docker-desktop-34m9)
- [https://raw.githubusercontent.com/bonben365/linux/main/docker-install.sh](https://raw.githubusercontent.com/bonben365/linux/main/docker-install.sh)