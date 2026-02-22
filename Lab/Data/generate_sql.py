import random
import datetime

random.seed(42)

# --- CUSTOMERS (50) ---
industries = [
    "Healthcare", "Education", "Financial Services", "Manufacturing",
    "Government", "Retail", "Legal", "Energy", "Hospitality",
    "Transportation", "Construction", "Agriculture", "Nonprofit",
    "Real Estate", "Technology"
]

tiers = ["Gold", "Silver", "Bronze"]
tier_weights = [0.25, 0.45, 0.30]

regions = {
    "West": ["CA", "WA", "OR", "AZ", "NV", "CO", "UT"],
    "Midwest": ["IL", "OH", "MN", "IA", "MI", "WI", "IN", "MO"],
    "Northeast": ["NY", "MA", "PA", "NJ", "CT", "MD", "VA"],
    "Southeast": ["FL", "GA", "NC", "SC", "TN", "AL"],
    "South": ["TX", "LA", "OK", "AR", "KY"]
}

sales_reps = [
    "Sarah Mitchell", "Marcus Johnson", "James Carter",
    "Tyler Brooks", "Elena Vasquez", "Kevin Park",
    "Rachel Simmons", "Andre Williams"
]

first_names = [
    "David", "Lisa", "Robert", "Karen", "Angela", "Steve", "Jennifer", "Mike",
    "Patricia", "Brian", "Rachel", "Tom", "Diana", "Frank", "Amy", "Greg",
    "Sandra", "Yusuf", "Megan", "Derek", "Christine", "Nathan", "Laura",
    "Carlos", "Emily", "Jason", "Priya", "Kevin", "Hannah", "Marcus",
    "Olivia", "Trevor", "Nina", "Ryan", "Samantha", "Daniel", "Alicia",
    "Brandon", "Sophia", "Tyler", "Maria", "Connor", "Aisha", "Ethan",
    "Jasmine", "Peter", "Victoria", "Ian", "Heather", "Wesley"
]

last_names = [
    "Chen", "Fernandez", "Tanaka", "Novak", "Washington", "Pham", "Whitfield",
    "Reeves", "Gomez", "Holt", "Kim", "Alvarez", "Russo", "Okafor", "Tran",
    "Mueller", "Price", "Hassan", "O'Brien", "Lawson", "Park", "Singh",
    "Campbell", "Martinez", "Anderson", "Taylor", "Thomas", "Jackson",
    "Rodriguez", "Williams", "Brown", "Davis", "Wilson", "Moore", "Clark",
    "Hall", "Young", "Allen", "Wright", "Torres", "Nguyen", "Rivera",
    "Cooper", "Reed", "Bailey", "Sullivan", "Perry", "Foster", "Barnes", "Gray"
]

company_names = [
    "Summit Healthcare Partners", "Bright Horizon Schools", "Cornerstone Financial Group",
    "Precision Manufacturing Inc", "Metro City Government", "Redline Retail Group",
    "Whitfield & Associates Law", "Cascade Energy Solutions", "Lakeview Medical Center",
    "Trident Logistics Co", "Northstar Insurance", "Greenfield School District",
    "Pacific Coast Hotels", "Atlas Construction Group", "Silverline Credit Union",
    "Heartland Ag Supplies", "Bayside City Council", "Pinnacle Pharma Labs",
    "Evergreen Community College", "Titan Auto Parts", "Meridian Health Systems",
    "Coastal Prep Academy", "Vanguard Wealth Advisors", "ProBuild Industries",
    "Riverside Township", "Urban Outfitters Plus", "Sterling Legal Partners",
    "SunPeak Solar Co", "Harbor View Resort", "Continental Freight Lines",
    "Patriot Mutual Insurance", "Westbrook University", "Grand Vista Properties",
    "Ironclad Security Services", "Columbia Savings Bank", "Prairie Land Equipment",
    "Oakdale County Admin", "BioCore Diagnostics", "Crestwood Academy",
    "Apex Machine Works", "Valley General Hospital", "Lakefront Realty Group",
    "Bridges Community Foundation", "NovaTech Solutions", "Commonwealth Electric",
    "Fairview School District", "Harborside Fish Market", "Summit Ridge Construction",
    "Pacific Northwest Labs", "CrossPoint Church"
]

customers = []
for i in range(50):
    cid = f"C{i+1:03d}"
    company = company_names[i]
    industry = random.choice(industries)
    tier = random.choices(tiers, weights=tier_weights, k=1)[0]
    region = random.choice(list(regions.keys()))
    state = random.choice(regions[region])
    rep = random.choice(sales_reps)

    start_year = random.choice([2023, 2024, 2025])
    start_month = random.randint(1, 12)
    start_day = random.randint(1, 28)
    contract_start = datetime.date(start_year, start_month, start_day)
    renewal = contract_start.replace(year=contract_start.year + 2)

    fname = first_names[i]
    lname = last_names[i]
    domain = company.lower().replace(" ", "").replace("&", "").replace("'", "")[:15]
    email = f"{fname[0].lower()}{lname.lower()}@{domain}.com"
    phone = f"555-{random.randint(1000, 9999)}"

    customers.append({
        "CustomerID": cid,
        "CompanyName": company,
        "Industry": industry,
        "AccountTier": tier,
        "Region": region,
        "State": state,
        "SalesRep": rep,
        "ContractStartDate": contract_start.isoformat(),
        "RenewalDate": renewal.isoformat(),
        "ContactName": f"{fname} {lname}",
        "ContactEmail": email,
        "Phone": phone
    })

# --- PRODUCTS ---
products = [
    # Software
    {"SKU": "MS-M365-BP", "Name": "Microsoft 365 Business Premium", "Category": "Software", "Vendor": "Microsoft", "Cost": 18.00, "Price": 22.00},
    {"SKU": "MS-M365-BS", "Name": "Microsoft 365 Business Standard", "Category": "Software", "Vendor": "Microsoft", "Cost": 11.00, "Price": 15.00},
    {"SKU": "MS-M365-E3", "Name": "Microsoft 365 E3", "Category": "Software", "Vendor": "Microsoft", "Cost": 33.00, "Price": 38.00},
    {"SKU": "MS-M365-E5", "Name": "Microsoft 365 E5", "Category": "Software", "Vendor": "Microsoft", "Cost": 54.00, "Price": 62.00},
    {"SKU": "MS-M365-A3", "Name": "Microsoft 365 A3 (Education)", "Category": "Software", "Vendor": "Microsoft", "Cost": 5.50, "Price": 7.50},
    {"SKU": "MS-M365-A5", "Name": "Microsoft 365 A5 (Education)", "Category": "Software", "Vendor": "Microsoft", "Cost": 10.00, "Price": 13.50},
    {"SKU": "MS-PBI-PRO", "Name": "Power BI Pro", "Category": "Software", "Vendor": "Microsoft", "Cost": 9.00, "Price": 13.00},
    {"SKU": "MS-DEF-E5", "Name": "Microsoft Defender for Endpoint P2", "Category": "Software", "Vendor": "Microsoft", "Cost": 4.50, "Price": 6.00},
    {"SKU": "MS-INTUNE", "Name": "Microsoft Intune Plan 1", "Category": "Software", "Vendor": "Microsoft", "Cost": 7.00, "Price": 10.00},
    {"SKU": "MS-COPILOT", "Name": "Microsoft 365 Copilot", "Category": "Software", "Vendor": "Microsoft", "Cost": 28.00, "Price": 33.00},
    # Cloud
    {"SKU": "MS-AZ-RSV", "Name": "Azure Reserved Instances (1yr)", "Category": "Cloud", "Vendor": "Microsoft", "Cost": 380.00, "Price": 475.00},
    {"SKU": "MS-AZ-SQL", "Name": "Azure SQL Database", "Category": "Cloud", "Vendor": "Microsoft", "Cost": 450.00, "Price": 575.00},
    {"SKU": "MS-AZ-VM", "Name": "Azure Virtual Machines", "Category": "Cloud", "Vendor": "Microsoft", "Cost": 280.00, "Price": 365.00},
    {"SKU": "MS-AZ-FABR", "Name": "Microsoft Fabric Capacity (F64)", "Category": "Cloud", "Vendor": "Microsoft", "Cost": 7500.00, "Price": 9375.00},
    {"SKU": "MS-AZ-BLOB", "Name": "Azure Blob Storage", "Category": "Cloud", "Vendor": "Microsoft", "Cost": 120.00, "Price": 160.00},
    # Hardware - Dell
    {"SKU": "DL-PS-R760", "Name": "PowerEdge R760 Server", "Category": "Hardware", "Vendor": "Dell", "Cost": 6200.00, "Price": 7450.00},
    {"SKU": "DL-PS-R660", "Name": "PowerEdge R660 Server", "Category": "Hardware", "Vendor": "Dell", "Cost": 5400.00, "Price": 6480.00},
    {"SKU": "DL-PS-T560", "Name": "PowerEdge T560 Tower", "Category": "Hardware", "Vendor": "Dell", "Cost": 4800.00, "Price": 5760.00},
    {"SKU": "DL-OW-7420", "Name": "OptiPlex 7420 Desktop", "Category": "Hardware", "Vendor": "Dell", "Cost": 890.00, "Price": 1070.00},
    {"SKU": "DL-OW-3420", "Name": "OptiPlex 3420 Desktop", "Category": "Hardware", "Vendor": "Dell", "Cost": 620.00, "Price": 745.00},
    {"SKU": "DL-LAT-5540", "Name": "Latitude 5540 Laptop", "Category": "Hardware", "Vendor": "Dell", "Cost": 920.00, "Price": 1105.00},
    # Hardware - HP
    {"SKU": "HP-EB-860", "Name": "EliteBook 860 G10 Laptop", "Category": "Hardware", "Vendor": "HP", "Cost": 1050.00, "Price": 1275.00},
    {"SKU": "HP-EB-840", "Name": "EliteBook 840 G10 Laptop", "Category": "Hardware", "Vendor": "HP", "Cost": 980.00, "Price": 1195.00},
    {"SKU": "HP-EB-640", "Name": "EliteBook 640 G10 Laptop", "Category": "Hardware", "Vendor": "HP", "Cost": 780.00, "Price": 950.00},
    {"SKU": "HP-ZB-G11", "Name": "ZBook Fury 16 G11", "Category": "Hardware", "Vendor": "HP", "Cost": 2100.00, "Price": 2520.00},
    {"SKU": "HP-CB-14", "Name": "HP Chromebook 14", "Category": "Hardware", "Vendor": "HP", "Cost": 310.00, "Price": 380.00},
    {"SKU": "HP-DL-380", "Name": "ProLiant DL380 Gen11", "Category": "Hardware", "Vendor": "HP", "Cost": 5800.00, "Price": 6960.00},
    # Networking - Cisco
    {"SKU": "CS-MR-46", "Name": "Meraki MR46 Access Point", "Category": "Networking", "Vendor": "Cisco", "Cost": 950.00, "Price": 1190.00},
    {"SKU": "CS-MR-56", "Name": "Meraki MR56 Access Point", "Category": "Networking", "Vendor": "Cisco", "Cost": 1300.00, "Price": 1625.00},
    {"SKU": "CS-C9300", "Name": "Catalyst 9300 Switch", "Category": "Networking", "Vendor": "Cisco", "Cost": 3800.00, "Price": 4560.00},
    {"SKU": "CS-C9200", "Name": "Catalyst 9200 Switch", "Category": "Networking", "Vendor": "Cisco", "Cost": 2400.00, "Price": 2880.00},
    {"SKU": "CS-FP-1010", "Name": "Firepower 1010 Firewall", "Category": "Networking", "Vendor": "Cisco", "Cost": 1200.00, "Price": 1500.00},
    {"SKU": "CS-FP-2110", "Name": "Firepower 2110 Firewall", "Category": "Networking", "Vendor": "Cisco", "Cost": 3500.00, "Price": 4375.00},
    # Networking - Fortinet
    {"SKU": "FT-FG-60F", "Name": "FortiGate 60F Firewall", "Category": "Networking", "Vendor": "Fortinet", "Cost": 750.00, "Price": 940.00},
    {"SKU": "FT-FG-100F", "Name": "FortiGate 100F Firewall", "Category": "Networking", "Vendor": "Fortinet", "Cost": 2200.00, "Price": 2750.00},
]

# --- GENERATE ORDERS (1000) ---
start_date = datetime.date(2025, 1, 1)
end_date = datetime.date(2026, 2, 20)
date_range = (end_date - start_date).days

statuses = ["Completed", "Completed", "Completed", "Completed", "Completed",
            "Completed", "Completed", "Completed", "Pending", "Cancelled"]

# Weight customers: Gold customers buy more
customer_weights = []
for c in customers:
    if c["AccountTier"] == "Gold":
        customer_weights.append(3)
    elif c["AccountTier"] == "Silver":
        customer_weights.append(2)
    else:
        customer_weights.append(1)

orders = []
for i in range(1000):
    oid = f"ORD-{i+1001}"
    cust = random.choices(customers, weights=customer_weights, k=1)[0]

    order_date = start_date + datetime.timedelta(days=random.randint(0, date_range))

    product = random.choice(products)

    # Realistic quantities based on category
    if product["Category"] == "Software":
        qty = random.choice([5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 150, 200, 250, 300, 500])
    elif product["Category"] == "Cloud":
        qty = random.choice([1, 2, 3, 5, 8, 10, 15, 20, 30, 50])
    elif product["Category"] == "Hardware":
        if "Server" in product["Name"] or "Tower" in product["Name"] or "ProLiant" in product["Name"]:
            qty = random.randint(1, 8)
        else:
            qty = random.choice([5, 10, 12, 15, 20, 25, 30, 40, 50, 60, 75, 100])
    else:  # Networking
        qty = random.choice([2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30])

    # Add some price variance (+/- 5%) to simulate negotiated pricing
    cost_variance = random.uniform(0.95, 1.05)
    price_variance = random.uniform(0.93, 1.07)
    unit_cost = round(product["Cost"] * cost_variance, 2)
    unit_price = round(product["Price"] * price_variance, 2)
    # Ensure price > cost
    if unit_price <= unit_cost:
        unit_price = round(unit_cost * 1.10, 2)

    # Recent orders more likely to be Pending
    if order_date > datetime.date(2026, 1, 15):
        status = random.choice(["Pending", "Pending", "Pending", "Completed"])
    else:
        status = random.choices(statuses, k=1)[0]

    # Deal registration more likely for Gold tier & Microsoft products
    deal_reg_chance = 0.3
    if cust["AccountTier"] == "Gold":
        deal_reg_chance += 0.25
    if product["Vendor"] == "Microsoft":
        deal_reg_chance += 0.15
    deal_reg = "Yes" if random.random() < deal_reg_chance else "No"

    orders.append({
        "OrderID": oid,
        "CustomerID": cust["CustomerID"],
        "OrderDate": order_date.isoformat(),
        "ProductSKU": product["SKU"],
        "ProductName": product["Name"],
        "ProductCategory": product["Category"],
        "Vendor": product["Vendor"],
        "Quantity": qty,
        "UnitCost": unit_cost,
        "UnitPrice": unit_price,
        "OrderStatus": status,
        "DealRegistration": deal_reg
    })

# Sort orders by date
orders.sort(key=lambda x: x["OrderDate"])

# --- WRITE SQL ---
def sql_escape(s):
    return s.replace("'", "''")

lines = []
lines.append("-- InnovAItion Partners Ltd. - Lab Database")
lines.append("-- Generated fake data for Microsoft Fabric lab")
lines.append("")
lines.append("-- =============================================")
lines.append("-- CUSTOMERS TABLE")
lines.append("-- =============================================")
lines.append("")
lines.append("""IF OBJECT_ID('dbo.Customers', 'U') IS NOT NULL
    DROP TABLE dbo.Customers;
GO

CREATE TABLE dbo.Customers (
    CustomerID NVARCHAR(10) PRIMARY KEY,
    CompanyName NVARCHAR(100) NOT NULL,
    Industry NVARCHAR(50) NOT NULL,
    AccountTier NVARCHAR(10) NOT NULL,
    Region NVARCHAR(20) NOT NULL,
    State NVARCHAR(5) NOT NULL,
    SalesRep NVARCHAR(50) NOT NULL,
    ContractStartDate DATE NOT NULL,
    RenewalDate DATE NOT NULL,
    ContactName NVARCHAR(50) NOT NULL,
    ContactEmail NVARCHAR(100) NOT NULL,
    Phone NVARCHAR(20) NOT NULL
);
GO
""")

# Insert customers in batches
lines.append("INSERT INTO dbo.Customers (CustomerID, CompanyName, Industry, AccountTier, Region, State, SalesRep, ContractStartDate, RenewalDate, ContactName, ContactEmail, Phone)")
lines.append("VALUES")
for i, c in enumerate(customers):
    comma = "," if i < len(customers) - 1 else ";"
    lines.append(f"    ('{c['CustomerID']}', '{sql_escape(c['CompanyName'])}', '{c['Industry']}', '{c['AccountTier']}', '{c['Region']}', '{c['State']}', '{c['SalesRep']}', '{c['ContractStartDate']}', '{c['RenewalDate']}', '{sql_escape(c['ContactName'])}', '{c['ContactEmail']}', '{c['Phone']}'){comma}")
lines.append("GO")
lines.append("")

lines.append("-- =============================================")
lines.append("-- SALES ORDERS TABLE")
lines.append("-- =============================================")
lines.append("")
lines.append("""IF OBJECT_ID('dbo.SalesOrders', 'U') IS NOT NULL
    DROP TABLE dbo.SalesOrders;
GO

CREATE TABLE dbo.SalesOrders (
    OrderID NVARCHAR(20) PRIMARY KEY,
    CustomerID NVARCHAR(10) NOT NULL,
    OrderDate DATE NOT NULL,
    ProductSKU NVARCHAR(20) NOT NULL,
    ProductName NVARCHAR(100) NOT NULL,
    ProductCategory NVARCHAR(20) NOT NULL,
    Vendor NVARCHAR(20) NOT NULL,
    Quantity INT NOT NULL,
    UnitCost DECIMAL(10,2) NOT NULL,
    UnitPrice DECIMAL(10,2) NOT NULL,
    OrderStatus NVARCHAR(15) NOT NULL,
    DealRegistration NVARCHAR(5) NOT NULL,
    CONSTRAINT FK_SalesOrders_Customers FOREIGN KEY (CustomerID) REFERENCES dbo.Customers(CustomerID)
);
GO
""")

# Insert orders in batches of 100 (SQL Server limit is 1000 rows per INSERT)
batch_size = 100
for batch_start in range(0, len(orders), batch_size):
    batch = orders[batch_start:batch_start + batch_size]
    lines.append("INSERT INTO dbo.SalesOrders (OrderID, CustomerID, OrderDate, ProductSKU, ProductName, ProductCategory, Vendor, Quantity, UnitCost, UnitPrice, OrderStatus, DealRegistration)")
    lines.append("VALUES")
    for i, o in enumerate(batch):
        comma = "," if i < len(batch) - 1 else ";"
        lines.append(f"    ('{o['OrderID']}', '{o['CustomerID']}', '{o['OrderDate']}', '{o['ProductSKU']}', '{sql_escape(o['ProductName'])}', '{o['ProductCategory']}', '{o['Vendor']}', {o['Quantity']}, {o['UnitCost']}, {o['UnitPrice']}, '{o['OrderStatus']}', '{o['DealRegistration']}'){comma}")
    lines.append("GO")
    lines.append("")

# Summary stats
print(f"Customers: {len(customers)}")
print(f"Orders: {len(orders)}")
print(f"Date range: {orders[0]['OrderDate']} to {orders[-1]['OrderDate']}")

vendor_counts = {}
cat_counts = {}
status_counts = {}
for o in orders:
    vendor_counts[o["Vendor"]] = vendor_counts.get(o["Vendor"], 0) + 1
    cat_counts[o["ProductCategory"]] = cat_counts.get(o["ProductCategory"], 0) + 1
    status_counts[o["OrderStatus"]] = status_counts.get(o["OrderStatus"], 0) + 1

print(f"\nBy vendor: {vendor_counts}")
print(f"By category: {cat_counts}")
print(f"By status: {status_counts}")

tier_counts = {}
for c in customers:
    tier_counts[c["AccountTier"]] = tier_counts.get(c["AccountTier"], 0) + 1
print(f"Customer tiers: {tier_counts}")

with open("/Users/russseaman/Projects/Work/InnoVate Conference/2026/InnovAIte2026/Lab/Data/InnovAItion_Partners_Lab.sql", "w") as f:
    f.write("\n".join(lines))

print("\nSQL file written successfully!")
