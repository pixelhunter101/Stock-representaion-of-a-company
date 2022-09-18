from django.shortcuts import render
from Backend_RestApi import Backend_SQLite

from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from Backend_SQLite.models import equity
from Backend_SQLite.models import daily_returns
from Backend_SQLite.serializers import equitySerializer, daily_returnsSerializer
from rest_framework.decorators import api_view

@csrf_exempt
def equityApi(request,id=0):
    if request.method=='GET':
        equitys = equity.objects.all()
        equity_Serializer = equitySerializer(equitys, many=True)
        return JsonResponse(equity_Serializer.data, safe=False)

    elif request.method=='PUT':
        equity_data = JSONParser().parse(request)
        equitys=equity.objects.get(equityid=equity_data['id'])
        equity_serializer=equitySerializer(equitys,data=equity_data)
        if equity_serializer.is_valid():
            equity_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        equity=equity.objects.get(equityId=id)
        equity.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)

@csrf_exempt
def daily_returnsApi(request,id=0):
    if request.method=='GET':
        returns = daily_returns.objects.all()
        returns_serializer = daily_returnsSerializer(returns, many=True)
        return JsonResponse(returns_serializer.data, safe=False)

    elif request.method=='POST':
        returns_data=JSONParser().parse(request)
        daily_returns_serializer = daily_returnsSerializer(data=returns_data)
        if returns_serializer.is_valid():
            returns_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        returns_data = JSONParser().parse(request)
        returns=returns.objects.get(returnsId=returns_data['returnsId'])
        returns_serializer=daily_returnsSerializer(returns,data=returns_data)
        if returns_serializer.is_valid():
            returns_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        returns=returns.objects.get(returnsId=id)
        returns.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


#@csrf_exempt
#def SaveFile(request):
   # file=request.FILES['uploadedFile']
   # file_name = default_storage.save(file.name,file)

   # return JsonResponse(file_name,safe=False)
