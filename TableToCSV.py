"""
   This script will convert a table to a .csv file. It will transfer domain
   descriptions, rather than just their coded values
"""
import arcpy
import os
import csv
import domainvalues


def export_to_csv(dataset, output, dialect):
    """Output the data to a CSV file"""
    # create the output writer
    out_writer = csv.writer(open(output, 'wb'), dialect=dialect)
    # return the list of field names and field values
    header, rows = domainvalues.header_and_iterator(dataset)

    # write the field names and values to the csv file
    out_writer.writerow(map(domainvalues._encodeHeader, header))
    for row in rows:
        out_writer.writerow(map(domainvalues._encode, row))

if __name__ == "__main__":
    # Get parameters
    dataset_name = arcpy.GetParameterAsText(0)
    output_file = arcpy.GetParameterAsText(1)
    delim = arcpy.GetParameterAsText(2).lower()
    dialect = 'excel'
    if delim == 'comma':
        pass
    else:
        dialect = 'excel-tab'
    try:
        export_to_csv(dataset_name, output_file, dialect)
    except Exception as err:
        arcpy.AddError('Error: {0}'.format(err))
