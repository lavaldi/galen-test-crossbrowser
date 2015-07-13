========================================
image         css      .article-image
title         css      .article-title
excerpt       css      .article-excerpt
button        css      .article-button
========================================

@ *
--------------------

button 
    centered horizontally inside: parent

@@ if
image
    visible
@@ do

title
    below: image 5 to 20 px
@@ end    

excerpt
    below: title 5 to 20 px

button
    below: excerpt 5 to 20 px