def grille_vide():
    grille=[[0 for j in range(7)] for i in range(6)]
    return grille
assert len(grille_vide())==6
assert len(grille_vide()[0])==7
grille_vide()

def affiche(grille):
    num=['  0 ','1 ','2 ','3 ','4 ','5 ','6 ']
    n=6
    for k in num:
        print(k, end='')
    print('')
    for i in grille:
        n=n-1
        print(n, end='')
        for j in i:
            if j==0:
                print('|.', end='')
            if j==1:
                print('|x', end='')
            if j==2:
                print('|O', end='')
        print("|")


def coup_possible(grille, col):
        if grille[0][col]==1:
            return False
        if grille[0][col]==2:
            return False
        if grille[0][col]==0:
            return True
assert coup_possible(grille_vide(),0)==True
assert coup_possible([[0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 2, 0, 0]],3)==False

def jouer(grille, j, col):
    k=[5,4,3,2,1,0]
    for i in k:
        if grille[i][col]==0:
            if j==1:
                grille[i][col]=1
                return grille
            if j==2:
                grille[i][col]=2
                return grille
assert jouer(grille_vide(),1,2)==[[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0]]
assert jouer([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 2, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0]],2,2)==[[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 2, 0, 0, 0, 0],
 [0, 0, 2, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0]]

def horiz (gril, j, lig):
    tabl=gril
    m=0
    if tabl[lig][0]==j and tabl[lig][1]==j and tabl[lig][2]==j and tabl[lig][3]==j:
        return True
    else :
        return False
    if tabl[lig][1]==j and tabl[lig][2]==j and tabl[lig][3]==j and tabl[lig][4]==j:
        return True
    else:
        return False
    if tabl[lig][2]==j and tabl[lig][3]==j and tabl[lig][4]==j and tabl[lig][5]==j:
        return True
    else:
        return False
    if tabl[lig][3]==j and tabl[lig][4]==j and tabl[lig][5]==j and tabl[lig][6]==j:
        return True
    else:
        return False     

assert horiz([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [1, 1, 1, 2, 1, 0, 0]],1,5)==False
assert horiz([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [2, 2, 2, 2, 0, 0, 0]],2,5)==True

def vert (gril, j, lig, col):
    tabl=gril
    if lig>2:
        return False
    if tabl[lig][col]==j and tabl[lig+1][col]==j and tabl[lig+2][col]==j and tabl[lig+3][col]==j:
        return True
    else :
        return False
assert vert([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 0, 0]],1,2,0)==False
assert vert([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [2, 0, 0, 0, 0, 0, 0],
 [2, 0, 0, 0, 0, 0, 0],
 [2, 0, 0, 0, 0, 0, 0],
 [2, 0, 0, 0, 0, 0, 0]],2,2,0)==True

def diag_haut(grille, j, lig, col):
    n=1
    if lig<3:
        return False
    if col>3:
        if grille[lig-1][col-1]==j:
            n+=1
        if grille[lig-2][col-2]==j:
            n+=1
        if grille[lig-3][col-3]==j:
            n+=1
        if n==4:
            return True
    n=1
    if col<3:
        if grille[lig-1][col+1]==j:
            n+=1
        if grille[lig-2][col+2]==j:
            n+=1
        if grille[lig-3][col+3]==j:
            n+=1
        if n==4:
            return True
    n=1  
    if col==3:
        if grille[lig-1][col-1]==j:
            n+=1
        if grille[lig-2][col-2]==j:
            n+=1
        if grille[lig-3][col-3]==j:
            n+=1
        if n==4:
            return True
        n=1
        if grille[lig-1][col+1]==j:
            n+=1
        if grille[lig-2][col+2]==j:
            n+=1
        if grille[lig-3][col+3]==j:
            n+=1
        if n==4:
            return True
    else:
        return False
assert diag_haut([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0]],1,5,1)==False
assert diag_haut([[1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0]],1,5,3)==True


def diag_bas(grille, j, lig, col):
    n=1
    if lig>2:
        return False
    if col>3:
        if grille[lig+1][col-1]==j:
            n+=1
        if grille[lig+2][col-2]==j:
            n+=1
        if grille[lig+3][col-3]==j:
            n+=1
        if n==4:
            return True
    n=1
    if col<3:
        if grille[lig+1][col+1]==j:
            n+=1
        if grille[lig+2][col+2]==j:
            n+=1
        if grille[lig+3][col+3]==j:
            n+=1
        if n==4:
            return True
    n=1  
    if col==3:
        if grille[lig+1][col-1]==j:
            n+=1
        if grille[lig+2][col-2]==j:
            n+=1
        if grille[lig+3][col-3]==j:
            n+=1
        if n==4:
            return True
        n=1
        if grille[lig+1][col+1]==j:
            n+=1
        if grille[lig+2][col+2]==j:
            n+=1
        if grille[lig+3][col+3]==j:
            n+=1
        if n==4:
            return True
    else:
        return False
assert diag_bas([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0]],1,5,1)==False
assert diag_bas([[1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0]],1,2,0)==True
  
def victoire (gril, j, lig, col):
    if horiz(gril, j, lig)==True or vert (gril, j, lig, col)==True or diag_haut(gril,j,lig,col)==True or diag_bas(gril,j,lig,col)==True:
        return True 
    else: 
        return False
assert victoire([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 1, 0, 0, 0],
 [0, 1, 0, 1, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0]],1,2,3)==True
assert victoire([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 1, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0]],1,2,3)==False


def match_nul(gril,j, col, lig):
    for k in range(1,3):
        for l in range(7):
            for z in range(6):
                if victoire(gril, k , z, l)==False: 
                    if coup_possible(gril, l)==False:
                        return True
    return False
assert match_nul([[1, 1, 2, 2, 1, 2, 1],
 [1, 1, 2, 1, 2, 2, 1],
 [2, 1, 2, 2, 1, 2, 2],
 [2, 2, 1, 2, 2, 1, 1],
 [2, 1, 1, 2, 2, 1, 2],
 [1, 2, 1, 1, 2, 1, 1]],1,1,1)==True
assert match_nul([[0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 0, 0],
 [0, 1, 0, 0, 0, 0, 0],
 [0, 0, 1, 0, 0, 0, 0],
 [0, 0, 0, 1, 0, 0, 0]],1,1,1)==False

