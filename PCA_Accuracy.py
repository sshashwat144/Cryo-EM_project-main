

def load_MRC(file_path):
    import mrcfile 
    with mrcfile.open(file_path) as mrc:
        a= mrc.data

    return a


def apply_pca(image, n_components):
    from sklearn.decomposition import PCA
    pca = PCA(n_components=n_components)
    transformed_image = pca.fit_transform(image)
    return pca, transformed_image
    
def reconstruct_image(pca, transformed_image):
    reconstructed_image = pca.inverse_transform(transformed_image)
    return reconstructed_image


#get eigenimages
def reconstructed_Image_Getter(n_components, num_of_images, num_of_pixels, data):
    import numpy as np
    #reshape files so PCA can be done
    A=np.reshape(data,(num_of_pixels*num_of_pixels, num_of_images))
    
    pca, transformed =  apply_pca(A, n_components=n_components)
    e = pca.explained_variance_ratio_.sum()
    reconstructed = reconstruct_image(pca, transformed)
    
    return np.reshape(reconstructed, (num_of_images, num_of_pixels, num_of_pixels)), e


#For loop repeat for 1000 images
def avg_MSE(data, reconstructed):
    import numpy as np
    import random
    from sklearn.metrics import mean_squared_error
    from skimage.metrics import structural_similarity as ssim
    total = 0
    new_total = 0
    data_range = (np.amax(data) - np.amin(data))
    for i in range(1000):
        ind = random.randint(0, data.shape[0] -1)
        adder = mean_squared_error(data[ind], reconstructed[ind]) #mse calculation
        new_total += ssim(data[ind], reconstructed[ind], data_range = data_range) #ssim calculation
        total += adder
        
    return total/1000, new_total/1000

def create_File(output_file):
    f = open(output_file, "w")
    f = open(output_file, "a")
    f.write("Number_of_Components MSE SSIM Explained_Variance" + "\n")
    f.close()

def main():
    
    i = int(input("Initial number of components: "))
    max = int(input("Maximum number of components: "))
    increment = int(input("Component Increment: "))
    mrc_file = input("MRC file:")
    output_file = input("Output file name: ")

    a = load_MRC(mrc_file)

    
    
    create_File(output_file)

    while (i<=max):
    
        compressed, explained_variance = reconstructed_Image_Getter(i, a.shape[0], a.shape[1], a)
        val, new_val = avg_MSE(a, compressed)
        f = open(output_file, "a")
        f.write(str(i) + " " + str(val) +" "+ str(new_val) + " " + str(explained_variance) + "\n" )
        f.close()


    
        i += increment





main()