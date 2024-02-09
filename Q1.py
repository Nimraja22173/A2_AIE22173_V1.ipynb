#1)Write a function to calculate the Euclidean distance and Manhattan distance between two vectors. The vectors dimension is variable.
import math
def euc_distance(vec1,vec2):
    distance=0
    for i in range(len(vec1)):
        distance += (vec1[i] - vec2[i]) ** 2
    return math.sqrt(distance)

def manhattan_distance(vec1,vec2):
    distance=0
    for i in range(len(vec1)):
        distance +=abs(vec1[i] - vec2[i])
    return distance

def main():
    vec1=input("enter the first vector: ").split()
    vec1=[int(x) for x in vec1]

    vec2=input("enter the first vector: ").split()
    vec2=[int(x) for x in vec2]

    euclidean=euc_distance(vec1,vec2)
    manhattan=manhattan_distance(vec1,vec2)

    print("euclidean distance:",euclidean)
    print("Manhattan distance:",manhattan)

if __name__=="__main__":
    main()
