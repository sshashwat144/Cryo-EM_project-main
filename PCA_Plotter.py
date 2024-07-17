def Write_to_File(arr, folder_name):
    import os
    import matplotlib.pyplot as plt
    import numpy as np
    
    #Create folder
    newpath = r'/home/useradmin/Project_cisTEM/' + folder_name
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    
    arr = np.transpose(arr)
    
    plt.plot(arr[0], arr[1])
    plt.title("MSE Plot")
    plt.xlabel("Components")
    plt.ylabel("MSE")
    plt.savefig("MSE Plot.png")
    plt.close()
    os.rename("MSE Plot.png" , folder_name + "/MSE Plot.png")
    
    
    plt.plot(arr[0], arr[2])
    plt.title("SSIM Plot")
    plt.xlabel("Components")
    plt.ylabel("SSIM")
    plt.savefig("SSIM Plot.png")
    plt.close()
    os.rename("SSIM Plot.png" , folder_name + "/SSIM Plot.png")
    
    
    plt.plot(arr[0], arr[3])
    plt.title("Explained Variance Plot")
    plt.xlabel("Components")
    plt.ylabel("Explained Variance")
    plt.savefig("Explained Variance Plot.png")
    plt.close()
    os.rename("Explained Variance Plot.png" , folder_name + "/Explained Variance Plot.png")



def Read_File(toRead):
    
    import numpy as np
    
    again = np.loadtxt(toRead, skiprows=1)
    
    return again


    
    
def Main():
    
    toRead = input("Text file to Plot: ")
    file_name = input("Name of output folder: ")
    
    arr = Read_File(toRead)
    
    Write_to_File(arr, file_name)
    
    
    

Main()




