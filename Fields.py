#-------------------------------------------------------------------------------
# Name:        Fields.py
# Purpose:     Definition of fields for feature class
#
# Author:      Artur Wojtas
#
# Created:     01-23-2019
# Copyright:   (c) Owner 2019
# Licence:     <your licence>
#
# 
#-------------------------------------------------------------------------------
import Domains as dom

#avalancheEvent = {"name": "AvalancheEventID", "type": "LONG", "precision": "", "scale": "", "length": "", "alias": "Avalanche Event",
#    "nullable": "NON_NULLABLE", "required": "REQUIRED", "domain": "" }

observationDate = {"name": "ObservationDate", "type": "DATE", "precision": "", "scale": "", "length": "", "alias": "Occurence Date",
    "nullable": "NON_NULLABLE", "required": "REQUIRED", "domain": "" }

timeWindow = {"name": "TimeWindow", "type": "FLOAT", "precision": "", "scale": "", "length": "", "alias": "Time Window",
    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": "" }

avalancheAtlasPath = {"name": "AvalancheAtlasPathID", "type": "TEXT", "precision": "", "scale": "", "length": 10, "alias": "Avalanche Path",
    "nullable": "NON_NULLABLE", "required": "REQUIRED", "domain": dom.avalancheAtlasPath["name"] }

target = {"name": "TargetID", "type": "TEXT", "precision": "", "scale": "", "length": 20, "alias": "Target", 
    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": dom.target["name"] }

qualitativeSize = {"name": "QualitativeSizeID", "type": "TEXT", "precision": "", "scale": "", "length": 2, "alias": "Qual Size",
    "nullable": "NON_NULLABLE", "required": "NON_REQUIRED", "domain": dom.qualitativeSize["name"] }

sizeSummary = {"name": "SizeSummary", "type": "FLOAT", "precision": "", "scale": "", "length": "", "alias": "Size", 
    "nullable": "NON_NULLABLE", "required": "REQUIRED", "domain": dom.size["name"] }

moistureStartZone = {"name": "MoistureStartZoneID", "type": "TEXT", "precision": "", "scale": "", "length": 2, "alias": "Moisture Start Zone",
    "nullable": "NON_NULLABLE", "required": "NON_REQUIRED", "domain": dom.moisture["name"] }

moistureDeposit = {"name": "MoistureStartZoneIDMoistureDeposit", "type": "TEXT", "precision": "", "scale": "", "length": 2, "alias": "Moisture Deposit",
    "nullable": "NON_NULLABLE", "required": "NON_REQUIRED", "domain": dom.moisture["name"] }

releaseType = {"name": "ReleaseTypeID", "type": "TEXT", "precision": "", "scale": "", "length": 2, "alias": "Release Type",
    "nullable": "NON_NULLABLE", "required": "NON_REQUIRED", "domain": dom.releaseType["name"] }

trigger = {"name": "TriggerID", "type": "TEXT", "precision": "", "scale": "", "length": 2, "alias": "Trigger",
    "nullable": "NON_NULLABLE", "required": "NON_REQUIRED", "domain": dom.trigger["name"] }

terminusCode = {"name": "TerminusCodeID", "type": "TEXT", "precision": "", "scale": "", "length": 3, "alias": "Terminus Code",
    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": dom.terminusCode["name"] }

terminusExtent = {"name": "TerminusExtentID", "type": "TEXT", "precision": "", "scale": "", "length": 3, "alias": "Terminus Extent",
    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": dom.terminusExtent["name"] }

terminusLength = {"name": "TerminusLength", "type": "TEXT", "precision": "", "scale": "", "length": 3, "alias": "Terminus Length",
    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": "" }

gunNo = {"name": "GunNo", "type": "TEXT", "precision": "", "scale": "", "length": 3, "alias": "Gun No.",
    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": "" }

impact = {"name": "ImpactID", "type": "SHORT", "precision": "", "scale": "", "length": "", "alias": "Impact",
    "nullable": "NON_NULLABLE", "required": "NON_REQUIRED", "domain": dom.impact["name"] }

shootType = {"name": "ShootTypeID", "type": "TEXT", "precision": "", "scale": "", "length": 4, "alias": "Shoot Type",
    "nullable": "NON_NULLABLE", "required": "NON_REQUIRED", "domain": dom.shootType["name"] }

tchLength = {"name": "TCHLength", "type": "FLOAT", "precision": "", "scale": "", "length": "", "alias": "Length on TCH",
    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": "" }

tchDepthMax = {"name": "TCHDepthMax", "type": "FLOAT", "precision": "", "scale": "", "length": "", "alias": "Max Depth on TCH",
    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": "" }

tchDepthAve  = {"name": "TCHDepthAve", "type": "FLOAT", "precision": "", "scale": "", "length": "", "alias": "Avg Depth on TCH",
    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": "" }

cprLength = {"name": "CPRLength", "type": "FLOAT", "precision": "", "scale": "", "length": "", "alias": "Length on CPR",
    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": "" }

cprDepthAve = {"name": "CPRDepthAve", "type": "FLOAT", "precision": "", "scale": "", "length": "", "alias": "Avg Depth on CPR",
    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": "" }

cprDepthMax = {"name": "CPRDepthMax", "type": "FLOAT", "precision": "", "scale": "", "length": "", "alias": "Max Depth on CPR",
    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": "" }

cprPercent = {"name": "CPRPercent", "type": "FLOAT", "precision": "", "scale": "", "length": "", "alias": "CPR Percent",
    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": "" }

dust = {"name": "DustID", "type": "TEXT", "precision": "", "scale": "", "length": 3, "alias": "Dust",
    "nullable": "NON_NULLABLE", "required": "NON_REQUIRED", "domain": dom.dust["name"] }

gully = {"name": "GullyID", "type": "SHORT", "precision": "", "scale": "", "length": "", "alias": "Gully",
    "nullable": "NON_NULLABLE", "required": "NON_REQUIRED", "domain": dom.gully["name"] }

tchStatus = {"name": "TCHStatusID", "type": "SHORT", "precision": "", "scale": "", "length": "", "alias": "TCH Status",
    "nullable": "NON_NULLABLE", "required": "REQUIRED", "domain": dom.tchStatus["name"] }

cprStatus = {"name": "CPRStatusID", "type": "SHORT", "precision": "", "scale": "", "length": "", "alias": "CPR Status",
    "nullable": "NON_NULLABLE", "required": "REQUIRED", "domain": dom.cprStatus["name"] }

damage = {"name": "DamageID", "type": "SHORT", "precision": "", "scale": "", "length": "", "alias": "Damage",
    "nullable": "NON_NULLABLE", "required": "NON_REQUIRED", "domain": dom.damage["name"] }

traffic = {"name": "TrafficID", "type": "SHORT", "precision": "", "scale": "", "length": "", "alias": "Traffic",
    "nullable": "NON_NULLABLE", "required": "NON_REQUIRED", "domain": dom.traffic["name"] }

debris = {"name": "DebrisID", "type": "SHORT", "precision": "", "scale": "", "length": "", "alias": "Debris",
    "nullable": "NON_NULLABLE", "required": "NON_REQUIRED", "domain": dom.debris["name"] }

#snowProfileFileName =  {"name": "SnowProfileFileName", "type": "TEXT", "precision": "", "scale": "", "length": 255, "alias": "Snow Profile FileName",
#    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": "" }

comments = {"name": "Comments", "type": "TEXT", "precision": "", "scale": "", "length": 1073741823, "alias": "Comments",
    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": "" }

#chargeSize = {"name": "ChargeSize", "type": "FLOAT", "precision": "", "scale": "", "length": "", "alias": "Charge Size",
#    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": "" }

#numCharges = {"name": "NumCharges", "type": "SHORT", "precision": "", "scale": "", "length": "", "alias": "Num Charges",
#    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": "" }

#checked = {"name": "Checked", "type": "SHORT", "precision": "", "scale": "", "length": "", "alias": "Checked",
#    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": "" }

#checkedBy  = {"name": "CheckedBy", "type": "TEXT", "precision": "", "scale": "", "length": 100, "alias": "Checked By",
#    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": "" }

created = {"name": "Created", "type": "DATE", "precision": "", "scale": "", "length": "", "alias": "Observation Date",
    "nullable": "NON_NULLABLE", "required": "REQUIRED", "domain": "" }

#createdBy = {"name": "CreatedBy", "type": "TEXT", "precision": "", "scale": "", "length": 100, "alias": "Created By",
#    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": " " }

#modified = {"name": "Modified", "type": "DATE", "precision": "", "scale": "", "length": "", "alias": "Modified",
#    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": "" }

#modifiedBy = {"name": "ModifiedBy", "type": "TEXT", "precision": "", "scale": "", "length": 100, "alias": "Modified By", 
#    "nullable": "NULLABLE", "required": "NON_REQUIRED", "domain": "" }

#photoF = {"name": "Photo", "type": "BLOB", "alias": "Photo", "nullable": "NULLABLE ", "required": "NON_REQUIRED"}
