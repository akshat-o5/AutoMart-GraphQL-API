import strawberry
from .models import VehicalInfo
from typing import List, Optional
from .database import collection

@strawberry.type
class Query:  
    
    # Get all Vehical Info
    @strawberry.field
    def getAllVehicalInfo(self) ->  List[VehicalInfo]:
        allInformation = []
        for info in collection.find():
            information = VehicalInfo(id=info["id"], model=info["model"], brand=info["brand"], type=info["type"], yearsOfUsage=info["yearsOfUsage"], price=info["price"], color=info["color"], engineType=info["engineType"], fuelType=info["fuelType"])
            allInformation.append(information)
        return allInformation    
    
    # Get Vehical Info according to it's id
    @strawberry.field
    def getSingleVehicalInfo(self, id:int) -> VehicalInfo | None:
        info = collection.find_one({"id":id})
        if info:
            return VehicalInfo(id=info["id"], model=info["model"], brand=info["brand"], type=info["type"], yearsOfUsage=info["yearsOfUsage"], price=info["price"], color=info["color"], engineType=info["engineType"], fuelType=info["fuelType"])
        else:
            return None

    # Get Vehical Info according to it's brand
    @strawberry.field
    def getInfoByBrand(self, brand:str) -> List[VehicalInfo] | None:
        all_information = []
        for info in collection.find({"brand": brand}):
            vehicle_info = VehicalInfo(
                id=info["id"],
                model=info["model"],
                brand=info["brand"],
                type=info["type"], 
                yearsOfUsage=info["yearsOfUsage"],
                price=info["price"],
                color=info["color"],
                engineType=info["engineType"],
                fuelType=info["fuelType"]
            )
            all_information.append(vehicle_info)
        if all_information:
            return all_information
        else:
            return None
            

    # Get Vehical Info according to it's model
    @strawberry.field
    def getInfoByModel(self, model:str) -> List[VehicalInfo] | None:
        all_information = []
        for info in collection.find({"model": model}):
            vehicle_info = VehicalInfo(
                id=info["id"],
                model=info["model"],
                brand=info["brand"],
                type=info["type"], 
                yearsOfUsage=info["yearsOfUsage"],
                price=info["price"],
                color=info["color"],
                engineType=info["engineType"],
                fuelType=info["fuelType"]
            )
            all_information.append(vehicle_info)
        if all_information:
            return all_information
        else:
            return None
            

    # Get Vehical Info according to it's type
    @strawberry.field
    def getInfoByType(self, type:str) -> List[VehicalInfo] | None:
        all_information = []
        for info in collection.find({"type": type}):
            vehicle_info = VehicalInfo(
                id=info["id"],
                model=info["model"],
                brand=info["brand"],
                type=info["type"], 
                yearsOfUsage=info["yearsOfUsage"],
                price=info["price"],
                color=info["color"],
                engineType=info["engineType"],
                fuelType=info["fuelType"]
            )
            all_information.append(vehicle_info)
        if all_information:
            return all_information
        else:
            return None

    # Get Vehical Info according to it's engine type
    @strawberry.field
    def getInfoByEngine(self, engineType:str) -> List[VehicalInfo] | None:
        all_information = []
        for info in collection.find({"engineType": engineType}):
            vehicle_info = VehicalInfo(
                id=info["id"],
                model=info["model"],
                brand=info["brand"],
                type=info["type"], 
                yearsOfUsage=info["yearsOfUsage"],
                price=info["price"],
                color=info["color"],
                engineType=info["engineType"],
                fuelType=info["fuelType"]
            )
            all_information.append(vehicle_info)
        if all_information:
            return all_information
        else:
            return None     
            
    
    # Get Vehical Info according to it's fuel type
    @strawberry.field
    def getInfoByFuel(self, fuelType:str) -> List[VehicalInfo] | None:
        all_information = []
        for info in collection.find({"fuelType": fuelType}):
            vehicle_info = VehicalInfo(
                id=info["id"],
                model=info["model"],
                brand=info["brand"],
                type=info["type"], 
                yearsOfUsage=info["yearsOfUsage"],
                price=info["price"],
                color=info["color"],
                engineType=info["engineType"],
                fuelType=info["fuelType"]
            )
            all_information.append(vehicle_info)
        if all_information:
            return all_information
        else:
            return None     
            

    # Get Vehical Info according to it's type and colour        
    @strawberry.field
    def getInfoByTypeColor(self, type:str, color:str) -> List[VehicalInfo] | None:
        all_information = []
        for info in collection.find({"type": type, "color":color}):
            vehicle_info = VehicalInfo(
                id=info["id"],
                model=info["model"],
                brand=info["brand"],
                type=info["type"], 
                yearsOfUsage=info["yearsOfUsage"],
                price=info["price"],
                color=info["color"],
                engineType=info["engineType"],
                fuelType=info["fuelType"]
            )
            all_information.append(vehicle_info)
        if all_information:
            return all_information
        else:
            return None      
            

    # Get Vehical Info according to it's brand and colour        
    @strawberry.field
    def getInfoBrandColor(self, brand:str, color:str) -> List[VehicalInfo] | None:
        all_information = []
        for info in collection.find({"brand": brand, "color":color}):
            vehicle_info = VehicalInfo(
                id=info["id"],
                model=info["model"],
                brand=info["brand"],
                type=info["type"], 
                yearsOfUsage=info["yearsOfUsage"],
                price=info["price"],
                color=info["color"],
                engineType=info["engineType"],
                fuelType=info["fuelType"]
            )
            all_information.append(vehicle_info)
        if all_information:
            return all_information
        else:
            return None         

    # Get Vehical Brands
    @strawberry.field
    def getVehicalBrands(self) ->  List[str]:
        brands = collection.distinct("brand")
        return brands 
    
    # Get Vehical Models
    @strawberry.field
    def getVehicalModels(self) ->  List[str]:
        models = collection.distinct("model")
        return models 
    
    # Get Vehical Types
    @strawberry.field
    def getVehicalTypes(self) ->  List[str]:
        types = collection.distinct("type")
        return types 
    
    
    # Get Vehical Info according to it's years of usage
    @strawberry.field
    def getInfoByUsage(self, yearsOfUsage:int) -> List[VehicalInfo] | None:
        all_information = []
        for info in collection.find({"yearsOfUsage": yearsOfUsage}):
            vehicle_info = VehicalInfo(
                id=info["id"],
                model=info["model"],
                brand=info["brand"],
                type=info["type"], 
                yearsOfUsage=info["yearsOfUsage"],
                price=info["price"],
                color=info["color"],
                engineType=info["engineType"],
                fuelType=info["fuelType"]
            )
            all_information.append(vehicle_info)
        if all_information:
            return all_information
        else:
            return None    
            

    # Get Vehical Info by Usage Range
    @strawberry.field
    def getInfoByUsageRange(self, min:int, max:int) -> List[VehicalInfo] | None: 
        all_information = []
        for info in collection.find({"yearsOfUsage": {"$gte": min, "$lte": max}}):
            vehicle_info = VehicalInfo(
                id=info["id"],
                model=info["model"],
                brand=info["brand"],
                type=info["type"], 
                yearsOfUsage=info["yearsOfUsage"],
                price=info["price"],
                color=info["color"],
                engineType=info["engineType"],
                fuelType=info["fuelType"]
            )
            all_information.append(vehicle_info)
        if all_information:
            return all_information
        else:
            return None    
            
    # Get Vehical Info by type and price range
    @strawberry.field
    def getInfoByTypeAndPriceRange(self, type:str, min:int, max:int) -> List[VehicalInfo] | None:
        all_information = []
        for info in collection.find({"type": type, "price": {"$gte": min, "$lte": max}}):
            vehicle_info = VehicalInfo(
                id=info["id"],
                model=info["model"],
                brand=info["brand"],
                type=info["type"], 
                yearsOfUsage=info["yearsOfUsage"],
                price=info["price"],
                color=info["color"],
                engineType=info["engineType"],
                fuelType=info["fuelType"]
            )
            all_information.append(vehicle_info)
        if all_information:
            return all_information
        else:
            return None        


            
    ###         -------------------------------------Will add more queries in future, if needed-------------------------------------------










@strawberry.type
class Mutation:
    
    # Creating a VehicalInfo
    @strawberry.mutation
    def createVehicalInfo(self, id:int, model : str, brand : str, type : str, yearsOfUsage : int, price : int, color : str, engineType : Optional[str], fuelType : Optional[str]) -> VehicalInfo :
        data = {"id":id, "model":model, "brand":brand, "type":type, "yearsOfUsage":yearsOfUsage, "price":price, "color":color, "engineType":engineType, "fuelType":fuelType}
        collection.insert_one(data)
        return VehicalInfo(id=data["id"], model=data["model"], brand=data["brand"], type=data["type"], yearsOfUsage=data["yearsOfUsage"], price=data["price"], color=data["color"], engineType=data["engineType"], fuelType=data["fuelType"])
    


    # Deleting a Vehical Info
    @strawberry.mutation
    def deleteVehicalInfo(self, id:int) -> str:
        data = collection.find_one_and_delete({"id": id})
        if data:
            return "Deleted Successfully"
        else:
            return "Id doesnot exists"    
        
    #Updating a Vehical Info
    # This mutation will be made as per the requirments of the user. Updation can be of anyform, of any fields. It solely depends upon the client an what specification he/she requires




schema = strawberry.Schema(query=Query, mutation=Mutation)





