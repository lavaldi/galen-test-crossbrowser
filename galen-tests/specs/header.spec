=========================================
header             css    .header
header-content     css    .header-content

brand              css    .brand
brand-logo         css    .brand-logo
brand-name         css    .brand-name

nav                css    .main-nav
nav-item-*         css    .main-nav > ul > li

toggle             css    .main-nav-toggle
=========================================


@ *
--------------------
header
    width: 100% of screen/width


header-content
    centered horizontally inside: header

brand 
    inside: header-content 0px top left
    height: 60px
    
brand-logo
    inside: brand 0px left
    height: 27px
    width: 26px


@ mobile 
------------------

header-content
    width: 80 to 100 % of header/width

brand-name
    absent

@@ if

nav 
    visible
@@ do

nav-item-*
    width: 100% of header-content/width

@@ end


@ desktop
------------------

header
    inside: screen 0px top left right
    height: 60px

header-content
    width: < 961px

brand-logo
    centered vertically inside: header 5px

brand-name 
    near: brand-logo 5 to 20px right
    text is: Galen Framework

toggle
    absent


nav 
    inside partly: header-content ~ 0px right

# Checking that all menu items 
# are actually located completely inside menu
nav
    contains: nav-item-*    

# Checking that every item of menu
# is located next to following
# item with 0 pixel margin
#
# Also we check that both items
# are aligned horizontally
# by both sides: top and left

[ 1 - ${count("nav-item-*")-1} ]
nav-item-@
    near: nav-item-@{+1} ~ 0px left
    aligned horizontally: nav-item-@{+1}

# The last item
nav-item-${count("nav-item-*")}
    inside: nav ~ 0px right
    aligned horizontally: nav-item-${count("nav-item-*")-1}