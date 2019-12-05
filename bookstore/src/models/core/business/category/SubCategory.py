
from bookstore.src.models.core.business.category.ParentCategory import Category

class SubCategory(Category):
    '''
    classdocs
    '''


    def __init__(self,sub_cat_id=None ,name= None):
        '''
        Constructor
        '''
        super(SubCategory,self).__init__(sub_cat_id ,name)
        