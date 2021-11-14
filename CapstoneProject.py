#-------------------------------------------------------------------------------
# Name:        Final Project
# Purpose:     Create domains and fields for avalanche point feature class 
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
# c:\Python27\ArcGIS10.6\python.exe CapstoneProject.py g:\Workspace
#Make sure Workspace folder already exists
#
# Python located under c:\User\user\AppData\Local\Programs\Python
##
#-------------------------------------------------------------------------------

import sys, time, os, traceback, datetime, argparse
import arcpy
import Fields as fl
import Domains as dom

#import arcpy.da as da
#import arcpy.sa as sa

def main(dataFolder):
    params = {"dataFolder" : dataFolder, "domainsFolder" : "domains",
        "dataset": {"base" : "Base", "editable" : "Editable"},   
        "database" : "GEOS459AvalancheDataCaptureProject.gdb",
        "fc" : "AvalancheEvents",        
        "gemoetryType" : "POINT",        
        'spatialRef' : 3857} #WGS84 Web Mercator 

    setupWorkspace(params)
    createDatabase(params)
    createDataset(params)
    createFeatureClass(params)
    createDomains(params)        
    sortSelectedDomains(params)    
    createFields(params)     
    assignDefaultValue(params)    
    #listFields(params)
    

def printError():
    tb = sys.exc_info( )[2]
    tbinfo = traceback.format_tb( tb )[0]
    pymsg = "PYTHON ERRORS:\nTraceback info:\n" + tbinfo + "\nError \
    Info:\n" + str( sys.exc_info( )[1] )    
    print(pymsg)


def wait(delay):
    '''
    Delay function in seconds
    delay   : integer
            delay in seconds
    '''
    for i in reversed(range(1,delay + 1)):
        #print("Wait {0} sec".format(i))
        time.sleep(1)
        

def setupWorkspace(params):
    '''    
    Setup workspace for the project
    '''
    print("Set up workspace...")
    workspace = params["dataFolder"] #os.path.join(params["dataFolder"], params["database"])

    arcpy.env.workspace = workspace
    arcpy.env.scratchWorkspace = workspace
    arcpy.env.overwriteOutput = True    
    
    product = arcpy.ProductInfo()
    print(product)
    print("{}: {}".format(product, arcpy.CheckProduct(product)))


def createDatabase(params):
    '''
    Create database for the project
    '''
    print("Creating database...")
    try:
        database = params["database"]
        if arcpy.Exists(database):
            print("Delete existing database: {0}\n".format(database))
            arcpy.Delete_management(database)
            #print(arcpy.GetMessages())            
    
        arcpy.CreateFileGDB_management(params["dataFolder"], params["database"])
        #print(arcpy.GetMessages())        
        wait(3) #Wait for database creation        
    except:
        printError()


def createDataset(params):
    '''
    Create base and editable datasets for the project
    '''
    print("Creating datasets...")
                      
    spatialRef = arcpy.SpatialReference(params["spatialRef"])
    arcpy.env.workspace = os.path.join(params["dataFolder"], params["database"])  
        
    for dataset in params["dataset"]:
        try:
            d = params["dataset"][dataset]
            arcpy.CreateFeatureDataset_management(arcpy.env.workspace, d, spatialRef)           
        except:
            printError()


def createFeatureClass(params):
    '''
    Create feature class for avalanche events   
    '''
    print("Creating feature class...")
        
    fc = params["fc"]
    dataset = params["dataset"]["editable"]
    arcpy.env.workspace = os.path.join(params["dataFolder"], os.path.join(params["database"], dataset))

    try:
        #Delete feature class if it exists
        if arcpy.Exists(fc):
                print("File exists")
                print("Delete existing file: {0}\n".format(fc))
                arcpy.Delete_management(fc)
                #print(arcpy.GetMessages())                
        
        arcpy.env.workspace = os.path.join(params["dataFolder"], params["database"])
        arcpy.CreateFeatureclass_management(dataset, params["fc"], params["gemoetryType"])
            #spatial_reference = params["spatialReference"])
        #print(arcpy.GetMessages())
    except:
        printError()


def createDomains(params):
    '''
    Create domains in database
    '''
    print("Create domains...")

    domains = [dom.avalancheAtlasPath, dom.qualitativeSize, dom.size, dom.moisture, dom.releaseType, dom.trigger,
        dom.terminusCode, dom.terminusExtent, dom.target, dom.impact, dom.shootType, dom.dust, dom.gully, dom.tchStatus, 
        dom.cprStatus, dom.damage, dom.traffic, dom.debris]

    arcpy.env.workspace = params["dataFolder"]
    database = params["database"]
    
    for domain in domains:
        try:
            #print("Creating Domain: {}".format(domain["name"]))                     
            arcpy.CreateDomain_management(database, domain["name"], domain["desc"], domain["field"], domain["domain"])            
            filename = os.path.join(params["domainsFolder"], domain["file"])
            if filename != "":
                with open(filename, "r") as infile:
                    print(" {}".format(filename))
                    if ".\\" in filename:
                        filename = filename.replace(".\\", "")
                    
                    for line in infile:                
                        line = line.rstrip("\n\r")
                        line = line.split(",", 1)        
                        if line:
                            #print(line)
                            value =  line[0]
                            desc = line[1]
                            #print("{} {}".format(value, desc))
                            arcpy.AddCodedValueToDomain_management(database, domain["name"], value, desc)
                    #print("")
            #arcpy.AssignDomainToField_management(inFeatures, inField, domName)
            #arcpy.AssignDomainToField_management(fc, "Avalanche", domainName)  #Filed dosn't exists yet
        except:
            printError()
            

def sortSelectedDomains(params):
    '''
    Sort specified domains in ascending order
    '''
    print("Sorting specified domains...")
    domainsName = ["AvalancheAtlasPath"]#, "Moisture"]
    try:               
        database = os.path.join(params["dataFolder"], params["database"])        
        
        for domainName in domainsName:            
            print("Sorting domain: {}".format(domainName))                        
            arcpy.SortCodedValueDomain_management(database, domainName, "DESCRIPTION", "ASCENDING")
    except:
        printError()


def createFields(params):
    '''
    Set up fields in a feature class    
    '''
    print("Creating fields...")

    fields = [fl.observationDate, fl.created, fl.timeWindow, fl.avalancheAtlasPath, fl.target, fl.qualitativeSize,
        fl.sizeSummary, fl.moistureStartZone, fl.moistureDeposit, fl.releaseType, fl.trigger, fl.terminusCode,
        fl.terminusExtent, fl.terminusLength, fl.gunNo, fl.impact, fl.shootType, fl.tchLength, fl.tchDepthMax, fl.tchDepthAve,
        fl.cprLength, fl.cprDepthAve, fl.cprDepthMax, fl.cprPercent, fl.dust, fl.gully, fl.tchStatus, fl.cprStatus,
        fl.damage, fl.traffic, fl.debris, fl.comments] 
    
    dataset = params["dataset"]["editable"]
    arcpy.env.workspace = os.path.join(params["dataFolder"], os.path.join(params["database"], dataset))
    fc = params["fc"]
    for field in fields:
        try:            
            #print("Adding field {}".format(e))
            arcpy.AddField_management(fc, field["name"], field["type"], field['precision'], field["scale"], field["length"],
                 field["alias"], field["nullable"], field["required"], field["domain"] )
        except Exception:
            printError()

    
def assignDefaultValue(params):
    '''
    Assing default values to fields...
    '''
    print("Assign default values...")    

    dataset = params["dataset"]["editable"]
    arcpy.env.workspace = os.path.join(params["dataFolder"], os.path.join(params["database"], dataset))
    fc = params["fc"]

    defaultFields = {fl.timeWindow["name"]:1, fl.sizeSummary["name"]: 0,
        fl.tchStatus["name"]:1, fl.cprStatus["name"]: 4,
        fl.observationDate["name"]: "2/1/2019", fl.created["name"]: "2/1/2019",
        fl.qualitativeSize['name']: "Un",
        fl.moistureStartZone['name']: "U", fl.moistureDeposit["name"]: "U",
        fl.releaseType["name"]: "U", fl.trigger["name"]: "Uk",
        fl.impact["name"]:4, fl.shootType["name"]:"NA",
        fl.dust["name"]:"0", fl.gully["name"]:0,
        fl.damage["name"]:0, fl.traffic["name"]:7, fl.debris["name"]:0 }
    
    for key, value in defaultFields.items():        
        try:
            print("Setting {} with value {}".format(key, value))            
            arcpy.AssignDefaultToField_management (fc, key, value)
        except Exception:
            printError()


def listFields(params):
    '''
    List created fields and their domains 
    '''
    print("Fields...")

    dataset = params["dataset"]["editable"]
    arcpy.env.workspace = os.path.join(params["dataFolder"], os.path.join(params["database"], dataset))
    fc = params["fc"]
       
    fieldList=arcpy.ListFields(fc)    
    for field in fieldList:                
        print(" Field: {}, Domain: {}".format(field.name, field.domain))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--output", help="Absolute path to workspace", default=None)
    
    args = parser.parse_args()
    output = args.output    
    if output == None:
        output = os.getcwd()
    
    print("Output path: {}".format(output))
    main(output)

else:
    print("Importing...")

'''
References
http://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/add-coded-value-to-domain.htm
http://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/assign-domain-to-field.htm
http://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/sort-coded-value-domain.htm
http://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/add-field.htm
http://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/assign-default-to-field.htm
http://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/make-feature-layer.htm
http://desktop.arcgis.com/en/arcmap/10.3/tools/data-management-toolbox/copy-features.htm
http://desktop.arcgis.com/en/arcmap/10.3/tools/environments/output-extent.htm
'''
