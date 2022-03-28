This downloads the proprietary amdgpu-pro AMF encoder component debian package, converts it to a Fedora RPM, and installs it  on the system

Using this requires the amdgpu-pro vulkan driver to be used with the application you are using AMF with. For example if using with OBS, you must launch OBS with the amdgpu-pro vulkan driver.

1. Before using this, clone http://github.com/gloriouseggroll/amdgpu-pro-vulkan-fedora and install it:

```
git clone http://github.com/gloriouseggroll/amdgpu-pro-vulkan-fedora
cd amdgpu-pro-vulkan-fedora
./install.sh
```

2. Next, run the install script from this folder:
```
./install.sh
```

3. Install the amdgpu-vulkan-switcher from copr:
```
sudo dnf copr enable gloriouseggroll/amdgpu-vulkan-switcher 
sudo dnf install -y amdgpu-vulkan-switcher
```

4. Run the application using the amdgpu-pro vulkan driver using `vk_pro <command>`

For example, if you want to use obs with AMF support in the 'Custom FFmpeg' option or [StreamFX](https://github.com/Xaymar/obs-streamfx) plugin:

```
vk_pro obs
```

**IMPORTANT NOTE**

If capturing another vulkan source, such as a video game, you must -also- run the game using vk_pro. For example with steam games:

```
vk_pro %command%
```

Otherwise the game may try to use RADV, leading to a GPU lockup/crash.
