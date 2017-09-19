I have generated random number using time.
time.time() provides us current time in miiliseconds.

So if we want to get range in [0 100), inclusive of 0 and exclusive of 100,
we can generate milliseconds and get last two digits of milliseconds everytime to generate a new random number.

So use a while loop to call generate_random(), then after calling
generate_random() function, use time.sleep() for generating some new value everytime after a little time lapse.

Now we want to get number greater than mid-value of range 73% of time, so set two counters, one for getting a number greater than mid-value and one for getting a value lower than mid-value.

Increment both the counters until they reach their max values.
For example in range of 0 to 100, 73 % of 100 is 73, so counter for greater values will be incremented until it reaches 73 and increment counter for lower values until it reaches 27.

Lets assume if lower number counter reaches its limit 27 first then we will ignore the values lower than 50, until, the higher counter reaches its limit 73 and we will only consider value which is greater then 73 and vice-versa.

Once both the counter reaches their max value we will break the loop.





 