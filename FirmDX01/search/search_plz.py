from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models import Q

class Search:

    def filter_plz(self, firm_list, search_input):

        self.firm_list = firm_list
        self.search_input = search_input

        vector = SearchVector('plz')
        query = SearchQuery(str(self.search_input))
        # print(firm_list)
        branch_firms = firm_list.annotate(rank=SearchRank(vector, query)).order_by('-rank')
        # branch_firms = firm_list.annotate(similarity=TrigramSimilarity('plz', str(search_input)),).filter(similarity__gt=0.3).order_by('-similarity')

        #https://docs.djangoproject.com/en/1.11/topics/db/queries/
        # branch_firms = firm_list.filter(Q(plz__lte=int(self.search_input)+1000),
        #                                 Q(plz__gte=int(self.search_input)-1000)
        #                                 ).annotate(rank=SearchRank(vector, query))

        #branch_firms = firm_list.annotate(similarity=TrigramSimilarity('plz', search_input),).filter(similarity__gt=0.3).order_by('-similarity')

        return branch_firms