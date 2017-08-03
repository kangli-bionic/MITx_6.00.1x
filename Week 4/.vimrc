"Guide https://realpython.com/blog/python/vim-and-python-a-match-made-in-heaven/

set nocompatible                " required
filetype off                    " required

" Being Vundle stuff
" ----------------------------------------------------
" Set the runtime path to include Vundle and intialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()

" Let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" Add all the plugins here
" SimpylFold
Plugin 'tmhedberg/SimpylFold'

" Indent Python
Plugin 'vim-scripts/indentpython.vim'

" YouCompleteMe
Bundle 'Valloric/YouCompleteMe'

" Syntastic
Plugin 'scrooloose/syntastic'

" Vim-Flake8 for PEP8 checking
Plugin 'nvie/vim-flake8'

" Solarized
Plugin 'altercation/vim-colors-solarized'

"NERDTree for a proper file tree
Plugin 'scrooloose/nerdtree'

"ctrlP for searching anything from within Vim
Plugin 'kien/ctrlp.vim'

" Powerline for status bar
Plugin 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}

" NO PLUGINS AFTER the following line

call vundle#end()                " required
" -----------------------------------------------

filetype plugin indent on        " required

" Control how the splits happen
set splitbelow
set splitright

" Key Mappings
" Map the leader to space
:let mapleader=" "

" Split navigation shortcuts
" Ctrl-<hjkl> to move splits with standard Vim moves
nnoremap <C-J> <C-W><C-J>
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" Mapping for YCM
" Go to the definition else go to declaration
map <leader>g :YcmCompleter GoTo<CR>

" Enable folding
set foldmethod=indent
set foldlevel=99

" Enable folding with just the spacebar
nnoremap <space> za

" See the DocStrings for folded code
let g:SimpylFold_docstring_preview=1

" Indentation and Tabs
set tabstop=4
set softtabstop=4
set shiftwidth=4
set textwidth=79
set expandtab
set autoindent
set fileformat=unix
filetype indent on

"Search highligting and ignore case
set hlsearch ic

" UTF8 Support
set encoding=utf-8

" Syntax Highligting
let python_highlight_all=1
syntax on

" Line numbering with relative numbers for
" everything but the current line
set number
set relativenumber

" Solarized background
colorscheme solarized
set background=light
"set background=dark
" Switch solarized background with F5
call togglebg#map("<F5>")

" Copy to system clipboard
"set clipboard=unnamed

"YouCompleteMe settings
let g:ycm_key_list_select_completion = ['<C-j>', '<Down>']
let g:ycm_key_list_previous_completion = ['<C-k>', '<Up>']
let g:ycm_autoclose_preview_window_after_completion=1
     
" Vim-Powerline
set laststatus=2
set t_Co=256
