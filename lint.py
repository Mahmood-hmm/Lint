#!/usr/bin/env python3
import subprocess
import sys
import os
import shutil
                                              
                                              

def check():
    try:
        import rich
        return True
    except:    
        return False  


def detect_manager():
    if os.system("command -v apt > /dev/null 2>&1") == 0:
        return "apt"
    elif os.system("command -v pacman > /dev/null 2>&1") == 0:
        return "pacman"
    elif os.system("command -v dnf > /dev/null 2>&1") == 0:
        return "dnf"
    else:
        return None

manager = detect_manager()

if not check() :
    down_choice = input ("You are missing rich pkg would you like to install it Automatically?")
    if down_choice in ["yes" , "y" , ""] :
        if manager == "apt" :
            subprocess.run([sys.executable , "-m" , "pip" ,"install" ,"rich" , "--break-system-packages"])
        elif manager == "dnf" :
            subprocess.run(["sudo", "dnf", "install", "python3-rich", "-y"])
        elif manager == "pacman" : 
            subprocess.run(["sudo" , "pacman" , "-S" , "python-rich"])
    elif down_choice in ["no" , "n"] :
        print ("Please download rich to start program")
        sys.exit()
    else :
        print ("Please try again")


import rich
from rich.console import Console
from rich.theme import Theme
from rich.table import Table
from rich.panel import Panel
from rich.align import Align


def check_curl():
    try:
        result = subprocess.run(["curl", "--version"], capture_output=True, text=True)
        
        if result.returncode == 0:
            return True
        else:
            return False
    except FileNotFoundError:
        return False


def download(pkg) :
    if manager== "apt" :
        subprocess.run (["sudo" ,"apt" ,"install" , "-y", pkg])
    elif manager== "dnf" :
        subprocess.run(["sudo" , "dnf" , "install" , "-y" , pkg])
    elif manager == "pacman" :
        subprocess.run(["sudo" , "pacman" ,  "-S" , "--noconfirm" , pkg])


Console = Console()


def choices() :
    Console.print("[cyan]Welcome to lint!! choose one :")
    Console.print("[yellow] [1][/yellow] Browser")
    Console.print("[yellow] [2][/yellow] Tools")
    Console.print("[yellow] [3][/yellow] Developer editors")
    Console.print("[yellow] [4][/yellow] Game launchers")
    Console.print("[yellow] [5][/yellow] Additional libraries")
    Console.print("[yellow] [6][/yellow] Video / Audio player")
    Console.print("[yellow] [7][/yellow] Block any bad sites Gambling / Adds / porn / FakeNews")
    Console.print("[yellow] [8][/yellow] Recommended fast install")
    Console.print("[yellow] [9][/yellow] Help")
    Console.print("[yellow] [10][/yellow] Exit")



def print_browser() :
    Console.print("\nPlease choose one of this :" , style="cyan")
    Console.print("[yellow] [1][/yellow] Brave     [dim][Most privecy browser][/dim]")
    Console.print("[yellow] [2][/yellow] Firefox   [dim][Open source classic browser][/dim]")
    Console.print("[yellow] [3][/yellow] Chrome    [dim][Most common browser][/dim]")
    Console.print("[yellow] [4][/yellow] Chromium  [dim][The base of most brosers][/dim]")
    Console.print("[yellow] [5][/yellow] Back")


# if the app dosent exict return true so you can only type 
#if check("app_name") and then download the pkg by download("app_name")

def check_app(app_name):
    if shutil.which(app_name):
        Console.print(f"{app_name} is already installed", style="yellow")
        return False
    return True



def print_tools() :
        Console.print("\nPlease choose one of this :" , style="cyan")
        Console.print("[yellow] [1][/yellow] Git        [dim][Light weight tool to download distro control][/dim]")
        Console.print("[yellow] [2][/yellow] FastFetch  [dim][To show distro, version and lot more][/dim]")
        Console.print("[yellow] [3][/yellow] Btop       [dim][Terminal tool show usige of ram , cpu and every thing][/dim]")
        Console.print("[yellow] [4][/yellow] TimeShift  [dim][Important tool if you got a problem you can simply go back]")
        Console.print("[yellow] [5][/yellow] Fish       [dim][Simmeler to bash but with many futers][/dim]")
        Console.print("[yellow] [6][/yellow] fzf        [dim][Command line finder][/dim]")
        Console.print("[yellow] [7][/yellow] Yazi       [dim][Fast terminal file maneger with rust lenguege][/dim]")
        Console.print("[yellow] [8][/yellow] Back")



def  continuee() :
    Console.input("[cyan]Enter to continue")



def print_dev_tools() :
        Console.print("\nPlease choose one of this :" , style="cyan")
        Console.print("[yellow] [1][/yellow] VSCode     [dim][Most common dev environment][/dim]")
        Console.print("[yellow] [2][/yellow] VScodium   [dim][Its VSCode but without micossoft spy][/dim]")
        Console.print("[yellow] [3][/yellow] Vim        [dim][Fast , light wheghit terminal text editor][/dim]")
        Console.print("[yellow] [4][/yellow] Kate       [dim][Open source dev codeing environment][/dim]")
        Console.print("[yellow] [5][/yellow] Back")


def print_game_launcher() :
        Console.print("\nPlease choose one of this :" , style="cyan")
        Console.print("[yellow] [1][/yellow] Lutris (Most common but can be dificult)")
        Console.print("[yellow] [2][/yellow] Bottles (Run windows apps)")
        Console.print("[yellow] [3][/yellow] Heroic game launcher (Most easy launcher come with all pkgs installed)")
        Console.print("[yellow] [4][/yellow] Back")


def print_libraries():
        Console.print("\nPlease choose one of this :" , style="cyan")
        Console.print("[yellow] [1][/yellow] FlatPack [dim](free,easy and fast to install)[/dim]")
        Console.print("[yellow] [2][/yellow] Snap     [dim](From ubuntu it might be a little heavy)[/dim]")
        Console.print("[yellow] [3][/yellow] Seal     [dim](To manege FlatPack apps)[/dim]")
        Console.print("[yellow] [4][/yellow] Back")



def print_block () :
        Console.print("[yellow] [1][/yellow] Steven black's hosts (porn/gambling/FakeNews) and more")
        Console.print("[yellow] [2][/yellow] Back")



def print_auto_install() :
        Console.print("Recommended install for important tools" , style="yellow")
        Console.print("[yellow] [1][/yellow] Install :Tools/Browser/Game launcher/FlatPack/Video Audio/block sites")
        Console.print("[yellow] [2][/yellow] Install :Tools/Terminal sound player/Game launcher/Block Sites")
        Console.print("[yellow] [3][/yellow] Install :Browser/FlatPack/Snap/Block Sites")
        Console.print("[yellow] [4][/yellow] Install :FlatPack/Snap/Block Sites")
        Console.print("[yellow] [5][/yellow] Back")



def print_video_audio() :
        Console.print("[yellow] [1][/yellow] VLC   [dim][Support every encode in this planet][/dim]")
        Console.print("[yellow] [2][/yellow] MPV   [dim][Devlopers love this player][/dim]")
        Console.print("[yellow] [3][/yellow] CMus  [dim][Terminal sound player][/dim]")
        Console.print("[yellow] [4][/yellow] Back")
        



def install_brave() :
    if not check_curl() :
        download("curl")
    else :
        if check_app("brave-browser") :
            subprocess.run ("curl -fsS https://dl.brave.com/install.sh | sh" , shell=True)




def install_yay():
    if not shutil.which("yay"):
        Console.print("[yellow]Yay not found ....[/yellow]")
        subprocess.run("sudo pacman -S --needed base-devel git -y", shell=True)
        commands = [
            "git clone https://aur.archlinux.org/yay.git",
            "cd yay && makepkg -si --noconfirm",
            "cd .. && rm -rf yay"
        ]
        for cmd in commands:
            subprocess.run(cmd, shell=True)


def browser() :
    while True :
        subprocess.run(["clear"])
        owl()
        print_browser()
        choice = Console.input ("[cyan]> [/cyan]")
        if choice == "1":
                if not check_curl() :
                    down_curl = Console.input ("[cyan]You are missing (curl) would you like to download in automatic?\n[/cyan]")
                    if down_curl in ["yes" , "y" , ""] :
                        download("curl")
                    elif down_curl in ["no" , "n"] :
                        Console.print ("Please download curl to download brave-browser")
                        continuee()
                else :
                    try :
                        if check_app("brave-browser") :
                            subprocess.run ("curl -fsS https://dl.brave.com/install.sh | sh" , shell=True)
                        continuee()
                    except Exception as e :
                        Console.print ("Error please try again" , style="red")
                    continuee()
        elif choice == "2":
            if check_app("firefox") :
                download("firefox")  
            continuee()
        elif choice == "3" :
            if manager == "apt" :
                subprocess.run("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb" , shell=True)
                subprocess.run ("sudo apt install ./google-chrome-stable_current_amd64.deb" , shell=True)
            elif manager  == "dnf" :
                subprocess.run("sudo dnf install fedora-workstation-repositories" , shell=True)
                subprocess.run("sudo dnf config-detect_manager() --set-enabled google-chrome" , shell=True)
                subprocess.run("sudo dnf install google-chrome-stable" , shell=True)
            elif manager == "pacman" :
                install_yay()
                subprocess.run("yay -S google-chrome" , shell=True)
        elif choice == "4" :
            if check_app("chromium") :
                download("chromium")
        elif choice == "5" :
            break
        else :
            Console.print ("Please choose on of above" , style="yellow") 




def install_tools() :
        if check_app("git") :
                download("git")
        if check_app("fastfetch") :
                download("fastfetch")
        if check_app("btop") :
                download("btop")
        if check_app("timeshift") :
                download("timeshift")
        if check_app("fish") :
                download("fish")



def tools() :
    while True :
        subprocess.run(["clear"])
        owl()
        print_tools()
        choice = Console.input("[cyan]> [/cyan]")
        if choice == "1" :
            if check_app("git") :
                download("git")
                continuee()

        elif choice == "2" :
            if check_app("fastfetch") :
                download("fastfetch")
                continuee()
        elif choice == "3" :
            if check_app("btop") :
                download("btop")
                continuee()
        elif choice == "4" :
            if check_app("timeshift") :
                download("timeshift")
                continuee()
        elif choice == "5" :
            if check_app("fish") :
                download("fish")
                continuee()
        elif choice == "6" :
            if  check_app("fzf") :
                download("fzf") 
                continuee()
        elif choice == "7" :
            if manager == "pacman":
                subprocess.run("sudo pacman -S --noconfirm yazi", shell=True)
                continuee()   
            elif manager == "dnf":
                subprocess.run("sudo dnf copr enable varlad/yazi -y", shell=True)
                subprocess.run("sudo dnf install yazi -y", shell=True)
                continuee()
            elif manager == "apt":
                Console.print("[blue]Downloading pre-built binary for Yazi...[/blue]")
                subprocess.run("wget https://github.com/sxyazi/yazi/releases/latest/download/yazi-x86_64-unknown-linux-gnu.zip", shell=True)
                subprocess.run("unzip yazi-x86_64-unknown-linux-gnu.zip", shell=True)
                subprocess.run("sudo mv yazi-x86_64-unknown-linux-gnu/yazi /usr/local/bin/", shell=True)
                subprocess.run("rm -rf yazi-x86_64-unknown-linux-gnu.zip yazi-x86_64-unknown-linux-gnu", shell=True)
                continuee()
            if not check_app("yazi") :
                Console.print("Download success!" , style= "green")
            else :
                Console.print("There was an error please try again" , style="red")
        elif choice == "8" :
            break
        else :
            Console.print("Please choose one of above" , style="yellow")



def dev_tools():
    while True :
        subprocess.run(["clear"])
        owl()
        print_dev_tools()
        tool = Console.input("[cyan]> [/cyan]")
        if tool == "1":
            if check_app("code") :
                if manager == "apt":
                    subprocess.run("wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg", shell=True)
                    subprocess.run("sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg", shell=True)
                    subprocess.run("echo 'deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main' | sudo tee /etc/apt/sources.list.d/vscode.list", shell=True)
                    subprocess.run("sudo apt update && sudo apt install code -y", shell=True)
                elif manager== "dnf":
                    subprocess.run("sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc", shell=True)
                    subprocess.run("sudo sh -c 'echo -e \"[code]\\nname=Visual Studio Code\\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\\nenabled=1\\ngpgcheck=1\\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc\" > /etc/yum.repos.d/vscode.repo'", shell=True)
                    subprocess.run("sudo dnf install code -y", shell=True)
                elif manager== "pacman":
                    install_yay()
                    subprocess.run("yay -S visual-studio-code-bin --noconfirm", shell=True)
                    continuee()
            else :
                Console.print("VSCode is already installed !!" , style = "yellow")
                continuee()
        elif tool == "2":
            if check_app("codium") :
                if manager== "apt":
                    subprocess.run("wget -qO - https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg | gpg --dearmor | sudo dd of=/usr/share/keyrings/vscodium-archive-keyring.gpg", shell=True)
                    subprocess.run("echo 'deb [ signed-by=/usr/share/keyrings/vscodium-archive-keyring.gpg ] https://download.vscodium.com/debs vscodium main' | sudo tee /etc/apt/sources.list.d/vscodium.list", shell=True)
                    subprocess.run("sudo apt update && sudo apt install codium -y", shell=True)
                elif manager == "dnf":
                    subprocess.run("sudo rpm --import https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg", shell=True)
                    subprocess.run("echo -e '[vscodium]\\nname=vscodium\\nbaseurl=https://download.vscodium.com/rpms/\\nenabled=1\\ngpgcheck=1\\ngpgkey=https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg' | sudo tee /etc/yum.repos.d/vscodium.repo", shell=True)
                    subprocess.run("sudo dnf install codium -y", shell=True)
                elif manager == "pacman":
                    subprocess.run("sudo pacman -S vscodium", shell=True)
                    continuee()
            else :
                Console.print("VSCodium is already installed !!" , style = "yellow")
                continuee()
        elif tool == "3":
            if check_app("vim") :
                download("vim") 
            else :
                Console.print("Vim is already installed !!" , style = "yellow")
                continuee()
        elif tool == "4":
            if check_app("kate") :
                download("kate")
            else :
                Console.print("Kate is already installed !!" , style = "yellow")
                Console.input("[cyan]Enter to continue[/cyan]")
        elif tool == "5" :
            break
        else :
            Console.print("Please choose one of above" , style="yellow")




def install_launcher() :
            if manager == "pacman":
                subprocess.run("sudo pacman -S heroic-games-launcher-bin --noconfirm", shell=True)
            elif manager== "apt":
                subprocess.run("wget https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/releases/latest/download/heroic_latest_amd64.deb", shell=True)
                subprocess.run("sudo apt install ./heroic_latest_amd64.deb -y && rm heroic_latest_amd64.deb", shell=True)
            elif manager == "dnf":
                subprocess.run("sudo dnf install heroic-games-launcher -y", shell=True)
                continuee()



def game_launcher() :
    while True :
        subprocess.run(["clear"])
        owl()
        print_game_launcher()
        choice = Console.input("[cyan]> [/cyan]")
        if choice == "1":
            if manager == "apt":
                subprocess.run("sudo add-apt-repository ppa:lutris-team/lutris -y && sudo apt update && sudo apt install lutris -y", shell=True)
            elif manager == "dnf":
                subprocess.run("sudo dnf install lutris -y", shell=True)
            elif manager == "pacman":
                subprocess.run("sudo pacman -S lutris --noconfirm", shell=True)

        elif choice == "2":
            if manager == "pacman":
                subprocess.run("sudo pacman -S bottles --noconfirm", shell=True)
            else:
                subprocess.run("flatpak install flathub com.usebottles.bottles -y", shell=True)
        elif choice == "3":
            install_launcher()
        elif choice == "4" :
            break
        else :
            Console.print("Please choose one of above" , style="yellow")





def add_flatpack() :
            if manager == "apt":
                subprocess.run("sudo apt update && sudo apt install flatpak -y", shell=True)
            elif manager == "dnf":
                subprocess.run("sudo dnf install flatpak -y", shell=True)
            elif manager == "pacman":
                subprocess.run("sudo pacman -S flatpak --noconfirm", shell=True)
            subprocess.run("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo", shell=True)
            continuee()



def add_snap() :
            if manager == "apt":
                subprocess.run("sudo apt update && sudo apt install snapd -y", shell=True)
            elif manager == "dnf":
                subprocess.run("sudo dnf install snapd -y && sudo ln -s /var/lib/snapd/snap /snap", shell=True)
            elif manager == "pacman":
                Console.print("[red]Snap on Arch requires manual AUR installation (snapd).[/red]")
            subprocess.run("sudo systemctl enable --now snapd.socket", shell=True)
            continuee()



def add_libraries() :
    while True :
        subprocess.run(["clear"])
        owl()
        print_libraries()
        choice = Console.input("[cyan]> [/cyan]")
        if choice =="1" :
            add_flatpack()
        elif choice == "2" :
            add_snap()
        elif choice == "3" :
            if not shutil.which("flatpak"):
                Console.print("[red]Flatpak is not installed! Installing it first...[/red]")
                add_flatpack() 
                result = subprocess.run("flatpak install flathub io.github.marcusantonioh.Seal -y", shell=True)
            if result.returncode == 0:
                Console.print("Seal installed successfully!" , style="green")
            else:
                Console.print("Failed to install Seal." , style = "red")
            continuee()

        elif choice == "4" :
            break
        else :
            Console.print("Please choose one of above" , style="yellow")



def auto_block_site() :
            url = "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn/hosts"
            subprocess.run(["clear"])
            owl() 
            cmd = f"curl -s {url} | sudo tee /etc/hosts > /dev/null"    
            try:
                result = subprocess.run(cmd, shell=True, check=True)
                if result.returncode == 0:
                    Console.print("Success !! " , style="green")
                else:
                    Console.print("Error please try again" , style = "bold red")
            except Exception as e:
                Console.print(f"[bold red]Error pleas try again[/bold red]")
                continuee()




def install_cmus():
    if check_app("cmus"):
        download("cmus")



def video_audio():
    while True:
        subprocess.run(["clear"])
        owl()
        print_video_audio()
        choice = Console.input("[cyan]> [/cyan]")
        if choice == "1":
            if check_app("vlc"):
                download("vlc")
        elif choice == "2":
            if check_app("mpv"):
                download("mpv")
        elif choice == "3":
            install_cmus() 
        elif choice == "4":
            break
        else:
            Console.print("Please choose one of above", style="yellow")




def block_site() :
    while True :
        subprocess.run (["clear"])
        owl()
        print_block()
        choice = Console.input("[cyan]>  [cyan]")
        if choice == "1" :
            auto_block_site()
        elif choice == "2" :
            break
        else :
            Console.print("Please choose one of above" , style="yellow")




def fast_install() :
    while True :
        subprocess.run(["clear"])
        owl()
        print_auto_install()
        choice = Console.input("[cyan]> [/cyan]")
        if choice == "1" :
            install_tools()
            install_brave()
            install_launcher()
            add_flatpack()
            # video_audio()
            auto_block_site()
        elif choice == "2" :
            install_tools()
            install_cmus()
            install_launcher()
            auto_block_site()
        elif choice == "3" :
            install_brave()
            add_flatpack()
            add_snap()
            auto_block_site()
        elif choice == "4" :
            add_flatpack()
            add_snap()
            auto_block_site()
            



def help() :
    while True :
        subprocess.run(["clear"])
        table = Table(title="Help" , show_lines=True)
        table.add_column("Question" , style="yellow")
        table.add_column("Description" , style="cyan")
        table.add_row("What is this app?" , "Lint project is open source and it help new/lazy linux people who want fast install")
        table.add_row("What does it do?" , "It download pkgs from your distro pkgs and add repository for other apps")
        table.add_row("What lint project goal?" , "My goal is to make install much easy as i can and make other options like block sites easy to make")
        table.add_row("What does recommended install do ?" , "Download a most recommended and important tools as you want")
        table.add_row("The app didn't work !" , "For now only fedora , ubuntu and arch are supported") 
        table.add_row("I didn't like the app style" , "You can easy change style/logo or even add futures this app have clearly to view functions")
        Console.print(table)
        continuee()
        break



def show_logo():

    logo = r'''
    
    ██╗     ██╗███╗   ██╗████████╗
    ██║     ██║████╗  ██║╚══██╔══╝
    ██║     ██║██╔██╗ ██║   ██║   
    ██║     ██║██║╚██╗██║   ██║   
    ███████╗██║██║ ╚████║   ██║  
    ╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝                                                   
    '''
   
    Console.print(
            logo,
            style="cyan bold",
        )
    

def owl():
    owl_art = (
r"""
 /\ /\ 
((ovo))
():::()
  VVV  
"""
    )
    centered_owl = Align.center(owl_art, style="cyan bold")

    Console.print(
        Panel(
            centered_owl,
            style="cyan bold",
            title="[white]Lint[/white]",
            subtitle="[yellow]v1.0.0[/yellow]",
            width=30,      
            expand=False,
            padding=(1, 4)  
        )
    )


## i will add seal and mp4/3 player then i will publish ثقافة انجليزي هههه

while True :
    subprocess.run(["clear"])
    show_logo()
    choices()
    choice = Console.input("[cyan]> [/cyan]")
    if choice == "1" :
        browser()
    elif choice == "2" :
        tools()
    elif choice == "3" :
        dev_tools() 
    elif choice == "4" :
        game_launcher()
    elif choice == "5" :
        add_libraries() 
    elif choice == "6" :
       video_audio() 
    elif choice == "7" :
        block_site()
    elif choice == "8" :
        fast_install()
    elif choice == "9" :
        help()
    elif choice == "10" :
        Console.print("Thank you for using us !!\nI hope you liked the app :)" , style="yellow")
        break

