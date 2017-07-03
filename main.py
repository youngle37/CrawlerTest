
# coding: utf-8

# In[18]:

from MyPackage import MyModule

sixty_second = "https://www.scientificamerican.com/podcast/60-second-science/?page="

page_num = MyModule.find_page_num(sixty_second+"1")
for page in range(1, page_num+1):
    link = sixty_second + str(page)
    MyModule.download_main(link)
    MyModule.download_link(link)

