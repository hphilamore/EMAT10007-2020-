# Part 5 - Using Data From imported les
# Python file to process the Douglas File
# At this point, the file has already been decrypted and saved separately
# using the Caesar cipher.

# Using numpy to compute max() and min() to have a nice plot for the 
# trend
import numpy as np

# Matplotlib to plot the data
from matplotlib import pyplot as plt

# GetData(Lines) -- Returns the data and the headers found in it
# The Lines should have been obtained elsewhere by the time this 
# function is called
def GetData(Lines):
	# SAMPLE MOISTURE KNOT_RATIO TREERING    E     DENSITY BEAMHEIGHT BENDING_STRENGTH
	# UNITS     %         -         MM     N/MM2    KG/M3      CM          N/MM2
	Data = {}
	# The Headers appear in the first line -- Obtaining them in an automated
	# fashion
	Headers = Lines[0].strip().split()
	for Header in Headers:
		Data[Header] = []

	# Saving all the data as a dictionary, in which each entry will contain
	# a list with the values to process
	for i in range(0, len(Lines)):
		Values = Lines[i].strip().split()
		for j in range(len(Headers)):
			# Need to convert to float if it is a number,
			# otherwise they will be treated as strings
			# by matplotlib and produce undesired results
			if Values[j].replace('.','').isnumeric():
				Data[Headers[j]].append(float(Values[j]))
			else:
				Data[Headers[j]].append(Values[j])
	return Data, Headers

# Getting the independent values and the coefficients, 
# This function can compute the expected values as per
# the trending line.
def FitData(x, Coeff):
	Fitted = []
	for i in X:
		NewX = 0
		for c in range(len(Coeff)):
			NewX += Coeff[c]*(i**(len(Coeff) - c - 1))
		Fitted.append(NewX)
	return Fitted

# To Compute the Root Mean Squared Error (RMSE)
# given the original and estimated data
def GetRMSE(x, y):
	RMSE = 0
	for xi, yi in zip(x,y):
		RMSE += (xi-yi)**2
	RMSE /= len(x)
	return RMSE**0.5

# 5.5.a The bending stiffness
# Given the whole data, this function calculates the bending stiffness
# and returns the result in the same format as the columns of the 
# original data
def GetBendingStiffness(Data):
	AllBendingStiffness = ['BENDING_STIFFNESS', 'N/MM']
	d = 100 # 10 cm = 100 mm
	for i in range(2,len(Data['E'])): # Skipping the first two rows
		L= Data['BEAMHEIGHT'][i]*10 - d # *10 to convert to mm
		I = 1/12 # b**4/12
		BendingStiffness = 3*Data['E'][i]*I/L
		AllBendingStiffness.append(BendingStiffness)
	return AllBendingStiffness

# 5.5.b Save in a CSV file
# Given the Data, this function saves the columns specified by Columns
# in a CSV file. The FilePath must contain the .CSV extension in it
def SaveCSV(Data, Columns, FilePath):
	f = open(FilePath, "w")
	NewContent = []
	for i in range(len(Data[Columns[0]])):
		NewLine = ""
		for Column in Columns:
			NewLine += str(Data[Column][i]).upper() + ","
		NewContent.append(NewLine + "\n")
	f.writelines(NewContent)
	f.close()


if __name__ == '__main__':
	# 5.1 Use your program to decrypt the le douglas data encrypted.txt
	# File containing the lines to process AFTER decryption
	FilePath = "douglas_data.txt"
	f = open(FilePath)
	Data = f.readlines()

	# Getting the data from file
	Data, Headers = GetData(Data)

	# Creating a linspace with values to plot the trend line
	X = np.linspace(np.array(Data['KNOT_RATIO'][2:]).min(), np.array(Data['KNOT_RATIO'][2:]).max(), 101)

	# Getting the coefficients assuming the polynomial to fit is of degree 2
	Coefficients = np.polyfit(Data['KNOT_RATIO'][2:], Data['BENDING_STRENGTH'][2:], 2)

	# Getting the fitted values correspondant to the knot ratios from the file
	FittedData = FitData(Data['KNOT_RATIO'][2:], Coefficients)

	# Getting the correspondant Y values for the X (for plotting purposes)
	FittedX = FitData(X, Coefficients)

	# Getting RMSE
	# 5.3 Find the RMSE for the raw data and tted data
	RMSE = GetRMSE(Data['BENDING_STRENGTH'][2:], FittedData)

	# 5.2 Plot the knot ratio against the bending strength of the beams.
	# Creating the figure. 
	# 5.4 It will be saved as PDF before closing it
	plt.figure()
	plt.scatter(Data['KNOT_RATIO'][2:], Data['BENDING_STRENGTH'][2:])
	plt.plot(X, FittedData, 'red')
	plt.xlabel('Knot Ratio')
	plt.ylabel('Bending Strength')
	plt.title("Knot Ratio vs Bending Strength\nRMSE = %.2f" % RMSE)
	plt.show()
	#Columns = ['sample', 'moisture', 'knot_ratio', 'treering', 'e', 'density', 'beamheight', 'bending_strength', 'bending_stiffness']"
	Data['BENDING_STIFFNESS'] = GetBendingStiffness(Data)

	# Saving to a CSV file
	Headers.pop(0)						# Removing "sample" column
	Headers.append('BENDING_STIFFNESS') # Adding new column "bending stiffness

	# Saving it in a CSV -- Using same filename with a different extension
	SaveCSV(Data, Headers, FilePath.replace('.txt', '.csv'))




