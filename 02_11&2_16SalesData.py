# -*- coding: utf-8 -*-
"""02/11&2/16IntroToPandas4&5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OhLoc9AF6ciCCs75K7FcJt9DTo_JTe-g
"""

import pandas as pd
import scipy.stats
xl = pd.ExcelFile("/content/TableauSalesData (1).xlsx")
SalesData = xl.parse("Orders")

print(SalesData.columns)

SubCats = SalesData["Sub-Category"].unique()
print(SubCats)

#To find total Sales and Profits for all Sub-Categories
SubCatProfits = SalesData[["Sub-Category", "Profit", "Sales"]]
Total = SubCatProfits.groupby(by="Sub-Category").sum().sort_values(by="Profit")
display(Total)

#To find total Sales and Profits for all Sub-Categories in the Supplies Sub-Category
SubCatSalesProfits = SalesData[["Sub-Category", "Profit", "Sales"]]
SuppliesProfSales = SubCatSalesProfits.loc[(SubCatSalesProfits["Sub-Category"]=="Supplies")]
Total = SuppliesProfSales.groupby(by=["Sub-Category"]).sum().round()
display(Total)

#To find total Sales&Profits for each product in the Supplies Sub-Category, Profit sorted by most profitable
Supplies = SalesData.loc[SalesData["Sub-Category"]=="Supplies"]
SuppliesProdProfSales = Supplies[["Product Name", "Profit", "Sales"]].groupby(by="Product Name").sum().sort_values("Profit", ascending = False)
display(SuppliesProdProfSales)

#To find only the profitable products in Supplies
Supplies = SalesData.loc[SalesData["Sub-Category"]=="Supplies"]
SuppliesProdProfSales = Supplies[["Product Name", "Profit"]].groupby(by="Product Name").sum().sort_values("Profit", ascending = False)
PosSupplies = SuppliesProdProfSales[SuppliesProdProfSales["Profit"]>0.0]
print(PosSupplies)

Supplies = SalesData.loc[SalesData["Sub-Category"]=="Supplies"]
SuppliesProdProfSales = Supplies[["Product Name", "Profit"]].groupby(by="Product Name").sum().sort_values("Profit", ascending = False)
print("The total number of Supply products is:")
print(SuppliesProdProfSales.count())
PosSupplies = SuppliesProdProfSales[SuppliesProdProfSales["Profit"]>0.0]
print("The total number of positive supplies is:")
print(PosSupplies.count())
display(PosSupplies)

SubCatSalesProf = SalesData[["Region", "Category", "Sales", "Profit"]]
CorpTableSalesProf = SubCatSalesProf.loc[(SubCatSalesProf["Region"]=="East") & (SubCatSalesProf["Category"]=="Furniture")]
Total = CorpTableSalesProf.groupby(by=["Region", "Category"]).sum().round()
print(Total)

"""Copier Segmentation / Region

"""

#Copiers segment broken in segment, profit, sales
JustCopiers = SalesData.loc[SalesData["Sub-Category"]=="Copiers"]
CopierSegment = JustCopiers[["Segment", "Profit", "Sales"]].groupby(by="Segment").sum()
print(CopierSegment)

#Copiers Region broken in region, profit, sales
CopierSegRegion = JustCopiers[["Segment", "Region", "Profit", "Sales"]]
EastCopierSegment = CopierSegRegion.loc[CopierSegRegion["Region"]=="East"]
EastProfSales = EastCopierSegment.groupby(by="Region").sum()
print("Profit and Sales for Copiers in the East Region")
print(EastProfSales)

#Profit and Sales for Copiers in the East Region
CopierSegRegion = JustCopiers[["Segment", "Region", "Profit", "Sales"]]
EastCopierSegment = CopierSegRegion.loc[CopierSegRegion["Region"]=="East"]
EastProfSales = EastCopierSegment.groupby(by="Segment").sum()
print("Profit and Sales for Copiers by Segment in the East Region")
print(EastProfSales)

#Creating a new Segment with the dataframe using Months
JustCopiersMonths = JustCopiers.copy()
JustCopiersMonths["Month"] = JustCopiersMonths["Order Date"].dt.month
MonthlyProfSales = JustCopiersMonths[["Month", "Profit", "Sales"]].groupby(by="Month").sum()
print("The monthly Profit of Sales for the Copiers are:")
print(MonthlyProfSales)

JustTablesQuarter = JustTables.copy()
JustTablesQuarter["Quarter"] = JustTablesQuarter["Order Date"].dt.quarter
QuarterlyProfSales = JustTablesQuarter[["Quarter", "Profit", "Sales"]].groupby(by="Quarter").sum()
print("The quarterly Profit of Sales for the Table are:")
print(QuarterlyProfSales)

"""Discounts Correlation to Sales """

import scipy.stats
x = "Discount"
y = "Sales"
GetCorrelation = scipy.stats.spearmanr(JustTables[x], JustTables[y])
Corr = GetCorrelation[0]
pValue = GetCorrelation[1]
print(Corr.round(2))
print(pValue.round(5))
#Negative correlation means weak correlation of Discounts to Sales, as Discounts + , Then Sales -

"""Time/Date Data for Tables"""