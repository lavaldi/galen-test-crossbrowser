===============================================
footer             css       .footer
footer-content     css       .footer .footer-content
footer-brand       css       .footer-brand
links              css       .footer-links
link-*             css       .footer-links li  
===============================================

@ *
------------------
footer
    width: 100% of screen/width

footer-content
    centered horizontally inside: footer

link-1
    aligned horizontally all: link-2

@ mobile
------------------
footer-brand, links
    centered horizontally inside: footer-content


@ desktop
------------------
footer-brand
    inside: footer-content 0px left
    centered vertically inside: footer-content 3px

links
    inside: footer-content 0px right
    centered vertically inside: footer-content 3px       
