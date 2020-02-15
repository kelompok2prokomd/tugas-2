# function
def lingkaran(r):
  return 22/7*r*r

if __name__ == "__main__":

    print("Menghitung Luas Lingkaran \n")
 
    r = int(input("Masukkan jari-jari: "))
    print("Rumus Luas Lingkaran = 22/7 * r * r")

    # variable
    a = lingkaran(r) # calculate area; then store in a and also are variable
    
    # branching => if elif else
    threshold = 100
    
    if (r > (threshold+1)):
      print("size: {} more than threshold: {}".format(r, threshold))
    elif( r == threshold):
      print("size: {} equal with threshold: {}".format(r, threshold))
    else:
      print("size: {} less than threshold: {}".format(r, threshold))
    
    print("\n")

    print("Luas Lingkaran adalah = {}".format(a))
