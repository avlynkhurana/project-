names = "John, Jennie, Jim, Jack, Joe"
print("names:",names)
#strings are immutable
upper_case_names=names.upper()
print("names now are:",names,id(names))
print("upper_case_names now:",upper_case_names,id(upper_case_names))
print("upper_case_names check:",upper_case_names.isupper())
s1=names.capitalize()
s2=names.title()
s3=names.swapcase()
s4=names.replace('J','KO')

print("s1:",s1)
print("s2:",s2)
print("s3:",s3)
print("s4:",s4)

password = input("Enter Your Password")
#rstrip(),lstrip()
print("Password:",password.strip())

data = '0000000035698700'
print("data:",data.strip('0'))

number = 3.560000
number = float(str(number).strip('0'))
print(number,type(number))

message="No Internet Connectivity"
print(message)
print(message.center(50))
print(message.ljust(50))
print(message.rjust(50))

data = "545"
print(data.zfill(50))

quote="search the candle rather than cursing the darkeness"
print(quote.find('sing'))
print(quote.find('the'))
print(quote.index('the'))
print(quote.rindex('the'))
print(quote.index('candle'))
idx1=quote.index('candle')
idx2=idx1+len('candle')
print("idx1:",idx1)
print("idx2:",idx2)
print(quote[idx1:idx2])
for ch in quote:
    print(ch,end=" ")
