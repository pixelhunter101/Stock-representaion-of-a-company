# Stock-representaion-of-a-company

- Front-End Used : Angular
- Back-End Used : Django
- DataBase Used : SQLite
- API Used : Django Rest API

CRUD Implementation

Pages Shown:

- Page 1 - Graphical Reprentation of Stocks of all the companies (Read)
- Page 2 - Add new Equity and then add upload button for adding daily_returns.CSV (Create)
- Page 3 - View all equities & returns in a tabular from where we can update or delete a data (Update & Delete)
- Page 4 - View all Daily_Returns.CSV where we can update or delete a data (Update & Delete)

Steps taken:
1. Representation of data through line graph
2. Button to redirect to 2nd and 3rd page 
    - Create New Entry - Page 2
    - Update or delete an Entry in Equity.csv - Page 3 
    - If a change is to be made on Returns then click on a row of equity.csv then get redirected to the returns of that csv
    - Update or delete an Entry in Daily_Returns.csv - Page 4 
3. When new entry is added, the page will redirect to page 1
4. When user is done with editing or deleting an entry from a table , redirect to page 1

Page Description:

- Page 1: 
  - A graph and at footer at two ends the button for create(page 2) or update and delete a data (page 3)

- Page 2:
  - Contains a form where it will have all the entries which was specified by equity.csv
  - An upload button to add daily returns.csv 
   - Make sure that the id is generated automatically for Equity. The number starts from 10277. Ends at 10286.
   - Primary key for Equity.CSV 
   - Foreign key for Daily_Returns.CSV
  
- Page 3:
  - In the table of eqity where the button is made at a column (update and delete)
  - It will also show all the returns of all the companies

- Page 4
  - It will be shown when a User clicks a specific row at page 3 and is redirected to page 4
  - The daily returns of that company is shown, where a column is made for update and delete
  
  
 Also attached the link for downloading the project:
 
 https://drive.google.com/drive/folders/1IAw-UNqcYJIlrVigNZYxO4DQVDNFtbkT?usp=sharing
 
 django using rest api- backend
 angular - frontend
 



