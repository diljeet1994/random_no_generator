import time;
# generate random no using time module
def generate_random(c, d):
    ticks = int(time.time())
    if (d <= 0):
        return 0
    c = d-1
    c = str(c)
    length = len(c)
    rand=''
    # get random value as per the length of value of max range, for ex b=100, then lenght is 2
    while(length > 0):
        ticks, r = divmod(ticks,10)
        rand = rand+ str(r)
        length = length - 1
    return(int(rand))


#Provide the range, for ex a=0 and b=100
# here a and b is the range of random no
a = int(input('enter the initial range : '))  
b = int(input('enter the final range : '))

lowerPercent = (b*27)//100 -1

lower_no = 0
higher_no = 0
low = False
high=False
lowList=[]
highList=[]

while(True):
    rand = generate_random(a, b)
    # get new value after a timelapse
    time.sleep(1.25)
    
    # if both the counter reaches their max value we will break the loop.
    if((higher_no > (b - lowerPercent)) and ( lower_no > lowerPercent)):
        break
    
    # lower counter reaches its max value first then we will ignore the values lower than 50.
    if(lower_no > lowerPercent):
        low = True
        rand = generate_random(a, b)

    # higher counter reaches its max value first then we will ignore the values greater than 50.
    if(higher_no > (b - lowerPercent)):
        high = True
        rand = generate_random(a, b)

    # if we get higher value then increment higher_no counter else increment lower_no counter else continue
    if(rand >= (b//2) and not high):
        higher_no = higher_no + 1
        highList.append(rand)
    elif(not low):
        lower_no = lower_no + 1
        lowList.append(rand)
    else:
        continue
    print(rand)
  
print("Total High Element Printed ", end='')
print(len(highList))
print(sorted(highList))

print("Total Low Element Printed ", end='')
print(len(lowList))
print(sorted(lowList))

