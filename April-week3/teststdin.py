#Import System module
import sys

print("Enter a number")
#input is read using stdin
x=int(sys.stdin.readline())
print(x)

#output printed using stdout
sys.stdout.write('This is stdout text\n')

#Error message is shown using stderr
sys.stderr.write('This is a stderror\n')
