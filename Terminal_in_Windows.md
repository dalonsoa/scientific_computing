# Terminal in Windows 

If you are a Mac or a Linux user, you will have already noticed that you can launch a terminal from which run UNIX/Linux commands. In general, most of the OS have the bash terminal installed, although this might not be your case. Anyhow, you have an easy access to the terminal, which you will be using during the short introduction to UNIX/Linux in the workshop.

On the contrary, if you are a Windows user, it might not be that easy for you to find the terminal in your system. By default, the Windows shell is the "Command prompt", which can be quickly accessed by typing these two words in the search bar of your desktop (i.e. Ask Cortana). However, this shell does not work like the bash shell, hence having different commands from the ones you are going to be learning in the UNIX/Linux introduction. Therefore, we have thought of three alternatives you have to install more-Linux shell in your Windows OS.

## 1. GitBash for Windows
You can install the GitBash for Windows, which can be downloaded from [here](https://git-scm.com/download/win). If you are unsure which options you should allow during the installation, you can follow this [tutorial](https://www.siteground.com/tutorials/git/windows-installation/). However, if you want to create from the terminal soft links (`ln -s`), I recommend you also enable this extra feature by clicking the `Enable symbolic links` box when it appears during the installation. Once the installation is finished, you will see the following icon in your Tasks bar, which means that you will have the GitBash terminal installed in your system!

<p align="center">
  <img width="100" height="100" src="https://mccarter.gallerycdn.vsassets.io/extensions/mccarter/start-git-bash/1.2.1/1499505567572/Microsoft.VisualStudio.Services.Icons.Small">
</p>


The coolest thing about this terminal is that you can manage your own Git repositories (cloning repos, removing and adding files, etc.) or clone others with simple commands. If you are thinking of becoming a GitHub user, this is your terminal! You might also want to install [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) to generate your SSH key. If you want more information about this last step and how to do it, you can follow [this tutorial](https://www.siteground.com/kb/How_to_generate_an_SSH_key_on_Windows_using_PuTTY/).

## 2. Install a Linux distribution in a Virtual Box (VB)
If you are keen on having a complete Linux experience and want to have more than a terminal, you can always create a Virtual Box with a Linux distribution.

We recommend you to download the [Virtual Box from Oracle](https://www.virtualbox.org/), install it in your PC, and then download your preferred Linux distribution. For instance, if you want to install Ubuntu, you can download the Ubuntu desktop from [here](https://www.ubuntu.com/download/desktop). Once you have the VB and the Linux distribution installed, just follow the instructions [here](http://www.psychocats.net/ubuntu/virtualbox). This tutorial explains how to install Ubuntu in the VB, but the same procedure can be followed by any other of the Linux distributions :smile: 

## 3. Activate the Linux subsystem for Windows

### **WARNING: DO NOT DO THIS IF YOU ARE NOT COMFORTABLE/EXPERIENCE ENOUGH WITH THE COMMAND LINE NOR WITH ACTIVATING THE DEVELOPER MODE**

The last option, which is available for only Windows 10 users, consists of installing a Linux environment as a subsystem inside your Windows. According to the [Documentation](https://docs.microsoft.com/en-us/windows/wsl/about), you can:

* Install your preferred Linux distributions.
* Run command-line utilities (e.g. grep, sed, awk, sort, etc.)
* Run bash shell scripts and Linux command-line applications such as tmux or vim.
* Choose your favorite Linux distributions from the Windows Store.
* Install Linux tools using (e.g. you can use `apt-get` as in Ubuntu)
* *... and many more - Check the documentation for more info*

You can follow [this tutorial](https://docs.microsoft.com/en-us/windows/wsl/install-win10) to install it if you are interested in testing this in your Windows.
