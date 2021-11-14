#-------------------------------------------------------------------------------
# Name:        Final Project
# Purpose:     Create domain definitions text files from database
#
# Author:      Artur Wojtas
#
# Created:     01-22-2019
# Copyright:   (c) Owner 2019
# Licence:     <your licence>
#
# NOTES
# To execute, enter path to Python environment from Arcgis, followed by scipt name and output path
# eg
# c:\Python27\ArcGIS10.6\python.exe ExportTables.py

import os
import traceback
import arcpy


def main():
    params = {"file": "Config.txt", 
        "folder": "domains"}      
    
    database, tables = getTableNames(params)
    print("Databse: {}".format(database))
    #print(tables)
    setup(params, database)
    createDomains(params, database, tables)


def getTableNames(params):
    '''
    Read file to find from which database domain tables have to be created
    '''
    print("Get Table Names")
    with open(params["file"], "r") as infile:
        database = infile.readline().strip('\n')
        tables = []
        for each in infile:
            tables.append(each.strip('\n'))

        return database, tables


def setup(params, database):
    '''
    Setup environment and create folder for domain files
    '''
    print("Setup workspace")
    current = os.getcwd()
    arcpy.env.workspace = os.path.join(current, database)    
    arcpy.env.scratchWorkspace = current
    arcpy.env.overwriteOutput = True

    product = arcpy.ProductInfo()
    print(product)
    print("{}: {}".format(product, arcpy.CheckProduct(product)))

    #Create domains folder if it doesn't exists
    txt = os.path.join(current, params['folder'])     
    if not os.path.exists(txt):
        os.mkdir(txt)


def createDomains(params, database, tables):
    '''
    Create domain definition for each table
    '''
    print("Create domains files")
    current = os.getcwd()
    txtFolder = os.path.join(current, params["folder"])    

    for each in tables:
        print(" {}".format(each))
        txtFile = os.path.join(txtFolder, each + ".txt")
        with open(txtFile, "w") as domainFile:
            fieldNames = arcpy.ListFields(each)
            col1 = fieldNames[0].name
            col2 = fieldNames[1].name
        
            cursor = arcpy.SearchCursor(each)
        
            for row in cursor:
                value = row.getValue(col1)
                desc = row.getValue(col2)
                #print("{} {}".format(value, desc))
                domainFile.write("{}, {}\n".format(value, desc))


if __name__ == "__main__":        
    main()

else:
    print("Importing {}".format(__name__))
