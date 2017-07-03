data1={}
f2=open("final_3",'w')
f3=open('processedData_0.85.txt','r')
f4=open('corres','w')
wenben=f3.readlines()
final=[]
cankao={}
def newstring(ele):
	a=""
	for i in range(len(ele)-1):
		a+=ele[i]
	return a
with open("disease1",'r') as f:
	w=f.readlines()
	for string in w:
		if(string[0]=="*"):
			continue
		else:
			if(data1.has_key(string)):
				data1[string]+=1
			else:
				data1[string]=1
	hang=0
	final_index=0
	for index in range(len(w)):
		if(data1.has_key(w[index]) and data1[w[index]]>=10):
			number=-1
			if(cankao.has_key(w[index])):
				number=cankao[w[index]]
			else:
				cankao[w[index]]=final_index
				number=final_index
				final_index+=1
			final.append(newstring(wenben[index]))
			#final[-1]+=w[index]
			final[-1]+=str(number)
			final[-1]+='\n'
	print final_index
	for i in range(len(final)):
		f2.write(final[i])
	for i in cankao:
		f4.write(i)
		f4.write(' ')
		f4.write(str(cankao[i]))
		f4.write('\n')
	f4.close()
	f2.close()




