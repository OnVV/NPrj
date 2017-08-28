from servicePr.firm import Firmeneintrag_new
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from servicePr.models_new import Firma

class Search:

    def filter_plz(self, firm_list, search_input):

        self.firm_list = firm_list
        self.search_input = search_input

        # vector = SearchVector('plz')
        # query = SearchQuery(self.search_input)
        branch_firms = firm_list.filter(plz__icontains=self.search_input) #.annotate(rank=SearchRank(vector, query))

        return branch_firms