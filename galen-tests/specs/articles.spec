=========================================
title            css    .section-title
content          css    .section

article-*        css    .article
=========================================

@ *
--------------------
content
    centered horizontally inside: header

title
    centered horizontally inside: content

article-*
    component: article.spec
	

@ mobile
--------------------
content
    width: 80 to 100 % of header/width

article-*
    width: 100% of content/width

@ desktop
--------------------

content
    width: < 961px

article-*
    width: 30 to 35 % of content/width