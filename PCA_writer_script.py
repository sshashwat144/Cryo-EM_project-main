def get_mapper(max_diff, starfile):
    import numpy as np
    star = np.loadtxt("peaks.txt")
    important = star[:, 3:6]
    big_star = np.loadtxt(starfile, skiprows=30)
    big_important = big_star[:, 1:4]
    
    mapper = {}
    max_diff = max_diff
    for i in range(important.shape[0]):
        possible = []
        for j in range(big_important.shape[0]):
            if(abs(important[i][0] - big_important[j][0]) <= max_diff):
                possible.append(j)
    
        k = 0
        while(k<len(possible)):
        # if(k>= len(possible)):
        #     continue
        
            if(abs(important[i][1] - big_important[possible[k]][1]) > max_diff):
                possible.pop(k)
                k-=1
            k+=1
        l = 0
        while(l<len(possible)):
            # if(l>= len(possible)):
            #     continue
            
            if(abs(important[i][2] - big_important[possible[l]][2]) > max_diff):
                possible.pop(l)
                l-=1
            l+=1
        mapper[i] = possible
        # print(i)
    
    
    count  = []
    for i in range(len(mapper)):
        if len(mapper[i]) ==0:
            count.append(i)
            
            
            
    print(count)
    max_diff += 10
    for i in count:

        possible = []
        for j in range(big_important.shape[0]):
            if(abs(important[i][0] - big_important[j][0]) <= max_diff):
                possible.append(j)
                
        
        k = 0
        while(k<len(possible)):
            # if(k>= len(possible)):
            #     continue
            
            if(abs(important[i][1] - big_important[possible[k]][1]) > max_diff):
                possible.pop(k)
                k-=1
            k+=1
        l = 0
        while(l<len(possible)):
            # if(l>= len(possible)):
            #     continue
            
            if(abs(important[i][2] - big_important[possible[l]][2]) > max_diff):
                possible.pop(l)
                l-=1
            l+=1
        mapper[i] = possible
        

    
    
    correct_mapper = {}

    for key, val in mapper.items():
        smallest = 100
        index = None
        for i in val:
            diff = abs(important[key][0] - big_important[i][0]) + abs(important[key][1] - big_important[i][1]) + abs(important[key][2] - big_important[i][2])
            if(diff < smallest):
                smallest = diff
                index = i
        correct_mapper[key] = index
    
    print(correct_mapper)    
        
    return correct_mapper



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

def main():
    
    import mrcfile 
    import numpy as np
    import os
    
    path = input("MRC File (Templates): ")
    folder = input("Folder Name:")
    max_diff = int(input("Maximum difference in angles: "))
    starfile = input("Starfile: ")
    

    correct_mapper = get_mapper(max_diff, starfile)

    
    templates = load_MRC(path)
    num_of_images = templates.shape[0]
    x_pixels = templates.shape[1]
    y_pixels = templates.shape[2]

    # #Create folder
    # newpath = r'/home/useradmin/Project_cisTEM/' + folder
    # if not os.path.exists(newpath):
    #     os.makedirs(newpath)

    i = 1
    while(i<=5):
        A=np.reshape(templates,(x_pixels*y_pixels, templates.shape[0]))
        pca_mrc, pca = apply_pca(A, i)
        r = reconstruct_image(pca, pca_mrc)
        reconstructed = np.reshape(r, (num_of_images, x_pixels, y_pixels))
        rec_matrix = np.zeros((92, templates.shape[1], templates.shape[2]), dtype='float32')
    
        for key, val  in correct_mapper.items():
            rec_matrix[key] = reconstructed[val]
        
        
    
    

    
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
            mrc.set_data(rec_matrix)

        mrc.close()
    
        i +=  1

        os.rename("PCA " +name, folder + "/" + "PCA " +name)
        os.rename("Reconstructed " +name, folder + "/" + "Reconstructed " +name)
    
    
main()