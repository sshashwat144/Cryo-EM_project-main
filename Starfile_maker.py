def main():
    import numpy as np

    original = input("Theta and Phi value text file: ")
    psi_inc = input("Psi increment: ")
    output = input("Output Star file name:")
    name = input("User Name: ")
    again = np.loadtxt(original)
    psi_max = 360.0
    psi_num = psi_max/float(psi_inc) 
    cols = again.shape[0] * psi_num
    cols = int(cols)
    print("Columns: " + str(cols))
    newArr = np.zeros([cols, 24])

    for i in range(cols):

        newArr[i][0] = i +1 #position
        newArr[i][1] = (i *1.5) % 360 #psi
        newArr[i][2] = again[int((i // psi_num))][0] #theta
        newArr[i][3] = again[int((i // psi_num))][1] #Phi
        newArr[i][10] = 1 #pshift
        newArr[i][11] = 1.00 #stat
        newArr[i][16] = 1.5 #pixel size
        newArr[i][17] = 300.00 # volt
        newArr[i][18] = 2.70 #cs
        newArr[i][19] = .0700 #ampc
    
    f = open(output, "w")
    f = open(output, "a")
    header = add(name)

    np.savetxt(output, newArr, delimiter=' ', fmt='%i %f %f %f %f %f %f %f %f %f %i %f %f %f %f %f %f %f %f %f %f %f %f %f', header = header, comments = '')
    



    f.close()
    
def add(name):
# # Written by Raison on 2024-06-21 10:09:15
    toWrite = "# Written by " + name + '\n'  + '\n'
# data_
    toWrite += "data_" +'\n' +'\n' 
    toWrite += "loop_" + '\n'
    
 
# loop_
    toWrite += "_cisTEMPositionInStack #1" +'\n' + "_cisTEMAnglePsi #2" +'\n' + "_cisTEMAngleTheta #3" +'\n' + "_cisTEMAnglePhi #4" +'\n' + "_cisTEMXShift #5" +'\n' + "_cisTEMYShift #6" +'\n' + "_cisTEMDefocus1 #7" +'\n' + "_cisTEMDefocus2 #8" +'\n' + "_cisTEMDefocusAngle #9" +'\n' + "_cisTEMPhaseShift #10" +'\n' + "_cisTEMImageActivity #11" +'\n' + "_cisTEMOccupancy #12" +'\n' + "_cisTEMLogP #13" +'\n' + "_cisTEMSigma #14" +'\n' + "_cisTEMScore #15" +'\n' + "_cisTEMScoreChange #16" +'\n' + "_cisTEMPixelSize #17" +'\n' + "_cisTEMMicroscopeVoltagekV #18" +'\n' + "_cisTEMMicroscopeCsMM #19" +'\n' + "_cisTEMAmplitudeContrast #20" +'\n' + "_cisTEMBeamTiltX #21" +'\n' + "_cisTEMBeamTiltY #22" +'\n' + "_cisTEMImageShiftX #23" +'\n' + "_cisTEMImageShiftY #24" +'\n'
    toWrite += "#    POS     PSI   THETA     PHI       SHX       SHY      DF1      DF2  ANGAST  PSHIFT  STAT     OCC      LogP      SIGMA   SCORE  CHANGE    PSIZE    VOLT      Cs    AmpC  BTILTX  BTILTY  ISHFTX  ISHFTY"
    return toWrite


main()