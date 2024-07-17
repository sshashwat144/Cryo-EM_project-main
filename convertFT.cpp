 //read mrc file
//perform fourier transform
//file name should be checked for mrc extension

// #include <iostream>
#include "../../core/core_headers.h"

class ConvertFT : public MyApp {
public:
    void DoInteractiveUserInput( );
    bool DoCalculation( );

private:
};

IMPLEMENT_APP(ConvertFT)

void ConvertFT::DoInteractiveUserInput( ) {
    UserInput* myInput = new UserInput("Perform Fourier Transform on image stack", 1.00);

    std::string input_mrc_filename = myInput->GetFilenameFromUser("Enter input MRC filename", "", "input.mrc", false);

    std::string output_filename = myInput->GetStringFromUser("Enter Output Filename", "", "output.mrc");

    delete myInput;

    my_current_job.Reset(2);

    my_current_job.ManualSetArguments("tt", input_mrc_filename.c_str( ), output_filename.c_str( ));
}

bool ConvertFT::DoCalculation( ) {
    std::string input_mrc_filename = my_current_job.arguments[0].ReturnStringArgument( );
    std::string output_filename    = my_current_job.arguments[1].ReturnStringArgument( );

    input_mrc_filename  = "/home/useradmin/Project_cisTEM/small_ribosome.mrc";

    Image current_image;

    Image temp_image;

    //mrc file name
    MRCFile mrc_file(input_mrc_filename);

    // Image* image_stack = new Image[mrc_file.ReturnNumberOfSlices()];

    // current_image.Allocate(current_image.logical_x_dimension, current_image.logical_y_dimension, 1);
    // mrc_file.OpenFile(input_mrc_filename);
    for ( int i = 0; i < mrc_file.ReturnNumberOfSlices( ); i++ ) {

        // image_stack[i].ReadSlice(&mrc_file, i +1);

        current_image.ReadSlice(&mrc_file, i + 1);

        temp_image.CopyFrom(&current_image);
        // current_image.QuickAndDirtyWriteSlice(output_filename, i + 1, false, 1.5);

        temp_image.ForwardFFT(false);
        temp_image.DivideByConstant(sqrt(current_image.number_of_real_space_pixels));
        temp_image.ComputeAmplitudeSpectrumFull2D(&current_image);
        current_image.ZeroCentralPixel( );
        current_image.QuickAndDirtyWriteSlice(output_filename, i + 1);
    }
    return true;
}

