from django.shortcuts import render


# Create your views here.
from django.http import JsonResponse

from .pagination import *
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class VendorList(APIView):
    def get(self, request):
        try:
            lista_vendor = Vendor.objects.all()
            paginator = PaginacaoVendor()
            result_page = paginator.paginate_queryset(lista_vendor, request)
            serializer = VendorSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception:
            return JsonResponse({'managem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = VendorSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Vendor.DoesNotExist:
            return JsonResponse({'mensagem': "A empresa a ser relacionada não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VendorDetalhes(APIView):
    def get(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': " 0 ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            vendor = Vendor.objects.get(pk=pk)
            serializer = VendorSerializer(vendor)
            return Response(serializer.data)
        except Vendor.DoesNotExist:
            return JsonResponse({'mensagem': "O vendedor não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            vendor = Vendor.objects.get(pk=pk)
            serializer = VendorSerializer(vendor, data=request.data)
            city_id = request.data['city']
            City.objects.get(pk=city_id)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Vendor.DoesNotExist:
            return JsonResponse({'mensagem': "O vendedor não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except City.DoesNotExist:
            return JsonResponse({'mensagem': "A empresa a ser relacionada não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return  JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                 status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            vendor = Vendor.objects.get(pk = pk)
            vendor.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Vendor.DoesNoExist:
            return JsonResponse({'mensagem': "O vendedor não existe."},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CityList(APIView):
    def get(self, request):
        try:
            lista_citys = City.objects.all()
            paginator = PaginacaoCity()
            result_page = paginator.paginate_queryset(lista_citys, request)
            serializer = CitySerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = CitySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class CityDetalhes(APIView):
    def get(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero"},
                                    status=status.HTTP_400_BAD_REQUEST)
            city = City.objects.get(pk=pk)
            serializer = CitySerializer(city)
            return Response(serializer.data)
        except City.DoesNotExist:
            return JsonResponse({'mensagem': "A cidade não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            city = City.objects.get(pk=pk)
            serializer = CitySerializer(city, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except City.DoesNotExist:
            return JsonResponse({'mensagem': "Cidade não cadastrada"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return  JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                 status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem': "O ID deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            city = City.objects.get(pk=pk)
            city.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except City.DoesNotExist:
            return JsonResponse({'mensagem': "A cidade não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
