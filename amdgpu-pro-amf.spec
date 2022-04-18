# This package is inspired and partially based on the AUR package
# by Christopher Snowhill, ipha, johnnybash and grmat.
# https://aur.archlinux.org/packages/opencl-amd/

# Download the source pkg with this command:
# wget --referer https://support.amd.com/en-us/kb-articles/Pages/AMDGPU-PRO-Driver-for-Linux-Release-Notes.aspx https://drivers.amd.com/drivers/linux/amdgpu-pro-20.20-1089974-ubuntu-20.04.tar.xz

# This package creates a wrapper file "amdgporun" which is similar to "optirun"
# or "primusrun" from Bumblebee times. In short, it enables the proprietary
# amdgpu-pro OpenCL stack on demand. If you want to eg. run Blender with it, you
# launch it the following way:
#
# $ amdgporun blender

# Important:
# The AMDGPU-PRO EULA forbids you from redistributing the source package.
# Therefore it's illegal to distribute the .src.rpm or .rpm files to third
# parties.

%global major 21.50.2
%global minor 1384496

# RPM flags
%global debug_package %{nil}

Name:           amdgpu-pro-amf
Version:        %{major}.%{minor}
Release:        1%{?dist}
Summary:        AMD AMF encoder driver for AMD graphic cards

License:        EULA NON-REDISTRIBUTABLE
URL:            https://www.amd.com/en/support/kb/release-notes/rn-amdgpu-unified-linux-21-50-2
Source0:        http://repo.radeon.com/amdgpu/%{major}/ubuntu/pool/proprietary/a/amf-amdgpu-pro/amf-amdgpu-pro_1.4.24-%{minor}_amd64.deb
Source1:        http://repo.radeon.com/amdgpu/%{major}/ubuntu/pool/proprietary/liba/libamdenc-amdgpu-pro/libamdenc-amdgpu-pro_1.0-%{minor}_amd64.deb
ExclusiveArch:  x86_64
#BuildRequires:  
Requires:       amdgpu-pro-vulkan

%description
AMD AMF encoder userspace driver as provided in the amdgpu-pro driver stack. This package
is intended to work along with the free amdgpu stack.


%prep
mkdir files
# AMF
cp %{SOURCE0} .
ar x amf-amdgpu-pro_1.4.24-%{minor}_amd64.deb
tar -xJC files -f data.tar.xz

cp %{SOURCE1} .
ar x libamdenc-amdgpu-pro_1.0-%{minor}_amd64.deb
tar -xJC files -f data.tar.xz

%install
mkdir -p %{buildroot}%{_libdir}/
install -p -m755 files/opt/amdgpu-pro/lib/x86_64-linux-gnu/* %{buildroot}%{_libdir}/

%files
%{_libdir}/libamf*
%{_libdir}/libamdenc*


%changelog
* Sun Mar 27 2022 initial commit - 21.50.2.1384495
- Update to 21.50
