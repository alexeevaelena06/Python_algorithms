# Alekseeva Elena
"""
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""


# Recursive Python program
# to count total number of
# handshakes when a person
# can shake hand with only one.

# function to find all
# possible handshakes
def handshake(n):
    # when n becomes 0 that means
    # all the persons have done
    # handshake with other
    if (n == 0):
        return 0
    else:
        return (n - 1) + handshake(n - 1)

# Driver Code
n = 9
print(handshake(n))

