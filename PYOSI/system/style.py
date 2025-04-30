class style:
    bold = print("\033[1")
    light = print("\033[2")
    italic = print("\033[3")
    underline = print("\033[4")
    slowblink = print("\033[5")
    fastblink = print("\033[6")
    revcolor = print("\033[7")
    hide = print("\033[8")
    deline = print("\033[9")
    upline = print("\033[53")

class cur:
    hide = print("\033[?25l")
    show = print("\033[?25h")
