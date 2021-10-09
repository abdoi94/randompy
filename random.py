import sys
sys.stdout = open("log.txt", "w")

#####                   #####
## builtin list functions  ##
#####                   #####

nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

sys.stdout.close()