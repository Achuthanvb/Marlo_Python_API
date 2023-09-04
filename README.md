# Marlo_Python_API
1_2_Pregistration_Login_API:
  Login API :
    login credentials are stored in MongoDB_atlas
    once login credentials is entered --> Fetch the same credentials from DB.
    If match found , login successfull or failed
    Here email is checked for domain, and length for validation
  Registeration API:
    Getting INPUT:
        Username, valid email ID, password 
    Stored in Mongodb-atlas
  Admin Login:
    Already admins might registered and if those email ID match , we can login 

3_product_upload:
  This page can be accessed only by admins.
  File upload option is given ,
      CSV file is uploaded
      converted to Dataframe
      converted to dictionary 
      stored in MongoDB 
  Some options are given to retive the stored data for view and delete option (no code)

  4_Product_review API:
    All product details fetched from database.
    Selection each product-->viewing the detials and price--> option to give rating and review comments.
    and ratings and review comments are stored in respctive product detials .

  5_product_view API:
    All product details fetched from database.
    Filter option is given (high to Low , Low to High).
    Based on filteration , products are soreted and viewed a based on ratings .
    Pagination Also done , Two products can be viewed per page .

Improvement Can be Done:
  All pages can be put together.
  Product Review option can be given in product view page only .
  Many other CSS , HTML can be aplied for  good looking API .
  
    
    
