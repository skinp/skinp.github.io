Title: No questions asked Ubuntu install
Date: 2013-12-13
Slug: auto-install-ubuntu
Summary: Automatically installing Ubuntu with a preseed file

Still in the process of correctly provisioning and configuring my Homelab and VPS with [Ansible](http://www.ansibleworks.com/), I ended up having to often reinstall servers just to make sure my playbooks were still working after a lot of edit+deploy iterations. I was really tired of having to log into the VNC console of my VPS providers and manually run through the whole ISO setup.

So today I decided I would take a break from coding Ansible playbooks and try to automate the provisioning of these servers ALA Kickstart... The goal:

__NO QUESTIONS ASKED__

So after a couple of iterations (again!!!), here is my preseed.cfg tested on [Ubuntu 12.04 LTS x86_64](http://www.ubuntu.com/download/server):

    ## Options to set on the command line
    d-i debian-installer/locale string en_US
    d-i console-setup/ask_detect boolean false
    d-i console-setup/layoutcode string us
    d-i keyboard-configuration/layoutcode string us
    d-i netcfg/get_hostname string unassigned-hostname
    d-i netcfg/get_domain string unassigned-domain

    ## Network config
    d-i netcfg/choose_interface select auto
    d-i netcfg/dhcp_timeout string 60

    ## Kernel
    d-i base-installer/kernel/override-image string linux-server

    ## Clock
    d-i clock-setup/utc-auto boolean true
    d-i clock-setup/utc boolean true
    d-i time/zone string US/Eastern
    d-i clock-setup/ntp boolean true

    ## Mirrors
    d-i mirror/country string US
    d-i mirror/http/proxy string
    d-i mirror/protocol string http
    d-i mirror/http/mirror select us.archive.ubuntu.com

    ## Partitions
    d-i partman-auto/method string lvm
    d-i partman-auto/purge_lvm_from_device boolean true
    d-i partman-auto/choose_recipe select atomic
    d-i partman/default_filesystem string ext4

    d-i partman-auto-lvm/guided_size string max
    d-i partman-lvm/device_remove_lvm boolean true
    d-i partman-lvm/confirm boolean true

    d-i partman/choose_partition select finish
    d-i partman/confirm_write_new_label boolean true
    d-i partman/confirm boolean true

    ## User accounts
    d-i passwd/root-login boolean false
    d-i passwd/user-fullname string ubuntu
    d-i passwd/username string ubuntu
    d-i passwd/user-uid string 1000
    d-i passwd/user-password password change_me_please
    d-i passwd/user-password-again password change_me_please
    d-i user-setup/allow-password-weak boolean true
    d-i user-setup/encrypt-home boolean false

    ## Packages to install
    tasksel tasksel/first multiselect standard, ubuntu-server
    d-i pkgsel/install-language-support boolean false
    d-i pkgsel/include string openssh-server

    ## Install security updates automatically
    d-i pkgsel/update-policy select unattended-upgrades

    ## Grub setup
    d-i grub-installer/only_debian boolean true
    d-i grub-installer/with_other_os boolean true

    ## Avoid that last message about the install being complete.
    d-i finish-install/reboot_in_progress note

You can view the meaning of all these statements [here](https://help.ubuntu.com/lts/installation-guide/i386/preseed-contents.html).

Unfortunatly, this process still isn't fully automated. Since the network setup only happens after some questions are asked (notably language and keyboard layout), we have to give some additionnal parameters to the boot prompt (__After the CD boots, select the language then F6__). The boot line should look like the following (all on one line):

    url=http://webserver.domain/path/preseed.cfg \
    debian-installer/locale=en_US \
    console-setup/ask_detect=false \
    console-setup/layoutcode=us \
    keyboard-configuration/layoutcode=us \
    netcfg/choose_interface=auto \
    hostname=YOURHOSTNAME \
    domain=YOURDOMAINE \
    initrd=/install/initrd.gz quiet --

In my opinion, it's still a lot better than having to go through the whole setup. Especially now that I can add some additionnal configuration (installed packages, user groups...) at provision time!
