#! /bin/bash

# Copyright <2022> <Strawberryai>
# Por la presente se concede permiso, libre de cargos, a cualquier persona que obtenga una copia 
# de este software y de los archivos de documentación asociados (el "Software"), a utilizar el 
# Software sin restricción, incluyendo sin limitación los derechos a usar, copiar, modificar, 
# fusionar, publicar, distribuir, sublicenciar, y/o vender copias del Software, y a permitir a 
# las personas a las que se les proporcione el Software a hacer lo mismo, sujeto a las siguientes 
# condiciones:
# 
# El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o partes 
# sustanciales del Software.
# 
# EL SOFTWARE SE PROPORCIONA "COMO ESTÁ", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO 
# PERO NO LIMITADO A GARANTÍAS DE COMERCIALIZACIÓN, IDONEIDAD PARA UN PROPÓSITO PARTICULAR E 
# INCUMPLIMIENTO. EN NINGÚN CASO LOS AUTORES O PROPIETARIOS DE LOS DERECHOS DE AUTOR SERÁN RESPONSABLES 
# DE NINGUNA RECLAMACIÓN, DAÑOS U OTRAS RESPONSABILIDADES, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO 
# O CUALQUIER OTRO MOTIVO, DERIVADAS DE, FUERA DE O EN CONEXIÓN CON EL SOFTWARE O SU USO U OTRO TIPO 
# DE ACCIONES EN EL SOFTWARE.

NO_EXECUTION="FALSE"

############################################################
#                       HELP                               #
############################################################
function HELP(){
    # Display help
    echo "Script de configuración automática"
    echo
    echo -e "\t-h\t Imprime la ayuda del script."
}

############################################################
#                       NVIM INSTALLATION                  #
############################################################
function neovimINSTALL(){
    echo "Installing neovim..."
    sudo apt update
    sudo apt install neovim

    echo "Installing powerline fonts..."
    sudo apt-get install fonts-powerline

    echo "Installing plug-install for Unix,Linux..."
    sudo apt install curl
    sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'

    echo "Installing Node.js v18.x for Ubuntu..."
    curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
    sudo apt-get install -y nodejs

    sudo add-apt-repository ppa:neovim-ppa/unstable
    sudo apt-get update
    sudo apt-get install neovim
}


############################################################
#                       DOTFILES INSTALLATION              #
############################################################
function dotfilesINSTALL(){
    echo "Copying dotfiles..."
    cp -r . ~/.config
}

############################################################
#                       MAIN                               #
############################################################
function main(){
   # Actualmente sólo está soportada la versión Melodic Ubuntu
   # Establece las opciones por defecto si no se han especificado otras
    echo "Iniciando script..."
    read -p "¿Desea isntalar NeoVim? [S/n]" opcion
    case $opcion in
        S)neovimINSTALL;;
        s)neovimINSTALL;;
        *)exit 0;;
    esac

    dotfilesINSTALL
}


# Process the input options
while getopts "h:" option; do
   case $option in
      h)
          HELP #Display help
          NO_EXECUTION="TRUE"
          ;; 
      \?)echo "ERROR: opción inválida. Prueba con -h para ver la ayuda.";;

   esac
done

# Si no se ha preguntado por la ayuda ejecutamos el script
if [ "$NO_EXECUTION" = "FALSE" ]; then main; fi

exit 0
