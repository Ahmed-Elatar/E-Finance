from django.http import HttpResponse ,JsonResponse

from rest_framework.views import APIView ,status
from rest_framework.generics import ListAPIView , RetrieveDestroyAPIView
from rest_framework.response import Response

from .models import *
from .serializers import *
from .tasks import *

import os ,requests , yfinance as yf

from dotenv import load_dotenv


load_dotenv()







class TakeSymbol(APIView):
    
    def post(self,request,symbol):
        result =send_data_to_fastapi({"sender":str(request.user) ,"symbol": symbol })
        print(result.status_code)
        
        return JsonResponse({'Data-Status': 'Recived'}, status=status.HTTP_200_OK)
    def get(self,request):

        return HttpResponse("Don't recive Ticker Symbol ?!..")

        





def send_data_to_fastapi(data):

    url = os.getenv('Fastapi_url')  
    result = requests.post(url, json=data)
    return result






class ReceiveTickerData(APIView):

    def post(self, request):
        
        
        response_data = request.data

        # Check if status is 'accepted'
        if response_data.get('status') == 'accepted':
            # Extract 'symbol' and 'name' from the response data
            ticker_data = {
                'symbol': response_data.get('symbol'),
                'name': response_data.get('name')
            }

            
            serializer = TickerSerializer(data=ticker_data)
            
            ## Save the Ticker instance after the Validation
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'status': response_data['status']}, status=status.HTTP_201_CREATED)
            
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        # If status is  'not-accepted', return the status as a response
        return JsonResponse({'status': response_data['status']}, status=status.HTTP_204_NO_CONTENT)






class TickersView(ListAPIView):

    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer     

class TickerView(RetrieveDestroyAPIView):

    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer



class TickersHistoryView(ListAPIView):

    queryset = History.objects.all().order_by('ticker')
    serializer_class = HistorySerializer     

class TickerHistoryView(ListAPIView):

    serializer_class = HistorySerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return History.objects.filter(ticker=pk)











def test_yahoo(request):

    #GOLD: Period  must be one of ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
    tkr= yf.Ticker("NVDA")
    stock_price = tkr.history(interval ='1h' ,period="1d")['Open']
    print(tkr.history(period ='1d'))

    

    return HttpResponse("HOME...")