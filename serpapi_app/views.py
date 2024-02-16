# serpapi_app/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from serpapi import GoogleSearch  
from rest_framework import generics



class SearchResultsAPIView(APIView):
    def post(self, request, *args, **kwargs):
        api_key = "402a0dbd50e57ebbe9a23abd414051234f16b96e452ab61d7ad93844b7077dba"  
        search_query = request.data.get('search_query', None)
        if not search_query:
            return Response({'error': 'search query is required'})
        
        params = {
            "engine": "google_jobs",
            "q": search_query,
            "hl": "en",
            "api_key": api_key
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        jobs_results = results.get("jobs_results", [])

        return Response(jobs_results)

