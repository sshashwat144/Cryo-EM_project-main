Loadings.ipynb - Used to try to find loadings (weight of each original image for each principal component), also used to find how SVD is used for PCA.
PCA_Accuracy.py - Used for determining SSIM and MSE of original images compared to reconstructed images
PCA_Combined.py - Used to plot SSIM, MSE, and Explained Variance of different principal components given input image stack
PCA_Plotter.py - Used to plot SSIM, MSE, and Explained Variance given text file of values
PCA_writer_script.py - Creates dictionary mapping peaks to certain images in the template stack, and loops and writes out principal components and specific reconstructed templates
PCA_writer.ipynb - Jupyter Notebook used to debug PCA_writer_script
Starfile_maker.py - using input theta and phi values, creates starfile to be used in project3D
Starfish_file_test copy.ipynb - used to debug Starfile_maker.py
convertFT.cpp - program used to perform fourier transform on image stack
cross_correlations_calculator.ipynb- was intended to calculate 2d cross correlations, but took too long for our purposes
eigenimageFinder.ipynb - File used to debug PCA_Accuracy
match_template_2D.cpp - was intended to change match_template.cpp from CisTEM to take in template stack rather than volume
old_convertFT.cpp - faulty version of convertFT.cpp
