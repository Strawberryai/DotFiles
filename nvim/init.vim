"1. Getting started with sets
set nocompatible            "Set this for compatibility
set nolist                  "Hides invisible characters
set rnu                     "Relative number
set number                  "Show line numbers
set encoding=utf-8          "Encoding
set noswapfile              "Just one .vimrc
set belloff=all

filetype on                 "Enable recognizing file types
filetype plugin indent on   "For plugins to load correctly

syntax on                   "Turn on syntax highlighting

set modelines=0             "Turn off modelines (file specific variables disabled) 
"set nowrap                  "Line wrap disabled

set textwidth=79            "Set the maximum with of the text in a line
set formatoptions=tcqrn1    "Set the autoformat options to t,c,q,r,n,1
set tabstop=4               "Number of spaces that a <TAB> in the file counts for
set shiftwidth=4            "Number of spaces to use for each step of autoindent
set softtabstop=4           "Different <TAB> size, However it is equals so it doesnt have a visual effect
set expandtab               "Convet new tabs to spaces
set noshiftround            "Disable shiftround so shiftwidth is not rounded
set smartindent
set autoindent

set matchpairs+=<:>         "Adds < and > to the matching pairs list
set hlsearch                "Hightligth matching search patterns
set incsearch               "Enable incremental search
set ignorecase              "Include matching uppercase words with lowercase search term
set smartcase               "Include only uppercase words with uppercase search term

set scrolloff=5             "Display 5 lines above/below the cursor when scrolling whith a mouse
set backspace=indent,eol,start    "Fixes common backspace problems

set laststatus=2            "Set status line visible to always
set statusline=%F%m%r%h%w\ [FORMAT=%{&ff}]\ [TYPE=%Y]\ [POS=%l,%v][%p%%]\ [BUFFER=%n]\ %{strftime('%c')}

set showmode                "Enables displaying the current mode
set showcmd                 "Show partial commands in the last line of the screen

set termguicolors       "Sets the color on the terminal
set shell=zsh

set splitbelow              "Set default split position
set splitright              "Set default split position

"2. Remaps
"Vim's auto indentation feature does not work properly with text copied from outside of Vim. Press the <F2> key to toggle paste mode on/off.
nnoremap <F2> :set invpaste paste?<CR>
imap <F2> <C-O>:set invpaste paste?<CR>
set pastetoggle=<F2>

let mapleader=","             "The mapleader is ',' now
noremap <leader>w :w<CR>
noremap <leader>q :wq<CR>
noremap <leader>gs :CocSearch
noremap <space> :/
noremap <leader><cr> <cr><c-w>h:q<cr>
noremap <leader>e :CocCommand explorer<CR>
noremap <leader>t :Term<CR>
" Vertical equivalent of C-w-n and C-w-N"
noremap <leader>n :vnew<CR>

"Autobrackets
inoremap " ""<left>
inoremap ' ''<left>
inoremap << <><left>
inoremap ( ()<left>
inoremap () ()
inoremap (<CR> (<CR>)<ESC>O
inoremap [ []<left>
inoremap [] []
inoremap { {}<left>
inoremap {} {}
inoremap {<CR> {<CR>}<ESC>O
inoremap /* /**/<left><left>

"Shift up the selected block, autoindents it and reselects it.
vnoremap J :m '>+1<CR>gv=gv
vnoremap K :m '<-2<CR>gv=gv

imap ii <Esc>
vnoremap ii <Esc>

"nnoremap <C-J> <C-W><C-J> "Ctrl-j to move down a split
"nnoremap <C-K> <C-W><C-K> "Ctrl-k to move up a split
"nnoremap <C-L> <C-W><C-L> "Ctrl-l to move	right a split
"nnoremap <C-H> <C-W><C-H> "Ctrl-h to move left a split

" Use ctrl-[hjkl] to select the active split!
nmap <silent> <c-k> :wincmd k<CR>
nmap <silent> <c-j> :wincmd j<CR>
nmap <silent> <c-h> :wincmd h<CR>
nmap <silent> <c-l> :wincmd l<CR>

tnoremap <leader>q <C-\><C-N>:bd!<CR>
tnoremap <Esc> <C-\><C-n>
tnoremap ii <C-\><C-n>
nnoremap <A-h> <C-w>h
nnoremap <A-j> <C-w>j
nnoremap <A-k> <C-w>k
nnoremap <A-l> <C-w>l

"4. Plugin's section
call plug#begin('~/.config/nvim/plugged')
Plug 'neoclide/coc.nvim', {'branch': 'release'}     "Coc server
Plug 'vim-airline/vim-airline'                      "Bottom and buffer bars
Plug 'vim-airline/vim-airline-themes'               "Themes for Airline
Plug 'bluz71/vim-nightfly-guicolors'                "Theme
call plug#end()

"4.1 Plugin's configuration
source ~/.config/nvim/coc-config.vim
let g:airline_theme = 'molokai'
let g:airline#extensions#hunks#enabled=0
let g:airline#extensions#branch#enabled=1
let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#formatter = 'unique_tail'

if !exists('g:airline_symbols')
  let g:airline_symbols = {}
endif
let g:airline_symbols.space = "\ua0"
let g:airline_powerline_fonts = 1

colorscheme nightfly    "Name of the theme
set background=dark     "Sets the background color

".5 Terminal configuration
function HrTermSplit()
    :sp
    :term
    :res 15
    :startinsert
endfunction
command Term call HrTermSplit()

