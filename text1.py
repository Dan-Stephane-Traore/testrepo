
def operation():
    
    print("***************************************")
    print("********** Calculatrice ***************")
    print("***************************************")
    
    
    
    
    while True:
        print("Operation")
    
            
        print("1. Addition \n 2.Soustraction \n 3.Multiplication \n 4.Division \n 5.Quitter")
        
        choix = int(input("Taper votre choix:"))
        print("")
        
        
        
        if(choix == 1):
            n1 = float(input("Tapper le premier nombre:"))
            
            n2 = float(input("Tapper le deuxieme nombre:"))
            
            somme = n1 + n2
            print(f"la Somme est: {somme}")
            
        
        elif(choix == 2):
            n1 = float(input("Tapper le premier nombre:"))
           
            n2 = float(input("Tapper le deuxieme nombre:"))
            
            soustraction = n1 - n2
            print(f"le resultat est: {soustraction}")
            
            
        elif(choix == 3):
            n1 = float(input("Tapper le premier nombre:"))
           
            n2 = float(input("Tapper le deuxieme nombre:"))
            
            Multiplication = n1 * n2
            print(f"le resultat est: {Multiplication}")
            
            
        elif(choix == 4):
            n1 = float(input("Tapper le premier nombre:"))
            
            n2 = float(input("Tapper le deuxieme nombre:"))
            
            if( n2 == 0):
                print("impossible")
            else:
                
                n1 = float(input("Tapper le premier nombre:"))
                
                n2 = float(input("Tapper le deuxieme nombre:"))
                
                Division = n1 / n2
                print(f"le resultat est: {Division}")
               
                
        elif(choix == 5):
            exit()
        
        else:
            print("***** Erreur   de choix.????  veuiller choisir entre 1 - 4 *****")
            
            

                
            
operation()       
            
            
        
    
    
    

    
