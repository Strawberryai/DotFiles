# Introduction
These are my linux configuration files. 
It includes my [NeoVim](https://neovim.io/) keybinds and plugins wich makes programming on the terminal more enjoyable, my [Qtile](https://github.com/qtile/qtile) config files to transform my desktop enviroment and my terminal configuration to have the best of [Alacritty](https://github.com/alacritty/alacritty).

# Installation
To install all these programs and its configuration you can do it manually or
with the provided installation script.

Installation script:
```
./installer.bash
```

## NeoVim

Install neovim (apt):
```
sudo apt install neovim
sudo apt-get install fonts-powerline
```

Install [vim-plug](https://github.com/junegunn/vim-plug):
```
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```

Install [nodejs](https://github.com/nodesource/distributions/blob/master/README.md#debinstall) for coc completion:
```
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
```

## Alacritty

## Qtile

## Config files

Set up the config files:
```
mkdir ~/temp && cd ~/temp
git clone https://github.com/Strawberryai/DotFiles
cp -r DotFiles/. ~/.config
rm -rf ~/temp
nvim #And inside vim make :PlugInstall
```
