set number
set relativenumber
set autowrite
filetype on
set softtabstop=4
set tabstop=4
set shiftwidth=4
set expandtab
syntax on
set incsearch
set ignorecase
set hlsearch
set ruler
autocmd BufNewFile *.cpp call append(0, ["#include <bits/stdc++.h>", "using namespace std;", "", "#define ll long long", "#define ar array", "", "int main(){", "   ios::sync_with_stdio(0    );", "    cin.tie(0);", "", " return 0;", "}"])
autocmd filetype python nnoremap <C-c> :w <bar> !python3 % <CR>
autocmd filetype cpp nnoremap <C-c> :w <bar> !g++ -std=c++17 % -o a.out <CR>
nnoremap <C-x> :w <bar> !./a.out <CR>
inoremap { {}<Esc>ha
inoremap ( ()<Esc>ha
inoremap [ []<Esc>ha
inoremap " ""<Esc>ha
inoremap ' ''<Esc>ha
inoremap ` ``<Esc>ha
augroup vimrc_python
    au!
    au FileType python nnoremap <buffer> <F9> :w <bar> !python3 %<CR>
augroup END
