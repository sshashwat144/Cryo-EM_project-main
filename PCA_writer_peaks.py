



def load_MRC(file_path):
    import mrcfile 
    with mrcfile.open(file_path) as mrc:
        a= mrc.data

    return a

def apply_pca(image, n_components):
    import numpy as np
    from sklearn.decomposition import TruncatedSVD
    pca = TruncatedSVD(n_components=n_components)
    image = image - (np.mean(image))
    transformed_image = pca.fit_transform(image)
    return transformed_image,pca

def reconstruct_image(pca, transformed_image):
    reconstructed_image = pca.inverse_transform(transformed_image)
    return reconstructed_image

# def create_File(output_file):
#     f = open(output_file, "w")
#     f = open(output_file, "a")
#     f.write("Number_of_Components Explained_Variance" + "\n")
#     f.close()



def main():
    
    import mrcfile 
    import numpy as np
    import os
    
    path = input("MRC File (Templates): ")
    folder = input("Folder Name:")
    i = int(input("Initial number components: "))
    ma = int(input("Maximum number of components: "))
    inc = int(input("Components increment: "))
    output_file = "Explained Variance"
    f = open(output_file, "w")
    f = open(output_file, "a")
    f.write("Number_of_Components Explained_Variance" + "\n")
    f.close()


    
    templates = load_MRC(path)
    num_of_images = templates.shape[0]
    x_pixels = templates.shape[1]
    y_pixels = templates.shape[2]

    # #Create folder
    # newpath = r'/home/useradmin/Project_cisTEM/' + folder
    # if not os.path.exists(newpath):
    #     os.makedirs(newpath)

    
    while(i<=ma):
        A=np.reshape(templates,(x_pixels*y_pixels, templates.shape[0]))
        pca_mrc, pca = apply_pca(A, i)
        e = pca.explained_variance_ratio_.sum()
        r = reconstruct_image(pca, pca_mrc)
        reconstructed = np.reshape(r, (num_of_images, x_pixels, y_pixels))


        
        
    
    

    
        name = str(i) + " components " + "ribosome.mrc"
        with mrcfile.new("PCA " + name, overwrite=True) as mrc: 
        # first = np.array()
        # for key, val in mapper:
        #     first = np.append(first, pca_mrc[val])
        #     first = np.reshape(first, (i, templates.shape[1], templates.shape[2]))
        

            mrc._set_voxel_size(1.5, 1.5, 1.5)

    

            mrc.set_data(np.reshape(pca_mrc, (i, x_pixels, y_pixels)))

        mrc.close()


        with mrcfile.new("Reconstructed " + name, overwrite=True) as mrc: 
        # first = np.zeros(())
        # for key, val in mapper:
        #     first = np.append(first, reconstructed[val])
        #     first = np.reshape(first, (i, templates.shape[1], templates.shape[2]))
        

            mrc._set_voxel_size(1.5, 1.5, 1.5)
            mrc.set_data(reconstructed[num_of_images-1])

        mrc.close()
        
        f = open(output_file, "a")
        f.write(str(i) + "     " + str(e) + "\n" )
        f.close()

        i +=  inc

        os.rename("PCA " +name, folder + "/" + "PCA " +name)
        os.rename("Reconstructed " +name, folder + "/" + "Reconstructed " +name)
    os.rename(output_file, folder + "/" + output_file)
        
    
    
main()