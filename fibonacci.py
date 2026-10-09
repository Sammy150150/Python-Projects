fibonacci = [1, 1]
termsInSequence = int(input('Please enter number of terms: ')) - len(fibonacci)
for i in range(termsInSequence):
  nthTerm = fibonacci[-1] + fibonacci[-2]
  fibonacci.append(nthTerm)
print(fibonacci)
print("Program finished!")
