#!/bin/sh

WHITE='#ffffffff'
BLANK='#00000000'  # blank

KEY='#000000aa'  # normal key color
BKEY='#e71414aa' # backspace

NORMAL='#1dd3bdee'  # default
WRONG='#e7305bee'
VERIFY='#438a5eee'
LINE='#0b0c08ee'
INSIDE='#00000044'

/usr/bin/i3lock \
\
--insidecolor=$INSIDE               \
--ringcolor=$NORMAL                 \
--linecolor=$BLANK                  \
--separatorcolor=$BLANK             \
\
--wrongcolor=$WRONG                 \
--insidewrongcolor=$INSIDE          \
--ringwrongcolor=$WRONG             \
--wrongtext="Nope!"                 \
\
--verifcolor=$VERIFY                \
--insidevercolor=$INSIDE            \
--ringvercolor=$VERIFY              \
--veriftext="Verifying"             \
\
--timecolor=$NORMAL                 \
--datecolor=$NORMAL                 \
--layoutcolor=$NORMAL               \
--keyhlcolor=$KEY                   \
--bshlcolor=$BKEY                   \
--noinputtext="Clean!"              \
\
--screen 1                          \
--blur 10                           \
--clock                             \
--indicator                         \
--radius 100                        \
--timestr="%H:%M"                   \
--datestr="%A, %m %Y"               \
--pass-screen-keys                  \
--ignore-empty-password             \
#--line-uses-ring			    \
#--keylayout 2         \

#--verifytext="Hmm...!" \
#--wrongtext="Nope!" \
# --textsize=20
# --modsize=10
# --timefont=comic-sans
# --datefont=monofur
# etc
