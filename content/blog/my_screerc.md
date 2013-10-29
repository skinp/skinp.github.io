Title: Starting things easily... My .screenrc
Date: 2013-10-29
Slug: starting-things-easily-my-screerc
Summary: Showing off my .screenrc config

A first blog post better be good right?
It better be original and try to get you some readers uh?

NO! You just want to test out if sh*t works...
So here it is, I'll just dump the content of my .screenrc:

    startup_message off
    nethack on
    defscrollback 5000

    shell -/bin/bash

    #termcapinfo xterm* 'is=\E[r\E[m\E[2J\E[H\E[?7h\E[?1;4;6l'

    hardstatus alwayslastline
    hardstatus string '%{= kG}%{g}[ %{G}%H %{g}][%= %{=kw}%?%-Lw%?%{r}(%{W}%n*%f%t%?(%u)%?%{r})%{w}%?%+Lw%?%?%= %{g}][ %{B}%Y-%m-%d %{W}%c %{g}]'

On a positive note, it could be usefull to someone...
