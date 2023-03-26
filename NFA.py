#facem citirea din fisier si creem un dictionar de date
f=open("inputNFA.txt")
s=f.readline()
stari_finale=s.strip().split()
print("stari finale="+s)
dictionardedate={}
s=f.readline()
while s!='':
    lista=s.strip().split()
    primel=lista[0]
    if primel not in dictionardedate:
        dictionardedate[primel]={}
    if lista[1] not in dictionardedate[primel]:
        dictionardedate[primel][lista[1]]=[lista[2]]
    else:
        dictionardedate[primel][lista[1]].append(lista[2])
    s=f.readline()
print(dictionardedate)

# #citim un cuvant
# #creem o variabila in care sa retinem starea curenta si un sir in care sa retin drumurile
drumuri="q0"
starecurenta='q0'
cuvant=input("cuvant= ")
b=1
ok=0
i=0
listadrumuri=[]
def Verificare_expresie(cuvant,expresie,starecurenta,drumuri,i):
    global ok
    if i == len(cuvant):
        if starecurenta in stari_finale:
            listadrumuri.append(drumuri)
            ok=1
            return
        else:
            return
    if cuvant[i] in dictionardedate[starecurenta]:    #parcurgem lista de tranzitii pentru fiecare stare
            for drum_posibil in range(len(dictionardedate[starecurenta][cuvant[i]])):
                drumuriposibile=drumuri[:]+dictionardedate[starecurenta][cuvant[i]][drum_posibil]
                starecurenta=dictionardedate[starecurenta][cuvant[i]][drum_posibil]
                Verificare_expresie(cuvant,cuvant[i+1:],starecurenta,drumuriposibile,i+1)
    else:
        print("Cuvantul nu este acceptat")

Verificare_expresie(cuvant,cuvant,starecurenta,drumuri,i)
if ok==0:
    print("Cuvantul nu este acceptat")
else:
    print("Cuvantul este acceptat")
    print(listadrumuri)