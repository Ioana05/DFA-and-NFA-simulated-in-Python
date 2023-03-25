#Algoritm pentru DFA

# #facem citirea din fisier
# f=open("inputDFA.txt")
# s=f.readline()
# stari_finale=s.strip().split()
# print("stari finale="+s)
# dictionardedate={}
# s=f.readline()
# while s!='':
#     lista=s.strip().split()
#     primel=lista[0]
#     if primel not in dictionardedate:
#         dictionardedate[primel]={}
#     if lista[1] not in dictionardedate[primel]:
#         dictionardedate[primel][lista[1]]=lista[2]
#     else:
#         dictionardedate[primel].append(lista[2])
#     s=f.readline()
#
# print(dictionardedate)
#
# #citim un cuvant
# #creem o variabila in care sa retinem starea curenta si un sir in care sa retin drumurile
# drumuri=""
# starecurenta='q0'
# cuvant=input("cuvant= ")
# b=1
# ok=1
# for i in range(len(cuvant)): #parcurgem literele cuvantului
#     for l in dictionardedate[starecurenta]:    #parcurgem lista de tranzitii pentru fiecare stare
#         if cuvant[i]==l:
#             drumuri=drumuri[:]+dictionardedate[starecurenta][l]
#             starecurenta=dictionardedate[starecurenta][l]
#             b=1
#             break
#     if b==0:
#         print("Cuvantul nu este acceptat!")
#         ok = 0
#         break
# if starecurenta in stari_finale and ok==1 :
#     print("Cuvantul este acceptat")
#     print(drumuri)
# else:
#     print("Cuvantul nu este acceptat")
#
#
#
#
#
#
#
# # #am folosit dictionar in dictionar
# # Date={q0:{'1':q0,'0':q1}, q1={'1':q0,'0':q2}, q2={'2':q3}}

