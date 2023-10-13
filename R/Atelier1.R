#Question 1
#Il faut évaluer l'intégrale(∫ x*sin(x)dx;) à l'aide d'intégration par partie
#Posons une variable u=x et la dérivé de la variable du=dx
#Posons la dérivé d'une autre variable dv=sin(x) et la variable est v=-cos(x)
#Avec cette information, il reste à le remettre dans l'équation: u*v-∫ v*du
x*cos(x)-∫ -cos(x)*dx
x*cos(x)+sin(x)
#Maintenant il faut l'évaluer pour les valeurs de (x=1 - x=0)
1*cos(1)+sin(1)= 0,301169

#Question 2
#Il faut créer deux matrices qui peuvent faire un produit de matrices
#Posons deux vecteurs qui seront les valeurs pour les matrices soient V1 pour la matrice A et V2 pour la matrice B
#Posons à la matrice A, une variable m égale au nombres de lignes, une variable p égale au nombre de colognes 
#Posons à la matrice B, une variable p égale au nombres de lignes, une variable n égale au nombre de colognes 
#Si le nombre de colognes dans la matrice A est égale au nombre de ligne de la matrice B
#Retourner le produit entre les deux matrices et le produit sera la matrice C
#Retourner le nombre de ligne et colognes de la matrice C, puis multiplier les deux pour avoir l'ordre de grandeur

#Question 3
#Dans cet algorithme, on débute avec les valeurs de x qui sont réels et positives
#De ce fait, la variable m est mal utilisé puisqu'elle est égale à 0 et une condition du code soit « (x[i]>m)».
#Pour tous valeur de X strictement positif et réel, il impossible que la condition soit fausse et que l'algorithme s'arrête

#Question 4
# a)
#Dans ce cas, nous avons un vecteur x des valeurs manquantes que je pose comme NA
x<-c(0,3,NA,4,5,6,NA,8,11,NA,15,NA,17,NA,19,20)
y<-x[!is.na(x)] #cette fonction permet d'enlever les Na et de garder les valeurs
y
#Avec la fonction lenght, on trouve le nombre de chiffre et le >12 pour ceux qui sont supérieur
w<-(y>12)
lenght(w)
# c)
#Avec la fonction mean, je vais trouver la moyenne. Puis si je soustrais 12 à q, je trouvé l'écart par rapport au valeurs
mean(w-12) 

srcdata
srcData <- getSourceData("script.R")
