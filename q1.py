def display(M = 3, N = 4):
    """Displays Triangles in python

    @param: positive integer
    @param: positive integer
    """
    for i in range(1, M+1):
        star_num = int(i*N/M)
        blank_num = N-star_num
        print(blank_num*' '+star_num*'* ')

display()

""" result:
   * 
  * * 
* * * * 
"""