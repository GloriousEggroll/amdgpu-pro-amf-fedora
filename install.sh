#!/bin/sh

OSVERSION=$(cat /etc/os-release | grep VERSION_ID | cut -d "=" -f 2)


sudo dnf -y install mock pykickstart fedpkg

# download AMD's AMDF libraries
if [ ! -f "amf-amdgpu-pro_1.4.24-1384496_amd64.deb" ]; then
wget --referer https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux-21-50 -N http://repo.radeon.com/amdgpu/21.50.2/ubuntu/pool/proprietary/a/amf-amdgpu-pro/amf-amdgpu-pro_1.4.24-1384496_amd64.deb
fi

if [ ! -f "libamdenc-amdgpu-pro_1.0-1384496_amd64.deb" ]; then
wget --referer https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux-21-50 -N http://repo.radeon.com/amdgpu/21.50.2/ubuntu/pool/proprietary/liba/libamdenc-amdgpu-pro/libamdenc-amdgpu-pro_1.0-1384496_amd64.deb
fi

# create a fedora srpm from the spec sheet
fedpkg --release f$OSVERSION srpm

# add current user to 'mock' build group
sudo usermod -a -G mock $USER

# turn selinux off if it's enabled
sudo setenforce 0

# build the package
mock -r /etc/mock/fedora-$OSVERSION-x86_64.cfg --rebuild amdgpu-pro-amf*.src.rpm
sudo mv /var/lib/mock/fedora-$OSVERSION-x86_64/result/* .

# re-enable selinux if needed
sudo setenforce 1

# install the package
sudo dnf -y --nogpgcheck install amdgpu-pro-amf-*.x86_64.rpm

# cleanup
rm *.log
mock -r /etc/mock/fedora-$OSVERSION-x86_64.cfg --scrub=all
