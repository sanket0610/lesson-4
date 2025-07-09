#Counting notes
a=int(input("Enter amount"))
n1=a//500
n2=(a%500)//100
n3=((a%500)%100)//50

print("500RS notes:", n1)
print("100RS notes:", n2)
print("50RS notes:", n3)