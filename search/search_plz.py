from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.db.models import Q

class Search:

    def filter_plz(self, firm_list, search_input):

        self.firm_list = firm_list
        self.search_input = search_input

        # vector = SearchVector('plz')
        # query = SearchQuery(self.search_input)

        branch_firms = firm_list.filter(Q(plz__lte=int(self.search_input)+1000),
                                        Q(plz__gte=int(self.search_input)-1000)
                                        )#.annotate(rank=SearchRank(vector, query))

        return branch_firms