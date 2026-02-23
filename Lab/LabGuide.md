# Lab Guide: InnovAItion Partners Ltd. — From Data Chaos to Insights with Microsoft Fabric

## Scenario

You are a data analyst at **InnovAItion Partners Ltd.**, a technology reseller that sells hardware, software, cloud services, and networking equipment from vendors like Microsoft, Dell, HP, Cisco, and Fortinet. Your sales and customer data lives in a SQL database, but leadership wants a unified, interactive view of the business.

In this lab, you will use **Microsoft Fabric** to ingest data from an Azure SQL Database into a Lakehouse, build a data model with relationships and measures, and create a Power BI dashboard — all without leaving the Fabric experience.

## What You Will Build

- A Fabric **Workspace** and **Lakehouse**
- Two **Data Pipelines** that pull data from Azure SQL
- A **Data Model** with relationships and DAX measures
- A **Power BI Dashboard** with interactive visuals

## Prerequisites

- A Microsoft Fabric trial or access to a Fabric-enabled capacity
- A modern web browser (Edge or Chrome recommended)
- The Azure SQL connection details provided below

## Azure SQL Connection Details

**Server:**
```
<your-sql-server>.database.windows.net
```

**Database:**
```
InnovAItionPartnersDB
```

**Username:**
```
<lab-username>
```

**Password:**
```
<lab-password>
```

**Authentication:** SQL Authentication

> **Note:** This is a read-only connection. You will not be able to modify the source database.

---

## Lab 1: Environment Setup (10-15 min)

### 1.1 — Navigate to Microsoft Fabric

Open an **InPrivate** (Edge) or **Incognito** (Chrome) browser window and go to:

```
https://app.fabric.microsoft.com
```

> **Important:** Always use InPrivate / Incognito mode to avoid conflicts with any personal or work Microsoft accounts you may already be logged into.

Sign in with the credentials provided to you for this lab.

### 1.2 — Start the Microsoft Fabric Trial

Since this is a fresh tenant, you will need to activate a Fabric trial before proceeding.

1. You should see a prompt to **Start trial** — click it
2. If you don't see the prompt, click your **profile icon** in the top-right corner → **Start trial**
3. Review the trial terms and click **Start trial**
4. Wait for the trial to activate (this may take a moment)
5. You should see a confirmation that your **Microsoft Fabric trial is active**

> **Note:** The trial gives you full access to all Fabric features for 60 days. This is all we need for today's lab.

### 1.3 — Create a New Workspace

1. In the left navigation pane, click **Workspaces**
2. Click **+ New workspace**
3. Name your workspace:

```
InnovAIte-[YourLastName]
```

> Example: `InnovAIte-Seaman`

4. Under **Advanced**, ensure **Fabric capacity** or **Trial** is selected as the license mode
5. Click **Apply**

### 1.4 — Create a Lakehouse

1. Inside your new workspace, click **+ New item**
2. Select **Lakehouse**
3. Name it:

```
InnovAItion_Lakehouse
```

4. Click **Create**

### 1.5 — Quick Tour

Take a moment to explore the Lakehouse interface:

- **Tables** — Where your structured data will live (this is where we're headed)
- **Files** — For unstructured data like CSVs, Parquet files, images, etc.
- **SQL analytics endpoint** — A read-only SQL layer over your Lakehouse tables (we'll use this later)

---

## Lab 2: Ingest Sales Orders (15-20 min)

In this lab, you will create a Data Pipeline to pull the `SalesOrders` table from Azure SQL into your Lakehouse.

### 2.1 — Create a Data Pipeline

1. From your Lakehouse, click **Get data** in the toolbar
2. Select **New data pipeline**
3. Name the pipeline:

```
Pipeline_SalesOrders
```

4. Click **Create**

### 2.2 — Configure the Copy Activity

1. In the pipeline canvas, select **Copy data** activity (or use the Copy Data assistant if prompted)
2. **Source configuration:**
   - Data store type: **Azure SQL Database**
   - Click **+ New connection**
   - Enter the server, database, username, and password from the connection details table above
   - Click **Test connection** to verify, then click **Next**
   - Select the table:
     ```
     dbo.SalesOrders
     ```
   - Click **Next** to preview the data — you should see order records with fields like OrderID, CustomerID, ProductName, Vendor, Quantity, UnitCost, UnitPrice, etc.

3. **Destination configuration:**
   - Data store type: **Lakehouse**
   - Select your `InnovAItion_Lakehouse`
   - Table name:
     ```
     SalesOrders
     ```
   - Load mode: **Overwrite**
   - Click **Next**

4. Review the mapping — the column names should map automatically
5. Click **Save + Run**

### 2.3 — Validate the Ingestion

1. Wait for the pipeline run to complete (typically 30-60 seconds)
2. Navigate back to your Lakehouse
3. Expand **Tables** — you should see `SalesOrders`
4. Click on the table to preview the data
5. Confirm you see approximately **1,000 rows**

> **Troubleshooting:** If the table doesn't appear, click the **refresh** icon above the Tables section. If the pipeline failed, double-check your connection credentials and try again.

---

## Lab 3: Ingest Customers with Dataflow Gen2 (10-15 min)

For the second data source, you'll use a **Dataflow Gen2** instead of a Data Pipeline. Dataflows give you a Power Query experience where you can transform data during ingestion — rename columns, filter rows, merge tables, and more.

### 3.1 — Create a Dataflow Gen2

1. Navigate back to your workspace
2. Click **+ New item** → **Dataflow Gen2**
3. The Power Query editor will open

### 3.2 — Connect to Azure SQL

1. In the Power Query editor, click **Get data** → **Azure SQL Database**
2. Enter the server and database from the connection details at the top of this guide
3. Use the **existing connection** credentials from Lab 2 (or re-enter them)
4. From the table list, select:
   ```
   dbo.Customers
   ```
5. Click **Next** — you should see a preview of the customer data

### 3.3 — Transform the Data

This is where Dataflows shine — you can shape the data before it lands in your Lakehouse.

**Rename `Tier` → `Tier`:**

1. Right-click the `Tier` column header
2. Select **Rename**
3. Type:
   ```
   Tier
   ```
4. Press **Enter**

**Rename `Contact` → `Contact`:**

1. Right-click the `Contact` column header
2. Select **Rename**
3. Type:
   ```
   Contact
   ```
4. Press **Enter**

> **Why rename?** In real-world scenarios, source systems often have inconsistent or overly technical column names. Dataflows let you clean this up before the data reaches your Lakehouse, so your analysts and reports use business-friendly names from the start.

### 3.4 — Set the Destination

1. In the bottom-right corner of the Power Query editor, click **Add data destination** → **Lakehouse**
2. Select your `InnovAItion_Lakehouse`
3. Table name:
   ```
   Customers
   ```
4. Update method: **Replace**
5. Click **Next** and review the column mappings

### 3.5 — Publish and Run

1. Click **Publish** in the bottom-right corner
2. The dataflow will automatically run after publishing
3. Wait for it to complete (typically 1-2 minutes)

### 3.6 — Validate

1. Navigate back to your Lakehouse
2. You should now see **two tables** under Tables:
   - `Customers` (~50 rows)
   - `SalesOrders` (~1,000 rows)
3. Click the `Customers` table and confirm:
   - The column is now named `Tier` (not `Tier`)
   - The column is now named `Contact` (not `Contact`)

> **Checkpoint:** If both tables are visible and the renamed columns look correct, you're ready to move on. Raise your hand if you need help catching up.

---

## Lab 4: Transform & Model (20-25 min)

With the data ingested, you'll now build a data model by creating relationships and business measures.

### 4.1 — Open the SQL Analytics Endpoint

1. In your Lakehouse, click the **Lakehouse** dropdown in the top-right corner
2. Switch to **SQL analytics endpoint**
3. You now have a SQL-queryable view of your Lakehouse tables

### 4.2 — Explore the Data with SQL (Optional)

Try running a few queries to get familiar with the data. Click **New SQL query** and paste:

```sql
-- Total orders by vendor
SELECT Vendor, COUNT(*) AS OrderCount, SUM(Quantity * UnitPrice) AS TotalRevenue
FROM SalesOrders
WHERE OrderStatus = 'Completed'
GROUP BY Vendor
ORDER BY TotalRevenue DESC;
```

```sql
-- Top 10 customers by revenue
SELECT c.CompanyName, c.AccountTier, COUNT(s.OrderID) AS Orders, SUM(s.Quantity * s.UnitPrice) AS Revenue
FROM SalesOrders s
JOIN Customers c ON s.CustomerID = c.CustomerID
WHERE s.OrderStatus = 'Completed'
GROUP BY c.CompanyName, c.AccountTier
ORDER BY Revenue DESC
OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY;
```

### 4.3 — Open the Data Model

1. At the bottom of the SQL analytics endpoint, click the **Model** tab (or navigate to it via the view switcher)
2. You should see both tables: `Customers` and `SalesOrders`

### 4.4 — Create the Relationship

1. Drag the `CustomerID` field from the `SalesOrders` table to the `CustomerID` field on the `Customers` table
2. Verify the relationship settings:
   - **Cardinality:** Many-to-one (SalesOrders → Customers)
   - **Cross filter direction:** Single
3. Click **OK** / **Confirm**

> You should now see a line connecting the two tables in the model diagram.

### 4.5 — Create DAX Measures

Click on the `SalesOrders` table in the model, then select **New measure** from the toolbar. Create the following measures one at a time:

**Total Revenue:**

```dax
Total Revenue = SUMX(SalesOrders, SalesOrders[Quantity] * SalesOrders[UnitPrice])
```

**Total Cost:**

```dax
Total Cost = SUMX(SalesOrders, SalesOrders[Quantity] * SalesOrders[UnitCost])
```

**Profit Margin:**

```dax
Profit Margin = DIVIDE([Total Revenue] - [Total Cost], [Total Revenue])
```

**Order Count:**

```dax
Order Count = COUNTROWS(SalesOrders)
```

> **Tip:** After creating each measure, press **Enter** or click the checkmark to save it. You should see each measure appear under the SalesOrders table with a calculator icon.

---

## Lab 5: Build a Power BI Dashboard (15-20 min)

Now for the payoff — turning your data model into an interactive dashboard.

### 5.1 — Create a New Report

1. From the Model view, click **New report** in the toolbar
2. The Power BI report editor will open with your data model already connected

### 5.2 — Add Card Visuals (KPIs)

Create three card visuals across the top of the report:

1. Click an empty area of the canvas → select **Card** visual from the Visualizations pane
2. Drag `Total Revenue` to the **Fields** well
3. Format the card: set the label to display as currency
4. Repeat for `Profit Margin` (format as percentage) and `Order Count`

Arrange all three cards in a row at the top of the report.

### 5.3 — Revenue by Vendor (Bar Chart)

1. Select **Clustered bar chart** from the Visualizations pane
2. **Y-axis:** `Vendor` (from SalesOrders)
3. **X-axis:** `Total Revenue`
4. This shows which vendors drive the most revenue for InnovAItion Partners

### 5.4 — Revenue by Category and Account Tier (Stacked Bar Chart)

1. Select **Stacked bar chart**
2. **Y-axis:** `ProductCategory`
3. **X-axis:** `Total Revenue`
4. **Legend:** `Tier` (from Customers)
5. This reveals which product categories are popular with your top-tier accounts

### 5.5 — Monthly Revenue Trend (Line Chart)

1. Select **Line chart**
2. **X-axis:** `OrderDate` (from SalesOrders)
3. **Y-axis:** `Total Revenue`
4. Power BI will automatically create a date hierarchy — drill down to the **Month** level
5. This shows revenue trends over time

### 5.6 — Top Customers Table

1. Select **Table** visual
2. Add the following fields:
   - `CompanyName` (from Customers)
   - `Tier` (from Customers)
   - `Order Count`
   - `Total Revenue`
   - `Profit Margin`
3. Sort by `Total Revenue` descending
4. This gives leadership a quick view of the most valuable accounts

### 5.7 — Add a Slicer

1. Select **Slicer** from the Visualizations pane
2. Add `Region` (from Customers) as the field
3. Change the slicer style to **Dropdown** (optional, saves space)
4. Test it — clicking a region should filter all visuals on the page

### 5.8 — Format and Save

1. Add a title text box at the top of the report:

```
InnovAItion Partners — Sales Overview
```

2. Adjust colors, fonts, and layout as desired
3. Click **File** → **Save**
4. Name the report:

```
InnovAItion Partners - Sales Dashboard
```

5. Save it to your workspace

---

## Wrap-Up

### What You Built

In this lab, you went from raw data in a SQL database to an interactive Power BI dashboard — all within Microsoft Fabric:

1. **Lakehouse** — A unified storage layer for your data
2. **Data Pipelines** — Automated ingestion from Azure SQL
3. **Data Model** — Relationships and business logic with DAX
4. **Power BI Dashboard** — Interactive visuals for decision-making

### Discussion Questions

- What data sources in **your** organization could benefit from this approach?
- How would you pitch this to an end customer who has data scattered across multiple systems?
- What other measures or visuals would make this dashboard more useful?

### Resources

- [Microsoft Fabric Documentation](https://learn.microsoft.com/en-us/fabric/)
- [DAX Reference Guide](https://learn.microsoft.com/en-us/dax/)
- [Power BI Best Practices](https://learn.microsoft.com/en-us/power-bi/guidance/)
