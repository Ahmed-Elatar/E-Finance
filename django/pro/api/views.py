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






"""
TakeSymbol class :~
This class uses APIViews and have to methods
POST : to send symbol and user data to FastAPI to check it's correctness
GET : return HttpResponse "Don't recive Ticker Symbol ?!.."
"""
class TakeSymbol(APIView):
    
    def post(self,request,symbol):
        result =send_data_to_fastapi({"sender":str(request.user) ,"symbol": symbol })
        print(result.status_code)
        
        return JsonResponse({'Data-Status': 'Recived'}, status=status.HTTP_200_OK)
    def get(self,request):

        return HttpResponse("Don't recive Ticker Symbol ?!..")

        




"""
send_data_to_fastapi Function :~
This function used to send data to FastAPI .

"""
def send_data_to_fastapi(data):

    url = os.getenv('Fastapi_url')  
    result = requests.post(url, json=data)
    return result





"""
ReceiveTickerData class :~
This class uses APIViews and have to methods
POST : to recive Ticker status from FastAPI if status is accepted saves it in postgreSQL
GET : return HttpResponse "NO Data recived from FastAPI"
"""
class ReceiveTickerData(APIView):

    def post(self, request):
        
        
        response = request.data

        # Check if status is 'accepted'
        if response.get('status') == 'accepted':
            # Extract 'symbol' and 'name' from the response data
            ticker_data = {
                'symbol': response.get('symbol'),
                'name': response.get('name')
            }

            
            serializer = TickerSerializer(data=ticker_data)
            
            ## Save the Ticker instance after the Validation
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'status': response['status']}, status=status.HTTP_201_CREATED)
            
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        # If status is  'not-accepted', return the status as a response
        return JsonResponse({'status': response['status']}, status=status.HTTP_204_NO_CONTENT)
    
    def get(self ,request):
    
        return HttpResponse("NO Data recived from FastAPI")





"""
TickersView class :~
This class uses the Generic Views to retrieve a list of Tickers data .
"""
class TickersView(ListAPIView):

    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer     

"""
TickerView class 
This class uses the Generic Views to retrieve a single Ticker data or delete it.
"""
class TickerView(RetrieveDestroyAPIView):

    queryset = Ticker.objects.all()
    serializer_class = TickerSerializer


"""
TickersHistoryView class :~
This class uses the Generic Views to retrieve a list of Tickers history data .
"""
class TickersHistoryView(ListAPIView):

    queryset = History.objects.all().order_by('ticker')
    serializer_class = HistorySerializer     

"""
TickerHistoryView class :~
This class uses the Generic Views to retrieve a list of single Ticker history data .
"""
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