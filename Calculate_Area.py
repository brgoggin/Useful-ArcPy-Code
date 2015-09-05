#how to calculate area of polygon in ArcGIS

tempPgs = "ChTr0812"
arcpy.AddField_management(tempPgs, "PopDensity", "DOUBLE")
arcpy.CalculateField_management(tempPgs, "PopDensity", "(!Population! / !Shape_Area!)", "PYTHON_9.3")