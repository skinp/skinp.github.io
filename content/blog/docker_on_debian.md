Title: Docker on Debian
Date: 2013-11-26
Slug: docker-on-debian
Summary: Installing docker (>= 0.7) on debian Wheezy

I wanted to reinstall my inactive KVM VPS for quite some time and I thought it would be great if I could get some support for lightweight "virtual" containers to ease my development workflow. At first, I had a couple problems:

* Ubuntu 12.04 (in fact, almost all recent 64 bits Ubuntu version) wasn't properly installing (The installer hanged during hardware discovery)
* Docker was mostly Ubuntu only (well for easy install at least)
* I had some trouble setting up simple lxc on Debian (There's some documented issues on templates)

So I was happy today when I saw [the announcement of the new 0.7 version of Docker](http://blog.docker.io/2013/11/docker-0-7-docker-now-runs-on-any-linux-distribution/) which adds Standard Linux Support.

Here's how I easily got it working:

    :::bash
    # We'll do this stuff as root...
    sudo -i

    # Install dependencies
    apt-get install lxc bridge-utils

    # Cgroup support
    echo 'cgroup    /sys/fs/cgroup  cgroup  defaults    0   0' > /etc/fstab
    mount -a

    # IP forwarding
    echo 'net.ipv4.ip_forward = 1' > /etc/sysctl.conf
    sysctl -p /etc/sysctl.conf

    # Download and install (in /usr/local/bin) docker
    wget http://get.docker.io/builds/Linux/x86_64/docker-latest.tgz
    tar -xf docker-latest.tgz -C /

    # Start and test...
    docker -d &
    docker run -i -t ubuntu /bin/bash

After some light testing, it works quite well for basic usage. I haven't tested any port forwarding and front facing services yet... next step.

Obviously, this has to be automated in some better way so I plan to write an [Ansible](https://github.com/ansible/ansible) playbook for it.
