!!!raw

##Bootloader
The program responsible to start the OS. Usually it is a Menu-Like program.
The most common ones are LILO and GRUB2.
You can configure the following in a bootloader:
    Background (https://wiki.archlinux.org/index.php/Grub#Background_image_and_bitmap_fonts)
    Menu
    Font (or size of font, changed when the screen size is set: http://www.linuxquestions.org/questions/debian-26/change-console-font-size-70181/ )
    splash screen
        Fbsplash
        Plymouth
        Splashy
        xplash
A lot of information can be found here https://wiki.archlinux.org/index.php/Grub#Visual_configuration
Changing the boot messages is the job of the init system.

##Shell
The Shell is the command line interface (CLI) that lets you interact with your OS, as opposed to the GUI (graphical user interface).
List of some available shells:
http://www.labtestproject.com/list_of_linux_shell

Remember that the shell is the door to your *nix world, a shell customized to your needs will make your life easier.

The most common things that are cutsomized in a shell are the following:
    * adding aliases
    * creating a custom prompt
    * adding color wrappers
    * customizing the way globing works
    * adding special completion behavior
    * customizing the behavior at specific times (inside git repo, at login, etc..)
    http://shreevatsa.wordpress.com/2008/03/30/zshbash-startup-files-loading-order-bashrc-zshrc-etc/

more documentation:
http://blog.twistedcode.org/2008/03/customizing-your-bash-prompt.html
https://wiki.archlinux.org/index.php/Bash
https://wiki.archlinux.org/index.php/Zsh
https://wiki.archlinux.org/index.php/Ksh

##TTY
TTY, the computer terminal, is the interface that lets you send keys and commands to the kernel/System so they can be interpreted.
The TTY is the most basic way to interact with a *nix system. Spending a lot of time in the TTY can be harsh if it hasn't been customized, it's like fighting a beast.

The TTY only accepts some specific types of fonts. On GNU/Linux they can be found in /usr/share/kbd/console/fonts. You can show the current font using the `showconsolefont` command and change the font using the `setfont` command.

The default TTY colors are white on black. To change them you'll have to use perl-term-extendedcolor-tty (ttycolor) or just use `echo` with some special escape characters for colors(set them in your shell).

To make it easy to multitask in the TTY you'll have to use a terminal multiplexer, a program that lets you use multiple terminals (emulator) in the same TTY and (but not inclusive) detach programs from one terminal to another. Tmux or dtach+dvtm can do this.

The framebuffer can be used to watch videos and view images in the TTY. (fbgs, fbi, mplayer -vo fbdev and others)

To learn more about the TTY:
http://www.linusakesson.net/programming/tty/index.php

##Login Manager
There are many ways to identify yourself on your *nix machine
The default way is normally to simply use the TTY and enter your username and password

Some programs called "login managers" or "display managers" are available to pretify this process.
They can also be used as a middle man to choose the environment you'll be dropped in after login.
Most of them are fully themable, from the background, to the font, passing by the layout and input boxes.

List of Display managers:
https://wiki.archlinux.org/index.php/Display_Manager

Along with the login process you might want to use multiple ways of authentication or 2 ways authentication.
On GNU/Linux the PAM (Pluggable Authentication Module) can be used to create custom way to do that such as captchas.

!!!de/wm

##Desktop Environment
A desktop environment is usually a big packages of multiple softwares that together give the user a working environment, in the sense that everything you'll ever need comes installed with the DE (Desktop Environment).
The number of softwares that are installed with a desktop environment varies greatly, some of them installs everyting from the window manager to the music player passing by the bluetooth manager.

In the ricing world desktop environments are rarely used because customizing them turns out into a job of uninstalling what has been installed and reconfiguring what has been configured for you.
DE are a great choice if you don't have any time to create your own setup.
Remember that everything that a DE is just a bunch of programs sticked together. They can still be installed outside of it.
Here are the most common DE:
    * Cinnamon
    * Enlightenment 
    * GNOME
    * KDE
    * LXDE
    * XFCE
    * MATE

You can find a bigger list here:
http://en.wikipedia.org/wiki/Comparison_of_X_Window_System_desktop_environments

More information here:
https://wiki.archlinux.org/index.php/Desktop_Environment

##Window manager
A window manager (WM) is a program which has the purpose of managing windows in the graphical environement. Managing windows can range from decorating them to moving them around the screen. The two main types of window managers are tiling WMs and floating (also known as stacking) WMs. For tiling WMs, the windows in a workspace are arranged by the WM and not the user. Tiling WMs can be either manual or automatic. For manual, the window layout is set by the user, and for automatic, the layout is pre-defined by the WM.

Some popular tiling WMs:
    * herbstluftwm (manual)
    * Awesome WM (automatic)
    * i3 (automatic)
    * bspwm (manual)
    * stumpwm (manual)

Floating WMs allow for windows to be moved around freely and stack on top of each other . This way of managing windows is the most used in other proprietary OS like MS Windows and OSX. 

Here are some popular floating WMs:
    * openbox (and all *box WMs) (star bucks lol)
    * xfwm4
    * evilwm
    * 2bwm
    * cwm

Other things that might differ across Wms are:

The way it is Configured. Some WMs provide GUI clients for configurations (all WMs included inside DEs, openbox), text files (i3, awesome, bspwm), scripts (awesome). 

The Border/window decoration(s). Borders can often be customized for different colors, widths, and shapes by the user. The window decorations are a feature that most often allow for quick identification and control of a window. A title bar and icons to allow minimization, maximization, and closing the window are the most common window decorations.

The way it handles Keybindings. Some Wms are keyboard driven, meaning that they are designed for quick control. Some other don't even handle keys and let a third party program do the job (for example bspwm).

The way it manages workspaces.There are many types of workspace, tags, desktops... (here need to explain it a bit for the dumb user)
A website with a long list of Wms: http://xwinman.org 


Along with the window manger some other programs can be used along to add fancy decoration to the windows. Often a compositor manager is used. A composite manager is a program that is used to render extra shadows, blurring, and transparency to the windows. Here is a list of well known composite
    * Xcompmgr 
    * Compiz 
    * Compton
    * Cairo Composite Manager

##Information System
An information system can be a status bar, a panel, a dock, a conky, or a taskbar.
Status bar. 

A status bar is a simple block of text information that stick to one of your screen side. It's suppose to show information about some things in time.
https://github.com/LemonBoy/bar
https://wiki.archlinux.org/index.php/Dzen

A panel is similar is similar to a taskbar in the way that it sticks to a side of the screen however it has more things to it. It adds the possibility to manipulate windows (maximize, minimize, etc..). It has widgets which are clickable.
https://wiki.archlinux.org/index.php/Tint2

A dock is a program that regroups some widgets (like a panel) to make it easierto open up programs. It might have a feature to manipulate windows.
https://wiki.archlinux.org/index.php/Cairo-Dock

A taskbar is the full-fledge bar. It has all the features of a panel pluts, it has a menu, it manages programs that runs hidden in the background (not daemons but programs that have a hide feature), it manages popup messages from programs (if you want to know more about popups check the nofication system part).
https://aur.archlinux.org/packages/gnome-panel/
https://www.archlinux.org/packages/?name=xfce4-panel

In the ricing world the customization can be done like so:
    * Use a custom set of icons
    * Change the colors
    * Choose what informations are displayed and write scripts for them
    * Choose the Geometry (size, position, side of the screen)
    * Change the fonts
    * Customized the popups

##GUI
Many programs written for GNU/Linux and unix-like OSs have a GUI, or Graphical User Interface. GUIs for most programs are built around a toolkit called GTK+. GTK+ is a highly-customizable platform that allows end users to tweak every part of how a GUI appears. Commonly, end users install GTK themes from the internet that they like.

Icons comprise mostly all the small pictures you see while interacting with a GUI. Icon packs can be found all over the internet, and contribute highly to an attractive GNU/Linux experience. Some popular icon packs are:
    * Numix/Numix Circle
    * Flattr
    * Moka 

GTK Themes are the backbone of ricing GUI applications. They are the difference between a dull, stock GUI, and a sexy one. The method for changing GTK themes varies by WM. Some WMs (like xfwm4) might even support their own themes outside of GTK. However, a reliable GTK theme changer is LXDE's "LXAppearance" program. Some GUIs rely on an older, more liked version of GTK known as GTK2, and some rely on the newer, less liked, GTK3, and some rely on both. Nonetheless, most theme packs come with support for both. 

Some popular GTK themes are:
    * Iris
    * simpliX
    * Numix
 
Many, many themes can be found elsewhere on the internet, and a quick search for what you're looking for will likely bring up a myriad of nice themes to pick from.

Next, we have the most finnicky of all riceable things: fonts. Fonts (specifically typefaces) comprise everything you read and write on your computer. For that reason, finding a font you like can be a challenge. 

Fonts come in two main styles: bitmap and stroke. 

Bitmap fonts (the nixers font style of choice) are made up of pixels that define the shape of the character. For this reason, they're light on resources and easy to render, but don't scale well and are often only found in one or two sizes. 

Stroke fonts, on the other hand, are made with mathematical formulas that allow them to scale to hundreds of different sizes. And within these two categories, there are hundreds of different styles. The two most common words you'll hear are sans and monospace typefaces. Sans fonts 

Mouse cursor (kinda the same as with icons)...

##Wallpaper
The wallpaper, aka background, is one of the hardest thing to choose in a setup.
The colors must fit with the rest of the theme, it should be coherent.
Remember that most of the time the wallpaper will have windows on it that will hide some parts of it.
The wallpaper should not interfere with your workflow.

The safest way is to use a non colorful tile or a blurred background.
If you don't go for that you need to take extra care and time into choose the perfect wallpaper.

Great ressources for wallpapers:
http://wallbase.cc
http://simpledesktops.com

Some programs can be used to simply setting the wallpaper instead of hardcoding it into the .xinitrc file.
    * bgs
    * esetroot
    * Feh
    * habak
    * hsetroot
    * Nitrogen
    * pybgsetter
    * wallpaperd
    * xli

Note: The wallpaper isn't related to the "icons" on the desktop. If you want those you'll need a DE shell or a file manager that does that.

!!!common applications

##Terminal emulator
Terminal emulators are graphical applications sitting between the user and the shell(isn't it a media to interact with the terminal) [ref needed]. Terminal emulators consist of a text input to interact with the shell, and with such there are only a few thing you can tweak: background, text colors, font and behavior.

As terminal emulators are graphical windows, you can change their aspect, starting by the background. 
Some terminals (like gnome-terminal, or konsole) include drop-down menus to customise most settings. 
In case of more minimalist terminals, you'll have to use another way to modify them. Common means are either by using the X resource database (xrdb), or by modifying the application at compilation time (by modifying a file commonly named "config.h" or "config"). 
In case of an "xrdb compliant" terminal, you will have to run `xrdb -merge /path/to/file` and relaunching the app to see your changes applied. For "config.h style terminals", a recompilation and restart of the app is needed. While drop-down menu like terminals are modified instantly.

Here is a list of commonly used terminals

Modified via mouse menus:
    * gnome-terminal
    * konsole
    * terminator
    * yakuake
    * xfce-terminal

Modified via xrdb
    * rxvt-unicode
    * xterm
    * aterm
    * mterm

Modified via config.h/config
    * evilvte
    * st
    * termite

Background
Terminal backgrounds consists of the rectangular area filling the whole window, behind the text. Most of the time, the default color is white (or purple, in ONE. SPECIAL. CASE). Depending on your terminal of choice, you'll be able to modify the color, transparency or image background. That's pretty much it. 

Speaking of transparency, one can make a distinction between true and fake transparency. 
True transparency make your terminal look like a teinted glass. Move it around and you'll be able to see what's behind it. It require a composite manager [ref needed] to run in order to work. 
Fake transparency is more of a hack: when the window will stop moving, it will "copy" your wallpaper on the background, and apply the ply the teint your specified to it. So if you place it in front of a window, you not see the window behind your terminal, but the portion of your wallpaper behind it.

Font
You can use two types of font: "xft" or "bitmap".
X font types (or XFT, for short) are well polished fonts. They are antialiased, scalable and well designed. They look great, but can be slow to draw sometimes. That's why bitmap fonts are still used. Those fonts are pixel based and not scalable. That's why they can be drawn faster.
Now it's just a matter of choice. Most terminals support both rendering, so do as you please !

Text Colors
A terminal usually make use of 8 differents colors: black, red, green, yellow, blue, magenta, cyan and white. Those 8 colors can come in two flavor: normal and bold. by default, bold colors are just a more flashy version of the color. It leaves use with a total of 16 different colors that we can tweak. This palette of 16 colors is commonly referred to as a "terminal colorscheme". 
To tweak this, the user (you) can assign each color an hexadecimal code that will be displayed when the color is used. Before assigning this code, you must be aware of how many different colors your terminal can display, and thus, which code you can use.

Most of the time, terminals supports 256 differents colors, that you can find here: http://www.calmar.ws/vim/256-xterm-24bit-rgb-color-chart.html.

Behavior
The behavior of the terminal is an important thing, because it's a central application on a linux desktop. Its behavior is defined by the features your terminal gives you. Some are modable via perl scripts, drop-down, have tabs, can resize font on the fly, can open URIs in your web browser, etc...
Just try them all !

##File Managers
The role of a file manager is to make it easy to browse your file system and manipulate files.
This role defines how a file manager acts.
There are 2 different kinds of file managers non-graphicals and graphicals.

Examples of non-graphical file managers:
    * core-utils
    * ranger
    * vifm
    * commander
    * mc (midnight commander)

Example of graphical file managers:
    * thunar
    * nautilus
    * dolphin
    * caja
    * gnome-commander

Some file managers follow the GTK theme (icons and colors), if graphical, some doesn't. 
The colors of the non-graphical ones can usually be riced.

It's important to configure how the file manager displays and list files.
For graphical file managers there are multiple ways of listing, some with preview, some with more information, etc..

Another feature some file managers adds is the ability to interact with files.
To execute scripts and macros by clicking them, to add a context menu when clicking on certain dir or files. Those are normally fully customizable.

A file manager might also be able to access files over the network.

A bunch files managers included in DE have the ability to manage the "Desktop", as in the icon displayed over the root window aka "background".

##Chat client
Chat clients, instant messagers.It's extremely hard to explain how to rice them due to their variety.

The mostly riced are the irc clients: irssi and weechat.

A list of things you can change in them:
    * Nickname alignement
    * Colors
    * Informations
    * Plugins

##Music/Media player
Like all items in this section, there's a wide variety of choices for a media player.
There are GUI ones, Curses ones, and CLI ones.
Most of them offer some sort of customization. The easiest ones to rice are the curses.

Things that can be riced:
    * Colors
    * UI elements
    * Equalizer
    * Visualizer

Ressources:
https://wiki.archlinux.org/index.php/Cmus
https://wiki.archlinux.org/index.php/Ncmpcpp

##Text editor
The choices for text editors aren't scarce.
The prefered choices for ricers are: EMACS, Sublime, and Vim.

The customization goes as follow:
    * Syntax highlighting
    * Theme (for UI elements arrangement)
    * Plugins

Ressources:
http://www.linux.org/threads/text-editors.4104/g

##Web browser
There's a lot of variety of browsers.

Things you can do with your browser are the following:
    * Change its appearance:
        * chrome.css (Firefox), and other files for other browsers
        * Move the widgets (tab bar,info,etc..)
    * Create a custom start page, a page that appears at the start of the browser.

!!!Others

##Show-off Colors
pipes.sh 
https://github.com/livibetter/pipes.sh
invaders.sh
cmatrix
http://dotshare.it/category/terms/colors/
more links...

##Notification system
Desktop notifications are pops-up that signals an event update.
They are used to keep you updated about multiple things. 

For example:
    * Change of sound volume
    * Change of brightness
    * Change of network connection

Ressources:
https://wiki.archlinux.org/index.php/Desktop_Notifications
http://blog.z3bra.org/2014/04/pop-it-up.html

##Information Displays
Archey
Conky
Screenfetch
Screenfo

##Monitoring Programs
htop

##Application launcher
An application launcher is a program used as a kind of menu to start other programs.
it can be a selection menu or a terminal like menu (input).

Some comes built-in inside a DE taskbar (gnome-panel) some are third parties.

Ressources:
https://wiki.archlinux.org/index.php/Category:Application_launchers
https://wiki.archlinux.org/index.php/Xdg-open

##Screen locker
A screen locker blocks input to your machine until the right password has been entered.

A lot of extravagant way can be used to achieve so:
    * Blurring the screen and adding a padlock to the middle
    * Changing the image to something else,
    * Do a futurist menu to enter your machine
    * have a nice input dialog
    * etc...

Ressources:
https://wiki.archlinux.org/index.php/List_of_applications#Screen_lockers

##Others

