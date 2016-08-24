#how to calculate area of polygon in ArcGIS

tempPgs = "ChTr0812"
arcpy.AddField_management(tempPgs, "PopDensity", "DOUBLE")
arcpy.CalculateField_management(tempPgs, "PopDensity", "(!Population! / !Shape_Area!)", "PYTHON_9.3")

Floor Area & 0.56$^{**}$ & -0.05$^{**}$ & 0.24$^{**}$ & 0.03$^{**}$ \\
 & (0.08) & (0.03) & (0.04) & (0.05) \\
Home Age & 6.13$^{**}$ & 0.76$^{**}$ & -5.03$^{**}$ & -1.87$^{**}$ \\
 & (1.95) & (0.79) & (1.00) & (0.92) \\
Number of Measures & -31.24 & -2.25 & -34.85$^{**}$ & 1.66 \\
 & (18.39) & (7.79) & (10.11) & (11.76) \\
WAP & -521.37$^{**}$ & -155.82$^{*}$ & 94.98 & -568.16$^{**}$ \\
 & (148.17) & (61.84) & (79.40) & (85.75) \\
\hline \\


#Test#