/* DATABASE & TABLE */
CREATE DATABASE GROCERIES;
CREATE TABLE tblProducts
(
ProductCode int,
CatCode int,
ProductName int PRIMARY KEY,
ProductPrice int,
);

CREATE TABLE tblStocks
(
ProductCode int,
ProductName int PRIMARY KEY,
NoofStocks int,
);

CREATE TABLE tblCategor
(
CatCode int,
CategoryName varchar (50) PRIMARY KEY,
);

/* Executions */
SELECT * FROM tblProducts;
SELECT * FROM tblStocks;
SELECT * FROM tblCategory;

SELECT tblProducts.ProductCode, tblProducts.ProductName, tblProducts.ProductPrice, tblStocks.NoofStocks, tblCategory.CategoryName
FROM tblProducts
FULL OUTER JOIN tblProducts ON 
tblProducts.ProductCode=tblCategory.CategoryName;
