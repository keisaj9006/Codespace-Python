# Initialize first two numbers of the series in a list
fibSeries = [0, 1]

i = 0 # index

while True:
    # Calculate next number in series
    nextNum = fibSeries[i] + fibSeries[i+1]

    # Check if number is not within the range
    if nextNum > 50:
        break # break the loop if out of range
    
    # Add number to series
    fibSeries.append(nextNum)

    i = i + 1 # increment index
    
# Print a list with the series    
print(fibSeries)